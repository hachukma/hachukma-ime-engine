import tkinter as tk
from tkinter import ttk
from datetime import datetime
from constants import CHART_DATA, NUMERAL_DATA, TONE_DATA

def setup_pua_register(app):
    app.pua_tab = tk.Frame(app.notebook, bg=app.bg_color)
    app.notebook.add(app.pua_tab, text="  📋  PUA REGISTER  ")

    # Main frame – no extra padding, fills the whole tab
    main_frame = tk.Frame(app.pua_tab, bg=app.bg_color)
    main_frame.pack(fill="both", expand=True)

    # Title and subtitle (with small padding)
    title = tk.Label(main_frame, text="Hachukma Script – Private Use Area (PUA) Register",
                     font=("Segoe UI", 16, "bold"), bg=app.bg_color, fg=app.accent_color)
    title.pack(pady=(10, 0))
    app.pua_title = title

    reg_date = datetime.now().strftime("%Y-%m-%d")
    # Subtitle removed per user request

    # Explanatory paragraph about PUA / Unicode status
    info_text = (
        "Hachukma currently does not use registered PUA code points and has not submitted any PUA registration proposal. "
        "This status will remain until the Hachukma script is accepted by both the Kokborok speakers and the relevant standards body."
    )

    info_msg = tk.Message(main_frame, text=info_text, width=900,
                          font=("Segoe UI", 10), bg=app.bg_color, fg=app.fg_color, justify="left")
    info_msg.pack(pady=(0, 10), padx=12)
    app.pua_info = info_msg

    # Treeview – fills remaining space
    columns = ("Glyph", "Code Point", "Type")
    tree = ttk.Treeview(main_frame, columns=columns, show="headings", height=20)
    tree.heading("Glyph", text="Glyph")
    tree.heading("Code Point", text="Code Point")
    tree.heading("Type", text="Type")
    tree.column("Glyph", width=200, anchor="center")
    tree.column("Code Point", width=140, anchor="center")
    tree.column("Type", width=120, anchor="center")

    # Tags – will be updated by apply_theme
    tree.tag_configure("glyph_font", font=(app.font_name, 20), foreground=app.fg_color)
    tree.tag_configure("even_row", background=app.keyboard_bg)
    tree.tag_configure("odd_row", background="#3a3a4a")  # placeholder

    # Prepare data
    data = []
    for glyph, _ in CHART_DATA:
        data.append((glyph, "Script"))
    for glyph, _ in TONE_DATA:
        data.append((glyph, "Script"))
    for glyph, _ in NUMERAL_DATA:
        data.append((glyph, "Numeral"))
    data.sort(key=lambda x: ord(x[0]))

    row_idx = 0
    for glyph, typ in data:
        code_point = f"U+{ord(glyph):04X}"
        tag = "even_row" if row_idx % 2 == 0 else "odd_row"
        tree.insert("", "end", values=(glyph, code_point, typ), tags=("glyph_font", tag))
        row_idx += 1

    tree.pack(fill="both", expand=True)

    scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    app.pua_tree = tree

    # Initial style – will be overridden by apply_theme
    app.style.configure("Treeview",
                        background=app.keyboard_bg,
                        foreground=app.fg_color,
                        fieldbackground=app.keyboard_bg,
                        rowheight=56)
    app.style.configure("Treeview.Heading",
                        background=app.sub_color,
                        foreground=app.fg_color)
