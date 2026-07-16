# Hachukma IME

A Windows-based Input Method Engine (IME) and learning interface for the custom Hachukma script, designed for the Kokborok language. This project includes a Tkinter demo app, keyboard guide, character chart, PUA register, typing practice, and roman transliteration support.

## Project Overview

Hachukma is a modern phonemic writing system built around cultural iconography from the Borok/Tripuri community. The IME maps standard QWERTY keys to Private Use Area glyphs and includes tone support, digraph handling, theming, and an interactive typing practice module.

## Design Summary

| Area | Details |
|---|---|
| Script type | Fully alphabetic (phonemic) |
| Direction | Left-to-right |
| Encoding | Unicode Private Use Area (U+E000–U+E024) |
| Glyph count | 37 total (26 letters, 10 numerals, 1 tone mark) |
| Tone support | HIGH TONE diacritic via double-tap `p` |
| Font | `font/Hachukma-Regular.ttf` |
| Platform | Windows (Tkinter UI, installer-ready structure) |

## Key Features

- Live IME demonstration through a built-in Notepad tab
- Keyboard guide with key → glyph mapping
- Character chart for consonants, vowels, numerals, and tone mark
- Private Use Area register for all Hachukma glyphs
- Typing practice module with romanization reminders
- Theme support with multiple color schemes
- Font auto-loading with fallback prompt when needed

## Installation

1. Install Python 3.x on Windows.
2. Ensure `tkinter` is available and working.
3. Place the repository on your machine.
4. Run the demo with `Hachukma software\run.bat`.

> The application expects the `Hachukma-Regular.ttf` font inside `Hachukma software\font`. If the font cannot load automatically, the app prompts you to locate it manually.

## Usage

- Launch `Hachukma software\run.bat`.
- Use the built-in tabs to explore the IME, keyboard guide, script chart, PUA register, and typing practice.
- Type letters on a standard keyboard to generate Hachukma glyphs.
- Double-tap `p` to insert the HIGH TONE diacritic.
- Use special keys for digraphs in the typing practice: `v` → `kh`, `q` → `th`, `x` → `ng`, `f` → `ph`, `c` → `ch`, `z` → `ə`.

## Mapping Examples

| Key | Hachukma Glyph | Roman Sound |
|---|---|---|
| `a` | `
