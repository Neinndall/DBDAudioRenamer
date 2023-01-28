@echo off
title DBDAudioRenamer v0.3.0.1 (PAK, BNK, XML files by Neinndall)
color b
:MENU_START
cls
SET DIR_BNK=Files\BNK
SET DIR_WEM=Files\WEM
SET DIR_XML=Files\XML
SET INPUT=FALSE
echo :::  _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____
echo :::  \____\\____\\____\\____\\____\\____\\____\\____\\____\\____\\____\
echo :::
echo :::			   MENU OPTIONS
echo :::  _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____
echo :::
echo :::	1) Extract Audio Files from BNK and rename them
echo :::	2) Extract Audio Files from the PAK files
echo :::	3) WIP
echo :::	4) Exit
echo :::
echo :::  _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____
echo :::  \____\\____\\____\\____\\____\\____\\____\\____\\____\\____\\____\
echo.
set /p MENU_OPTION="OPTION: "
IF %MENU_OPTION%==1 GOTO EXTRACT_BNK
IF %MENU_OPTION%==2 GOTO EXTRACT_GAME
IF %MENU_OPTION%==4 GOTO EXIT
IF %INPUT%==FALSE GOTO ERROR

:EXTRACT_BNK
echo The extract audio from BNK files will start. Press a key for continue...
pause>nul
cls
FOR %%A IN ("%DIR_BNK%\*.BNK") DO ("Tools\bnkextr.exe" "%%A" /nodir & MOVE %DIR_BNK%\*.WEM "%DIR_WEM%")
echo :::  _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____
echo :::  
echo :::  BNK Files was extracted to %DIR_WEM%. Press a key for continue...
echo :::  _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____
pause>nul
cls
set /p DIR_FOLDER="Do you want a dir to be created in %DIR_WEM% called: Output, if it wasn't created? [Y/N]?: "

IF %DIR_FOLDER%==Y goto yes
IF %DIR_FOLDER%==y goto yes
IF %DIR_FOLDER%==N goto EXIT
IF %DIR_FOLDER%==n goto EXIT
IF %INPUT%==FALSE GOTO ERROR

:yes
mkdir %DIR_WEM%\Output
echo :::  _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____
echo :::  
echo :::  The Output directory was created! Press a key for continue...
echo :::  _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____
pause>nul

MOVE %DIR_XML%\*.XML %DIR_WEM%
echo :::  _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____
echo :::  
echo :::  All the XML files was moved to %DIR_WEM% folder. Press a key for continue...
echo :::  _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____
pause>nul
cls
echo Note: It will ask you if you want to overwrite because the files already exist, the recommendation is: A
pause>nul

FOR %%B IN ("%DIR_WEM%\*.XML") DO ("Tools\quickbms.exe" "Tools\scripts\New_parse.bms" "%%B" "Files\WEM\Output")
echo :::  _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____
echo :::  
echo :::  The Audio Files was renamed in %DIR_WEM%\Output. Press a key for continue...
echo :::  _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____
pause>nul

MOVE %DIR_WEM%\*.XML %DIR_XML%
echo :::  _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____
echo :::  
echo :::  The XML was moved to %DIR_XML% folder. Press a key for continue...
echo :::  _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____
pause>nul

CD Files\WEM\Output
FOR /R %%C IN (\*.WEM) DO ("..\..\..\ww2ogg\ww2ogg.exe" "%%C" --pcb "..\..\..\ww2ogg\packed_codebooks_aoTuV_603.bin")
echo :::  _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____
echo :::  
echo :::  The Audio Files was converted to OGG. Are located in Files/WEM/Output folder. Press a key for continue...
echo :::  _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____
pause>nul
echo.
set /p clean="To end, do u want to clean up unnecessary audio files [Y/N]?: "
IF %clean%==Y del /s /q *.wem
IF %clean%==y del /s /q *.wem
IF %clean%==N GOTO EXIT
IF %clean%==n GOTO EXIT

echo :::  _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____
echo :::  
echo :::  Finishing process, press a Key for close.
echo :::  _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____
GOTO EXIT

REM --------------------------------------------------------------------------------- Extract files from *.PAK

:EXTRACT_GAME
REM set /p input1="Choose Files PAK: "
REM echo Please put the following address: Extrated PAK Files
REM set /p input2="Output: "
echo :::  _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____
echo :::  
echo :::  Main files of audio will be extrated. Press a key for continue...
echo :::  _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____
"Tools\quickbms_4gb_files.exe" "Tools\scripts\unreal_tournament_4_0.4.27.bms" "C:\Program Files (x86)\Steam\steamapps\common\Dead by Daylight\DeadByDaylight\Content\Paks\pakchunk1-WindowsNoEditor.pak" "Extrated PAK Files"
echo :::  _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ 
echo :::  
echo :::  Now files linked to the ARCHIVES (Tome) will be extracted. Press a key for continue...
echo :::  _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ 
pause>nul
"Tools\quickbms_4gb_files.exe" "Tools\scripts\unreal_tournament_4_0.4.27.bms" "C:\Program Files (x86)\Steam\steamapps\common\Dead by Daylight\DeadByDaylight\Content\Paks\pakchunk2-WindowsNoEditor.pak" "Extrated PAK Files"
pause>nul

REM --------------------------------------------------------------------------------- Options(EXIT, ERROR...)

:EXIT
echo :::  _____ _____ _____ _____ _____ _____ 
echo :::  
echo :::  The application is closing...
echo :::  _____ _____ _____ _____ _____ _____ 
pause>nul
exit

:ERROR
echo Option not available, return to the menu...
timeout 2 > nul
cls
GOTO MENU_START