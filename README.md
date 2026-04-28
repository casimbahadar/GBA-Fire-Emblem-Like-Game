# Ash and Iron

A GBA-aesthetic Fire Emblem fan game built with the [Lex Talionis / LT-Maker](https://gitlab.com/rainlash/lt-maker) engine.

## Story

The kingdom of Valdres is invaded by the Solaran Empire. Kira, a Royal Guard lieutenant,
must escort the young crown prince to safety — while uncovering the truth about her father,
General Varek, now fighting for the other side as the masked "Ashen Knight."

8-chapter vertical slice with original characters, full support conversations, branching
class promotions, and a two-phase final boss.

## Features

- 12 playable characters with personal skills
- 16 classes (7 base + 9 promoted) with branching promotions
- Full weapon triangle (physical + magic)
- 8 support pairs with C/B/A conversations
- Normal / Hard / Lunatic difficulty modes
- GBA-inspired pixel art at 480×320 (2× scale)

## Setup

**Requirements:** Python 3.10–3.11

```bash
# Clone with submodules
git clone --recurse-submodules <repo-url>
cd GBA-Fire-Emblem-Like-Game

# Create virtual environment
python -m venv .venv
source .venv/bin/activate      # Linux/macOS
.venv\Scripts\activate         # Windows

pip install -r requirements.txt

# Run the game
cd lt-maker
python run_engine.py --project ../ash_and_iron.ltproj

# Run the editor (to draw maps, wire portraits/sprites)
python run_editor.py
# Then: File > Open Project > select ../ash_and_iron.ltproj
```

## Project Structure

```
lt-maker/           — Engine (git submodule, do not edit)
ash_and_iron.ltproj/
  game_data/        — All JSON data (classes, units, items, events, levels)
  resources/        — Assets (tilemaps, portraits, sprites, music)
docs/               — Design notes and balance records
```

## Development Status

- [x] Project scaffolding and engine submodule
- [x] All game data: classes, units, items, skills
- [x] Chapter level files (1–8)
- [x] Chapter event scripts
- [x] Support conversations (24 total)
- [x] Custom skill components
- [ ] Chapter tilemaps (requires LT-Maker GUI Map Maker)
- [ ] Portrait and sprite wiring (requires LT-Maker GUI editor)
- [ ] Playtesting and balance pass
