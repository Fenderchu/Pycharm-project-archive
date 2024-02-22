import PyInstaller.__main__
import os

PyInstaller.__main__.run([
    'name-%s%' % 'Abridged_ver01.exe',
    '--onefile',
    '--windowed',
    os.path.join('/Users/haydenb/PycharmProjects/Abridged/main.py', 'main.py'), """your script and path to the script"""
])
