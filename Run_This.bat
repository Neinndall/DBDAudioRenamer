@echo off
title DBD-Extractor v0.1.1 (BNK Files and XML Files) by Th3Nigh7mare
color b
for /r %%d in (*.bnk) do ".\Tools\bnkextr.exe" "%%d" /nodir
pause
mkdir "Files\decoding"
pause
"Tools\quickbms.exe" "Tools\scripts\Wwise_parse.bms" "Files\*.xml" "Files\decoding"
pause
for /r %%d in (*.wem) do ".\ww2ogg\ww2ogg.exe" "%%d" --pcb ".\ww2ogg\packed_codebooks_aoTuV_603.bin"
echo. Unpack and parser finished! The files are in Files/decoding
pause
