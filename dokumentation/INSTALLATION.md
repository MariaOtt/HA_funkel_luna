# Installation und Gerätezuordnung

## 1. Bestehende Home-Assistant-Konfiguration sichern

Home Assistant mit Packages und Media Source wird vorausgesetzt. Für das Dashboard werden **Mushroom Cards** und **Ring-Tile Card** benötigt.

## 2. Zwei Packages installieren

Kopiere **beide** Dateien nach `/config/packages/`:

- `home-assistant/funkel_luna_package.yaml`: das ursprüngliche Hauptpackage mit **29 Skripten und 6 Automationen**, weiterhin eine einzige Datei.
- `home-assistant/funkel_luna_geraete.yaml`: sämtliche **logischen Geräte-Aliasse**, Browser-Testmodus sowie simulierte Licht- und Rollo-Entities.

Unter `configuration.yaml` muss die Paket-Einbindung existieren:

```yaml
homeassistant:
  packages: !include_dir_named packages
```

Der Geräteplan ist ein **zweites HA-Package**, keine Datei mit `!include`-Anweisungen im Hauptpackage. Dadurch sind beide YAMLs unabhängig prüfbar und in Home Assistant automatisch eingebunden. Nach Änderungen die HA-Konfiguration prüfen und neu starten.

## 3. Browser-Testmodus (Standard)

**Voraussetzung: [Browser Mod](https://github.com/thomasloven/hass-browser_mod).** Home Assistant selbst stellt einen geöffneten Webbrowser nicht automatisch als `media_player` bereit.

1. Browser Mod über HACS installieren, als Integration hinzufügen und Home Assistant neu starten.
2. Home Assistant im gewünschten Browser öffnen. Unter Browser Mod den Browser **registrieren**, damit seine `media_player`-Entity verfügbar ist.
3. Die Browser-Entity in Home Assistant auf **`media_player.funkel_browser`** umbenennen. Alternativ die neun `children:`-Einträge in `funkel_luna_geraete.yaml` auf die tatsächlich erzeugte Browser-Mod-Player-ID ändern.
4. Den Browser geöffnet lassen. Gegebenenfalls einmal in den Browser klicken: Browser können das automatische Abspielen von Audio und Video bis zur Benutzerinteraktion blockieren.
5. Der Standardwert **`input_boolean.funkel_luna_browser_test: initial: true`** aktiviert die Browser-Ausgabe für alle neun Player-Aliasse. **Es sind keine echten Licht- oder Rollo-Geräte nötig.** Diese Aktionen werden über virtuelle Template-Entities simuliert.
6. Bei Video überspringt das Skript `funkel_luna_kodi_vorbereiten` im Browser-Testmodus die sonst nötige Fire-TV-/Kodi-Vorbereitung; alle übrigen automatischen Clipfolgen bleiben erhalten.

Die neuen Alias-Entities heißen weiterhin `media_player.funkel_audio_station_1` bis `_5`, `media_player.funkel_kodi_station_1`/`_6` sowie `media_player.funkel_tv_station_1`/`_6`. Sie zeigen im Browser-Modus auf den einen registrierten Browser. Einzelne Browsertabs auf verschiedenen Computern sind **nicht automatisch synchronisiert**; abgespielt wird auf dem in der Geräte-Datei zugewiesenen Browser-Mod-Gerät.

## 4. Eigene Hardware anschließen (Realmodus)

Öffne **ausschließlich** `/config/packages/funkel_luna_geraete.yaml`. Dort sind folgende Einstellungen gesammelt:

| Logische Entity (bleibt unverändert) | Ziel in der Geräte-Datei |
| --- | --- |
| `media_player.funkel_audio_station_1` bis `_5` | `children:` auf eigene Audio-Media-Player |
| `media_player.funkel_kodi_station_1` und `_6` | `children:` auf eigene Kodi-Player |
| `media_player.funkel_tv_station_1` und `_6` | `children:` auf eigene Fire-TV-/ADB-Player |
| `light.funkel_effekt_station_3` und `_4` | `light.beispiel_licht_station_3/4` durch eigene Licht-Entities ersetzen |
| `cover.funkel_rollo_station_4_a` und `_b` | `cover.beispiel_rollo_station_4_a/b` durch eigene Rollos ersetzen |

Stelle `input_boolean.funkel_luna_browser_test` auf **off**, z. B. über Entwicklerwerkzeuge, oder ändere in der Geräte-Datei den Standard `initial: true` auf `initial: false`. Danach laufen echte Licht-/Rollo-Befehle und die originale Kodi-/ADB-Vorbereitung.

**Nicht** die logischen Entity-IDs umbenennen: Hauptpackage und Dashboard referenzieren genau diese Alias-Namen. Falls Home Assistant eine neue Alias-Entity mit Suffix `_2` anlegt, prüfe auf Namenskonflikte und korrigiere das Entity-Register, statt die Hauptskripte zu verändern.

## 5. Dashboard und Medien

Den Inhalt von `home-assistant/funkel_luna_dashboard.yaml` in den Rohkonfigurationseditor eines bestehenden Dashboards übernehmen.

- `media/Audio/*` nach `/media/funkel_luna/Audio/`
- `media/Video/*` nach `/media/funkel_luna/Video/`
- `media/References/*` enthält Referenzbilder und muss für den Spielablauf nicht auf HA installiert werden.

Die Media-Source-Pfade im Hauptpackage und die Clipnamen sind **unverändert**.

## 6. Funktionstest

Einzelclips starten, dann die Clipfolgen testen: 1A → 1B, 2B → 3A mit 10 Sekunden Übergang, 4B → 5A_1 mit 3 Sekunden Übergang und 6A → 6B_1; das Finale 6B_2 startet separat nach Erfolg. Auch sieben Erfolgskarten sowie MEDIEN-STOPP und Reset testen.

Die universellen Alias-Media-Player übernehmen den Wiedergabestatus vom zugewiesenen Player. Für automatische Übergänge muss Browser Mod zuverlässig `playing` und anschließend `idle` melden. Je nach Browser und Codec kann die Wiedergabe unterschiedlich ausfallen. **Die statische CI-Prüfung ersetzt keinen Test mit echter Home-Assistant-Instanz und Browser.**

Offizielle Hinweise: [Browser Mod](https://github.com/thomasloven/hass-browser_mod), [Universal Media Player](https://www.home-assistant.io/integrations/universal), [Home Assistant Packages](https://www.home-assistant.io/docs/configuration/packages).
