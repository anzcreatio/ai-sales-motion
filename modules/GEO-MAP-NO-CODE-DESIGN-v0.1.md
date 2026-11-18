# Geo map, no-code version: design v0.1 (18 Nov 2026)

**Goal (Renzo):** turn the BPD Bali map (`usr.BpdMap`, package `UsrBpdMapUi`) into a reusable `labUiKit` component that
an SC sets up in the Freedom UI Designer with pickers, on any objects, with no code. BPD Bali's set-up becomes one
example configuration. Rules: `apac-sc-motion/standards/UI-KIT-STANDARD-v0.6.md` and `BUILD-RULES-v0.6.md` §5.
Source today: `Deals/bpd-bali-wn/map-sandbox/source/bpd_map` and `map-sandbox/BPD-MAP-COMPONENT-README.md`.

## 1. What is BPD-specific today, and what replaces it

| Hard-coded today | Becomes a setting (picked, not typed) |
|---|---|
| Objects Lead, Account, UsrAgunan; their columns | **Layers** (1–4): object, latitude and longitude columns (number), title column, colour-by column (lookup or text) with a colour per value, owner column, date column, up to 2 filter columns (lookups → drop-downs), up to 4 pop-up columns, photo column (image), marker shape |
| UsrBranch with GeoJSON boundary, centre | **Areas** (optional): area object, boundary column (text, GeoJSON), centre latitude/longitude columns; on each layer the column linking a record to its area; default area or a page field |
| "Outside the area" from a stored flag | Worked out on the map (point in polygon), no stored column needed |
| UsrMapRule rows (radius, tolerance, same point) | Numbers in the settings, **or** a rules object + code/value columns (so the business changes them live: keeps the D1 moment) |
| Benchmark on UsrValue / UsrValuationDate / UsrType | **Record check** (optional): value column, valuation-date column, type column, tolerance %, months back |
| Writes to UsrNearbyCount, UsrWarning, … | **Store the check** (optional, says "writes" in the panel): pick up to 5 target columns |
| Sawah + Kebun tile, AO table, Hot/Warm/Cool | **Summary** (optional): a "count by" bar on a picked lookup; a "compare by" table on a picked owner column with one picked "reached" condition (kit condition rows) |
| Bahasa / English strings | Kit i18n (id, en first), wording overrides in the panel |
| Nominatim, OSM tiles | Geocoder URL and country, tile URL and attribution (defaults OSM); empty geocoder = no address search |

## 2. Modes (each switched on in the panel)

| Mode | On a | Does |
|---|---|---|
| **Area map** | Home or dashboard page | Layers, heat, areas with borders, filters, summary |
| **Near a point** | Home page or a record | Pin from a click, GPS or a preset list; radius buttons (km list in settings); list sorted by distance |
| **Record check** | Record page | The open record's point (two-way bound to its latitude/longitude/address page fields), duplicates within radius and same point, benchmark, GPS, address search, pin → address |

## 3. Kit fit

| Kit rule | How |
|---|---|
| Pickers for every setting | `kit-picker`: object, column filtered by type, lookup values with colours, page fields, numbers with units, condition rows |
| Model only, caps, aggregation | `kit-data` (per layer cap, "first N" shown); counts for the summary via aggregation where the stand supports it |
| Writes | `kit-write` (`canSave` + `ensureOk`), only in record mode, only to picked columns |
| Safe defaults, "Set me up" | No layer picked → "Set me up" card; a broken setting → alert inside the component |
| Type name | **`usr.GeoMap`** ("Map"); `usr.BpdMap` stays installed for BPD Bali until it moves over |
| Mobile | Not shown (custom components don't render in the mobile app; the native `crt.Map` covers mobile) |

## 4. Build route

1. Own git worktree of `lab-ui-kit` from `main` (0.6.4), branch `geomap`, folder `C:\Projects\builds\ui-kit-geomap`
   (the `ui-kit` and `ui-kit-ewb` working copies belong to other chats).
2. **Increment 1 (about 1 day):** layers + area map + near a point, panel with pickers, i18n, tests. Configure it on
   clean82 to reproduce Peta Cabang from settings only (no code), side by side with `usr.BpdMap`.
3. **Increment 2 (about 1 day):** record check (duplicates, benchmark, GPS, address, pin, store the check), summary
   block. Reproduce the collateral page from settings only.
4. README with BPD Bali as the worked example; kit version 0.7.0; export to SharePoint `Library/ui-kit/`.

**Install note:** clean82 has `labUiKit` 0.6.2. A `geomap` build replaces it there (one package, one version line);
`main` 0.6.4 is the published superset, so the branch carries everything 0.6.2 had.

## 5. Not in v1

Road routing; clustering beyond the current light version; drawing or editing areas on the map; offline; any write
outside record mode.
