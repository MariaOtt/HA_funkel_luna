# 🐉 Funkel & Luna: Home-Assistant-Schnitzeljagd

Eine interaktive Schnitzeljagd für Kinder mit **6 Stationen, 7 Aufgaben**, Audio-/Videobotschaften und einer zentralen Home-Assistant-Spielleitung.

**Vorlagenstand:** Home-Assistant-Package **4.17**, Dashboard **4.19**. Die Spielsteuerung ist gegenüber dem Ausgangsprojekt unverändert; lediglich private Namen, Raumbezeichnungen und tatsächliche externe Geräte-Entity-IDs wurden neutralisiert.

## Projektstruktur

```text
HA_funkel_luna/
├── README.md
├── home-assistant/
│   ├── funkel_luna_package.yaml
│   └── funkel_luna_dashboard.yaml
├── media/
│   ├── Audio/                # 18 MP3-Sprachclips
│   ├── Video/                # 6 MP4-Videos
│   └── References/           # 8 PNG-Referenzbilder
├── dokumentation/
│   ├── INSTALLATION.md
│   ├── STORYBOOK.md
│   └── REQUISITEN.md
└── scripts/
    └── validate.py
```

Die Medien werden über einen **separaten Pull Request** ergänzt. Erst nach dessen Merge ist der gesamte Medienbestand Teil dieses öffentlichen Repositories. Die 24 Clipnamen und die Original-Media-Source-Pfade bleiben erhalten.

## Was passiert in der Schnitzeljagd?

Funkel (Drache) und Luna (Einhorn) leiten durch sechs Szenen: **Drachennest → Regenbogen → Zaubersteine → Lavafeld → Schlüssel & Ei → Schatz**. Audio- und Videoclips, Licht- und Rolloeffekte begleiten die Aufgaben. Die Spielleitung kann jeden Schritt einzeln oder als Clipfolge auslösen und sieben Erfolge bestätigen. Das Dashboard besitzt sieben Ansichten: die Hauptregie und sechs Einzelsteuerungen.

Das Projekt besteht weiterhin aus **einem einzigen Package** mit den Helfern, 29 Skripten und 6 Automationen. Es darf nicht in Teilpackages auseinandergezogen werden.

## Installation

Siehe [Installationsanleitung](dokumentation/INSTALLATION.md). Die angegebenen `media_player.*`, `light.*` und `cover.*` sind **Beispiel-IDs** und müssen konsistent in Package und Dashboard durch eigene Geräte-Entities ersetzt werden.

| Dateien im Repository | Ziel auf Home Assistant |
| --- | --- |
| `home-assistant/funkel_luna_package.yaml` | `/config/packages/funkel_luna_package.yaml` |
| `home-assistant/funkel_luna_dashboard.yaml` | Rohkonfigurationseditor eines Dashboards |
| `media/Audio/*` | `/media/funkel_luna/Audio/*` |
| `media/Video/*` | `/media/funkel_luna/Video/*` |
| `media/References/*` | Produktionsreferenzen, kein Pflichtordner für Home Assistant |

Voraussetzungen: Home Assistant mit Packages und Media Source, passende Audio-Player, für Videos die hier verwendete Kodi-/Fire-TV-Steuerung, sowie **Mushroom Cards** und **Ring-Tile Card** für das Dashboard.

## Prüfung

```bash
pip install -r requirements-dev.txt
python scripts/validate.py
# Wenn alle 24 Clips nach der Medien-PR vorhanden sind:
python scripts/validate.py --require-media
```

Die YAML-Prüfung ersetzt keinen Test mit den tatsächlichen Home-Assistant-Geräten.

## Datenschutz und Medien

Diese Veröffentlichung enthält **keine echten Hardware-IDs, privaten Kindernamen, Zugangsdaten oder persönliche ChatGPT-Freigabelinks** in der bereitgestellten YAML-Dokumentation. Die Medien werden ohne technische oder inhaltliche Umwandlung übernommen.

### Hinweise
- Die Spielabläufe bleiben erhalten, die Platzhalter-IDs sind nicht unmittelbar lauffähig.
- Für die Audios, Videos und Referenzbilder gelten die jeweils zu klärenden Urheber- und Nutzungsrechte. Die Veröffentlichung als GitHub-Repository gewährt ohne gesonderte Lizenz nicht automatisch eine Weiterverwendungserlaubnis.
- Beim Anpassen der Vorlage keine eigenen Secrets, personenbezogenen Daten oder echten Entity-IDs zurück ins öffentliche Repository committen.

