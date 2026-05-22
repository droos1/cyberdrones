"""Generate black & white cyberpunk RPG illustrations using Gemini Nano Banana."""

import os
import sys
import time
import base64
from pathlib import Path

from google import genai
from google.genai import types

OUTPUT_DIR = Path(__file__).parent / "artwork"
OUTPUT_DIR.mkdir(exist_ok=True)

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

STYLE_PREFIX = (
    "Black and white ink illustration in the style of classic 1980s/1990s cyberpunk "
    "RPG rulebook art. High contrast, heavy blacks, crosshatching, bold linework. "
    "No color, purely monochrome black ink on white. "
    "Gritty, detailed, atmospheric. "
)

IMAGES = [
    # --- CHARACTERS ---
    {
        "filename": "solo_portrait",
        "caption": "The Solo — Street Samurai",
        "category": "Characters",
        "prompt": (
            "Portrait of a cyberpunk street samurai / solo mercenary. East Asian male, "
            "wild spiked hair, intense eyes, mechanical cyberarm with visible hydraulics "
            "on left side, wearing a battered armored bodysuit. Assault rifle slung across back. "
            "Scars and chrome. Urban decay background with neon signage. Waist-up portrait."
        ),
    },
    {
        "filename": "fixer_portrait",
        "caption": "The Fixer — Deal Maker",
        "category": "Characters",
        "prompt": (
            "Portrait of a cyberpunk fixer / deal-maker. East Asian male with a sharp mohawk, "
            "ritual scarification on cheeks and neck, wearing expensive high-fashion street clothes — "
            "tailored jacket over armored vest. Confident smirk, voice stress analyzer visible "
            "as a subtle throat implant. Smoke curling from a cigarette. Night city alley background."
        ),
    },
    {
        "filename": "netrunner_portrait",
        "caption": "Digitz — The Netrunner",
        "category": "Characters",
        "prompt": (
            "Portrait of a cyberpunk netrunner / hacker. Pacific Islander male, young, "
            "short spiked hair, urban flash clothing style — tech-wear jacket with glowing "
            "data cables. Neural interface port visible on temple. Holding a tanto knife "
            "in one hand. Expression of cool detachment. Digital code fragments floating "
            "in background. Waist-up portrait."
        ),
    },
    {
        "filename": "ryla_vox",
        "caption": "Ryla Vox — Investigative Journalist",
        "category": "Characters",
        "prompt": (
            "Portrait of a cyberpunk investigative journalist / media personality. "
            "Young woman, determined expression, press credentials around neck, "
            "recording cybereye with subtle red recording light, wearing a rumpled "
            "trench coat over street clothes. Holding a microphone-shaped data recorder. "
            "News screens and holographic displays in background showing breaking news."
        ),
    },
    {
        "filename": "dr_voss",
        "caption": "Dr. Yuki Voss — Underground Ripperdoc",
        "category": "Characters",
        "prompt": (
            "Portrait of a cyberpunk underground surgeon / ripperdoc. Japanese woman, "
            "middle-aged, calm and precise, wearing surgical scrubs under a heavy apron, "
            "cybernetic magnification lenses flipped up on forehead, surgical tools in hand. "
            "Behind her: a pristine but hidden operating room with chrome surgical arms "
            "and banks of medical monitors. Sterile contrast to the gritty world outside."
        ),
    },
    {
        "filename": "cpl_reyes",
        "caption": "Cpl. Reyes — Arasaka Recovery Team",
        "category": "Characters",
        "prompt": (
            "Portrait of a corporate military operator / squad leader. Latino male, "
            "professional and cold, wearing heavy tactical armor with Arasaka corporate "
            "logo, assault rifle at ready, tactical visor over one eye, radio headset. "
            "Behind him, his tactical squad stacks up in silhouette. Urban warfare setting."
        ),
    },
    # --- ADVENTURE 1 SCENES ---
    {
        "filename": "scene_awakening",
        "caption": "The Awakening — \"Why are we on the news?\"",
        "category": "Adventure 1: Cyber Drones",
        "prompt": (
            "Three cyberpunk mercenaries in a dingy safehouse, staring in horror at a "
            "wall-mounted television screen showing security footage of themselves "
            "committing a massacre they don't remember. One clutches his head in confusion, "
            "another reaches for a weapon. The room is cramped — mattresses on floor, "
            "takeout containers, drawn blinds with neon light leaking through. "
            "The TV casts harsh light on their faces. Dramatic noir lighting."
        ),
    },
    {
        "filename": "scene_pachinko",
        "caption": "The Pachinko Parlor — Hacking Under Neon",
        "category": "Adventure 1: Cyber Drones",
        "prompt": (
            "Interior of a seedy cyberpunk pachinko parlor. A netrunner sits at a machine, "
            "secretly jacking a data cable into a hidden port beneath the console while "
            "pretending to play. Rows of flashing pachinko machines stretch into the distance. "
            "Other patrons are oblivious. A suspicious guard approaches from the background. "
            "Sensory overload of screens and chrome. Overhead view looking down at an angle."
        ),
    },
    {
        "filename": "scene_arasaka_assault",
        "caption": "Level 17 — Assault on Arasaka Tower",
        "category": "Adventure 1: Cyber Drones",
        "prompt": (
            "Dramatic action scene: cyberpunk mercenaries breaching a sterile corporate "
            "laboratory floor. One kicks through a reinforced door, assault rifle blazing. "
            "Corporate security guards in tactical gear return fire from behind overturned "
            "desks and server racks. Laser beams cut through smoke. A massive signal "
            "transmitter tower/antenna dominates the room's center. Shattered glass, "
            "sparking electronics, chaos. Dynamic diagonal composition."
        ),
    },
    # --- ADVENTURE 2 SCENES ---
    {
        "filename": "scene_fire_escape",
        "caption": "Dead Signal — The Escape",
        "category": "Adventure 2: Dead Signal",
        "prompt": (
            "Three figures descending a rusted, collapsing fire escape on the side of a "
            "massive cyberpunk building at night. An AV (flying police vehicle) sweeps a "
            "searchlight beam across the building face, barely missing them. The city sprawls "
            "far below — towers, neon, smog, traffic. One figure hangs by one arm as the "
            "metal gives way. Rain and sparks. Vertigo-inducing perspective looking down."
        ),
    },
    {
        "filename": "scene_kojos_safehouse",
        "caption": "Kojo's Safehouse — The Shipping Container",
        "category": "Adventure 2: Dead Signal",
        "prompt": (
            "Interior of a converted shipping container used as a safehouse in the dockyards. "
            "A nervous fixer (African male, chain-smoking, gold rings) sits across from "
            "the team at a makeshift table. On the table: a military-grade counter-battery "
            "radar system — chunky military hardware with targeting screens. Dim lighting "
            "from a single hanging bulb. Stacked crates line the walls. Paranoid atmosphere."
        ),
    },
    {
        "filename": "scene_depot_heist",
        "caption": "The Depot Job — Northside Medical Heist",
        "category": "Adventure 2: Dead Signal",
        "prompt": (
            "Silhouettes of cyberpunk operatives breaking into a Trauma Team medical warehouse "
            "at night. One figure bypasses a security panel while another watches for guards. "
            "A third crouches by a locked medical storage cabinet. Guard dogs patrol in the "
            "distance. Motion sensor beams visible as thin lines. Industrial setting — "
            "loading docks, medical supply crates with red crosses. Stealth and tension."
        ),
    },
    {
        "filename": "scene_clinic_siege",
        "caption": "The Siege at Tanaka's Fish Market",
        "category": "Adventure 2: Dead Signal",
        "prompt": (
            "Climactic battle scene: a hidden clinic behind a fish market under assault. "
            "Outside, corporate tactical operators with sniper rifles on rooftops fire down. "
            "Inside the fish market, a massive full-borg cyborg (hulking chrome humanoid) "
            "defends the entrance, ripping apart cover. Through a doorway in the back, "
            "a surgeon operates on a patient under bright surgical lights while combat "
            "rages around her. Explosions, gunfire, fish market stalls destroyed. Split "
            "composition showing interior and exterior simultaneously."
        ),
    },
    {
        "filename": "scene_extraction",
        "caption": "The Extraction — Pulling the Droneware",
        "category": "Adventure 2: Dead Signal",
        "prompt": (
            "Close-up medical horror scene: a ripperdoc surgeon carefully extracts "
            "thread-thin cybernetic implants from the base of a patient's skull. "
            "The droneware — sinister black filaments with tiny blinking nodes — is being "
            "pulled free with specialized surgical tools. Medical monitors show neural "
            "activity patterns. The patient is conscious, gritting teeth. Bright surgical "
            "light creates extreme contrast. Detailed, almost technical-manual illustration."
        ),
    },
    # --- MOOD / SETTING ---
    {
        "filename": "night_city_skyline",
        "caption": "Night City — The Urban Sprawl",
        "category": "Setting & Mood",
        "prompt": (
            "Panoramic cityscape of a massive cyberpunk megacity at night. Towering "
            "corporate arcology buildings dominate the skyline, covered in holographic "
            "advertisements. Below, a maze of smaller buildings, elevated highways, "
            "and neon-lit streets. Flying vehicles (AVs) cruise between towers. "
            "Smog layer cuts the buildings at mid-height. A massive Arasaka corporate "
            "logo glows on the tallest tower. Wide format, establishing shot. "
            "Incredibly detailed architectural linework."
        ),
    },
    {
        "filename": "droneware_diagram",
        "caption": "DRONEWARE MK.III — Technical Schematic",
        "category": "Setting & Mood",
        "prompt": (
            "Technical diagram / blueprint style illustration of illegal military cyberware. "
            "Shows a human nervous system with cybernetic implants threaded along the spine "
            "and into the brain stem. Callout labels point to components: signal receiver, "
            "motor override nodes, memory suppressor, neural bridge. Style of a military "
            "technical manual or medical textbook illustration. Clean linework, annotation "
            "arrows, cross-section views. Schematic / blueprint aesthetic with black lines "
            "on white background."
        ),
    },
]


def generate_image(entry: dict, index: int, total: int) -> bool:
    """Generate a single image and save it."""
    filepath = OUTPUT_DIR / f"{entry['filename']}.png"
    if filepath.exists():
        print(f"  [{index}/{total}] SKIP (exists): {entry['filename']}")
        return True

    full_prompt = STYLE_PREFIX + entry["prompt"]
    print(f"  [{index}/{total}] Generating: {entry['caption']}...")

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-image",
            contents=[full_prompt],
            config=types.GenerateContentConfig(
                response_modalities=["TEXT", "IMAGE"],
            ),
        )

        for part in response.parts:
            if part.inline_data is not None:
                image = part.as_image()
                image.save(str(filepath))
                print(f"           Saved: {filepath.name}")
                return True

        print(f"           WARNING: No image in response for {entry['filename']}")
        # Try to print any text response for debugging
        for part in response.parts:
            if part.text:
                print(f"           Response text: {part.text[:200]}")
        return False

    except Exception as e:
        print(f"           ERROR: {e}")
        return False


def main():
    total = len(IMAGES)
    print(f"\nGenerating {total} cyberpunk illustrations...\n")

    success = 0
    failed = []

    for i, entry in enumerate(IMAGES, 1):
        ok = generate_image(entry, i, total)
        if ok:
            success += 1
        else:
            failed.append(entry["filename"])

        # Rate limiting - be gentle with the API
        if i < total:
            time.sleep(3)

    print(f"\n{'='*50}")
    print(f"Done! {success}/{total} images generated.")
    if failed:
        print(f"Failed: {', '.join(failed)}")
    print(f"Output directory: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
