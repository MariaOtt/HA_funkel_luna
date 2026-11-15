# 🐉 Funkel & Luna: Home-Assistant-Schnitzeljagd

Eine interaktive Schnitzeljagd für Kinder mit **6 Stationen, 7 Aufgaben**, Audio-/Videobotschaften und einer zentralen Home-Assistant-Spielleitung.

**Vorlagenstand:** Home-Assistant-Package **4.17**, Dashboard **4.19**. Die Spielsteuerung ist gegenüber dem Ausgangsprojekt unverändert; lediglich private Namen, Raumbezeichnungen und tatsächliche externe Geräte-Entity-IDs wurden neutralisiert.

## Projektstruktur

```text
HA_funkel_luna/
├── README.md
├── home-assistant/
│   ├── funkel_luna_package.yaml      # 4.17: Spielsteuerung
│   ├── funkel_luna_geraete.yaml      # Browser/Testmodus + Gerätezuordnung
│   └── funkel_luna_dashboard.yaml    # 4.19: Bedienoberfläche
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

Der vollständige veröffentlichte Projektstand umfasst **18 MP3-Audios, 6 MP4-Videos und 8 Referenzbilder**. Die Medien sind unter `media/` organisiert. Die 24 Clipnamen und die Original-Media-Source-Pfade bleiben erhalten.

## Was passiert in der Schnitzeljagd?

Funkel (Drache) und Luna (Einhorn) leiten durch sechs Szenen: **Drachennest → Regenbogen → Zaubersteine → Lavafeld → Schlüssel & Ei → Schatz**. Audio- und Videoclips, Licht- und Rolloeffekte begleiten die Aufgaben. Die Spielleitung kann jeden Schritt einzeln oder als Clipfolge auslösen und sieben Erfolge bestätigen. Das Dashboard besitzt sieben Ansichten: die Hauptregie und sechs Einzelsteuerungen.

Die **29 Skripte, 6 Automationen und Spielhelfer** bleiben im einen Hauptpackage. Die neue, getrennte Datei `funkel_luna_geraete.yaml` ist ein **zweites Konfigurationspackage** für logische Player-, Licht- und Rollo-Entities. Dadurch müssen Nutzer für ihre Geräte **weder das Hauptpackage noch das Dashboard bearbeiten**.

## Installation

Siehe [Installationsanleitung](dokumentation/INSTALLATION.md). **Alle echten Geräte-IDs werden ausschließlich in `home-assistant/funkel_luna_geraete.yaml` zugeordnet.** Die logischen `media_player.funkel_*`, `light.funkel_*` und `cover.funkel_*` in Hauptpackage und Dashboard bleiben unverändert.

| Dateien im Repository | Ziel auf Home Assistant |
| --- | --- |
| `home-assistant/funkel_luna_package.yaml` | `/config/packages/funkel_luna_package.yaml` |
| `home-assistant/funkel_luna_geraete.yaml` | `/config/packages/funkel_luna_geraete.yaml` |
| `home-assistant/funkel_luna_dashboard.yaml` | Rohkonfigurationseditor eines Dashboards |
| `media/Audio/*` | `/media/funkel_luna/Audio/*` |
| `media/Video/*` | `/media/funkel_luna/Video/*` |
| `media/References/*` | Produktionsreferenzen, kein Pflichtordner für Home Assistant |

**Browser-Testmodus:** Standardmäßig aktiviert, mit einem für Audio/Video gemeinsamen Browser-Mod-Media-Player. Installiere [Browser Mod](https://github.com/thomasloven/hass-browser_mod), registriere den HA-Browser und benenne dessen Media-Player-Entity in `media_player.funkel_browser` um (oder passe die `children:`-Einträge in der Geräte-Datei an). Ein Klick im Browser kann wegen der Autoplay-Sperre erforderlich sein. Für diese Testvariante werden Licht und Rollos nur simuliert; Fire-TV-/Kodi-Vorbereitung entfällt. Ohne Browser Mod kann Home Assistant den Browser nicht direkt als adressierbaren Medienplayer verwenden.

**Realbetrieb:** In `funkel_luna_geraete.yaml` `input_boolean.funkel_luna_browser_test` auf `off` stellen und dort die neun `children:`-Geräte sowie die vier beispielhaften Licht-/Rollo-Ziele durch eigene Entity-IDs ersetzen. Die Kodi-/Fire-TV-Logik ist dann wieder aktiv.

Voraussetzungen: Home Assistant mit Packages und Media Source; Browser Mod für den Browser-Test bzw. passende echte Audio- und Video-Player, dazu **Mushroom Cards** und **Ring-Tile Card** für das Dashboard.

## Prüfung

```bash
pip install -r requirements-dev.txt
python scripts/validate.py --require-media
python scripts/validate_devices.py
```

Die YAML-Prüfung ersetzt keinen Test mit den tatsächlichen Home-Assistant-Geräten.

## Datenschutz und Medien

Diese Veröffentlichung enthält **keine echten Hardware-IDs, privaten Kindernamen, Zugangsdaten oder persönliche ChatGPT-Freigabelinks** in der bereitgestellten YAML-Dokumentation. Die Medien werden ohne technische oder inhaltliche Umwandlung übernommen.

### Hinweise
- Im Browser-Testmodus ist die Medienwiedergabe nach einmaliger Browser-Mod-Einrichtung möglich. Reale Hardware erfordert ausschließlich Anpassungen in der Geräte-Datei.
- Für die Audios, Videos und Referenzbilder gelten die jeweils zu klärenden Urheber- und Nutzungsrechte. Die Veröffentlichung als GitHub-Repository gewährt ohne gesonderte Lizenz nicht automatisch eine Weiterverwendungserlaubnis.
- Beim Anpassen der Vorlage keine eigenen Secrets, personenbezogenen Daten oder echten Entity-IDs zurück ins öffentliche Repository committen.

