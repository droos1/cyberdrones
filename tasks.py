"""Task automation for the cyberdrones campaign repo.

Run with: `invoke <task> [args]`

Tasks:
  render-pdf  Render an adventure markdown to printable PDF using print.css
"""

from pathlib import Path

from invoke import task

ROOT = Path(__file__).parent


def _resolve_adventure(arg: str) -> Path:
    """Accept either a path to a markdown file or an adventure folder slug."""
    p = Path(arg)
    if p.is_file():
        return p
    # treat as folder slug under adventures/
    candidate = ROOT / "adventures" / p.name / "adventure.md"
    if candidate.exists():
        return candidate
    # also try as a bare path relative to repo root
    candidate = ROOT / arg
    if candidate.is_file():
        return candidate
    raise SystemExit(f"No adventure markdown found for: {arg}")


@task(help={"adventure": "Adventure folder slug (e.g. 03-costa-muerta) or path to adventure.md"})
def render_pdf(c, adventure):
    """Render an adventure markdown to PDF using print.css.

    Examples:
      invoke render-pdf -a 03-costa-muerta
      invoke render-pdf -a adventures/02-dead-signal/adventure.md
    """
    md = _resolve_adventure(adventure)
    pdf = md.with_suffix(".pdf")
    css = ROOT / "print.css"
    title = md.parent.name.replace("-", " ").title()
    c.run(
        f'pandoc "{md}" --css="{css}" --pdf-engine=weasyprint '
        f'--standalone --metadata title="{title}" -o "{pdf}"'
    )
    print(f"Wrote {pdf}")
