import tkinter as tk
from tkinter import ttk

def setup_about_ime_tab(app):
    app.about_ime_tab = tk.Frame(app.notebook, bg=app.bg_color)
    app.notebook.add(app.about_ime_tab, text="  ℹ️  ABOUT IME ")

    text_frame = tk.Frame(app.about_ime_tab, bg=app.bg_color)
    text_frame.pack(fill="both", expand=True, padx=30, pady=30)

    app.about_ime_text = tk.Text(text_frame, wrap="word", bg=app.keyboard_bg, fg=app.fg_color,
                                 font=("Segoe UI", 12), relief="flat", padx=20, pady=20)
    scrollbar = ttk.Scrollbar(text_frame, orient="vertical", command=app.about_ime_text.yview)
    app.about_ime_text.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    app.about_ime_text.pack(side="left", fill="both", expand=True)

    content = """
═══════════════════════════════════════════════════════════
                    HACHUKMA IME ENGINE
═══════════════════════════════════════════════════════════

Developer: Anan Debbarma


What is the IME?
────────────────
This is an Input Method Engine (IME) – the core technology
that lets you type the Hachukma script using a standard
QWERTY keyboard. The IME intercepts your keystrokes,
translates them into the corresponding PUA‑encoded glyphs,
and inserts them into the active text field.

The IME engine runs in the background, waiting for key
presses and converting them on the fly. It is not just
a notepad – it’s a system‑level input method.

The built‑in Notepad tab is a demonstration and testing
environment. It allows you to try the IME, see how your
keystrokes become Hachukma characters, and view a live
Roman transliteration. It is not the IME itself – the IME
works wherever you type (e.g., in any text editor, if
integrated system‑wide).

How the IME works (technical)
─────────────────────────────
• The IME monitors keyboard events. When you press a key
  (e.g., 'a'), it looks up the corresponding Hachukma glyph
  from its internal mapping table (Private Use Area,
  U+E000–U+E024).
• It then inserts that glyph into the currently focused
  text input (the Notepad, or any other application when
  the IME is active).
• Multi‑tap detection: if you tap 'p' twice within 500 ms,
  the IME inserts the HIGH TONE diacritic (  ) after the
  base /p/ glyph.
• Tone modifier: type any letter (e.g., 'o') and then press
  'p' – the IME will apply the tone mark to that letter.
• Dedicated tone key: press the '~' (tilde) key to insert
  the tone mark alone.
• Digraph strike‑through: when you type two characters
  that form a digraph (th, kh, ph, ch, ng), the IME applies
  a red strike‑through to both glyphs to indicate they
  represent a single combined sound.
  For example, if you type t+h+a+n+g, the IME will strike
  through t and h (forming th) and n and g (forming ng),
  showing you that they should be read as single sounds.
  The correct spelling is th + a + ng.
• The Roman transliteration panel is a helpful feature
  for learners – it shows the Latin‑script equivalent of
  your typed text in real time.

Technical Details
─────────────────
• Font: Hachukma‑Regular.ttf
• Character set: Private Use Area (U+E000–U+E024)
• IME core: key‑to‑glyph mapping, multi‑tap detection,
  tone modifier, digraph strike, reverse transliteration
• Theme support: 6 built‑in colour schemes
• The built‑in Notepad is a demo editor – the IME itself
  is the real engine.

Contact
───────
For questions, suggestions, or script inquiries, please
reach out at: hachukma@gmail.com

Thank you for using the Hachukma IME Engine!
    """
    app.about_ime_text.insert("1.0", content)
    app.about_ime_text.config(state="disabled")
