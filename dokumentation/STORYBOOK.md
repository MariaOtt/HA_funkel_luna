# Funkel & Luna · Storybook und Technikregie

**Version:** Hauptpackage 4.17 · Dashboard 4.19 · sechs Stationen und sieben Aufgaben.

Funkel, ein Drache, und Luna, ein Einhorn, führen durch sechs magische Stationen. Audio- und Videoszenen werden über Home Assistant ausgelöst. Die Spielleitung kann Aufgaben starten, Ergebnisse bestätigen und die Medien einzeln steuern.

| Station | Geschichte | Home-Assistant-Ablauf |
| --- | --- | --- |
| **1 · Drachennest** | Nest entdecken und Hilferuf wahrnehmen | 1A: drei Audios; danach 1B: zwei Videos |
| **2 · Regenbogen** | Regenbogen reparieren und Fundstück finden | 2A: drei Audios; Erfolg startet 2B (Video); 3A folgt mit zehn Sekunden Verzögerung |
| **3 · Zaubersteine** | Kartoffel-/Zaubersteine finden | 3A: zwei Audios; Erfolg startet 3B (Audio) |
| **4 · Lavafeld** | Lavafeld bewältigen | 4A: zwei Audios und Lichteffekt; Erfolg startet 4B; danach 5A_1 nach drei Sekunden |
| **5 · Schlüssel & Ei** | Glitzerschlüssel zusammensetzen und Drachenei finden | 5A_1 als Vorabansage, 5A_2 bei Stationsstart; separate Erfolgskarten für 5B und 5C |
| **6 · Schatz** | Schatz suchen und Finale erleben | 6A startet 6B_1; nach Bestätigung des Schatzfunds folgt 6B_2 separat |

Die Hauptansicht enthält Fortschritt, aktuelle Station, Spielvorbereitung, Medien-Stopp und Reset. Jede Station hat eine eigene Einzelsteuerung. Alle Abläufe bleiben im einzigen Hauptpackage erhalten.

Die 24 Originalclips werden unter `media/Audio/` und `media/Video/` bereitgestellt.
