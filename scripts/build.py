"""Render a dependency-free, GitHub Pages-compatible academic homepage."""
from pathlib import Path
import html
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
escape = html.escape
RESOURCE_ORDER = ("Paper", "Publisher", "Demo", "Playground", "Code", "Models", "Benchmark", "Supplement")


def publication(p):
    authors = ', '.join(
        f'<strong>{escape(a)}</strong>' if a == 'Hankun Wang' else escape(a)
        for a in p['authors']
    )
    unknown = set(p['links']) - set(RESOURCE_ORDER)
    if unknown:
        raise ValueError(f'Unknown resource labels: {unknown}')
    resources = ' '.join(
        f'<a href="{escape(p["links"][label], quote=True)}">{escape(label)}</a>'
        for label in RESOURCE_ORDER if label in p['links']
    )
    badge = f'<p class="pub-highlight">{escape(p["badge"])}</p>' if p.get('badge') else ''
    venue = str(p['year']) if p['venue'].lower() == 'arxiv' else f"{p['venue']} {p['year']}"
    if p.get('venue_note'):
        venue += f" ({p['venue_note']})"
    demo = p['links'].get('Demo')
    demo_line = f'<p class="abstract-demo">Demo page: <a href="{escape(demo, quote=True)}">{escape(demo)}</a></p>' if demo else ''
    return f'''<article class="publication" id="{escape(p['id'])}">
      <div class="year">{p['year']}</div>
      <div><h3 class="pub-title"><button class="abstract-toggle" type="button" aria-expanded="false" aria-controls="abstract-{escape(p['id'])}">{escape(p['title'])}<span class="disclosure-mark" aria-hidden="true">+</span></button></h3>
      <p class="authors">{authors}</p>
      <div class="pub-bottom"><span class="venue">{escape(venue)}</span>
      <div class="resources" aria-label="Resources for {escape(p['title'], quote=True)}">{resources}</div></div>{badge}
      <div class="paper-abstract" id="abstract-{escape(p['id'])}" hidden>
        {demo_line}<h4>Abstract</h4><p>{escape(p['abstract'])}</p>
      </div></div>
    </article>'''



def build():
    papers = json.loads((ROOT / 'data/publications.json').read_text())
    assert len({p['id'] for p in papers}) == len(papers), 'Duplicate publication IDs'
    entries = sorted(
        papers,
        key=lambda p: (p['authors'][0] == 'Hankun Wang', p['year'], p['sort_date'], p['first_posted']),
        reverse=True,
    )
    report = next(p for p in entries if p['id'] == 'dots-tts')
    entries.remove(report)
    entries.insert(1, report)
    publications = '<div class="publication-list">' + '\n'.join(map(publication, entries)) + '</div>'
    template = (ROOT / 'scripts/page.html').read_text()
    css_version = hashlib.sha256((ROOT / 'assets/style.css').read_bytes()).hexdigest()[:12]
    template = template.replace('assets/style.css"', f'assets/style.css?v={css_version}"')
    (ROOT / 'index.html').write_text(template.replace('<!-- PUBLICATIONS -->', publications))
    print(f'Built index.html with {len(papers)} publications.')


if __name__ == '__main__':
    build()
