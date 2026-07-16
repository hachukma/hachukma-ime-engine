# Hachukma IME

![Platform](https://img.shields.io/badge/Platform-Windows-blue) ![Language](https://img.shields.io/badge/Language-Python%203-brightgreen) ![Script](https://img.shields.io/badge/Script-Hachukma-orange)

A Windows-based Input Method Engine (IME) for the Hachukma script, with an
interactive demo, learning tools, and script documentation. The engine itself is
what makes the IME work: it converts keyboard input into Hachukma glyphs and
inserts them into the active text field.

## Project Overview

Hachukma is a phonemic script designed for Kokborok. It is built with cultural
iconography from the Borok/Tripuri community and encoded using the Unicode
Private Use Area (PUA).

The project is centered around a working IME engine that:

- maps standard QWERTY keys to Hachukma glyphs,
- supports a dedicated high-tone diacritic,
- handles digraphs such as `th`, `kh`, `ph`, `ch`, and `ng`,
- provides real-time romanized output, and
- includes a rich demo to learn and test the script.

## Engine vs Demo

### IME Engine

The engine is the core software logic that performs the input method conversion.
It is not just the demo window; it is the behavior that translates physical
keystrokes into Hachukma script glyphs.

- Core files: `Hachukma software\hachukma\note_pad.py`, `Hachukma software\hachukma\constants.py`
- Function: Convert keyboard keys into PUA glyph code points.
- Tone input: Double-tap `p` to apply the HIGH TONE diacritic.
- Digraph detection: Recognizes combined sounds and treats them as a single
  script unit in the typing module.
- Font handling: Loads `Hachukma-Regular.ttf` automatically and prompts the user
  if the font is missing.

### Demo Interface

The built-in Tkinter application is a learning and presentation layer for the
IME engine. It includes the Notepad demo, typing practice, keyboard guide,
character chart, PUA register, and script explanation tabs.

## Design Summary

| Area | Details |
|---|---|
| Script type | Fully alphabetic (phonemic) |
| Direction | Left-to-right |
| Encoding | Unicode Private Use Area `U+E000`–`U+E024` |
| Glyph count | 37 total (26 letters, 10 numerals, 1 tone mark) |
| Tone system | High tone diacritic via `pp` |
| Font | `font/Hachukma-Regular.ttf` |
| Themes | 6 built-in colour schemes |
| Core engine | `note_pad.py`, `constants.py` |

## Core Features

- Fully working IME engine with live glyph conversion.
- Script-aware demo Notepad for immediate feedback.
- Keyboard guide with exact key → glyph relationships.
- Character chart for consonants, vowels, numerals, and tone mark.
- PUA register showing glyph code points and script categories.
- Typing practice module with romanisation and accuracy tracking.
- Theme support across Dark, Light, Ocean, Forest, Sunset, and Monochrome.

## Keyboard Rules and Behavior

- Standard keys map directly to Hachukma glyphs.
- Double-tap `p` to add the HIGH TONE diacritic after a base glyph.
- Digraphs are recognized in practice mode and rendered as a combined sound.
- The engine updates roman transliteration immediately for easier learning.

## Example Key Mapping

| Key | Code Point | Sound |
|---|---|---|
| `a` | `U+E00A` | /a/ |
| `b` | `U+E00B` | /b/ |
| `c` | `U+E00C` | /ch/ |
| `d` | `U+E00D` | /d/ |
| `p` | `U+E019` | /p/ |
| `q` | `U+E01A` | /th/ |
| `v` | `U+E01F` | /kh/ |
| `x` | `U+E021` | /ng/ |
| `z` | `U+E023` | /ə/ |

## Installation

1. Install Python 3.x on Windows.
2. Verify `tkinter` is installed and working.
3. Place the repository on your machine.
4. Run the demo with:

```bat
Hachukma software\run.bat
```

> If the Hachukma font is not found, the application will prompt you to locate
> `Hachukma-Regular.ttf`.

## Usage

- Launch `Hachukma software\run.bat`.
- Explore the tabs: Notepad, Typing Practice, Keyboard Guide, Character Chart,
  PUA Register, Script Info, and About IME.
- Type on a standard keyboard to generate Hachukma glyphs.
- Double-tap `p` to insert the high tone mark.
- In typing practice, use `v` → `kh`, `q` → `th`, `x` → `ng`, `f` → `ph`, `c` → `ch`,
  and `z` → `ə`.

## File Structure

- `Hachukma software/`
  - `run.bat` — launcher for the demo
  - `font/` — contains `Hachukma-Regular.ttf`
  - `hachukma/` — Python source code for the IME and UI
    - `about_ime.py` — About page content
    - `character_chart.py` — Character chart tab
    - `constants.py` — glyph mapping and theme data
    - `keyboard_guide.py` — keyboard guide tab
    - `monkeytype.py` — typing practice module
    - `note_pad.py` — main app UI and IME engine
    - `pua_register.py` — PUA register tab
    - `script_info.py` — script design and history info
  - `installers/` — installer assets and EULA text

## Notes and Disclaimers

- The Hachukma glyphs use unofficial PUA codepoints and are intended for testing,
  education, and presentation.
- Documents created with Hachukma require the custom font to view correctly.
- The project is under active development; encoding and script choices may evolve.

## License & Contact

See `Hachukma software/installers/EULA.text` for the license and usage disclaimer.

Contact: `hachukma@gmail.com`
