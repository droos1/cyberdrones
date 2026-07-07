# Cyberpunk RED — Rules Quick Reference

Minimal cheat sheet for at-the-table fast lookup. The core book has the full rules and the detail tables (hit locations, ammo types, critical injury table, cyberware Humanity costs, netrunning architecture). This file is just enough to spot-check during play and to size up NPC stats on the fly.

> **This sheet now follows the official Cyberpunk RED core rules,** with **one deliberate house rule:** the campaign's compressed Difficulty Value ladder (11 / 13 / 15 / 17 / 19), because that's what every adventure in `adventures/` is written to. It's flagged with 📖 below; everything else here is book-accurate.

---

## The one house rule: the DV ladder

| | Easy | Standard | Difficult | Hard | Very Hard |
|--|------|----------|-----------|------|-----------|
| **This campaign** | 11 | 13 | 15 | 17 | 19 |
| **Official RED** | *(none)* | 13 Everyday | 15 Difficult | 17 Professional | 21 Heroic · 24 Incredible |

The middle of the ladder (13 / 15 / 17) already matches the book — the campaign just adds an easier **DV 11** tier and caps the top at **19** instead of the book's 21 / 24. Kept on purpose so the DVs baked into the adventures stay calibrated. Everything else in this file is the book rule as written.

---

## Skill Checks

**Formula:** `1d10 + STAT + SKILL  vs.  DV`

- **Natural 10** on the d10 → roll *another* d10 and **add** (exploding success). Chains.
- **Natural 1** on the d10 → roll *another* d10 and **subtract** (critical failure). Chains.

**Campaign DV scale** (matches what's used in `adventures/`):

| DV | Difficulty | Example |
|----|-----------|---------|
| 11 | Easy | Hailing a cab, basic stealth in dim cover |
| 13 | Standard | Routine professional task, awareness in a crowd |
| 15 | Difficult | Hacking a panel under pressure, hard negotiation, fooling a guard |
| 17 | Hard | Cross a collapsing rooftop, talk a corp exec into a real concession |
| 19 | Very Hard | Spot the Arasaka watch logo in dim light, talk a pro killer into walking away |

> 📖 **Official ladder:** 13 Everyday · 15 Difficult · 17 Professional · 21 Heroic · 24 Incredible. Ours compresses/renames it (13/15/17 line up; 11 and 19 are house).

**Opposed checks:** both sides roll, highest wins, ties favor defender.

---

## Combat Turn Structure

**Initiative:** `1d10 + REF` (no skill bonus). Rolled once at combat start; order holds.

**Each turn, choose:**
- **Move Action** (up to **MOVE ×2** metres) **+ 1 Action**
- *or* **Run** — spend your Action on a second Move Action for **MOVE ×4** metres total (no attack)

**Common Actions:** attack, aimed shot, autofire, suppressive fire, reload, draw weapon, skill use, brace, dodge, pick someone up.

**Defending:**
- **Dodge** ranged: `1d10 + DEX + Evasion` vs. attacker's roll — but **only if you have REF 8+** (otherwise you can't dodge bullets). Most NPCs don't bother; they take the hit and rely on armor.
- **Block / Parry** melee: `1d10 + DEX + Melee or Brawling` vs. attacker's roll.

---

## Attack Rolls

**Ranged:** `1d10 + REF + Weapon Skill` vs. target's defense (their Evasion roll, or DV by range if they don't dodge).

**Ranged DV by range & weapon** (the DV to hit — each weapon type has its own row):

| Range | Pistol | Shotgun (shell) | Assault Rifle |
|-------|--------|-----------------|---------------|
| 0–6m | 13 | 13 | 17 |
| 7–12m | 15 | 15 | 16 |
| 13–25m | 20 | 20 | 15 |
| 26–50m | 25 | 25 | 13 |
| 51–100m | 30 | 30 | 15 |
| 101–200m | 30 | 35 | 20 |
| 201–400m | — | — | 25 |
| 401–800m | — | — | 30 |

Pistols and shotguns are close-range tools — cheap DVs out to ~25m, brutal past that. Rifles stay usable far out (an AR is *easiest* at 26–50m). SMGs track the pistol column closely; snipers mirror the rifle (poor up close, best at range) — check the book for the exact SMG, sniper, bow and grenade rows.

**Melee:** `1d10 + DEX + Melee Weapon or Brawling` vs. defender's Evasion or Block.

**Autofire:** Roll the **Autofire skill** (`1d10 + REF + Autofire`) vs the target's normal range DV. Damage = **2d6 × (how much you beat the DV by)**, capped at the gun's Autofire rating (**SMG ×3, Assault Rifle ×4**). Only works at **≤25m**.

**Suppressive Fire:** Spend a **Full Action + 10 rounds** to saturate an area (~8×8m). **No damage** — it's area denial: anyone caught in the zone who does anything other than stay/move in cover is penalised. Pins heads down.

**Aimed Shot:** -8 to roll, choose location (most often head = damage ×2 after head armor).

---

## Damage

1. Roll weapon dice
2. Subtract target's **SP** (Stopping Power) at the relevant location
3. Remaining = HP loss
4. **Ablation:** each hit that penetrates armor reduces that armor's SP by 1 (AP ammo ablates by 2)
5. **Critical Injury:** roll **two or more 6s** on the damage dice → the target takes **+5 bonus damage straight to HP (ignoring armor)** *and* a Critical Injury (roll on the Head or Body table, or pick a fast-play effect below)

**Headshot:** damage doubled *after* head armor is applied.
**Armor-Piercing ammo:** halves the target's SP for that hit (round up) and ablates that armor by 2 instead of 1.

**Weapon damage at-a-glance (use for NPCs):**

| Weapon | Damage | ROF | Typical Range |
|--------|--------|-----|---------------|
| Light Pistol | 1d6 | 2 | 50m |
| Medium Pistol | 2d6 | 2 | 50m |
| Heavy Pistol | 3d6 | 2 | 50m |
| Very Heavy Pistol | 4d6 | 1 | 50m |
| SMG / Heavy SMG | 2d6 / 3d6 | 1 (autofire 3) | 50m |
| Shotgun (slug) | 5d6 | 1 | 50m |
| Assault Rifle | 5d6 | 1 (autofire 4) | 400m |
| Sniper Rifle | 5d6 | 1 | 800m |
| Combat Knife / Light Melee | 1d6 | 2 | melee |
| Heavy Melee (sword, axe) | 3d6 | 2 | melee |
| Big Knux (brawling+) | 2d6 | 2 | melee |
| Frag Grenade | 6d6 | — | 8m radius |

---

## Critical Injuries

**Natural 10 on a roll** explodes that roll — roll again and add. On an **attack roll** that just means a bigger to-hit total (it can turn a near-miss into a hit); it does **not** add to damage. RED has no separate bonus-damage "critical hit."

**Critical Injury (two or more 6s in the damage roll):** on top of the +5 bonus damage, the target suffers a lasting injury. Roll on the Body or Head Critical Injury table in the book, OR — for fast play — pick from this lazy substitute:

| Quick Crit Effect | Use For |
|-------------------|---------|
| Broken arm — that weapon disabled until First Aid + downtime | Limb hits |
| Concussion — -2 to all INT/REF actions for rest of combat | Head hits |
| Bleeding — 1d6 / round until First Aid stops it | Generic torso |
| Crushed leg — MOVE halved | Lower body |
| Lost eye — -4 to ranged attacks permanently until replaced | Headshot crits |

When in doubt: **-2 to all rolls for the rest of the fight** is the boring default.

---

## Wounded States & Death

**HP brackets:**

| State | Threshold | Effect |
|-------|-----------|--------|
| **Lightly Wounded** | > HP/2 | No penalty |
| **Seriously Wounded** | ≤ HP/2 | **−2 to all rolls.** Pain Editor cyberware ignores this. |
| **Mortally Wounded** | 0 or below | **−4 to all Checks, −6 MOVE** (min 1); Death Save each turn; auto-Critical Injury if hit again. *Not* unconscious — you can still act. |

**Death Save (start of each turn while Mortally Wounded):**
- Roll `1d10 + cumulative death-save penalty`. If the total is **under your BODY**, you survive the turn and act normally. **A natural 10 always fails.**
- Penalty starts at 0, **+1 per save attempt** (and +1 whenever you're hit while down) — so it gets harder each turn.
- Surviving a save does **not** stabilize you; you keep rolling every turn until treated.
- **Stabilize:** a **First Aid or Paramedic check, DV 15**. Success ends the Death Saves and leaves the character at 1 HP (unconscious).

---

## Healing

| Method | Effect | Notes |
|--------|--------|-------|
| **First Aid** (TECH + First Aid; DV 15 to stabilize, DV 13 to treat some injuries) | **No HP** — stabilizes the dying and treats specific Critical Injuries | Does not restore hit points |
| **Paramedic / Medtech** | Stabilizes; a Medtech restores HP via **Surgery** & pharma over downtime | The real source of HP recovery besides rest |
| **Natural rest** | **BODY HP per full day** of rest (once stabilized) | Cumulative |
| **Speedheal / drugs** | Some consumables restore HP | See gear lists |

> **No mid-combat topping-up:** by the book you can't just First-Aid someone back to fighting shape during a fight — HP returns over downtime. If you want faster in-scene healing for pacing, make that a deliberate house call.

---

## NPC Quick-Build Reference

For sizing NPCs on the fly. Stat-block columns to fill: `| Type | SP | HP | Weapon | Notes |`

### HP Tiers

| Tier | HP | Rough Stats | Examples |
|------|----|-----------|----------|
| **Mook / Goon** | 20-30 | BODY 4-5, no specials, single weapon | Street thug, low-rent gangbanger |
| **Pro / Lieutenant** | 35-45 | BODY 5-7, one signature trick (Kerenzikov, cyberlimb, etc.), decent armor | Corp guard, raider crew member, Pacers |
| **Boss / Specialist** | 50-60 | BODY 7-9, heavy armor, named cyberware, multiple-action economy | Cpl. Reyes, Doña Esperanza's bodyguard, Section-9 op |
| **Mini-Boss / Borg** | 60-80+ | BODY 8-10, full-borg or SP 18+, premium weapons | Udo, El Padre, Section-9 Team Lead |

### SP (Armor) Tiers

| SP | Typical Kit |
|----|------|
| 7 | Light / civilian (leathers) |
| 11 | Standard bodyweight suit (most working pros) |
| 13 | Light Armorjack |
| 15 | Medium Armorjack / Bodyweight + Subdermal |
| 17-18 | Heavy Armorjack / full-borg plating |
| 20+ | Metalgear / vehicle-grade |

### To-Hit Modifier by Tier

For NPC attack rolls (`1d10 + REF + Weapon Skill`), the **net bonus** is what matters at the table:

| Tier | Net Modifier | Typical (REF + Skill) |
|------|--------------|----------------------|
| Mook | +10 | REF 6 + Skill 4 |
| Pro | +13 | REF 7 + Skill 6 |
| Boss | +15 | REF 8 + Skill 7 |
| Elite | +17+ | REF 8 + Skill 9+ |

### Initiative

NPCs roll `1d10 + REF`. Quick-tier:
- Civilian: +0 to +3
- Pro: +5 to +8
- Sandevistan **active** (1 minute, once per combat): **+3 on top of base**
- Kerenzikov: **+2 passive**

### Weapon Assignment by Tier

| Tier | Suggested Loadout |
|------|-------------------|
| Mook | Heavy Pistol (3d6) or SMG (2d6) |
| Pro | Heavy SMG (3d6) or Assault Rifle (5d6), one grenade |
| Boss | Tech-rifle / Sniper / Heavy Assault (5d6) + sidearm + grenades + signature cyberware |

---

## Common Modifiers

**Cover:** while **fully behind** something that can stop a bullet, you **can't be hit** — but the cover has its own HP (each 2×2m chunk) and gets shot away; at 0 HP it's gone. You're exposed the moment you lean out to shoot. No flat to-hit bonus.

> *Fast-play option:* if tracking cover HP is a drag, many tables instead give the defender **+2 (light) / +4 (heavy)**. Use it if you like, but it's a house shortcut, not the book rule.

**Range:** use the Ranged DV table above — the DV is set by weapon type and range band.

**Visibility / Environment:**
- Darkness (no low-light optics): -3 ranged
- Light smoke or haze: -2
- Heavy smoke / fire suppression: -5, range halved
- Prone target at range: defender +2 DV
- Prone target in melee: attacker +2 DV

**Aimed Shot:** -8 to roll for choice of hit location

---

## What's Not in This File

These are in the book — don't paraphrase from memory at the table:

- Full hit-location table (Head / Body / Right Arm / Left Arm / Right Leg / Left Leg, with hit chances and effects)
- Full Critical Injury tables (Body and Head — pages 184ish of core book)
- Specific cyberware Humanity costs (2d6 typical for serious chrome, ranges by piece)
- Ammo subtypes (AP, Hollow-point, Rubber, Incendiary, Smart, Biotoxin, etc.)
- Vehicle combat detail (chase rules, ramming, mounted weapons, vehicle Critical Hits)
- Net architecture rules (NET runs, Black ICE, Daemons, program slots, NET Actions)
- Trauma Team contract tiers
- Lifepath and chargen tables
