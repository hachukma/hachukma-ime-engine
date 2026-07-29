import sys
sys.dont_write_bytecode = True

import tkinter as tk
from tkinter import font, ttk, messagebox, colorchooser, filedialog
import ctypes
import os
import time
import colorsys

# Import shared data
from constants import MAPPINGS, REVERSE_MAPPINGS, THEMES

# ============================================================
#  USER SETTINGS
# ============================================================


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path.replace("/", os.sep))


FONT_PATH = resource_path("font/Hachukma-Regular.ttf")
FONT_FAMILY_OVERRIDE = ""
# ============================================================

FR_PRIVATE = 0x10

# Digraphs mapping (used for red strike‑through)
DIGRAPHS = {
    'th': '\uE01A',   # q
    'kh': '\uE01F',   # v
    'ph': '\uE00F',   # f
    'ch': '\uE00C',   # c
    'ng': '\uE021',   # x
}

def get_font_candidates(script_dir):
    candidates = []
    if FONT_PATH:
        full_path = os.path.join(script_dir, FONT_PATH)
        if os.path.exists(full_path):
            candidates.append(full_path)
    return candidates

def load_font(font_path):
    if not os.path.exists(font_path):
        return False
    try:
        pathbuf = ctypes.create_unicode_buffer(font_path)
        ret = ctypes.windll.gdi32.AddFontResourceExW(ctypes.byref(pathbuf), FR_PRIVATE, 0)
        ctypes.windll.user32.PostMessageW(0xFFFF, 0x001D, 0, 0)
        return ret != 0
    except Exception:
        return False

class HachukmaNotepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Hachukma Script - IME Engine")
        self.root.geometry("1400x950")
        self.root.minsize(1000, 750)

        self.current_theme = "Light"
        self._load_theme_data(self.current_theme)

        self.style = ttk.Style()
        self.style.theme_use('clam')

        # Load font
        self.font_name = self._get_font_family()
        print(f"Using font family: {self.font_name}")

        self.default_font_size = 48
        self.hachukma_font = font.Font(family=self.font_name, size=self.default_font_size)
        self.hachukma_font_key = font.Font(family=self.font_name, size=18)
        self.roman_font = font.Font(family="Consolas", size=16)

        # IME state
        self.last_key = None
        self.last_time = 0
        self.multi_tap_delay = 0.5
        self.pending_tone_letter = None

        # Roman buffer for digraph detection
        self.roman_buffer = ""

        # Counters for unique tags
        self.color_tag_counter = 0
        self.size_tag_counter = 0

        # Build notebook
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill="both", padx=15, pady=15)
        self.notebook.bind("<<NotebookTabChanged>>", self.on_tab_change)

        from keyboard_guide import setup_keyboard_guide_tab
        from character_chart import setup_character_chart_tab
        from about_ime import setup_about_ime_tab
        from script_info import setup_script_info_tab
        from pua_register import setup_pua_register
        from monkeytype import setup_monkeytype

        self.setup_notepad_tab()
        setup_monkeytype(self)
        setup_keyboard_guide_tab(self)
        setup_character_chart_tab(self)
        setup_script_info_tab(self)
        setup_pua_register(self)
        setup_about_ime_tab(self)

        self.update_ttk_style()
        self.apply_theme()
        self.text_area.focus_set()

    # --------------------------------------------------------
    # Font detection (improved to find the font automatically)
    # --------------------------------------------------------
    def _get_font_family(self):
        # 1. If the user explicitly overrode the family, use it.
        if FONT_FAMILY_OVERRIDE:
            return FONT_FAMILY_OVERRIDE

        # 2. Check if the font is already installed system-wide.
        installed = [f for f in font.families() if "hachukma" in f.lower()]
        if installed:
            return installed[0]

        # 3. Build a list of possible paths to the .ttf file.
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Use the existing resource_path for PyInstaller compatibility, but also add fallbacks.
        possible_paths = [
            resource_path("font/Hachukma-Regular.ttf"),   # normal location
            os.path.join(script_dir, "font", "Hachukma-Regular.ttf"),
            os.path.join(script_dir, "Hachukma-Regular.ttf"),
            os.path.join(os.getcwd(), "font", "Hachukma-Regular.ttf"),
            os.path.join(os.getcwd(), "Hachukma-Regular.ttf"),
        ]
        # Remove duplicates while preserving order.
        seen = set()
        unique_paths = []
        for p in possible_paths:
            if p not in seen:
                seen.add(p)
                unique_paths.append(p)

        # 4. Try to load the font from each path.
        for path in unique_paths:
            if os.path.exists(path) and load_font(path):
                # After loading, check again if the family is now available.
                installed = [f for f in font.families() if "hachukma" in f.lower()]
                if installed:
                    return installed[0]
                else:
                    # Some loaded fonts might not appear in the family list immediately;
                    # return the expected family name – it usually works.
                    return "Hachukma-Regular"

        # 5. If still not found, ask the user (this is the only manual step).
        msg = ("Could not find or load Hachukma font automatically.\n"
               "Please locate the font file (e.g., Hachukma-Regular.ttf).")
        messagebox.showinfo("Font Required", msg)
        file_path = filedialog.askopenfilename(
            title="Select Hachukma Font File",
            filetypes=[("Font files", "*.ttf *.tff"), ("All files", "*.*")]
        )
        if file_path and load_font(file_path):
            installed = [f for f in font.families() if "hachukma" in f.lower()]
            if installed:
                return installed[0]
            else:
                return "Hachukma-Regular"

        # 6. Ultimate fallback – shows a warning but doesn't break.
        messagebox.showwarning("Font Fallback",
                               "Could not load Hachukma font.\n"
                               "Using Segoe UI Symbol as fallback.\n"
                               "Glyphs may not display correctly.")
        return "Segoe UI Symbol"

    # --------------------------------------------------------
    # Theme handling (unchanged)
    # --------------------------------------------------------
    def _load_theme_data(self, theme_name):
        t = THEMES[theme_name]
        self.bg_color = t["bg"]
        self.fg_color = t["fg"]
        self.accent_color = t["accent"]
        self.sub_color = t["sub"]
        self.keyboard_bg = t["keyboard_bg"]
        self.editor_bg = t["editor_bg"]
        self.editor_fg = t["editor_fg"]

    def load_theme(self, theme_name):
        self._load_theme_data(theme_name)
        self.update_ttk_style()
        self.apply_theme()

    def _adjust_color(self, hex_color, amount=0.08):
        try:
            r = int(hex_color[1:3], 16)
            g = int(hex_color[3:5], 16)
            b = int(hex_color[5:7], 16)
            h, l, s = colorsys.rgb_to_hls(r/255, g/255, b/255)
            l = max(0, min(1, l + amount))
            r2, g2, b2 = colorsys.hls_to_rgb(h, l, s)
            return f"#{int(r2*255):02x}{int(g2*255):02x}{int(b2*255):02x}"
        except:
            return "#3a3a4a"

    def apply_theme(self):
        self.root.configure(bg=self.bg_color)

        for tab_name in ['notepad_tab', 'monkey_tab', 'keyboard_guide_tab',
                    'character_chart_tab', 'script_info_tab', 'pua_tab', 'about_ime_tab']:
            if hasattr(self, tab_name):
                getattr(self, tab_name).configure(bg=self.bg_color)

        if hasattr(self, 'text_area'):
            default_font = ("Segoe UI", self.default_font_size)
            self.text_area.configure(bg=self.editor_bg, fg=self.editor_fg, font=default_font)
            self.text_area.tag_configure("glyph", font=self.hachukma_font)
        if hasattr(self, 'translator_frame'):
            self.translator_frame.configure(bg=self.keyboard_bg)
        if hasattr(self, 'translation_text'):
            self.translation_text.configure(bg=self.keyboard_bg, fg=self.fg_color)
        if hasattr(self, 'hachukma_title_label'):
            self.hachukma_title_label.configure(bg=self.bg_color, fg=self.accent_color)
        if hasattr(self, 'roman_interpreter_label'):
            self.roman_interpreter_label.configure(bg=self.keyboard_bg, fg=self.accent_color)

        for attr in ('about_ime_text', 'script_info_text'):
            if hasattr(self, attr):
                getattr(self, attr).configure(bg=self.keyboard_bg, fg=self.fg_color)

        if hasattr(self, 'monkey_target'):
            self.monkey_target.configure(bg=self.keyboard_bg, fg=self.fg_color)
        if hasattr(self, 'monkey_entry'):
            self.monkey_entry.configure(bg=self.editor_bg, fg=self.fg_color)
        if hasattr(self, 'monkey_stats'):
            self.monkey_stats.configure(bg=self.bg_color, fg=self.sub_color)

        if hasattr(self, 'monkey_word_cards'):
            for card, glyph_lbl, roman_lbl in self.monkey_word_cards:
                card.config(bg=self.keyboard_bg)
                glyph_lbl.config(bg=self.keyboard_bg, fg=self.fg_color)
                roman_lbl.config(bg=self.keyboard_bg, fg=self.sub_color)

        odd_bg = self.editor_bg if self.editor_bg != self.keyboard_bg else self._adjust_color(self.keyboard_bg, 0.08)

        if hasattr(self, 'keyboard_guide_tree'):
            tree = self.keyboard_guide_tree
            tree.tag_configure("even_row", background=self.keyboard_bg)
            tree.tag_configure("odd_row", background=odd_bg)
            tree.tag_configure("glyph_font", font=(self.font_name, 24), foreground=self.fg_color)
            tree.tag_configure("key_font", font=("Segoe UI", 14, "bold"), foreground=self.fg_color)

        for name in ['guide_cons_text', 'guide_vowel_text', 'guide_num_text', 'guide_tone_text']:
            if hasattr(self, name):
                t = getattr(self, name)
                t.configure(bg=self.keyboard_bg, fg=self.fg_color)
                t.tag_configure("even_row", background=self.keyboard_bg)
                t.tag_configure("odd_row", background=odd_bg)
                t.tag_configure("sep", foreground=self.sub_color)
                t.tag_configure("glyph", foreground=self.fg_color)
                t.tag_configure("content", foreground=self.fg_color)

        if hasattr(self, 'pua_tree'):
            tree = self.pua_tree
            self.style.configure("Treeview", background=self.keyboard_bg,
                                 foreground=self.fg_color, fieldbackground=self.keyboard_bg)
            self.style.configure("Treeview.Heading", background=self.sub_color,
                                 foreground=self.fg_color)
            tree.tag_configure("even_row", background=self.keyboard_bg)
            tree.tag_configure("odd_row", background=odd_bg)
            tree.tag_configure("glyph_font", font=(self.font_name, 20), foreground=self.fg_color)

        if hasattr(self, 'pua_title'):
            self.pua_title.configure(bg=self.bg_color, fg=self.accent_color)
        if hasattr(self, 'pua_subtitle'):
            self.pua_subtitle.configure(bg=self.bg_color, fg=self.sub_color)

        if hasattr(self, 'monkey_title'):
            self.monkey_title.configure(bg=self.bg_color, fg=self.accent_color)
        if hasattr(self, 'monkey_timer_label'):
            self.monkey_timer_label.configure(bg=self.bg_color, fg=self.fg_color)
        if hasattr(self, 'monkey_input_label'):
            self.monkey_input_label.configure(bg=self.bg_color, fg=self.fg_color)
        if hasattr(self, 'monkey_cards_frame'):
            self.monkey_cards_frame.configure(bg=self.keyboard_bg)

        def _is_ancestor(widget, candidate):
            try:
                anc = widget
                while anc is not None:
                    if anc is candidate:
                        return True
                    anc = getattr(anc, 'master', None)
            except Exception:
                return False
            return False

        def _apply_widget_theme(widget):
            try:
                cls = widget.winfo_class()
            except Exception:
                cls = None

            try:
                if cls == 'Text':
                    if widget is getattr(self, 'text_area', None):
                        widget.configure(bg=self.editor_bg, fg=self.editor_fg, insertbackground=self.accent_color)
                    else:
                        widget.configure(bg=self.keyboard_bg, fg=self.fg_color, insertbackground=self.accent_color)
                elif cls in ('Entry', 'TEntry', 'Spinbox'):
                    try:
                        widget.configure(bg=self.editor_bg, fg=self.fg_color, insertbackground=self.accent_color)
                    except Exception:
                        pass
                elif cls in ('Label', 'Button'):
                    if _is_ancestor(widget, getattr(self, 'translator_frame', None)) or _is_ancestor(widget, getattr(self, 'monkey_cards_frame', None)):
                        widget.configure(bg=self.keyboard_bg, fg=self.fg_color)
                    else:
                        widget.configure(bg=self.bg_color, fg=self.fg_color)
                elif cls in ('Frame', 'PanedWindow'):
                    if _is_ancestor(widget, getattr(self, 'translator_frame', None)) or _is_ancestor(widget, getattr(self, 'monkey_cards_frame', None)):
                        widget.configure(bg=self.keyboard_bg)
                    else:
                        widget.configure(bg=self.bg_color)
                elif 'Scrollbar' in str(cls):
                    try:
                        widget.configure(background=self.sub_color)
                    except Exception:
                        pass
            except Exception:
                pass

            try:
                for ch in widget.winfo_children():
                    _apply_widget_theme(ch)
            except Exception:
                pass

        try:
            _apply_widget_theme(self.notebook)
        except Exception:
            pass

    def update_ttk_style(self):
        self.style.configure("TNotebook", background=self.bg_color, borderwidth=0)
        self.style.configure("TNotebook.Tab",
                             background=self.sub_color,
                             foreground=self.fg_color,
                             padding=[25, 8],
                             font=("Segoe UI", 11, "bold"))
        self.style.map("TNotebook.Tab",
                   background=[("selected", self.accent_color), ("active", self.sub_color), ("pressed", self.accent_color)],
                   foreground=[("selected", self.bg_color), ("active", self.fg_color)])
        self.style.configure("TButton",
                             background=self.sub_color,
                             foreground=self.fg_color,
                             borderwidth=0,
                             font=("Segoe UI", 10, "bold"))
        self.style.map("TButton",
                       background=[("active", self.accent_color)],
                       foreground=[("active", self.bg_color)])

    def change_theme(self, event=None):
        selected = self.theme_var.get()
        if selected in THEMES:
            self.current_theme = selected
            self.load_theme(selected)

    def on_tab_change(self, event):
        idx = self.notebook.index(self.notebook.select())
        if idx == 0:
            self.text_area.focus_set()

    # --------------------------------------------------------
    # Notepad tab
    # --------------------------------------------------------
    def setup_notepad_tab(self):
        self.notepad_tab = tk.Frame(self.notebook, bg=self.bg_color)
        self.notebook.add(self.notepad_tab, text="  ✍️  NOTEPAD  ")

        toolbar = tk.Frame(self.notepad_tab, bg=self.bg_color)
        toolbar.pack(side="top", fill="x", pady=(20, 10))

        file_frame = tk.Frame(toolbar, bg=self.bg_color)
        file_frame.pack(side="left", padx=10)
        save_btn = ttk.Button(file_frame, text="💾 Save", command=self.save_file)
        save_btn.pack(side="left", padx=2)
        load_btn = ttk.Button(file_frame, text="📂 Load", command=self.load_file)
        load_btn.pack(side="left", padx=2)

        font_frame = tk.Frame(toolbar, bg=self.bg_color)
        font_frame.pack(side="left", padx=10)
        tk.Label(font_frame, text="Font Size:", bg=self.bg_color, fg=self.fg_color,
                 font=("Segoe UI", 10)).pack(side="left")
        self.font_size_var = tk.IntVar(value=48)
        self.font_size_var.trace_add("write", lambda *_: self.change_font_size())
        size_spin = ttk.Spinbox(font_frame, from_=24, to=96, textvariable=self.font_size_var,
                                width=5)
        size_spin.pack(side="left", padx=5)

        color_frame = tk.Frame(toolbar, bg=self.bg_color)
        color_frame.pack(side="left", padx=10)
        bg_color_btn = ttk.Button(color_frame, text="🎨 BG Color", command=self.pick_bg_color)
        bg_color_btn.pack(side="left", padx=2)
        fg_color_btn = ttk.Button(color_frame, text="✏️ Text Color", command=self.pick_fg_color)
        fg_color_btn.pack(side="left", padx=2)

        theme_frame = tk.Frame(toolbar, bg=self.bg_color)
        theme_frame.pack(side="left", padx=10)
        tk.Label(theme_frame, text="Theme:", bg=self.bg_color, fg=self.fg_color,
                 font=("Segoe UI", 10)).pack(side="left")
        self.theme_var = tk.StringVar(value=self.current_theme)
        theme_menu = ttk.Combobox(theme_frame, textvariable=self.theme_var,
                                  values=list(THEMES.keys()), width=10, state="readonly")
        theme_menu.pack(side="left", padx=5)
        theme_menu.bind("<<ComboboxSelected>>", self.change_theme)

        self.wordcount_label = tk.Label(toolbar, text="Chars: 0 | Words: 0",
                                        bg=self.bg_color, fg=self.sub_color,
                                        font=("Segoe UI", 10))
        self.wordcount_label.pack(side="left", padx=20)

        clear_btn = ttk.Button(toolbar, text="🗑️ Clear all", command=self.clear_notepad)
        clear_btn.pack(side="right", padx=20)

        main_pane = tk.PanedWindow(self.notepad_tab, orient=tk.HORIZONTAL,
                                   bg=self.bg_color, sashrelief="flat", sashwidth=6)
        main_pane.pack(expand=True, fill="both", padx=20, pady=10)

        editor_frame = tk.Frame(main_pane, bg=self.bg_color)
        main_pane.add(editor_frame, width=850)

        self.hachukma_title_label = tk.Label(editor_frame, text="📝  Hachukma Script",
                                             font=("Segoe UI", 12, "bold"),
                                             bg=self.bg_color, fg=self.accent_color)
        self.hachukma_title_label.pack(anchor="w", padx=10, pady=(0, 5))

        text_frame = tk.Frame(editor_frame, bg=self.bg_color)
        text_frame.pack(expand=True, fill="both")

        default_font = ("Segoe UI", self.default_font_size)
        self.text_area = tk.Text(
            text_frame,
            font=default_font,
            wrap="word",
            undo=True,
            bg=self.editor_bg,
            fg=self.editor_fg,
            insertbackground=self.accent_color,
            relief="flat",
            padx=30,
            pady=30,
            spacing2=15,
            spacing3=12
        )
        scrollbar = ttk.Scrollbar(text_frame, orient="vertical", command=self.text_area.yview)
        self.text_area.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self.text_area.pack(side="left", expand=True, fill="both")

        self.text_area.tag_configure("glyph", font=self.hachukma_font)

        self.text_area.bind("<KeyRelease>", self.update_wordcount, add='+')
        self.text_area.bind("<KeyRelease>", self.update_translation, add='+')
        self.text_area.bind("<KeyPress>", self.handle_keypress, add='+')

        translator_frame = tk.Frame(main_pane, bg=self.keyboard_bg, relief="flat", bd=1)
        main_pane.add(translator_frame, width=320)

        self.roman_interpreter_label = tk.Label(translator_frame, text="📖  Roman Interpreter",
                                                font=("Segoe UI", 12, "bold"),
                                                bg=self.keyboard_bg, fg=self.accent_color)
        self.roman_interpreter_label.pack(pady=10)

        self.translation_text = tk.Text(
            translator_frame,
            font=self.roman_font,
            bg=self.keyboard_bg,
            fg=self.fg_color,
            relief="flat",
            wrap="word",
            padx=15,
            pady=15,
            height=20,
            spacing2=5
        )
        self.translation_text.pack(fill="both", expand=True, padx=10, pady=5)
        self.translation_text.config(state="disabled")

        copy_btn = ttk.Button(translator_frame, text="📋 Copy Roman",
                              command=self.copy_translation)
        copy_btn.pack(pady=(0, 15))

        self.translator_frame = translator_frame
        self.update_translation()

    # --------------------------------------------------------
    # Helper: apply glyph tags to a range (skip spaces/newlines)
    # --------------------------------------------------------
    def apply_glyph_tags(self, start="1.0", end="end"):
        """Apply the 'glyph' tag to all Hachukma glyphs in the given range."""
        content = self.text_area.get(start, end)
        pos = start
        for ch in content:
            if ch in MAPPINGS.values():
                self.text_area.tag_add("glyph", pos, f"{pos}+1c")
            pos = self.text_area.index(f"{pos}+1c")

    # --------------------------------------------------------
    # Helper: apply Hachukma font to glyphs in a selection with a specific size
    # --------------------------------------------------------
    def apply_glyph_font_to_selection(self, start, end, size):
        """Apply the Hachukma font with the given size to glyphs in the selection."""
        glyph_font_obj = font.Font(family=self.font_name, size=size)
        tag_name = f"glyph_size_{self.size_tag_counter}"
        self.text_area.tag_configure(tag_name, font=glyph_font_obj)
        content = self.text_area.get(start, end)
        pos = start
        for ch in content:
            if ch in MAPPINGS.values():
                self.text_area.tag_add(tag_name, pos, f"{pos}+1c")
            pos = self.text_area.index(f"{pos}+1c")
        return tag_name

    # --------------------------------------------------------
    # Word count
    # --------------------------------------------------------
    def update_wordcount(self, event=None):
        content = self.text_area.get("1.0", tk.END).strip()
        chars = len(content)
        words = len(content.split()) if content else 0
        self.wordcount_label.config(text=f"Chars: {chars} | Words: {words}")

    # --------------------------------------------------------
    # Roman interpreter – shows transliteration + punctuation as‑is
    # --------------------------------------------------------
    def update_translation(self, event=None):
        hachu_text = self.text_area.get("1.0", tk.END).strip()
        roman_text = self.hachukma_to_roman(hachu_text)
        self.translation_text.config(state="normal")
        self.translation_text.delete("1.0", tk.END)
        self.translation_text.insert("1.0", roman_text)
        self.translation_text.config(state="disabled")

    def hachukma_to_roman(self, hachu):
        result = []
        for ch in hachu:
            if ch in REVERSE_MAPPINGS:
                result.append(REVERSE_MAPPINGS[ch])
            else:
                result.append(ch)
        return ''.join(result)

    # --------------------------------------------------------
    # Font size – applies to selected text if any, else whole document
    # --------------------------------------------------------
    def change_font_size(self):
        new_size = self.font_size_var.get()

        try:
            sel_start = self.text_area.index("sel.first")
            sel_end = self.text_area.index("sel.last")
            has_selection = True
        except tk.TclError:
            has_selection = False

        if has_selection:
            self.size_tag_counter += 1
            base_tag = f"size_tag_{self.size_tag_counter}"
            self.text_area.tag_configure(base_tag, font=("Segoe UI", new_size))
            self.text_area.tag_add(base_tag, sel_start, sel_end)
            self.apply_glyph_font_to_selection(sel_start, sel_end, new_size)
        else:
            self.default_font_size = new_size
            self.text_area.configure(font=("Segoe UI", new_size))
            self.hachukma_font.configure(size=new_size)
            self.text_area.tag_configure("glyph", font=self.hachukma_font)

    # --------------------------------------------------------
    # Pick foreground color – apply to selected text if any, else whole document
    # --------------------------------------------------------
    def pick_fg_color(self):
        try:
            sel_start = self.text_area.index("sel.first")
            sel_end = self.text_area.index("sel.last")
            has_selection = True
        except tk.TclError:
            has_selection = False

        color = colorchooser.askcolor(title="Choose Text Color", parent=self.root)
        if not color[1]:
            return

        if has_selection:
            self.color_tag_counter += 1
            tag_name = f"user_color_{self.color_tag_counter}"
            self.text_area.tag_configure(tag_name, foreground=color[1])
            self.text_area.tag_add(tag_name, sel_start, sel_end)
        else:
            self.text_area.configure(fg=color[1])
            self.editor_fg = color[1]

    # --------------------------------------------------------
    # Pick background color – applies to whole text area
    # --------------------------------------------------------
    def pick_bg_color(self):
        color = colorchooser.askcolor(title="Choose Background Color", parent=self.root)
        if color[1]:
            self.editor_bg = color[1]
            self.text_area.configure(bg=self.editor_bg)

    # --------------------------------------------------------
    # IME core – with Enter key fix
    # --------------------------------------------------------
    def handle_keypress(self, event):
        if event.state & 0x4 or event.state & 0x20000:
            return
        char = event.char
        if not char or (ord(char) < 32 and char not in ('\r', '\n')):
            return

        lower_char = char.lower()
        now = time.time()

        # ---- 1. Dedicated tone key ----
        if char == '~':
            self.text_area.insert("insert", '\uE024', ("glyph",))
            self.last_key = None
            self.pending_tone_letter = None
            return "break"

        # ---- 2. Handle 'p' key ----
        if lower_char == 'p':
            if self.last_key == 'p' and (now - self.last_time) < self.multi_tap_delay:
                self.text_area.delete("insert-1c", "insert")
                cursor = self.text_area.index("insert")
                if cursor != "1.0":
                    prev_char = self.text_area.get(f"{cursor} -1c", cursor)
                    if prev_char in MAPPINGS.values():
                        self.text_area.insert(cursor, '\uE024', ("glyph",))
                    else:
                        self.text_area.insert(cursor, MAPPINGS['p'], ("glyph",))
                else:
                    self.text_area.insert(cursor, MAPPINGS['p'], ("glyph",))
                self.last_key = None
                self.last_time = 0
                self.roman_buffer = ""
                return "break"

            self.text_area.insert("insert", MAPPINGS['p'], ("glyph",))
            self.last_key = 'p'
            self.last_time = now
            self.roman_buffer += 'p'
            return "break"

        # ---- 3. Letters ----
        if 'a' <= lower_char <= 'z' and lower_char != 'p':
            glyph = MAPPINGS[lower_char]
            self.text_area.insert("insert", glyph, ("glyph",))
            self.last_key = lower_char
            self.last_time = now
            self.roman_buffer += lower_char
            self.pending_tone_letter = glyph

            for digraph in DIGRAPHS.keys():
                if self.roman_buffer.endswith(digraph):
                    start = self.text_area.index("insert-2c")
                    end = self.text_area.index("insert")
                    self.text_area.tag_add("digraph_strike", start, end)
                    self.text_area.tag_config("digraph_strike", overstrike=True, foreground="red")
                    self.roman_buffer = ""
                    break
            return "break"

        # ---- 4. Digits ----
        if '0' <= lower_char <= '9':
            if lower_char in MAPPINGS:
                self.text_area.insert("insert", MAPPINGS[lower_char], ("glyph",))
                self.last_key = lower_char
                self.last_time = now
                self.pending_tone_letter = None
                self.roman_buffer = ""
                return "break"

        # ---- 5. Everything else: punctuation, symbols, spaces, newlines ----
        else:
            self.roman_buffer = ""
            self.pending_tone_letter = None
            # Insert without a tag – uses default font (Segoe UI)
            # Convert carriage return to newline for proper line breaks
            if char == '\r':
                insert_char = '\n'
            else:
                insert_char = char
            self.text_area.insert("insert", insert_char)
            self.last_key = None
            return "break"

        return None

    # --------------------------------------------------------
    # File operations
    # --------------------------------------------------------
    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                  filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(self.text_area.get("1.0", tk.END))
            messagebox.showinfo("Saved", f"File saved to {file_path}")

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert("1.0", content)
            self.apply_glyph_tags()
            self.update_wordcount()
            self.update_translation()
            self.roman_buffer = ""
            self.pending_tone_letter = None

    def clear_notepad(self):
        self.text_area.delete("1.0", tk.END)
        self.update_wordcount()
        self.update_translation()
        self.roman_buffer = ""
        self.pending_tone_letter = None

    # --------------------------------------------------------
    # Other helpers
    # --------------------------------------------------------
    def copy_translation(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.translation_text.get("1.0", tk.END).strip())
        self.root.update()
        messagebox.showinfo("Copied", "Roman transliteration copied to clipboard.")

if __name__ == "__main__":
    root = tk.Tk()
    app = HachukmaNotepad(root)
    root.mainloop()
