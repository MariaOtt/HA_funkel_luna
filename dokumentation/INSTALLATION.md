# Installation und Anpassung

## 1. Home Assistant sichern
Erstelle ein Backup deiner Home-Assistant-Instanz. Prüfe Packages-Unterstützung und die Medienquelle `local`.

## 2. Beispiel-Geräte-IDs ersetzen
Die externe Hardware ist absichtlich anonymisiert. **Ersetze alle Vorkommen** in `home-assistant/funkel_luna_package.yaml` **und** `home-assistant/funkel_luna_dashboard.yaml`, auch in Jinja-Vorlagen und Einzelsteuerungen:

| Beispiel-Entity-ID | Funktion |
| --- | --- |
| `media_player.funkel_audio_station_1` | Audio Station 1 |
| `media_player.funkel_audio_station_2` | Audio Station 2 |
| `media_player.funkel_audio_station_3` | Audio Station 3 |
| `media_player.funkel_audio_station_4` | Audio Station 4 |
| `media_player.funkel_audio_station_5` | Audio Station 5 |
| `media_player.funkel_tv_station_1` | Video-Gerät Station 1 (ADB/Fire TV) |
| `media_player.funkel_tv_station_6` | Video-Gerät Station 6 (ADB/Fire TV) |
| `media_player.funkel_kodi_station_1` | Kodi-Player Station 1 |
| `media_player.funkel_kodi_station_6` | Kodi-Player Station 6 |
| `light.funkel_effekt_station_3` | Lichteffekt Station 3 |
| `light.funkel_effekt_station_4` | Lichteffekt Station 4 |
| `cover.funkel_rollo_station_4_a` | Rollo A (Station 4) |
| `cover.funkel_rollo_station_4_b` | Rollo B (Station 4) |

Die internen `funkeI_luna`-Helfer und Skripte (Schreibweise: `funkel_luna`) sind Bestandteile des Packages und sollen unverändert bleiben. Die Stellen `Medienzone_1` und `Spielbereich 6` im Skript zur Kodi-Vorbereitung sind interne Auswahlwerte und müssen übereinstimmen.

## 3. Package übernehmen
```yaml
homeassistant:
  packages: !include_dir_named packages
```

Falls noch nicht vorhanden, die Package-Einbindung in `configuration.yaml` ergänzen. Das **eine** Package nach `/config/packages/funkel_luna_package.yaml` kopieren. YAML-Konfiguration prüfen und Home Assistant neu starten.

## 4. Dashboard importieren
Das YAML `home-assistant/funkel_luna_dashboard.yaml` als Rohkonfiguration für ein bestehendes Dashboard übernehmen. Benötigt werden Mushroom Cards und Ring-Tile Card.

## 5. Medien bereitstellen
- `media/Audio/*` nach `/media/funkel_luna/Audio/`
- `media/Video/*` nach `/media/funkel_luna/Video/`
- `media/References/*` sind Referenzbilder und für den Betrieb nicht erforderlich

Die Mediennamen und Media-Source-Pfade sind in der Vorlage unverändert.

## 6. Test
Einzelclips vor kompletten Folgen testen. Prüfe Station 1 (Audio → Video), Regenbogen → Station 3 (10 s Verzögerung), Lavafeld → Station 5 (3 s Verzögerung), die sieben Erfolgskarten und den separaten Schlussclip 6B_2. Bei fehlenden Geräten funktionieren die betreffenden Szenen nicht.

Die Vorlage ist **kein sofort lauffähiger Komplettimport**, sondern das vollständige Skript- und Dashboardgerüst, das an die eigene HA-Installation angepasst werden muss.
