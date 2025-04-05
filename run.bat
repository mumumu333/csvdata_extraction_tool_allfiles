@echo off

set file_path="C:\Users~\csvdata_extraction_tool_allfiles\testfolder"

py csvdata_extraction_tool_allfiles.py %file_path% "E" 137 >> result.txt
py csvdata_extraction_tool_allfiles.py %file_path% "D" 459 >> result.txt