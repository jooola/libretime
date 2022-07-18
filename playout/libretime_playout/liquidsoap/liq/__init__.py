from pathlib import Path

from jinja2 import Template

here = Path(__file__).parent

entrypoint_template_path = here / "entrypoint.liq"
entrypoint_template = Template(entrypoint_template_path.read_text())
