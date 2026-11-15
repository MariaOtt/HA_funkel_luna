#!/usr/bin/env python3
"""Statischer Konsistenztest für die zentrale Funkel-&-Luna-Gerätezuordnung.

Dies ist kein Ersatz für einen Home-Assistant-Konfigurations- und Gerätetest.
"""
from pathlib import Path
import re
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
PATHS = {
    "package": ROOT / "home-assistant/funkel_luna_package.yaml",
    "dashboard": ROOT / "home-assistant/funkel_luna_dashboard.yaml",
    "devices": ROOT / "home-assistant/funkel_luna_geraete.yaml",
}
EXPECTED_MEDIA = {
    *(f"media_player.funkel_audio_station_{i}" for i in range(1, 6)),
    "media_player.funkel_kodi_station_1",
    "media_player.funkel_kodi_station_6",
    "media_player.funkel_tv_station_1",
    "media_player.funkel_tv_station_6",
}
EXPECTED_LIGHTS = {"light.funkel_effekt_station_3", "light.funkel_effekt_station_4"}
EXPECTED_COVERS = {
    "cover.funkel_rollo_station_4_a",
    "cover.funkel_rollo_station_4_b",
}
ENTITY_PATTERN = re.compile(r"\\b(?:media_player|light|cover)\\.funkel_[a-z0-9_]+\\b")
FORBIDDEN = re.compile(
    r"(?i)(josefine|karolina|homematicip_local|00165d89bbaec0|nrl_|"
    r"tvkueche|tvwohnzimmer|chatgpt\\.com/share)"
)


def check() -> None:
    text = {name: path.read_text(encoding="utf-8-sig") for name, path in PATHS.items()}
    config = {name: yaml.safe_load(content) for name, content in text.items()}
    assert all(isinstance(value, dict) for value in config.values()), "YAML-Wurzel ungueltig"

    for name, value in text.items():
        if FORBIDDEN.search(value):
            raise ValueError(f"Private Altkennung in {name} gefunden")

    package = config["package"]
    dashboard = config["dashboard"]
    devices = config["devices"]

    assert len(package.get("script", {})) == 29, "Hauptpackage: 29 Skripte erwartet"
    assert len(package.get("automation", [])) == 6, "Hauptpackage: 6 Automationen erwartet"
    assert len(dashboard.get("views", [])) == 7, "Dashboard: sieben Views erwartet"

    testmode = devices.get("input_boolean", {}).get("funkel_luna_browser_test", {})
    assert testmode.get("initial") is True, "Browser-Testmodus muss standardmaessig an sein"

    players = devices.get("media_player", [])
    assert len(players) == 9, "Neun logische Media-Player erwartet"
    actual = set()
    for player in players:
        assert player.get("platform") == "universal", "Player muss Universal-Alias sein"
        alias = f"media_player.{player['name']}"
        actual.add(alias)
        assert player.get("children") and len(player["children"]) == 1, alias + " ohne Zielplayer"
    assert actual == EXPECTED_MEDIA, "Unerwartete Media-Player-Aliasse"

    tpl = devices.get("template", [])
    assert isinstance(tpl, list), "Template-Entities fehlen"
    lights = {
        "light." + item["name"]
        for entry in tpl for item in entry.get("light", [])
    }
    covers = {
        "cover." + item["name"]
        for entry in tpl for item in entry.get("cover", [])
    }
    assert lights == EXPECTED_LIGHTS, "Licht-Aliasse unvollstaendig"
    assert covers == EXPECTED_COVERS, "Rollo-Aliasse unvollstaendig"

    used = set(ENTITY_PATTERN.findall(text["package"] + text["dashboard"]))
    missing = used - (EXPECTED_MEDIA | EXPECTED_LIGHTS | EXPECTED_COVERS)
    assert not missing, "Nicht konfigurierte Geräte: " + ", ".join(sorted(missing))

    kodi = package["script"]["funkel_luna_kodi_vorbereiten"]["sequence"]
    guard = kodi[0].get("if", [{}])[0] if kodi else {}
    assert guard.get("entity_id") == "input_boolean.funkel_luna_browser_test", (
        "Browser-Testmodus muss die Kodi-/ADB-Vorbereitung ueberspringen"
    )
    assert kodi[0].get("then", [{}])[0].get("stop"), "Browser-Kodi-Guard fehlt"

    print("OK: 29 Skripte, 6 Automationen, 7 Views, 9 Player, 2 Lichter, 2 Rollos")
    print("OK: Browser-Mod-Testmodus ist aktiv, Kodi-Vorbereitung wird uebersprungen")
    print("Hinweis: Laufzeittest mit registriertem Browser-Mod-Player bleibt erforderlich")


if __name__ == "__main__":
    try:
        check()
    except (AssertionError, ValueError, OSError, yaml.YAMLError, KeyError, IndexError, TypeError) as exc:
        print(f"FEHLER: {exc}", file=sys.stderr)
        sys.exit(1)
