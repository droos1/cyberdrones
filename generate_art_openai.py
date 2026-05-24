# /// script
# requires-python = ">=3.10"
# dependencies = ["openai>=1.50"]
# ///
"""Generate Costa Muerta scene art via OpenAI gpt-image-1, B&W ink style."""

import base64
import os
import sys
import time
from pathlib import Path

from openai import OpenAI

OUTPUT_DIR = Path.home() / "Desktop" / "Costa-Muerta-Art"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

client = OpenAI()

STYLE_PREFIX = (
    "Black and white ink illustration in the style of classic 1980s/1990s cyberpunk "
    "RPG rulebook art (think Cyberpunk 2020, Shadowrun, late-era Heavy Metal magazine). "
    "High contrast, heavy blacks, crosshatching, bold confident linework, no halftone gradients. "
    "Purely monochrome black ink on white background. No color whatsoever. "
    "Gritty, atmospheric, cinematic composition. Detailed architectural and figure work. "
    "Scene: "
)

SCENES = [
    {
        "filename": "01_convoy_south",
        "caption": "The Long Road — convoy heading south at dusk",
        "prompt": (
            "Wide establishing shot of a gritty cargo van and a flanking roadbike rider "
            "cruising south down a cracked old American interstate at dusk. Dust trails "
            "behind them. Abandoned rusted vehicles line the median. In the far background, "
            "the colossal silhouette of Night City's megastructure recedes, towers stacked "
            "like teeth against a smog-streaked sky. Vultures circle overhead. The road "
            "stretches into a heat-shimmer Free Fire Zone."
        ),
    },
    {
        "filename": "02_bicho_ambush",
        "caption": "Don Bicho's highway ambush",
        "prompt": (
            "Frenetic action scene on a sun-blasted desert highway. Three Mad-Max-style "
            "pickup truck technicals with autocannons mounted in the beds are closing on "
            "a fleeing cargo van. A heavily chromed raider warlord (lean, scarred, mantis-blade "
            "cyberarm extended) rides a hover-cycle alongside. A lone motorcycle rider — "
            "leather jacket, wild spiked hair, cyberarm pistol popping up — flanks the "
            "technicals and returns fire. Exhaust, dust trails, headlight lens flares, "
            "muzzle flashes. Dynamic diagonal composition with motion lines."
        ),
    },
    {
        "filename": "03_snakes_nest",
        "caption": "The Snake's Nest — Aldecaldos waystation",
        "prompt": (
            "Lived-in establishing shot of a converted gas station and motel complex on "
            "an old highway, ringed by junker trucks and buses welded together into walls. "
            "Smoke curls from a grill where someone is cooking. Aldecaldos Nomad kids run "
            "between vehicles. Two snipers in welding goggles lounge on a flat roof, rifles "
            "across their knees. A working outdoor stage where someone tunes an electric guitar. "
            "Marigold garlands strung between trucks for the coming Día de los Muertos. "
            "Warm-feeling community despite the post-apocalyptic shell."
        ),
    },
    {
        "filename": "04_mateo_office",
        "caption": "Mateo Cruz — the Aldecaldos elder",
        "prompt": (
            "Tight character portrait. An old Nomad warrior-elder, mid-60s, sits in a "
            "converted gas-station office. Snake tattoos coil up both bare forearms. The "
            "left half of his face is heavy with old burn scarring; the right half is sharp, "
            "weathered, eyes that miss nothing. A snake-mark coin hangs on a chain around "
            "his neck. He sits behind a wooden desk with a chess board mid-game, a wood "
            "stove behind him, a single bare bulb overhead. Low light, hard shadows, "
            "noir-style chiaroscuro."
        ),
    },
    {
        "filename": "05_la_frontera",
        "caption": "La Frontera — the border checkpoint",
        "prompt": (
            "Wide shot of a rusted-out US-Mexico border crossing. The old federal "
            "infrastructure is salt-weathered and corroded. A battery of salvaged anti-aircraft "
            "guns is bolted onto a watchtower. A long line of cargo trucks, motorcycles, and "
            "one impossibly old yellow taxi waits to cross. Uniformed checkpoint soldiers "
            "in mismatched-but-disciplined fatigues work the line — clipboards, scanners, "
            "vehicle searches. The whole operation has the feel of a TSA checkpoint run by "
            "a competent feudal warlord. Dawn light, long shadows."
        ),
    },
    {
        "filename": "06_la_viuda",
        "caption": "La Lucha Cromada — Reyna La Viuda mid-strike",
        "prompt": (
            "Inside a converted bullring at night, packed crowd of face-painted Día de los "
            "Muertos sugar skulls, sugar-skull patterns painted on every support column. "
            "Brass band visible on the side. In the ring: a Latina cyber-luchadora in a "
            "black-and-silver fighting suit, mid-Sandevistan strike — heavy chrome speed-blur "
            "trails behind her — a monomolecular fan blade extended but visibly *pulled* "
            "at the last microsecond. Her cyberarm sweeps in a glowing arc. Across from her, "
            "a bulky cyberarm street samurai (East Asian, spiked hair) braces for impact. "
            "Dramatic spot-lighting from above, deep shadows, motion lines."
        ),
    },
    {
        "filename": "07_plaza_santa_cecilia",
        "caption": "Plaza Santa Cecilia — Día de los Muertos buyer meet",
        "prompt": (
            "A pre-festival altar plaza in Tijuana, packed with marigolds, hanging "
            "photographs of the dead, candles, and pan de muerto on tables. A free-clinic "
            "tent on one side staffed by a calm matriarchal ripperdoc in black. A "
            "Militech-flagged parade float being assembled at the other end of the plaza, "
            "a sharp linen-suited man overseeing setup from a folding chair under a "
            "marigold awning. Three figures (two men, one between them) move across the "
            "plaza between the two tents. Sugar-skull-painted children dart between adults. "
            "Vivid Day-of-the-Dead atmosphere rendered in stark black ink."
        ),
    },
    {
        "filename": "08_tia_esme_cantina",
        "caption": "Tía Esmé — Cantina La Serpiente",
        "prompt": (
            "Interior of a Nomad-owned cantina in a compound on the edge of Tijuana. "
            "A senior Aldecaldos woman, lean, mid-50s, gray-streaked braid down one shoulder, "
            "a snake-mark coin on a chain at her throat, sits at a corner table with two "
            "bowls of birria steaming in front of her. Three figures sit across from her — "
            "smaller in the warm composition. Behind, a band plays norteño-electric "
            "(visible: an accordion, an electric guitar, a drummer), kids run between tables, "
            "bandana-and-leather Nomad crowd. Warm string lights overhead, deep shadows."
        ),
    },
    {
        "filename": "09_nueva_costa",
        "caption": "Nueva Costa — the rig city at sundown",
        "prompt": (
            "Sweeping establishing shot from a low-flying helicopter approaching at sundown. "
            "A daisy-chain of converted Pemex oil platforms lashed together over open Pacific "
            "ocean with gangways, cable bridges, and ropes. Strings of bare bulbs stretched "
            "between platforms. The central platform hosts a converted helicopter hangar — "
            "the Salón de la Casa Muerta — its facade lined with massive painted skulls and "
            "marigold garlands for Día de los Muertos. Other rigs host markets, ripperdoc "
            "clinics, residential quarters. The sun is half-below the ocean horizon, casting "
            "the whole rig city in dramatic backlit silhouette."
        ),
    },
    {
        "filename": "10_seccion_9_breach",
        "caption": "The Section-9 raid on the auction",
        "prompt": (
            "Chaotic action scene inside an elegant converted helicopter-hangar auction hall, "
            "the Salón de la Casa Muerta, lined with painted skulls and marigold garlands. "
            "The main double doors have just been breached — six Arasaka Section-9 tactical "
            "operators in light EVA-style stealth suits and full tactical masks are pushing "
            "in through smoke. A masked auctioneer in a black-and-gold skull mask stands "
            "frozen at the podium. In the foreground, an older matriarchal woman in a black "
            "dress draws a chrome derringer from her sleeve; nearby, a lean Nomad woman "
            "shouts tactical orders to two armed cousins. On a central glass pedestal: a "
            "sealed black-market case. Emergency red-lighting rendered as harsh black shadows."
        ),
    },
]


def generate_image(entry: dict, index: int, total: int) -> bool:
    filepath = OUTPUT_DIR / f"{entry['filename']}.png"
    if filepath.exists():
        print(f"[{index:>2}/{total}] SKIP (exists): {entry['filename']}.png", flush=True)
        return True

    full_prompt = STYLE_PREFIX + entry["prompt"]
    print(f"[{index:>2}/{total}] Generating: {entry['caption']}...", flush=True)

    try:
        response = client.images.generate(
            model="gpt-image-1",
            prompt=full_prompt,
            size="1536x1024",
            quality="medium",
            n=1,
        )
        b64 = response.data[0].b64_json
        if not b64:
            print(f"           WARNING: empty response for {entry['filename']}", flush=True)
            return False
        filepath.write_bytes(base64.b64decode(b64))
        print(f"           Saved: {filepath.name}", flush=True)
        return True
    except Exception as e:
        print(f"           ERROR: {e}", flush=True)
        return False


def main():
    total = len(SCENES)
    print(f"\nGenerating {total} Costa Muerta scenes via gpt-image-1...\n", flush=True)
    print(f"Output: {OUTPUT_DIR}\n", flush=True)

    success = 0
    failed = []
    for i, entry in enumerate(SCENES, 1):
        if generate_image(entry, i, total):
            success += 1
        else:
            failed.append(entry["filename"])
        if i < total:
            time.sleep(2)  # be gentle

    print(f"\n{'=' * 50}", flush=True)
    print(f"Done. {success}/{total} images generated.", flush=True)
    if failed:
        print(f"Failed: {', '.join(failed)}", flush=True)
    print(f"Output: {OUTPUT_DIR}", flush=True)


if __name__ == "__main__":
    main()
