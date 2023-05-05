echo off

set input_path=%1
set input_path=%input_path:\=/%
set input_path=%input_path:"=%
set command="input_path=\"%input_path%\""

start PATH\TO\NatronRenderer.exe %~dp0/output_srgb_to_aces.py -c %command%
