import tkinter as tk
from tkinter import ttk, messagebox
import random
import time
from constants import MAPPINGS



# 445 totals words added
ROMAN_WORDS = [ "awang",
  "bacha", "khunju", "nahar", "nono", "norok", "nəng", 
  "phai", "tabuk", "takhukrok,", "tamo", "tei", "thang", "aboni", "abono",
  "ang", "ani", "apha", "aphuru", "ba", "bini", "bo", "borok", "bəsa", "bəsano",
  "bərəima", "bəkhnai", "chini", "choba", "ha", "joto", "juda",
  "kaham","kerongno", "khajak", "khoroksa", "kothoma", "kotor", "kəplai",
  "kəthar", "kəthəi", "lamthai", "langma", "musi",  "naisik", "nokhao",
  "nono", "norok", "norokni", "nɘng", "orono", "phola", "sinai",


  "sindrai", "səkango", "ta", "takhukrok", "tamni", "tamo",                       
  "tatal", "tei", "tong", "təimuk", "ulo", "yak", "yang", "abo", "achugui",
  "achuk", "achukjak", "agi", "agini", "agibo", "ainani", "aitor", "ama",
  "amjokna", "ano", "antəi", "aphuru", "arirokno", "aro", "aroni",
  "asək", "athukiri",  "bacha", "bachai", "bagəi", "bai", "baithang",
  "baksa", "bao", "bebak", "bedek", "belai", "bera", "bini", "birjak", "birman",
  "birəi", "bisingni", "bisiktham", "bithi", "bləisa", "bobo", "boh", "bohok",
  "bono", "bori", "borok", "borokrok", "bororokni",
  "bororokno", "bosong", "bosong,", "bosongni,", "bosongno", "brum", "brəi",
  "brəio", "bujak", "bukhuk", "bukhugo", "bului", "bumukhang", "bumun", "buro",


  "buya", "bəcha", "bəchap", "bədam", 

  "bərirokno", "bərəima", "bərəi", "bəskang", "bəthai",                       
  "bətəino", "cha", "chadi", "chana", "chap", "chini", "chirikhok", "chirik",
  "choba", "chəngsacha", "chərai", "da", "daina", "dakti", "di", "dolsa",
  "dopha", "dumjak", "eba", "garing", "glak", "gosinai", "gosio", "gədal",
  "gənang", "haino", "hai", "hambai", "hamjak", "hamya", "hao", "hasing",
  "hatai", "haya", "holong", "homchang", "hor", "horljaini", "huijak", "hən",
  "hənjak", "həno", "hənəi", "jabra", "jak", "jolijak", "jora", "jorsa",
  "jotoni", "jotono", "kaisa", "kangsa", "kangnəi", "kanjak", "kaya",                       
  "kebeng", "kebo", "kha", "khaching", "khajaknaino;", "khajuri", "khak",
  "khaksa", "khakthamni", "kham", "khar", "kharəi", "kheno", "khibinai",
  "khitar", "khlai", "kho", "khobjak,", "khogəi", "khok", "kholob", "khorang",
  "khoroksa", "khoroksani", "khoroksano", "khoroktham", "khulum", "khəi",
  "kiching", "kirima", "kiri", "kisa", "klaijak", "klai", "klaiəi", "kok",
  "kolok",  "kotor", "kotorma", 


  "kotoino", "kotor rok", "kothor", "kubui", 
  "kuphur", "kuphur", "kuplung", "kutung", "kutung", "kusu", "kutukma",
  "kəbangma", "kəbangma", "kəchak", "kəchak.", "kəchang", "kəchar",                  
  "kəcharo", "kəcharni", "kəchəng", "kəkhrang", "kəma", "kəmai", "kənəi",                     
  "kəplai", "kəplairok", "kərəi", "kərəng", "kəsa", "kətal", "kəthang",                       
  "kəthar", "kəthəi", "kəthəngrok", "kətəi",  "lai",
  "laijak", "laina", "laio", "laiəi", "lam", "lama", 


  "langta", "lobmani", "logi", "mani", "mano", "manthok", "manəi", "mari",
  "masano", "modu", "motok", "muchung", "muchungma", "muktəi", "mung",              
  "mungsa", "məsa", "naidi", "nang", "nango", "nini", "nobar", "nogo",
  "nok", "nokha", "norok", "norokbo", "norokni", "nugui", "nugo", "nuhur",
  "nuk", "nukjak", "nukmani", "nəng", "nəngjak", "okra", "omo", "ongkhor",
  "ongkhlai", "paibo", "pai", "painai", "phaina", "phan", "phano", "phataro",
  "philik", "phiya", "phiyok", "phunuk", "phunukna", "phunuknai",
  "pohor", "pətap", "pətapsa", "raidang", "rak", "ri", "riphrik",   
  
  
  "rogo", "rohor", "rohorjak", "rohorjaknai", "rom", "romo", "rə",
  "rəjak", "rəjakma", "rəjaknai", "rəjagəi", "rəkhtharjak", "rəma", "rəmani",
  "rəmano", "rənai", "rəng", "sa", "sabo", "sai", "sajak", "sak",
  "saka", "saklaina", "sal", "salbo", "salkabaini", "salo", "salsani",
  "saltham", "sama", "samani", "samano", "sanai", "sao,", "satok", "satokjak",
  "seleng", "seng", "sengkrak", "sicha", "sikla", "sikok", "simi",
  "simino", "sina", "sini", "sinino", "sio", "sitra", "skango", "smai",
  "snamjak", "snamnai", "snamo", "sokdi", "songni", "səi", "səijak",
  "səkdi", "səkagəi", "səkak", "səkakma", "səkango", "səndək", "səng",    
  
  
  "səngchar", "səngcharni", "səngcharno", "takhuk", "tak",
  "tal", "tamni", "tamna", "tamono", "tang", "tangma", "tangmani",
  "tangna", "tangnai", "tangsa", "tapsa", "tatal", "tei", "tekto", "tektoni",
  "thai", "thango", "thani", "thəi", "thəima", "toling", "tongdi", "təi",
  "təimuk", "ulo", "əng", "əngjak", 
  "yabrəi", "yachak", "yakung", "yaksi", "yang", "yaphango",
  "yapharjak", "yarok", "yarokno", "yasku" ,"watəi" , "wa","wasung" , "wacheng" ,"thang",

]
NUM_WORDS = 10

TOKEN_TO_KEY = {
    'kh': 'v', 'th': 'q', 'ph': 'f', 'ch': 'c', 'ng': 'x', 'ə': 'z'
}
KEY_TO_TOKEN = {v: k for k, v in TOKEN_TO_KEY.items()}

def roman_to_key_sequence(roman_word: str) -> str:
    tokens = []
    i = 0
    while i < len(roman_word):
        found = False
        for digraph in ['kh', 'th', 'ph', 'ch', 'ng']:
            if roman_word[i:i+len(digraph)] == digraph:
                tokens.append(digraph)
                i += len(digraph)
                found = True
                break
        if not found:
            tokens.append(roman_word[i])
            i += 1
    keys = []
    for token in tokens:
        keys.append(TOKEN_TO_KEY.get(token, token))
    return ''.join(keys)

def roman_to_hachukma(roman_word: str) -> str:
    key_seq = roman_to_key_sequence(roman_word)
    return ''.join(MAPPINGS.get(ch, ch) for ch in key_seq)

def typed_to_roman(typed: str) -> str:
    typed = typed.replace('\u200B', '').replace('\u0336', '')
    result = []
    i = 0
    while i < len(typed):
        if typed[i] in KEY_TO_TOKEN:
            result.append(KEY_TO_TOKEN[typed[i]])
            i += 1
        else:
            result.append(typed[i])
            i += 1
    return ''.join(result)

def setup_monkeytype(app):
    app.monkey_tab = tk.Frame(app.notebook, bg=app.bg_color)
    app.notebook.add(app.monkey_tab, text="  🐵  Typing Practice  ")

    main = tk.Frame(app.monkey_tab, bg=app.bg_color)
    main.pack(fill="both", expand=True, padx=40, pady=30)

    title = tk.Label(main, text=f"⏱️  Type {NUM_WORDS} Words", font=("Segoe UI", 16, "bold"),
                     bg=app.bg_color, fg=app.accent_color)
    title.pack(pady=(0, 15))
    app.monkey_title = title

    info = tk.Label(main, text="Use shortcut keys: v→kh, q→th, x→ng, f→ph, c→ch, z→ə",
                    font=("Segoe UI", 10), bg=app.bg_color, fg=app.sub_color)
    info.pack(pady=(0, 10))
    app.monkey_info_label = info

    timer_frame = tk.Frame(main, bg=app.bg_color)
    timer_frame.pack(pady=5)
    timer_label = tk.Label(timer_frame, text="Time limit (seconds):", font=("Segoe UI", 11),
                           bg=app.bg_color, fg=app.fg_color)
    timer_label.pack(side="left", padx=5)
    app.monkey_timer_label = timer_label
    timer_var = tk.IntVar(value=60)
    timer_spin = tk.Spinbox(timer_frame, from_=15, to=180, textvariable=timer_var,
                            width=6, bg=app.bg_color, fg=app.fg_color, relief="flat")
    timer_spin.pack(side="left", padx=5)
    app.monkey_timer_spin = timer_spin

    progress = ttk.Progressbar(main, length=400, mode='determinate', maximum=NUM_WORDS)
    progress.pack(pady=10)

    display_frame = tk.Frame(main, bg=app.keyboard_bg, relief="ridge", bd=2)
    display_frame.pack(fill="x", pady=10, padx=20, ipady=30)
    glyph_label = tk.Label(display_frame, text="", font=(app.font_name, 48, "bold"),
                           bg=app.keyboard_bg, fg=app.fg_color)
    glyph_label.pack(pady=(10, 0))
    roman_label = tk.Label(display_frame, text="", font=("Segoe UI", 14, "italic"),
                           bg=app.keyboard_bg, fg=app.sub_color)
    roman_label.pack(pady=(0, 10))

    completed_frame = tk.Frame(main, bg=app.bg_color)
    completed_frame.pack(fill="x", pady=5)
    tk.Label(completed_frame, text="Completed:", font=("Segoe UI", 10),
             bg=app.bg_color, fg=app.sub_color).pack(anchor="w")
    completed_container = tk.Frame(completed_frame, bg=app.bg_color)
    completed_container.pack(fill="x", pady=2)
    completed_labels = []

    progress_label = tk.Label(main, text=f"Word 0 / {NUM_WORDS}", font=("Segoe UI", 11),
                              bg=app.bg_color, fg=app.sub_color)
    progress_label.pack(pady=5)

    input_frame = tk.Frame(main, bg=app.bg_color)
    input_frame.pack(fill="x", pady=10)
    tk.Label(input_frame, text="Type the word (press Space or Enter):",
             font=("Segoe UI", 11), bg=app.bg_color, fg=app.fg_color).pack(anchor="w")

    user_text = tk.Text(input_frame, height=1, font=("Consolas", 18),
                        bg=app.editor_bg, fg=app.fg_color,
                        insertbackground=app.accent_color,
                        relief="sunken", bd=2, wrap="none")
    user_text.pack(fill="x", pady=5, ipady=5)
    user_text.config(state="disabled")
    user_text.tag_configure("error", foreground="red", overstrike=True)

    control_frame = tk.Frame(main, bg=app.bg_color)
    control_frame.pack(fill="x", pady=8)
    start_btn = ttk.Button(control_frame, text="🚀 Start", command=lambda: start_test())
    start_btn.pack(side="left", padx=5)
    reset_btn = ttk.Button(control_frame, text="🔄 Reset", command=lambda: reset_test())
    reset_btn.pack(side="left", padx=5)

    stats_frame = tk.Frame(main, bg=app.bg_color)
    stats_frame.pack(pady=10)
    stats_label = tk.Label(stats_frame, text="WPM: 0   |   Acc: 0%   |   Time: 0s",
                           font=("Segoe UI", 12), bg=app.bg_color, fg=app.sub_color)
    stats_label.pack(side="left")
    info_btn = ttk.Button(stats_frame, text="ℹ️", width=2,
                          command=lambda: messagebox.showinfo(
                              "What do the stats mean?",
                              "📊 WPM (Words Per Minute):\n"
                              "How many words you type per minute on average.\n"
                              "Example: If you type 3 words in 30 seconds, your WPM is 6.\n\n"
                              "🎯 Accuracy:\n"
                              "The percentage of words you typed correctly.\n"
                              "Example: If you type 4 words correctly out of 5 attempts, your Accuracy is 80%.\n\n"
                              "📈 Avg WPM (in chart):\n"
                              "The average of each word's individual WPM.\n"
                              "Example: If your per‑word WPMs are 10, 15, 20, the Avg WPM is 15.\n\n"
                              "📊 Avg Accuracy (in chart):\n"
                              "The average of each word's individual accuracy.\n"
                              "Example: If your per‑word accuracies are 100%, 100%, 0%, the Avg Accuracy is 66%.\n\n"
                              "✅ Words:\n"
                              f"Number of words you completed out of {NUM_WORDS}.\n\n"
                              "⏱️ Time:\n"
                              "The remaining time or the total time taken.\n\n"
                              "📉 Chart colors:\n"
                              "  - Orange bars: WPM for each word.\n"
                              "  - Green bars: Accuracy for each word (100% if correct, 0% if wrong).\n\n"
                              "The chart shows WPM and Accuracy for each individual word."
                          ))
    info_btn.pack(side="left", padx=8)

    state = {
        "roman_words": [],
        "glyph_words": [],
        "current_index": 0,
        "start_time": None,
        "finished": False,
        "word_results": [],
        "total_correct": 0,
        "total_attempts": 0,
        "time_limit": 60,
        "time_left": 60,
        "word_display_times": [],
        "word_times": [],
        "word_wpm": [],
        "word_acc": [],
    }

    def update_strikes(event=None):
        raw = user_text.get("1.0", tk.END).rstrip('\n')
        user_text.tag_remove("error", "1.0", tk.END)
        digraphs = ["th", "kh", "ph", "ch", "ng"]
        for d in digraphs:
            start = 0
            while True:
                pos = raw.find(d, start)
                if pos == -1:
                    break
                start_idx = f"1.0+{pos}c"
                end_idx = f"1.0+{pos+len(d)}c"
                user_text.tag_add("error", start_idx, end_idx)
                start = pos + len(d)

    def on_keypress(event):
        ch = (event.char or '').lower()
        if not ch:
            return
        if ch in KEY_TO_TOKEN:
            digraph = KEY_TO_TOKEN[ch]
            if len(digraph) == 2:
                insert_text = digraph[0] + '\u200B' + digraph[1]
            else:
                insert_text = digraph
            user_text.insert(tk.INSERT, insert_text)
            app.root.after(10, update_strikes)
            return "break"
        return None

    def handle_submit(event):
        if state["finished"]:
            return "break"
        raw = user_text.get("1.0", tk.END).rstrip('\n')
        if not raw:
            return "break"
        if user_text.tag_ranges("error"):
            # Flash the background red
            user_text.config(bg="#FF6B6B")
            # Blink the error tags: temporarily change their foreground to white then back to red
            user_text.tag_configure("error", foreground="white")
            # Blink the info label: change its foreground to red then back to sub_color
            info.config(fg="red")
            # Revert after 300ms
            def revert():
                user_text.tag_configure("error", foreground="red")
                user_text.config(bg=app.editor_bg)
                info.config(fg=app.sub_color)
            app.root.after(300, revert)
            return "break"
        check_word(raw)
        return "break"

    def check_word(raw_typed):
        if state["finished"] or state["current_index"] >= len(state["roman_words"]):
            return
        idx = state["current_index"]
        target = state["roman_words"][idx]
        converted = typed_to_roman(raw_typed)
        correct = (converted == target)
        state["total_attempts"] += 1
        if len(state["word_display_times"]) > idx:
            word_time = time.time() - state["word_display_times"][idx]
        else:
            word_time = 0
        state["word_results"][idx] = correct
        if correct:
            state["total_correct"] += 1
            state["word_times"].append(word_time)
            wpm = int((1 / word_time) * 60) if word_time > 0.5 else 120
            state["word_wpm"].append(wpm)
            state["word_acc"].append(100)
        else:
            state["word_times"].append(0)
            state["word_wpm"].append(0)
            state["word_acc"].append(0)
            user_text.config(bg="#FFB6C1")
            app.root.after(300, lambda: user_text.config(bg=app.editor_bg))
        state["current_index"] += 1
        user_text.delete("1.0", tk.END)
        update_display()
        update_live_stats()
        if state["current_index"] >= len(state["roman_words"]):
            finish_test()

    def update_display():
        if state["finished"]:
            glyph_label.config(text="🎉")
            roman_label.config(text="All done!")
            progress_label.config(text=f"{len(state['roman_words'])} / {len(state['roman_words'])}")
            return
        if state["current_index"] >= len(state["roman_words"]):
            finish_test()
            return
        idx = state["current_index"]
        glyph_label.config(text=state["glyph_words"][idx])
        roman_label.config(text=state["roman_words"][idx])
        progress_label.config(text=f"Word {idx+1} of {len(state['roman_words'])}")
        state["word_display_times"].append(time.time())
        correct_count = sum(1 for r in state["word_results"] if r is True)
        progress['value'] = correct_count
        progress.update()
        for lbl in completed_labels:
            lbl.destroy()
        completed_labels.clear()
        for i, word in enumerate(state["roman_words"]):
            if i < len(state["word_results"]):
                if state["word_results"][i] is True:
                    fg = "#4CAF50"
                    font_style = ("Segoe UI", 10)
                elif state["word_results"][i] is False:
                    fg = "#FF6B6B"
                    font_style = ("Segoe UI", 10, "overstrike")
                else:
                    continue
                chip = tk.Frame(completed_container, bg=app.bg_color)
                chip.pack(side="left", padx=4, pady=2)
                tk.Label(chip, text=state["glyph_words"][i],
                         font=(app.font_name, 16, "bold"),
                         bg=app.bg_color, fg=fg).pack()
                tk.Label(chip, text=word, font=font_style,
                         bg=app.bg_color, fg=fg).pack()
                completed_labels.append(chip)

    def update_live_stats():
        if state["start_time"] is None or state["finished"]:
            return
        elapsed = time.time() - state["start_time"]
        correct = state["total_correct"]
        wpm = int((correct / (elapsed / 60))) if elapsed > 0 and correct > 0 else 0
        attempts = state["total_attempts"]
        acc = int((state["total_correct"] / attempts) * 100) if attempts > 0 else 0
        stats_label.config(text=f"WPM: {wpm}   |   Acc: {acc}%   |   Time: {state['time_left']}s")

    def update_timer():
        if state["finished"] or state["start_time"] is None:
            return
        elapsed = int(time.time() - state["start_time"])
        state["time_left"] = max(0, state["time_limit"] - elapsed)
        update_live_stats()
        if state["time_left"] <= 0:
            finish_test(timed_out=True)
            return
        app.root.after(1000, update_timer)

    def show_chart():
        if len(state["word_wpm"]) == 0:
            messagebox.showinfo("No Data", "No word data to display.")
            return

        chart_window = tk.Toplevel(app.root)
        chart_window.title("Hachukma Typing Results")
        chart_window.geometry("750x480")
        chart_window.configure(bg=app.bg_color)

        chart_window.update_idletasks()
        x = (chart_window.winfo_screenwidth() // 2) - (750 // 2)
        y = (chart_window.winfo_screenheight() // 2) - (480 // 2)
        chart_window.geometry(f"+{x}+{y}")

        canvas = tk.Canvas(chart_window, bg=app.bg_color, highlightthickness=0)
        canvas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        wpm_data = state["word_wpm"]
        acc_data = state["word_acc"]
        n = len(wpm_data)
        labels = [f"W{i+1}" for i in range(n)]

        max_wpm = max(wpm_data) if wpm_data else 1
        max_acc = max(acc_data) if acc_data else 1
        max_val = max(max_wpm, max_acc, 1)

        bar_width = 30
        spacing = 20
        group_width = 2 * bar_width + spacing
        total_width = n * group_width + 40
        chart_width = max(550, total_width)

        canvas.create_text(chart_width // 2, 25, text="📊 Typing Results",
                           fill=app.accent_color, font=("Segoe UI", 14, "bold"))

        start_x = 30
        y_base = 280

        canvas.create_text(start_x + (n * group_width) // 2, 55,
                           text="WPM", fill=app.fg_color, font=("Segoe UI", 11, "bold"))
        start_x2 = start_x + bar_width + spacing
        canvas.create_text(start_x2 + (n * group_width) // 2, 55,
                           text="Accuracy", fill=app.fg_color, font=("Segoe UI", 11, "bold"))

        for i, (lbl, val) in enumerate(zip(labels, wpm_data)):
            x = start_x + i * group_width
            height = (val / max_val) * 200 if max_val > 0 else 0
            canvas.create_rectangle(x, y_base - height, x + bar_width, y_base,
                                    fill="#ffb86c", outline="")
            canvas.create_text(x + bar_width/2, y_base + 15, text=lbl, fill=app.fg_color, font=("Segoe UI", 9))
            if val > 0:
                canvas.create_text(x + bar_width/2, y_base - height - 8, text=str(val), fill=app.fg_color, font=("Segoe UI", 9))

        for i, (lbl, val) in enumerate(zip(labels, acc_data)):
            x = start_x2 + i * group_width
            height = (val / max_val) * 200 if max_val > 0 else 0
            canvas.create_rectangle(x, y_base - height, x + bar_width, y_base,
                                    fill="#4CAF50", outline="")
            canvas.create_text(x + bar_width/2, y_base + 15, text=lbl, fill=app.fg_color, font=("Segoe UI", 9))
            if val > 0:
                canvas.create_text(x + bar_width/2, y_base - height - 8, text=f"{val}%", fill=app.fg_color, font=("Segoe UI", 9))

        avg_wpm = int(sum(wpm_data)/len(wpm_data)) if wpm_data else 0
        avg_acc = int(sum(acc_data)/len(acc_data)) if acc_data else 0
        canvas.create_text(chart_width // 2, 340,
                           text=f"Avg WPM: {avg_wpm}  |  Avg Accuracy: {avg_acc}%  |  Words: {len(wpm_data)}/{NUM_WORDS}",
                           fill=app.accent_color, font=("Segoe UI", 12, "bold"))

        close_btn = ttk.Button(chart_window, text="Close", command=chart_window.destroy)
        close_btn.pack(pady=5)

    def start_test():
        state["time_limit"] = timer_var.get()
        state["time_left"] = state["time_limit"]
        roman_words = shuffle_words()
        state["roman_words"] = roman_words
        state["glyph_words"] = [roman_to_hachukma(w) for w in roman_words]
        state["current_index"] = 0
        state["word_results"] = [None] * len(roman_words)
        state["start_time"] = time.time()
        state["finished"] = False
        state["total_correct"] = 0
        state["total_attempts"] = 0
        state["word_display_times"] = []
        state["word_times"] = []
        state["word_wpm"] = []
        state["word_acc"] = []

        user_text.config(state="normal")
        user_text.delete("1.0", tk.END)
        user_text.focus_set()
        start_btn.config(state="disabled")
        timer_spin.config(state="disabled")
        stats_label.config(text=f"WPM: 0   |   Acc: 0%   |   Time: {state['time_left']}s")
        update_display()
        app.root.after(100, update_timer)

    def finish_test(timed_out=False):
        if state["finished"]:
            return
        state["finished"] = True
        user_text.config(state="disabled")
        start_btn.config(state="normal")
        timer_spin.config(state="normal")
        elapsed = state["time_limit"] - state["time_left"]
        correct = state["total_correct"]
        total_words = len(state["roman_words"])
        wpm = int((correct / elapsed) * 60) if elapsed > 0 and correct > 0 else 0
        accuracy = int((state["total_correct"] / state["total_attempts"]) * 100) if state["total_attempts"] > 0 else 0
        stats_label.config(text=f"WPM: {wpm}   |   Acc: {accuracy}%   |   Time: {elapsed}s")
        update_display()
        msg = f"You ran out of time!\n\nCompleted: {correct} / {total_words} words correct\nWPM: {wpm}\nAccuracy: {accuracy}%" if timed_out else f"You completed all words!\n\nCorrect: {correct} / {total_words}\nWPM: {wpm}\nAccuracy: {accuracy}%\nTime: {elapsed}s"
        if messagebox.askyesno("Results", msg + "\n\nView detailed chart?"):
            show_chart()

    def reset_test():
        state["finished"] = True
        state["roman_words"] = []
        state["glyph_words"] = []
        state["current_index"] = 0
        state["word_results"] = []
        state["start_time"] = None
        state["total_correct"] = 0
        state["total_attempts"] = 0
        state["time_left"] = timer_var.get()
        state["word_display_times"] = []
        state["word_times"] = []
        state["word_wpm"] = []
        state["word_acc"] = []

        user_text.config(state="disabled")
        user_text.delete("1.0", tk.END)
        start_btn.config(state="normal")
        timer_spin.config(state="normal")
        stats_label.config(text=f"WPM: 0   |   Acc: 0%   |   Time: {state['time_left']}s")
        progress['value'] = 0
        glyph_label.config(text="")
        roman_label.config(text="")
        progress_label.config(text=f"0 / {NUM_WORDS}")
        for lbl in completed_labels:
            lbl.destroy()
        completed_labels.clear()
        user_text.config(bg=app.editor_bg)

    def shuffle_words():
        selected = random.sample(ROMAN_WORDS, min(NUM_WORDS, len(ROMAN_WORDS)))
        random.shuffle(selected)
        return selected

    user_text.bind("<Key>", on_keypress)
    user_text.bind("<KeyRelease>", update_strikes)
    user_text.bind("<space>", handle_submit)
    user_text.bind("<Return>", handle_submit)

    app.monkey_progress = progress
    app.monkey_entry = user_text
    app.monkey_stats = stats_label
    app.monkey_timer_spin = timer_spin
    app.monkey_glyph_label = glyph_label
    app.monkey_roman_label = roman_label
    app.monkey_progress_label = progress_label
    app.monkey_completed_container = completed_container

    reset_test()
