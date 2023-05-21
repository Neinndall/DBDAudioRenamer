# DBDAudioRenamer
It is a tool for Dead by Daylight that can extract UE4 files and rename audio files based on XML files.

# What do you need?
- [Python v3.9.0](https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe)

# How to use it

- Open CMD
- cd C:\Users\Neinndall\Downloads\DBDAudioRenamer
- pip install -r requirements.txt

If anything else is missing, let me know and I'll update it.

# Features
- [ ] [Removed, for now...] Extract files from PAK files from UE (v.4.27)
- [x] Extract sound files (.bnk -> .wem)
- [x] Convert audio files (.wem -> .ogg) 
- [x] Convert audio files (.ogg -> .ogg revorb)
- [x] Rename audio files with the (.xml) files

# Suggestions
Any new feature suggestions? Create a ticket talking about it.

# Libraries
- QuickBMS: https://aluigi.altervista.org/quickbms.htm
- ww2ogg: https://github.com/hcs64/ww2ogg
- bnkextr: https://github.com/eXpl0it3r/bnkextr
