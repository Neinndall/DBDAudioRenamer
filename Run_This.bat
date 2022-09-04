"Tools\quickbms.exe" "Tools\Wwise.bms" "Files\*.bnk" "Files"
pause
mkdir "Files\Decoding"
pause
"Tools\quickbms.exe" "Tools\Wwise_parse.bms" "Files\*.xml" "Files\Decoding"
pause
for /r %%f in (*.wem) do ".\ww2ogg\ww2ogg.exe" "%%f" --pcb ".\ww2ogg\packed_codebooks_aoTuV_603.bin"
pause

@echo off
echo. -------------------------------------------------------------
echo. Unpack finished! Files will be in the 'Files/decoding' folder
echo. -------------------------------------------------------------