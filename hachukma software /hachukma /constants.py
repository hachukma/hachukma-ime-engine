# constants.py – shared data across all modules

MAPPINGS = {
    'a': '\uE00A', 'b': '\uE00B', 'c': '\uE00C', 'd': '\uE00D', 'e': '\uE00E',
    'f': '\uE00F', 'g': '\uE010', 'h': '\uE011', 'i': '\uE012', 'j': '\uE013',
    'k': '\uE014', 'l': '\uE015', 'm': '\uE016', 'n': '\uE017', 'o': '\uE018',
    'p': '\uE019', 'q': '\uE01A', 'r': '\uE01B', 's': '\uE01C', 't': '\uE01D',
    'u': '\uE01E', 'v': '\uE01F', 'w': '\uE020', 'x': '\uE021', 'y': '\uE022',
    'z': '\uE023', '0': '\uE000', '1': '\uE001', '2': '\uE002', '3': '\uE003',
    '4': '\uE004', '5': '\uE005', '6': '\uE006', '7': '\uE007', '8': '\uE008',
    '9': '\uE009', ' ': ' ', '\r': '\n', '\n': '\n',
}

REVERSE_MAPPINGS = {
    '\uE00A': 'a', '\uE00B': 'b', '\uE00C': 'ch', '\uE00D': 'd', '\uE00E': 'e',
    '\uE00F': 'ph', '\uE010': 'g', '\uE011': 'h', '\uE012': 'i', '\uE013': 'j',
    '\uE014': 'k', '\uE015': 'l', '\uE016': 'm', '\uE017': 'n', '\uE018': 'o',
    '\uE019': 'p', '\uE01A': 'th', '\uE01B': 'r', '\uE01C': 's', '\uE01D': 't',
    '\uE01E': 'u', '\uE01F': 'kh', '\uE020': 'w', '\uE021': 'ng', '\uE022': 'y',
    '\uE023': 'ə',
    '\uE000': '0', '\uE001': '1', '\uE002': '2', '\uE003': '3', '\uE004': '4',
    '\uE005': '5', '\uE006': '6', '\uE007': '7', '\uE008': '8', '\uE009': '9',
}


MULTI_TAP = {}
for ch, glyph in MAPPINGS.items():
    # only letters should get the diacritic mapping
    if ch.isalpha():
        MULTI_TAP[ch] = glyph + '\uE024'

CHART_DATA = [
    ('\uE00A', '/a/ng'),
    ('\uE00B', '/b/uphang-kəthəi'),
    ('\uE00C', '/ch/əng'),
    ('\uE00D', '/d/angdol'),
    ('\uE00E', '/e/imang'),
    ('\uE00F', '/ph/arok'),
    ('\uE010', '/g/olari'),
    ('\uE011', '/h/angrai-nok'),
    ('\uE012', '/i/aikha'),
    ('\uE013', '/j/ubar-bubar'),
    ('\uE014', '/k/owai-buphang'),
    ('\uE015', '/l/anga'),
    ('\uE016', '/m/əsəi-bokhorok'),
    ('\uE017', '/n/oboraisa'),
    ('\uE018', '/o/nchi'),
    ('\uE019', '/p/otdo-bubar'),
    ('\uE01A', '/th/aichumui'),
    ('\uE01B', '/r/omo'),
    ('\uE01C', '/s/indrai'),
    ('\uE01D', '/t/ok-thunta'),
    ('\uE01E', '/u/nklog'),
    ('\uE01F', '/kh/unta'),
    ('\uE020', '/w/a'),
    ('\uE021', '/ng/wasung'),
    ('\uE022', '/y/akung'),
    ('\uE023', '/ə/rə'),
]

# Vowels (6): a, e, i, o, u, ə
VOWELS = [
    ('\uE00A', '/a/ng'),
    ('\uE00E', '/e/imang'),
    ('\uE012', '/i/aikha'),
    ('\uE018', '/o/nchi'),
    ('\uE01E', '/u/nklog'),
    ('\uE023', '/ə/rə'),
]

# Consonants (all others)
CONSONANTS = [
    ('\uE00B', '/b/uphang-kəthəi'),
    ('\uE00C', '/ch/əng'),
    ('\uE00D', '/d/angdol'),
    ('\uE00F', '/ph/arok'),
    ('\uE010', '/g/olari'),
    ('\uE011', '/h/angrai-nok'),
    ('\uE013', '/j/ubar-bubar'),
    ('\uE014', '/k/owai-buphang'),
    ('\uE015', '/l/anga'),
    ('\uE016', '/m/əsəi-bokhorok'),
    ('\uE017', '/n/oboraisa'),
    ('\uE019', '/p/otdo-bubar'),
    ('\uE01A', '/th/aichumui'),
    ('\uE01B', '/r/omo'),
    ('\uE01C', '/s/indrai'),
    ('\uE01D', '/t/ok-thunta'),
    ('\uE01F', '/kh/unta'),
    ('\uE020', '/w/a'),
    ('\uE021', '/ng/wasung'),
    ('\uE022', '/y/akung'),
]

NUMERAL_DATA = [
    ('\uE000', 'sa (one)'),
    ('\uE001', 'nəi (two)'),
    ('\uE002', 'tham (three)'),
    ('\uE003', 'brəi (four)'),
    ('\uE004', 'ba (five)'),
    ('\uE005', 'dok (six)'),
    ('\uE006', 'sni (seven)'),
    ('\uE007', 'char (eight)'),
    ('\uE008', 'chuku (nine)'),
    ('\uE009', 'chi (ten)'),
]

TONE_DATA = [
    ('\uE024', 'TONE HIGH diacritic'),
]

THEMES = {
    "Dark": {
        "bg": "#1e1f2c", "fg": "#f8f8f2", "accent": "#ffb86c", "sub": "#6272a4",
        "keyboard_bg": "#282a36", "editor_bg": "#282a36", "editor_fg": "#f8f8f2"
    },
    "Light": {
        "bg": "#f0f0f0", "fg": "#1e1f2c", "accent": "#ff8c00", "sub": "#75715e",
        "keyboard_bg": "#e0e0e0", "editor_bg": "#ffffff", "editor_fg": "#1e1f2c"
    },
    "Ocean": {
        "bg": "#0b3b42", "fg": "#e0fbfc", "accent": "#ee6c4d", "sub": "#98c1d9",
        "keyboard_bg": "#1c4e5a", "editor_bg": "#1c4e5a", "editor_fg": "#e0fbfc"
    },
    "Forest": {
        "bg": "#1e3b2e", "fg": "#d4e6c3", "accent": "#f4a261", "sub": "#7d9d6e",
        "keyboard_bg": "#2a4a3a", "editor_bg": "#2a4a3a", "editor_fg": "#d4e6c3"
    },
    "Sunset": {
        "bg": "#3b2a3f", "fg": "#ffd6ba", "accent": "#ff9f1c", "sub": "#c77dff",
        "keyboard_bg": "#4a3b52", "editor_bg": "#4a3b52", "editor_fg": "#ffd6ba"
    },
    "Monochrome": {
        "bg": "#2c2c2c", "fg": "#d4d4d4", "accent": "#b0b0b0", "sub": "#808080",
        "keyboard_bg": "#3c3c3c", "editor_bg": "#3c3c3c", "editor_fg": "#d4d4d4"
    }
} 
