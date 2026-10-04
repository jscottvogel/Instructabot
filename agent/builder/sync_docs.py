#!/usr/bin/env python3
"""
Instructabot Web Textbook Sync & Site Generator
-----------------------------------------------
Compiles the 51 markdown curriculum modules, syllabus, simulations,
and autonomous editorial reports into an interactive MkDocs Material textbook.
Generates a complete, responsive navigation structure.
"""

import sys
import os
import shutil
import re
from pathlib import Path

# Windows console encoding safety
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
CURRICULUM_DIR = REPO_ROOT / "curriculum"
SIMULATIONS_DIR = REPO_ROOT / "simulations"
REVIEWS_DIR = REPO_ROOT / "reviews"
DOCS_DIR = REPO_ROOT / "docs"
MKDOCS_YML = REPO_ROOT / "mkdocs.yml"


def extract_title_from_md(filepath: Path) -> str:
    """Extracts first H1 or H2 from a Markdown file to use as the menu label."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("# "):
                    return line[2:].strip()
                if line.startswith("## ") and not line.startswith("## 1."):
                    return line[3:].strip()
    except Exception:
        pass
    return filepath.stem.replace("-", " ").title()


def sync_textbook():
    print("=" * 65)
    print("📚 Instructabot Interactive Web Textbook Sync")
    print("=" * 65)

    # 1. Clean and prepare docs directory
    if DOCS_DIR.exists():
        shutil.rmtree(DOCS_DIR)
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    print("Created fresh docs/ directory.")

    # 2. Copy home page (README.md -> docs/index.md) with link fixes
    readme_path = REPO_ROOT / "README.md"
    if readme_path.exists():
        content = readme_path.read_text(encoding="utf-8")
        content = content.replace("curriculum/SYLLABUS.md", "syllabus.md")
        # Collapse multiple dashes in anchors (e.g. syllabus.md#unit-0-...--... -> -...)
        content = re.sub(r"(syllabus\.md#[a-z0-9\-]+)", lambda m: re.sub(r"-+", "-", m.group(1)), content)
        content = content.replace(".github/workflows/curriculum_evolution.yml", "https://github.com/jscottvogel/Instructabot/blob/main/.github/workflows/curriculum_evolution.yml")
        (DOCS_DIR / "index.md").write_text(content, encoding="utf-8")
        print("✅ Synced & sanitized Home: README.md -> docs/index.md")

    # 3. Copy Syllabus
    syllabus_path = CURRICULUM_DIR / "SYLLABUS.md"
    if syllabus_path.exists():
        shutil.copy2(syllabus_path, DOCS_DIR / "syllabus.md")
        print("✅ Synced Master Syllabus: curriculum/SYLLABUS.md -> docs/syllabus.md")

    # 3.1 Copy Getting Started & Glossary
    getting_started_path = CURRICULUM_DIR / "GETTING_STARTED.md"
    if getting_started_path.exists():
        gs_content = getting_started_path.read_text(encoding="utf-8")
        gs_content = re.sub(r'\(unit-([a-z0-9\-]+)/', r'(curriculum/unit-\1/', gs_content)
        gs_content = gs_content.replace("(SYLLABUS.md)", "(syllabus.md)")
        (DOCS_DIR / "getting_started.md").write_text(gs_content, encoding="utf-8")
        print("✅ Synced Getting Started Guide -> docs/getting_started.md")

    glossary_path = CURRICULUM_DIR / "GLOSSARY.md"
    if glossary_path.exists():
        shutil.copy2(glossary_path, DOCS_DIR / "glossary.md")
        print("✅ Synced Plain-English Glossary -> docs/glossary.md")

    # 3.2 Copy Hardware Kits & Monetization Guide
    kits_path = REPO_ROOT / "hardware" / "KITS_AND_MONETIZATION.md"
    if kits_path.exists():
        shutil.copy2(kits_path, DOCS_DIR / "hardware_kits.md")
        print("✅ Synced Hardware Kits & Monetization Blueprint -> docs/hardware_kits.md")

    # 4. Copy Simulations Guide with link fixes
    sim_readme = SIMULATIONS_DIR / "README.md"
    if sim_readme.exists():
        sim_content = sim_readme.read_text(encoding="utf-8")
        sim_content = sim_content.replace("cad_urdf/", "https://github.com/jscottvogel/Instructabot/tree/main/simulations/cad_urdf/")
        sim_content = sim_content.replace("webots/worlds/", "https://github.com/jscottvogel/Instructabot/tree/main/simulations/webots/worlds/")
        (DOCS_DIR / "simulations.md").write_text(sim_content, encoding="utf-8")
        print("✅ Synced & sanitized Simulations Guide -> docs/simulations.md")

    # 4.1 Copy Standalone In-Browser Circuit Simulator
    sim_html = SIMULATIONS_DIR / "web" / "simulator.html"
    if sim_html.exists():
        shutil.copy2(sim_html, DOCS_DIR / "simulator.html")
        print("✅ Synced Standalone Web Circuit Simulator -> docs/simulator.html")

    # 5. Copy All Reviews and Packets
    reviews_target_dir = DOCS_DIR / "reviews"
    reviews_target_dir.mkdir(parents=True, exist_ok=True)
    if REVIEWS_DIR.exists():
        for r_file in REVIEWS_DIR.glob("*.md"):
            shutil.copy2(r_file, reviews_target_dir / r_file.name)
        print("✅ Synced complete reviews/ directory into docs/reviews/.")

    # 6. Copy Reports
    reports_target_dir = DOCS_DIR / "reports"
    reports_target_dir.mkdir(parents=True, exist_ok=True)
    for report_file in ["autonomous_evolution_report.md", "editorial_board_report.md", "evolution_brief.md"]:
        src = REVIEWS_DIR / report_file
        if src.exists():
            shutil.copy2(src, reports_target_dir / report_file)
            print(f"✅ Synced Report: {report_file} -> docs/reports/{report_file}")

    # 6. Copy Notebooks Directory
    notebooks_source_dir = REPO_ROOT / "notebooks"
    notebooks_target_dir = DOCS_DIR / "notebooks"
    notebooks_target_dir.mkdir(parents=True, exist_ok=True)
    if notebooks_source_dir.exists():
        for nb_file in notebooks_source_dir.glob("*.md"):
            nb_content = nb_file.read_text(encoding="utf-8")
            (notebooks_target_dir / nb_file.name).write_text(nb_content, encoding="utf-8")
        print("✅ Synced notebooks/ directory into docs/notebooks/.")

    # 7. Copy Curriculum Units with Link Sanitation
    curriculum_target_dir = DOCS_DIR / "curriculum"
    curriculum_target_dir.mkdir(parents=True, exist_ok=True)

    nav_units = []
    unit_dirs = sorted([d for d in CURRICULUM_DIR.iterdir() if d.is_dir() and d.name.startswith("unit-")])

    for u_dir in unit_dirs:
        unit_slug = u_dir.name
        dest_unit_dir = curriculum_target_dir / unit_slug
        dest_unit_dir.mkdir(parents=True, exist_ok=True)

        md_files = sorted(u_dir.glob("*.md"))
        unit_nav_items = []
        unit_display_title = unit_slug.replace("-", " ").title()

        for md_f in md_files:
            content = md_f.read_text(encoding="utf-8")
            # Sanitize navigation and syllabus links for MkDocs
            content = re.sub(r'\(\.\./SYLLABUS\.md\)', r'(../../syllabus.md)', content)
            content = re.sub(r'\(\.\./GETTING_STARTED\.md\)', r'(../../getting_started.md)', content)
            content = re.sub(r'\(\.\./\.\./README\.md\)', r'(../../index.md)', content)

            dest_file = dest_unit_dir / md_f.name
            dest_file.write_text(content, encoding="utf-8")

            page_title = extract_title_from_md(md_f)
            # Truncate long titles for clean sidebar display
            if ":" in page_title:
                page_title = page_title.split(":")[-1].strip()
            rel_doc_path = f"curriculum/{unit_slug}/{md_f.name}"
            unit_nav_items.append({page_title: rel_doc_path})

        nav_units.append({unit_display_title: unit_nav_items})

    print(f"✅ Synced {len(unit_dirs)} units ({sum(len(items[list(items.keys())[0]]) for items in nav_units)} modules) into docs/curriculum/.")

    # 8. Generate mkdocs.yml
    generate_mkdocs_yml(nav_units)
    print("✅ Generated mkdocs.yml configuration.")
    print("=" * 65)


def generate_mkdocs_yml(nav_units):
    lines = [
        'site_name: "Instructabot 🤖📚"',
        'site_description: "State-of-the-Art Autonomous Robotics Curriculum for High School & College Students"',
        'site_author: "Instructabot Educational Team"',
        'repo_url: "https://github.com/jscottvogel/Instructabot"',
        'repo_name: "jscottvogel/Instructabot"',
        'docs_dir: "docs"',
        '',
        'theme:',
        '  name: material',
        '  features:',
        '    - navigation.tabs',
        '    - navigation.sections',
        '    - navigation.expand',
        '    - navigation.top',
        '    - search.suggest',
        '    - search.highlight',
        '    - content.code.copy',
        '  palette:',
        '    - scheme: default',
        '      primary: indigo',
        '      accent: cyan',
        '      toggle:',
        '        icon: material/brightness-7',
        '        name: Switch to dark mode',
        '    - scheme: slate',
        '      primary: indigo',
        '      accent: cyan',
        '      toggle:',
        '        icon: material/brightness-4',
        '        name: Switch to light mode',
        '',
        'markdown_extensions:',
        '  - admonition',
        '  - pymdownx.details',
        '  - pymdownx.superfences:',
        '      custom_fences:',
        '        - name: mermaid',
        '          class: mermaid',
        '          format: !!python/name:pymdownx.superfences.fence_code_format',
        '  - pymdownx.arithmatex:',
        '      generic: true',
        '  - pymdownx.highlight:',
        '      anchor_linenums: true',
        '  - pymdownx.inlinehilite',
        '  - pymdownx.snippets',
        '  - tables',
        '  - footnotes',
        '',
        'extra_javascript:',
        '  - https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-mml-chtml.js',
        '',
        'nav:',
        '  - Home: index.md',
        '  - "🚀 Getting Started (Quickstart)": getting_started.md',
        '  - "🗺️ Master Syllabus": syllabus.md',
        '  - "📖 Plain-English Glossary": glossary.md',
        '  - "🎮 Simulations & Labs": simulations.md',
        '  - "💼 Official Hardware Kits & BOM": hardware_kits.md',
        '  - Curriculum Units:'
    ]

    # Add each unit
    for u in nav_units:
        for u_title, items in u.items():
            lines.append(f'      - {u_title}:')
            for item in items:
                for label, path in item.items():
                    clean_label = label.replace('"', '\\"')
                    lines.append(f'          - "{clean_label}": {path}')

    lines.extend([
        '  - "📓 Engineering Notebooks":',
        '      - "Overview & CLI Guide": notebooks/README.md',
        '      - "Master Notebook Template": notebooks/MASTER_NOTEBOOK_TEMPLATE.md',
        '      - "Lab 00: Systems Decomposition": notebooks/lab-00-systems-decomposition-log.md',
        '      - "Lab 01: Zero-Code Nightlight": notebooks/lab-01-nightlight-log.md',
        '      - "Lab 02: Intersection Controller": notebooks/lab-02-intersection-controller-log.md',
        '      - "Lab 03: Sonar Radar Scanner": notebooks/lab-03-sonar-radar-scanner-log.md',
        '      - "Lab 04: Motor Drive & Acceleration": notebooks/lab-04-motor-drive-acceleration-log.md',
        '      - "Lab 05: Robotic Arm CAD Sizing": notebooks/lab-05-robotic-arm-cad-sizing-log.md',
        '      - "Lab 06: Webots Maze Navigation": notebooks/lab-06-maze-navigation-webots-log.md',
        '      - "Lab 07: Pan-Tilt Visual Turret": notebooks/lab-07-pan-tilt-visual-turret-log.md',
        '      - "Lab 08: Modular ROS 2 Package": notebooks/lab-08-modular-ros2-package-log.md',
        '      - "Lab 09: Warehouse SLAM & Nav2": notebooks/lab-09-autonomous-warehouse-nav2-log.md',
        '      - "Lab 10: SOTA AI Sim2Real Capstone": notebooks/lab-10-semantic-object-fetching-capstone-log.md',
        '  - Autonomous Reports & Audits:',
        '      - "Continuous Evolution Audit": reports/autonomous_evolution_report.md',
        '      - "Editorial Board Report": reports/editorial_board_report.md',
        '      - "Research Trends Brief": reports/evolution_brief.md'
    ])

    with open(MKDOCS_YML, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    sync_textbook()
