echo off

set folder=%1
set folder=%folder:\=/%
set command="folder=\"%folder%\""

start PATH\TO\NatronRenderer.exe %~dp0/aces_to_srgb.py -c %command%
