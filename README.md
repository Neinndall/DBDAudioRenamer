# DBDAudioRenamer
Tool made for dead by daylight, which u can extract files from UE4 and rename the audio files based on XML files!

# What do you need?
- [Python v3.X](https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe)

# How to use it

- Open CMD
- cd C:\Users\Neinndall\Downloads\DBDAudioRenamer
- pip install -r requirements.txt

If anything else is missing, let me know and I'll update it.

# Features
- [X] [Supported Games] DeadByDaylight but could work with other games (notify me)
- [X] Extract files from PAK files from UE (v.5.2)
  - Main Audio (Killers, survivors, gameplay...)
  - Audio from Tomes (Tome01, Tome02...)
- [X] Extract sound files (.bnk -> .wem)
- [X] Convert audio files (.wem -> .ogg) 
- [X] Convert audio files (.ogg -> .ogg revorb)
- [X] Rename audio files (.wem) with the new script parser renamer for (.xml) files

# Suggestions
Any new feature suggestions? Create a ticket talking about it.

# Libraries
- [revorb](https://github.com/ItsBranK/ReVorb)
- [ww2ogg](https://github.com/hcs64/ww2ogg)
- [bnkextr](https://github.com/eXpl0it3r/bnkextr)
- [renamer-parser](https://github.com/Neinndall/renamer-parser)
