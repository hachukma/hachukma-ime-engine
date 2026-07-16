import tkinter as tk
from tkinter import ttk
from constants import MAPPINGS

def setup_keyboard_guide_tab(app):
    app.keyboard_guide_tab = tk.Frame(app.notebook, bg=app.bg_color)
    app.notebook.add(app.keyboard_guide_tab, text="  ⌨️  KEYBOARD GUIDE  ")

    main_frame = tk.Frame(app.keyboard_guide_tab, bg=app.bg_color)
    main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    # Title
    title = tk.Label(main_frame, text="⌨️  Key → Glyph Mapping", font=("Segoe UI", 14, "bold"),
                     bg=app.bg_color, fg=app.accent_color)
    title.pack(pady=(0, 15))
    app.keyboard_guide_title = title

    # Create a Treeview with two columns
    columns = ("Key", "Glyph")
    tree = ttk.Treeview(main_frame, columns=columns, show="headings", height=22)
    tree.heading("Key", text="Key")
    tree.heading("Glyph", text="Glyph")
    tree.column("Key", width=150, anchor="center")
    tree.column("Glyph", width=200, anchor="center")

    # Configure tags for alternating row colours and glyph font
    tree.tag_configure("even_row", background=app.keyboard_bg)
    odd_bg = app.editor_bg if app.editor_bg != app.keyboard_bg else "#3a3a4a"
    tree.tag_configure("odd_row", background=odd_bg)
    tree.tag_configure("glyph_font", font=(app.font_name, 24))
    tree.tag_configure("key_font", font=("Segoe UI", 14, "bold"))

    # Insert data – alternating rows
    row_idx = 0
    for key, glyph in MAPPINGS.items():
        if key in (' ', '\r', '\n'):
            continue
        tag = "even_row" if row_idx % 2 == 0 else "odd_row"
        tree.insert("", "end", values=(key, glyph), tags=(tag, "key_font", "glyph_font"))
        row_idx += 1

    # Add tone mark entry
    tree.insert("", "end", values=("pp (double-tap)", "\uE024"),
                tags=("even_row" if row_idx % 2 == 0 else "odd_row", "key_font", "glyph_font"))

    # Add scrollbar
    scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)

    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Store for theme updates
    app.keyboard_guide_tree = tree
    app.keyboard_guide_title = title
