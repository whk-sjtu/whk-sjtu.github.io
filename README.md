# Hankun Wang — academic homepage

A static, responsive academic homepage. Text, resource links, and navigation are rendered as static HTML. A small script toggles the publication abstracts. No external fonts or build dependencies are required.

## Edit

- `data/publications.json`: publication metadata and verified resource links.
- `scripts/page.html`: profile, education, experience, honors, and service.
- `assets/style.css`: responsive layout and print styles.
- `assets/`: portrait extracted from the supplied CV, downloadable CV, and favicon.

Run `python3 scripts/build.py` after editing content. Commit the generated `index.html` together with its source files. Publications appear in a single list, with papers naming Hankun Wang first placed before coauthored papers; each part is ordered by year and date descending. Same-event ties use the first preprint date. Resource links always follow `Paper → Publisher → Demo → Playground → Code → Models → Benchmark → Supplement`, omitting unavailable entries. The renderer rejects unknown resource labels so new types receive an explicit ordering.

## Local preview

```sh
python3 -m http.server 22339 --bind 0.0.0.0 --directory .
```

Open `http://localhost:22339` on the server machine, or its reachable address on port 22339 from another machine.

## GitHub Pages

The homepage is published at https://whk-sjtu.github.io/. GitHub Pages deploys from `main` and `/ (root)`. Run the build script and commit the generated `index.html` with its sources before pushing updates.

## Content maintenance

The publication selection is maintained by the owner. Citation counts are not displayed. Metadata uses published versions where verified. The full list is linked through Google Scholar.

For another talk or news item, add a section only when its title, date, venue, and announcement URL are available. Keep research notes and screenshots in the canonical artifacts directory, outside the website checkout.

## Visual hierarchy

Use neutral black (`#222`) for primary content and semibold (`600`) for entry titles and emphasized names. Section headings use regular weight and larger size. Dates, author lists, venues, degrees, and department details use neutral gray (`#666`) and regular weight. Resource links and navigation actions use green (`#28634f`) and regular weight. Links embedded in prose inherit their surrounding color and weight, with underlines on hover and visible keyboard focus.
