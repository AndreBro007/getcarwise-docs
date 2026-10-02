#!/usr/bin/env python3
"""Build an existing-app OpenAI submission ZIP. Python 3; standard library only."""
import argparse
import copy
import json
import re
import struct
import zipfile
from pathlib import Path, PurePosixPath


def safe_path(name):
    parts = name.rstrip('/').split('/')
    return bool(name) and not name.startswith('/') and '\\' not in name and all(p not in ('', '.', '..') for p in parts)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('source', type=Path, help='Downloaded release or complete existing package ZIP')
    p.add_argument('--version', required=True, help='Three-part package version; independent of application version')
    p.add_argument('--output', required=True, type=Path)
    p.add_argument('--listing-json', type=Path, help='Optional interface-field overrides; omit to retain current listing')
    p.add_argument('--icon', type=Path, help='Square PNG to embed as primary logo and composer icon')
    p.add_argument('--release-notes', type=Path, help='UTF-8 text file with factual release notes')
    p.add_argument('--correct-draft', action='store_true', help='Allow same source version for a draft correction; portal acceptance remains separate')
    a = p.parse_args()
    if not re.fullmatch(r'(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)', a.version):
        p.error('Use a numeric semantic version, e.g. 3.0.2')
    if a.source.resolve() == a.output.resolve():
        p.error('Preserve source: output must be a different file')
    with zipfile.ZipFile(a.source) as z:
        names = z.namelist()
        if len(names) != len(set(names)) or any(not safe_path(n) for n in names):
            p.error('Duplicate or unsafe archive paths')
        manifests = [n for n in ('plugin.json', '.codex-plugin/plugin.json') if n in names]
        if len(manifests) != 1:
            p.error('Require exactly one supported manifest at archive root; review mixed formats manually')
        manifest_path = manifests[0]
        entries = {n: z.read(n) for n in names}
    m = json.loads(entries[manifest_path])
    original = copy.deepcopy(m)
    if not m.get('name'):
        p.error('Source package identity is missing')
    if m.get('version') == a.version and not a.correct_draft:
        p.error('For a same-version draft correction use --correct-draft explicitly')
    m['version'] = a.version
    if manifest_path == 'plugin.json':
        interface = m.setdefault('extensions', {}).setdefault('com.openai', {}).setdefault('interface', {})
    else:
        interface = m.setdefault('interface', {})
    if a.listing_json:
        updates = json.loads(a.listing_json.read_text(encoding='utf-8'))
        if not isinstance(updates, dict):
            p.error('Listing overrides must be a JSON object')
        interface.update(updates)
        # Root package description is distinct; retain it rather than copying a long listing.
    if a.release_notes:
        m.setdefault('extensions', {}).setdefault('com.openai', {}).setdefault('publication', {})['release_notes'] = a.release_notes.read_text(encoding='utf-8').strip()
    if a.icon:
        data = a.icon.read_bytes()
        if len(data) < 24 or data[:8] != b'\x89PNG\r\n\x1a\n' or data[12:16] != b'IHDR':
            p.error('Icon must be PNG; this helper deliberately supports PNG only')
        width, height = struct.unpack('>II', data[16:24])
        if width != height or not 48 <= width <= 4096 or len(data) > 5 * 1024 * 1024:
            p.error('Icon must be square, 48–4096 pixels and at most 5 MiB')
        entries['assets/carclever-icon.png'] = data
        interface['logo'] = interface['composerIcon'] = './assets/carclever-icon.png'
    for key, limit in [('displayName', 30), ('shortDescription', 30), ('longDescription', 4000), ('developerName', 80)]:
        value = interface.get(key)
        if not isinstance(value, str) or not value.strip() or len(value) > limit:
            p.error(f'{key} missing or exceeds final submission limit {limit}')
    for key in ('websiteURL', 'supportURL', 'privacyPolicyURL', 'termsOfServiceURL'):
        value = interface.get(key, '')
        if not isinstance(value, str) or not value.startswith('https://') or len(value) > 1024:
            p.error(f'{key} requires a public HTTPS URL for MCP review')
    for key in ('logo', 'composerIcon', 'logoDark', 'composerIconDark'):
        value = interface.get(key)
        if key in ('logo', 'composerIcon') and not value:
            p.error(f'{key} missing; use --icon')
        if value and (not value.startswith('./') or not safe_path(value[2:]) or value[2:] not in entries):
            p.error(f'{key} references an image not included at plugin root')
    for value in interface.get('screenshots', []):
        if not value.startswith('./') or not safe_path(value[2:]) or value[2:] not in entries:
            p.error('Screenshot references a missing/unsafe archive asset')
    entries[manifest_path] = (json.dumps(m, indent=2, ensure_ascii=False) + '\n').encode('utf-8')
    a.output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(a.output, 'w', zipfile.ZIP_DEFLATED) as z:
        for n, data in entries.items():
            z.writestr(n, data)
    with zipfile.ZipFile(a.output) as z:
        if z.testzip() is not None or any(z.read(n) != data for n, data in entries.items()):
            raise RuntimeError('ZIP integrity or byte verification failed')
        assert json.loads(z.read(manifest_path))['name'] == original['name']
    print(f'Created {a.output}: {m["name"]}, package version {a.version}')
    print('Preserved source components; embedded assets verified. Portal checks and review remain required.')


if __name__ == '__main__':
    main()
