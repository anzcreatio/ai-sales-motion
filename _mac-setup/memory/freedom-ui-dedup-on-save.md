---
name: freedom-ui-dedup-on-save
description: Freedom UI duplicate pop-up on save needs feature EnableDeduplicationFreedomUI registered + on (not shipped registered on demo stands)
metadata:
  node_type: memory
  type: reference
  originSessionId: 69932eee-c02d-4721-baed-df69aa8ad575
  modified: 2026-11-23T05:22:39.969Z
---

Creatio Freedom UI "Potential duplicates found" pop-up on save (Contacts) needs feature toggles `ESDeduplication` AND
`EnableDeduplicationFreedomUI`, plus `DeduplicationWebApiUrl` set and a duplicate rule with "Use this rule on save".
On demo stands (seen 19 Nov 2026, v10.1.0, bpd-bali-map) `EnableDeduplicationFreedomUI` is not even registered, so
saves go through silently. Fix: Feature toggles page (`/0/Nui/ViewModule.aspx#BaseSchemaModuleV2/FeaturesPage`) →
Create feature → toggle on → Save changes → full page reload. That page enables it for the current user only
(Supervisor); other demo users need their own state or an "All employees" row. Source: Academy 8.3.3 Twin changelog.
Bulk "Show duplicate" search works without it (finished in ~3 min; the page needs a reload to show results).

**Shipping the feature in a package (23 Nov 2026, GenLife install test on 11015214):** a Feature + AdminUnitFeatureState
row installed as package data is in the database (`/0/rest/FeatureService/GetFeatureState` = 1) but the browser still
reports it off (`Terrasoft.Features.getIsEnabled` = false), even after a fresh sign-in: the server feature cache isn't
refreshed by a package install. Fix: save it once (`/0/rest/FeatureService/SetFeatureState` {code, state:1,
forAllUsers:true}, or tick + Save on the Features page), reload: pop-up works, no restart. Put this step in any
install instructions for a package that ships a feature.
