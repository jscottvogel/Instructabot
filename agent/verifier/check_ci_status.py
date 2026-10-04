#!/usr/bin/env python3
"""
Instructabot CI/CD Workflow Diagnostics Tool
---------------------------------------------
Queries GitHub Actions API using local git credentials to report
real-time status, health, and logs of the CI/CD pipelines.
"""

import subprocess
import urllib.request
import json
import sys

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except AttributeError:
        pass


def get_token():
    try:
        p = subprocess.Popen(
            ['git', 'credential', 'fill'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        out, _ = p.communicate(input='protocol=https\nhost=github.com\n\n', timeout=5)
        for line in out.splitlines():
            if line.startswith('password='):
                return line[len('password='):].strip()
    except Exception:
        pass
    return None


def check_ci_runs(limit=5):
    token = get_token()
    if not token:
        print("❌ Could not retrieve Git credentials for GitHub.")
        return False

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "User-Agent": "Instructabot-CI-Diagnostics"
    }

    url = f"https://api.github.com/repos/jscottvogel/Instructabot/actions/runs?per_page={limit}"
    req = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            runs = data.get("workflow_runs", [])
            print("=" * 70)
            print(f"📊 INSTRUCTABOT GITHUB ACTIONS STATUS (Latest {len(runs)} Runs)")
            print("=" * 70)
            for r in runs:
                status_icon = "🟢" if r['conclusion'] == 'success' else ("⏳" if r['status'] in ['in_progress', 'queued'] else "❌")
                print(f"{status_icon} [{r['status'].upper()}/{r['conclusion']}] {r['name']}")
                print(f"   Commit : {r['head_sha'][:7]} - {r.get('head_commit', {}).get('message', '').splitlines()[0]}")
                print(f"   Run ID : {r['id']} | Event: {r['event']} | Created: {r['created_at']}")
            print("=" * 70)
            return True
    except Exception as e:
        print(f"❌ Error querying GitHub API: {e}")
        return False


if __name__ == "__main__":
    check_ci_runs()
