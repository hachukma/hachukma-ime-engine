"""
setup.py - Build script for macOS using py2app
Run: python setup_macos.py py2app
"""

from setuptools import setup, find_packages
from py2app.util import alias_files
import os

# Get the directory containing this file
APP_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(APP_DIR)

APP = [os.path.join(PROJECT_DIR, 'hachukma', 'note_pad.py')]

OPTIONS = {
    'py2app': {
        'argv_emulation': True,
        'packages': [
            'tkinter',
            'PIL',
            'pyperclip',
        ],
        'includes': [],
        'excludes': [],
        'iconfile': os.path.join(PROJECT_DIR, 'assets', 'hachukma.icns'),
        'plist': {
            'NSPrincipalClass': 'NSApplication',
            'NSHighResolutionCapable': 'True',
            'CFBundleDisplayName': 'Hachukma IME',
            'CFBundleName': 'Hachukma IME',
            'CFBundleVersion': '1.0.0',
            'CFBundleShortVersionString': '1.0.0',
            'CFBundleIdentifier': 'com.hachukma.ime',
            'LSMinimumSystemVersion': '10.9',
        },
        'resources': [
            os.path.join(PROJECT_DIR, 'assets'),
            os.path.join(PROJECT_DIR, 'font'),
        ],
    },
}

setup(
    name='Hachukma IME',
    version='1.0.0',
    description='Hachukma Input Method Editor',
    author='Hachukma',
    url='https://github.com/hachukma/hachukma-ime-engine',
    app=APP,
    options=OPTIONS,
    setup_requires=['py2app'],
)
