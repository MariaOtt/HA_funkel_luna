#!/usr/bin/env python3
"""Syntaxprüfung der Quell-YAMLs und optional Medien-Vollständigkeit."""
from pathlib import Path
import argparse
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
PKG = ROOT / 'home-assistant' / 'funkel_luna_package.yaml'
DASH = ROOT / 'home-assistant' / 'funkel_luna_dashboard.yaml'

parser = argparse.ArgumentParser(description='Funkel-&-Luna-Projekt prüfen')
parser.add_argument('--require-media', action='store_true', help='Fehlende Clipdateien als Fehler behandeln')
args = parser.parse_args()

try:
    package = yaml.safe_load(PKG.read_text(encoding='utf-8-sig'))
    dashboard = yaml.safe_load(DASH.read_text(encoding='utf-8-sig'))
except (yaml.YAMLError, OSError) as exc:
    print('FEHLER: YAML-Datei konnte nicht gelesen werden:', exc)
    sys.exit(1)

if not isinstance(package, dict) or 'script' not in package or 'automation' not in package:
    sys.exit('FEHLER: Hauptpackage ist unvollständig.')
if not isinstance(dashboard, dict) or not isinstance(dashboard.get('views'), list):
    sys.exit('FEHLER: Dashboard enthält keine gültige View-Liste.')

pattern = r'Clip\d+[A-Z](?:_\d+)?(?:_[A-Za-z0-9]+)?\.(?:mp3|mp4)'
package_refs = set(re.findall(pattern, PKG.read_text(encoding='utf-8-sig')))
dashboard_refs = set(re.findall(pattern, DASH.read_text(encoding='utf-8-sig')))
if package_refs != dashboard_refs:
    print('WARNUNG: Mediendateinamen unterscheiden sich zwischen Package und Dashboard:')
    print('  Nur Package:', ', '.join(sorted(package_refs - dashboard_refs)))
    print('  Nur Dashboard:', ', '.join(sorted(dashboard_refs - package_refs)))

missing = sorted(
    name for name in package_refs | dashboard_refs
    if not (ROOT / 'media' / ('Audio' if name.endswith('.mp3') else 'Video') / name).is_file()
)
print(f"YAML OK: {len(package['script'])} Skripte, {len(package['automation'])} Automationen, "
      f"{len(dashboard['views'])} Dashboard-Views, {len(package_refs | dashboard_refs)} Medienreferenzen")
if missing:
    print(f'HINWEIS: {len(missing)} Mediendateien fehlen im Repository (siehe media/MEDIENLISTE.md).')
    if args.require_media:
        print('\n'.join('  - ' + name for name in missing))
        sys.exit(1)
print('Projektprüfung abgeschlossen.')
