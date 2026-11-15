# Medienübersicht · Funkel & Luna

Zur öffentlichen Vorlage gehören **18 Audio-Clips, 6 Videos und 8 Referenzbilder**. Die Original-Dateinamen und Formate sind Bestandteil des Spielablaufs und dürfen nicht verändert werden.

## `media/Audio/` (18 Dateien)

- `Clip1A_1_Funkel.mp3`
- `Clip1A_2_Luna.mp3`
- `Clip1A_3_Funkel.mp3`
- `Clip2A_1_Luna.mp3`
- `Clip2A_2_Funkel.mp3`
- `Clip2A_3_Luna.mp3`
- `Clip3A_1_Funkel.mp3`
- `Clip3A_2_Luna.mp3`
- `Clip3B_1_Funkel.mp3`
- `Clip4A_1_Funkel.mp3`
- `Clip4A_2_Luna.mp3`
- `Clip4B_1_Funkel.mp3`
- `Clip5A_1_Luna.mp3`
- `Clip5A_2_Luna.mp3`
- `Clip5B_1_Funkel.mp3`
- `Clip5B_2_Luna.mp3`
- `Clip5C_1_Luna.mp3`
- `Clip5C_2_Luna.mp3`

## `media/Video/` (6 Dateien)

- `Clip1B_1.mp4`
- `Clip1B_2.mp4`
- `Clip2B.mp4`
- `Clip6A.mp4`
- `Clip6B_1.mp4`
- `Clip6B_2.mp4`

## `media/References/` (8 Dateien)

- `Funkel_und_Luna_am_Zauberwasserfall.png`
- `Funkel.png`
- `Hintergrund1B.png`
- `Hintergrund2A.png`
- `Hintergrund6A.png`
- `Hintergrund6B.png`
- `Luna.png`
- `Szene2A.png`

## Home-Assistant-Pfade

Die Audio- und Videodateien müssen in `/media/funkel_luna/Audio/` und `/media/funkel_luna/Video/` liegen. `References/` enthält Produktionsreferenzen für die Gestaltung und ist für den Ablauf nicht nötig.

**Vollständigkeit prüfen:** `python scripts/validate.py --require-media`, sobald die Konfigurations-PR und die Medien-PRs zusammengeführt sind. Die veröffentlichten Clips werden unverändert übernommen.
