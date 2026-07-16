import tkinter as tk
from tkinter import ttk
from constants import CONSONANTS, VOWELS, NUMERAL_DATA, TONE_DATA

def setup_character_chart_tab(app):
    app.character_chart_tab = tk.Frame(app.notebook, bg=app.bg_color)
    app.notebook.add(app.character_chart_tab, text="  📊  CHARACTER CHART  ")

    main_frame = tk.Frame(app.character_chart_tab, bg=app.bg_color)
    main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    title = tk.Label(main_frame, text="📊  Character Chart", font=("Segoe UI", 12, "bold"),
                     bg=app.bg_color, fg=app.accent_color)
    title.pack(pady=(0, 10))

    # Container for boxes – using grid 2x2
    boxes_container = tk.Frame(main_frame, bg=app.bg_color)
    boxes_container.pack(fill=tk.BOTH, expand=True)

    # Configure 2 rows and 2 columns with equal weight
    boxes_container.rowconfigure(0, weight=1)
    boxes_container.rowconfigure(1, weight=1)
    boxes_container.columnconfigure(0, weight=1)
    boxes_container.columnconfigure(1, weight=1)

    def create_box(parent, title_text, data, row, col):
        box = tk.Frame(parent, bg=app.bg_color)
        box.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

        title_label = tk.Label(box, text=title_text, font=("Segoe UI", 11, "bold"),
                               bg=app.bg_color, fg=app.accent_color)
        title_label.pack(pady=2)

        text = tk.Text(box, wrap="none", bg=app.keyboard_bg, fg=app.fg_color,
                       font=("Segoe UI", 14), relief="flat", padx=8, pady=8,
                       spacing1=2, spacing2=2, spacing3=2)
        scroll = ttk.Scrollbar(box, orient="vertical", command=text.yview)
        text.configure(yscrollcommand=scroll.set)
        text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)

        text.tag_configure("glyph", font=(app.font_name, 20))
        text.tag_configure("sep", font=("Segoe UI", 14), foreground=app.sub_color)
        text.tag_configure("content", font=("Segoe UI", 14))
        text.tag_configure("even_row", background=app.keyboard_bg)
        text.tag_configure("odd_row", background=app.editor_bg if app.editor_bg != app.keyboard_bg else "#3a3a4a")

        row_idx = 0
        for glyph, desc in data:
            tag = "even_row" if row_idx % 2 == 0 else "odd_row"
            text.insert(tk.END, f"{glyph}  ", ("glyph", tag))
            text.insert(tk.END, "=  ", ("sep", tag))
            text.insert(tk.END, f"{desc}\n", ("content", tag))
            row_idx += 1
        text.config(state="disabled")
        return text, title_label

    # ---- Four boxes in 2x2 grid ----
    cons_text, cons_title = create_box(boxes_container, "Consonants", CONSONANTS, 0, 0)
    vowel_text, vowel_title = create_box(boxes_container, "Vowels (6)", VOWELS, 0, 1)
    num_text, num_title = create_box(boxes_container, "Numerals", NUMERAL_DATA, 1, 0)
    tone_text, tone_title = create_box(boxes_container, "Tone Diacritic", TONE_DATA, 1, 1)   # ✅ Tone box added

    app.guide_cons_text = cons_text
    app.guide_vowel_text = vowel_text
    app.guide_num_text = num_text
    app.guide_tone_text = tone_text  # store for theme updates

    app.guide_cons_title = cons_title
    app.guide_vowel_title = vowel_title
    app.guide_num_title = num_title
    app.guide_tone_title = tone_title 
