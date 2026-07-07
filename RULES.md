# Cyberpunk RED — Rules Quick Reference

Minimal cheat sheet for at-the-table fast lookup. The core book has the full rules and the detail tables (hit locations, ammo types, critical injury table, cyberware Humanity costs, netrunning architecture). This file is just enough to spot-check during play and to size up NPC stats on the fly.

> **📖 = official core-book rule.** This sheet runs several deliberate house simplifications. Where we diverge from the book, a `📖` line notes what the original rule is, so we know what we're bending. Summary below; details inline.

---

## House Rules vs. Official RED — at a glance

| Rule | This table (house) | Official Cyberpunk RED |
|------|--------------------|------------------------|
| **Difficulty ladder** | 11 / 13 / 15 / 17 / 19 (Easy→Very Hard) | 13 Everyday · 15 Difficult · 17 Professional · 21 Heroic · 24 Incredible |
| **Move distance** | MOVE in metres; run = ×2 | MOVE **×2** metres per Move Action; run (2nd Move Action) = ×4 |
| **Dodging bullets** | Anyone may dodge ranged fire | Only characters with **REF 8+** can Evade ranged attacks |
| **Range DVs** | Flat 13 / 15 / 20 / 25 | A separate range-DV table **per weapon type** (our flat table ≈ a pistol) |
| **Autofire** | Pick ROF 2–4, DV 17, damage ROF × 2d6 | **Autofire skill** vs normal range DV; damage 2d6 × (amount you beat the DV), capped at the gun's Autofire (SMG ×3 / AR ×4); ≤25m |
| **Suppressive fire** | 25m area, Evasion DV 15 or take 2d6 | 8×8m area, **no damage**; acting in the zone = −2; costs a Full Action + 10 rounds |
| **Critical Injury trigger** | Any **two matching** damage dice; no bonus damage | **Two or more 6s** → **+5 damage that ignores armor** *and* roll on the Critical Injury table |
| **"Critical Hit" (nat 10 to-hit)** | Roll a d10, add to damage | No such rule — a natural 10 explodes the **attack roll**, not damage |
| **AP ammo** | Halves target SP | Halves SP **and** ablates armor by **2** (not 1) |
| **Mortally Wounded** | Unconscious | Still **conscious & can act**, at −4 to all Checks and −6 MOVE; auto-Critical Injury if hit again |
| **Death Save success** | "Stabilizes" you | Only **survives that round** — you keep rolling every turn until someone Stabilizes you |
| **Stabilize DV** | First Aid DV 13 | First Aid **or** Paramedic at **DV 15** |
| **First Aid / MedTech HP** | Heal 1d6 / 2d6 per scene | First Aid only **stabilizes** (0 HP restored); HP returns via rest (BODY/day) or Medtech surgery |
| **Cover** | +2 light / +4 heavy to defense | Cover has its **own HP** and gets shot away — no flat defense bonus |

Everything not listed here (skill-check formula, exploding 10 / fumble 1, initiative, ranged/melee attack rolls, damage → SP → HP, ablation on penetrating hits, headshot ×2, aimed-shot −8, Seriously Wounded −2, natural healing = BODY/day, Pain Editor) matches the book as written.

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
- **Move** (up to your MOVE stat in meters) **+ 1 Action**
- *or* **Move ×2** (run, no action)

> 📖 **Book:** a Move Action covers MOVE **×2** metres; running is a second Move Action (MOVE ×4 total) and spends your Action. Ours is ~half book speed.

**Common Actions:** attack, aimed shot, autofire, suppressive fire, reload, draw weapon, skill use, brace, dodge, pick someone up.

**Defending:**
- **Dodge** ranged: `1d10 + DEX + Evasion` vs. attacker's roll. Most NPCs don't bother — they take the hit and rely on armor.
  - 📖 **Book:** only characters with **REF 8+** may Evade ranged attacks at all. The DEX + Evasion roll itself is book-correct.
- **Block / Parry** melee: `1d10 + DEX + Melee or Brawling` vs. attacker's roll.

---

## Attack Rolls

**Ranged:** `1d10 + REF + Weapon Skill` vs. target's defense (their Evasion roll, or DV by range if they don't dodge).

**Default range DVs** (when not using book bands):

| Range | DV |
|-------|----|
| Point Blank / Close (≤6m) | 13 |
| Medium (≤25m) | 15 |
| Long (≤50m) | 20 |
| Extreme (50m+) | 25 |

**Melee:** `1d10 + DEX + Melee Weapon or Brawling` vs. defender's Evasion or Block.

**Autofire:** Choose ROF 2-4. DV 17 base to hit. Damage = ROF × 2d6 (typical) or as weapon spec.

> 📖 **Book:** autofire uses the separate **Autofire skill** vs the normal range DV; damage = 2d6 × (how much you beat the DV), capped at the gun's Autofire rating (SMG ×3, AR ×4), range ≤25m. No flat DV 17, no "choose ROF."

**Suppressive Fire:** All targets in 25m area make Evasion DV 15 or take 2d6, must stay in cover.

> 📖 **Book:** suppressive fire deals **no damage** — it's an 8×8m zone (Full Action + 10 rounds); anyone who acts inside it other than moving in cover takes −2.

**Aimed Shot:** -8 to roll, choose location (most often head = damage ×2 after head armor).

---

## Damage

1. Roll weapon dice
2. Subtract target's **SP** (Stopping Power) at the relevant location
3. Remaining = HP loss
4. **Ablation:** each hit that goes *through* armor reduces that armor's SP by 1
5. **Critical Injury trigger:** if any **two dice match** in the damage roll, target also takes a Critical Injury (roll on table OR pick a flavorful penalty — see below)

> 📖 **Book:** a Critical Injury triggers only on **two or more 6s**, and it also deals **+5 damage straight to HP (ignoring armor)**. We use any matching pair and drop the +5.

**Headshot:** damage doubled *after* head armor is applied.
**Armor-Piercing ammo:** target SP is halved for that hit.

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

## Critical Hits & Injuries

**Critical Hit (natural 10 to-hit roll):** Roll a second d10. **Add** to damage roll. (If the second roll is also a 10, keep exploding.)

> 📖 **Book:** RED has no bonus-damage crit. A natural 10 explodes the **attack roll** (roll again, add to the to-hit), not damage — the only bonus damage in the book is the +5 from a two-6s Critical Injury. Our "add a d10 to damage" is a house call.

**Critical Injury (two matching dice in the damage roll):** Beyond HP loss, the target suffers a lasting injury. Roll on the Body or Head Critical Injury table in the book, OR — for fast play — pick from this lazy substitute:

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
| **Seriously Wounded** | ≤ HP/2 | **-2 to all rolls.** Pain Editor cyberware ignores this. |
| **Mortally Wounded** | 0 or below | Unconscious; begin Death Saves |

> 📖 **Book:** a Mortally Wounded character isn't knocked out — they can still act, at **−4 to all Checks and −6 MOVE** (min 1), and take an **automatic** Critical Injury if hit again. (Seriously Wounded's −2 is book-correct.)

**Death Save (each round at 0 HP or below):**
- Roll `1d10`
- If `d10 + cumulative death-save penalty ≤ BODY` → stabilize this round
- If exceeds BODY → death
- Penalty starts at 0, **+1 per prior save attempt**
- A successful **First Aid (DV 13)** or **MedTech (DV 15)** stabilizes them and stops further saves

> 📖 **Book:** you roll **under** your BODY (a natural 10 always fails), and passing only means you **survive that round and can still act** — it does NOT stabilize you. Stabilizing is a separate First Aid **or** Paramedic check at **DV 15** (our DV 13 is a house discount); one success ends the saves and leaves you at 1 HP.

---

## Healing

| Method | Effect | Notes |
|--------|--------|-------|
| **First Aid** (TECH, DV 13) | 1d6 HP / scene | Once per character per scene |
| **MedTech / Paramedic** (TECH, DV 15) | 2d6 HP / scene | Also stabilizes Death Saves |
| **MedTech autoinjector** | 1d6 HP | Single-use consumable |
| **Surgery / clinic** | Restores HP over hours/days of downtime | Ripperdoc / Trauma Team work |
| **Natural rest** | BODY HP per day of full rest | Cumulative |

> 📖 **Book:** First Aid only **stabilizes** — it restores **0 HP**. Lost HP comes back through natural rest (BODY/day, once stabilized) or a Medtech's Surgery over downtime. Our per-scene 1d6 / 2d6 heals are a house shortcut to keep fights moving. (Natural rest = BODY/day is book-correct.)

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

**Cover (adds to defender's effective DV / Evasion):**
- Light cover (chair, car door): +2
- Heavy cover (wall, engine block): +4
- Full cover with firing slit: effectively immune except through slit

> 📖 **Book:** cover gives no flat bonus — each 2×2m chunk of cover has its **own HP** and gets shot away; you're safe behind it until it's destroyed or you lean out. The +2/+4 is our fast stand-in.

**Range step beyond close (when not using book bands):** +3 DV to hit per step

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
