# Proposed brand and entity plan for GetCarWise and CarClever

**Proposed, pending André confirmation. Not for publication.**

## Which name should describe the publisher and which the product?

The naming rule is approved: use **GetCarWise** for the publisher and **CarClever** for the product. GetCarWise is the research publisher and website; CarClever is the AI car-shopping product offered through supported assistants and related tools. This matches the company’s own story page and terms, which identify GetCarWise as publisher of CarClever.

Use that distinction consistently in page titles, author and publisher references, About text, app listings, and future structured data. A page about the organization should identify GetCarWise. A page explaining how to search inventory or evaluate a listing may identify CarClever as the tool. Do not use “GetCarWise” as though it were the name of the app, and do not imply that CarClever is a separate publisher.

Sources: [GetCarWise story and methodology](https://getcarwise.app/about-getcarwise-our-story/) and [GetCarWise Terms of Service](https://getcarwise.app/terms-of-service/).

## What is the current source of truth for each name?

Use the official site at [getcarwise.app](https://getcarwise.app/) as the source for publisher identity, product disclosures, and links to CarClever. Use the live [CarClever - Find My Car ChatGPT listing](https://chatgpt.com/plugins/plugin_asdk_app_6a85781882508191b1794888c5bbf728) as a product-directory record. The listing currently opens the “CarClever - Find My Car” page and identifies it as a live car-search product. Keep that app listing distinct from a social-media or company profile.

The handoff and Part 3 implementation log report brand confusion in search results for “GetCarWise,” including unrelated businesses with similar names. This is a reason to use the exact domain and consistent publisher/product naming in owned materials, not a reason to associate the brand with unrelated profiles. The observation is documented in the [SEO/GEO strategy handoff](https://github.com/AndreBro007/getcarwise-docs/blob/main/HANDOFF_CHATGPT_SEO_GEO_CONTENT_STRATEGY_BRIEF_20261006.md) and [Part 3 implementation log](https://github.com/AndreBro007/getcarwise-docs/blob/main/IMPLEMENTATION_LOG_SEO_GEO_20261006_PART3.md).

## Which real profiles are verified for an organization profile list?

André confirmed on Oct 6, 2026 that GetCarWise and CarClever have no official social or company profiles today. The official website is an owned web property, and the ChatGPT directory entry is a product listing; neither should be represented as a social or company profile.

Do not add guessed profile URLs, lookalike “Carwise” pages, or personal accounts to an Organization profile list. Profile creation and app-marketing research are parked for later in [TASK_SOCIAL_PROFILES_AND_APP_MARKETING_RESEARCH_20261006.md](TASK_SOCIAL_PROFILES_AND_APP_MARKETING_RESEARCH_20261006.md).

| Candidate | Current assessment | Action |
|---|---|---|
| getcarwise.app | Official owned publisher website | Keep as the canonical publisher URL |
| ChatGPT app listing for CarClever - Find My Car | Verified product listing, not a publisher social profile | Link as a product destination where useful; do not present as a GetCarWise social profile |
| Official social and company profiles | None exist today, as confirmed by André on Oct 6, 2026 | Leave profile URLs out; see [the later task](TASK_SOCIAL_PROFILES_AND_APP_MARKETING_RESEARCH_20261006.md) |

## What does Google mean by Organization sameAs?

Google’s Organization documentation describes sameAs as a URL to another page with additional information about the organization, such as an organization’s social-media or review profile. That means the property should point to a real page that identifies the same organization. A similarly named company, an unrelated personal profile, or a product listing should not be included just to make the list longer.

Google says Organization structured data can help it understand and disambiguate an organization, but it does not guarantee a particular search appearance. The practical aim here is accurate identification, not a promised ranking or knowledge panel.

Source: [Google Search Central: Organization structured data](https://developers.google.com/search/docs/appearance/structured-data/organization).

## Which directories are genuinely applicable?

Maintain the ChatGPT directory entry as a **product listing** for CarClever while the app is available there. Add other assistant directories only where CarClever has an actual current listing and the listing can be independently verified. Do not list a directory merely because it accepts submissions or because a third-party tracker mentions the brand.

For GetCarWise as publisher, consider a professional or review directory only if there is a real, maintained profile with accurate ownership, contact, and business details. A local business directory is not automatically appropriate for an online publisher; confirm eligibility and actual customer-facing location requirements before creating one. Avoid duplicate profiles and unrelated “Carwise” businesses.

## What should the website say about the relationship?

Use a short, consistent description on the About page and in future publisher references:

> GetCarWise is an independent research publisher. CarClever is its car-shopping research product.

The existing GetCarWise story page already describes GetCarWise as an independent publisher and CarClever as its product. Before reusing this sentence, confirm it still reflects the current ownership and product arrangement. Preserve the existing affiliate disclosure near applicable Edmunds links; the company’s current story page explains that GetCarWise may earn a commission on qualifying referrals and says that this does not influence its recommendations.

Source: [GetCarWise story and methodology](https://getcarwise.app/about-getcarwise-our-story/).

## What should happen before any entity implementation?

The publisher/product naming rule is approved: GetCarWise is the publisher and CarClever is the product. André confirmed there are no official social or company profiles today, so no social/profile URLs should be added to an Organization profile list. Future profile creation and app-marketing research are tracked in [TASK_SOCIAL_PROFILES_AND_APP_MARKETING_RESEARCH_20261006.md](TASK_SOCIAL_PROFILES_AND_APP_MARKETING_RESEARCH_20261006.md). Claude can implement approved identity references and validate the result against Google’s current documentation after André confirms a future implementation request.

The owned website remains the publisher’s canonical web property; the ChatGPT listing remains a separate CarClever product destination. This draft includes no structured-data code and does not authorize implementation.
