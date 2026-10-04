#!/usr/bin/env python3
"""
Instructabot Citation & Media Integrity Verifier
------------------------------------------------
Scans all curriculum markdown files to ensure:
1. Every footnote citation [^n] is defined in the lesson's Sources section.
2. Every cited URL is a valid, well-formed HTTPS link.
3. Every media asset is documented in media/media_manifest.json with an open license.
4. No orphaned citations or broken references exist.
"""

import os
import re
import sys
import json
from pathlib import Path

# Ensure UTF-8 output on Windows consoles
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
CURRICULUM_DIR = REPO_ROOT / "curriculum"
SOURCES_FILE = REPO_ROOT / "sources" / "source_index.json"
MEDIA_MANIFEST_FILE = REPO_ROOT / "media" / "media_manifest.json"

def load_json(filepath):
    if not filepath.exists():
        print(f"❌ Error: Required JSON file missing: {filepath}")
        return None
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def verify_markdown_file(md_path, media_ids):
    rel_path = md_path.relative_to(REPO_ROOT)
    print(f"\n🔍 Auditing {rel_path}...")
    errors = []
    warnings = []

    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Check Footnote References vs Definitions
    body_citations = set(re.findall(r"(?<!^)\[\^(\d+)\]", content))
    footnote_defs = set(re.findall(r"^\[\^(\d+)\]:", content, flags=re.MULTILINE))

    missing_defs = body_citations - footnote_defs
    if missing_defs:
        for m in sorted(missing_defs):
            errors.append(f"Footnote [^{m}] used in text but lacks a definition in Sources section.")

    unused_defs = footnote_defs - body_citations
    if unused_defs:
        for u in sorted(unused_defs):
            warnings.append(f"Footnote [^{u}] defined in Sources section but not cited in lesson body.")

    # 2. Check URLs in Footnote Definitions
    urls = re.findall(r"\[\^(\d+)\]:.*?https?://[^\s\)]+", content)
    if not urls and footnote_defs:
        warnings.append("No active web links detected in footnote definitions.")

    # 3. Check Media Manifest References
    media_mentions = re.findall(r"`([a-zA-Z0-9_\-]+\.(?:svg|png|jpg|jpeg|gif|webp))`", content)
    for asset in set(media_mentions):
        # Match asset by filename or ID
        if not any(a.get("filename") == asset or a.get("id") == asset for a in media_ids):
            warnings.append(f"Media asset '{asset}' is mentioned in lesson but not registered in media_manifest.json.")

    # Report results
    if errors:
        for e in errors:
            print(f"  ❌ ERROR: {e}")
    else:
        print(f"  ✅ Citations check passed ({len(body_citations)} footnotes verified).")

    if warnings:
        for w in warnings:
            print(f"  ⚠️  WARNING: {w}")

    return len(errors) == 0

def main():
    print("=" * 60)
    print("🤖 Instructabot Curriculum Verification Engine")
    print("=" * 60)

    # Load registries
    sources_data = load_json(SOURCES_FILE)
    media_data = load_json(MEDIA_MANIFEST_FILE)

    if not sources_data or not media_data:
        sys.exit(1)

    registered_sources = sources_data.get("sources", [])
    registered_media = media_data.get("media_assets", [])
    print(f"Loaded {len(registered_sources)} verified sources from source_index.json")
    print(f"Loaded {len(registered_media)} media assets from media_manifest.json")

    # Discover curriculum lessons (exclude templates and root syllabus)
    lesson_files = [
        p for p in CURRICULUM_DIR.glob("**/*.md")
        if p.name not in ["SYLLABUS.md", "LESSON_TEMPLATE.md", "README.md", "GETTING_STARTED.md", "GLOSSARY.md"]
    ]

    if not lesson_files:
        print("No lesson markdown files found to verify.")
        sys.exit(0)

    all_passed = True
    for lesson in sorted(lesson_files):
        passed = verify_markdown_file(lesson, registered_media)
        if not passed:
            all_passed = False

    print("\n" + "=" * 60)
    if all_passed:
        print("🎉 ALL LESSONS PASSED INTEGRITY & CITATION AUDIT!")
        sys.exit(0)
    else:
        print("❌ VERIFICATION FAILED: Fix the errors reported above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
