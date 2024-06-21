# DBDAudioRenamer
It is a tool for Dead by Daylight that can extract UE4 files and rename audio files based on XML files.

# How to use it
1. Open ur CMD and write:
2. Example: cd C:\Users\Neinndall\Downloads\DBDAudioRenamer
3. pip install -r requirements.txt

If anything else is missing, let me know and I'll update it.

# Features
- [X] Extract files from PAK files from UE (v5.2)
  - Audio from Tomes (Tome01, Tome02...)
  - Main Audio (Killers, Survivors, Gameplay...)
- [X] Extract sound files (.bnk -> .wem)
- [X] Convert audio files (.wem -> .ogg) 
- [X] Convert audio files (.ogg -> .ogg revorb)
- [X] Rename audio files (.wem) with the new script parser renamer for (.xml) files

# Roadmap (To do)
- [ ] Move the extracted .pak files to their corresponding folders

# Suggestions
Any new feature suggestions? Create a ticket talking about it.

# Libraries
- [revorb](https://github.com/ItsBranK/ReVorb)
- [ww2ogg](https://github.com/hcs64/ww2ogg)
- [bnkextr](https://github.com/eXpl0it3r/bnkextr)
- [renamer-parser](https://github.com/Neinndall/renamer-parser)
