# Cyberdrones — Quick Start for Claude

This repo is a **Cyberpunk RED tabletop RPG campaign**. Daniel is the GM. The "code" here is just tooling for generating art and printing PDFs — the real artifacts are the markdown adventures.

## Cast (do not relearn this from files every time)

**Players**
- **Fredrik** — Solo, combat specialist. East Asian, wild spiked hair, Pop-up Very Heavy Pistol cyberarm. In therapy (Humanity 18/40).
- **Mats** — Fixer, social/connections. Mohawk, ritual scars, businesswear. Operator Rank 5.

**GM-run**
- **Daniel** — GM. Also runs **Digitz** (Netrunner) as GMPC. Olof may take Digitz over if he ever joins.

Full PC stats and loadouts: `campaign/player-characters.md`. Character sheet photos: `campaign/character-sheets/`. NPC quick-reference: `campaign/npc-cheat-sheet.md`.

## Repo Layout

```
adventures/
  01-cyber-drones/   adventure.md + session-notes.md (COMPLETE)
  02-dead-signal/    adventure.md + adventure.pdf + map-clinic.svg + map-depot.svg
  03-...             (next adventure goes here)
campaign/
  player-characters.md      single source of truth for PC sheets
  character-sheets/         photos of physical sheets
artwork/                    generated B&W ink illustrations + gallery.html
generate_art.py             Gemini Nano Banana image generator
print.css                   styles for adventure-md → PDF
```

## Adventure Status

| # | Title | Status |
|---|-------|--------|
| 1 | Cyber Drones | Completed 2024-02-03 — session notes filed |
| 2 | Dead Signal | Completed ~April 2026 — session notes filed |
| 3 | Costa Muerta | First draft of adventure.md filed; details still in flight |

**Adventure 3 frame ("Costa Muerta"):** Players go south to sell two droneware units on the black market. Tijuana + Nueva Costa (offshore Free-City rig). Day of the Dead aesthetic. Cyber-lucha credibility gate. Four buyers including a trap (Arasaka counterintel under cover). Auction-night Section-9 raid as climax. Combat variety: highway ambush (vehicle) / Aldecaldos camp defense (Ricochet) / cyber-lucha (melee) / safehouse robbery (urban CQB) / auction siege.

**Continuity carrying into Adventure 4:** Mole exfil-network mystery, Don Bicho road grudge, Aldecaldos family bond (if taken), Militech call-in debt (if sold to Vega), Tanaka file (captured or escaped), Reyna Solano wanting out of the lucha circuit.

## How adventures are written

Look at `adventures/02-dead-signal/adventure.md` as the template. Style conventions:

- Markdown, structured by Parts (Part 1, Part 2, …) with a "Background", "Major NPCs" table, and "Timeline" up top
- NPC stat blocks in tables: `| Type | SP | HP | Weapon | Notes |`
- `**GM Note:**` blockquotes/paragraphs for pacing and out-of-fiction guidance
- Italic blockquotes for read-aloud / NPC dialogue
- Cyberpunk RED DV scale used: 11 / 13 / 15 / 17 / 19 (Easy → Very Hard)
- Map diagrams as ascii in fenced blocks OR as separate `map-*.svg` files
- Final section is always an "Aftermath" / epilogue that sets up the next adventure

## Tooling

**Generate artwork** (only when explicitly asked — costs API credits):
```
GEMINI_API_KEY=… uv run generate_art.py
```
Skips files that already exist. Add new entries to the `IMAGES` list in `generate_art.py`.

**Render adventure to PDF** (via `invoke` + pandoc + weasyprint; print.css drives layout):
```
invoke render-pdf -a 03-costa-muerta              # by adventure slug
invoke render-pdf -a adventures/02-dead-signal/adventure.md   # by path
```
Output PDF lands next to the adventure.md.

## When picking up a new session

1. Skim recent commits (`git log --oneline`) for what changed since last time
2. Read the latest adventure md and its session-notes.md if it exists
3. Check `campaign/player-characters.md` for current HP/Humanity/loadout state
4. Ask Daniel what was decided in the last session before drafting the next one — session notes may lag
