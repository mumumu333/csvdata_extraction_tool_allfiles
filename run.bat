@echo off

set file_path="C:\Users\~\csvdata_extraction_tool_allfiles\testfolder"

py csvdata_extraction_tool_allfiles.py %file_path%  137 >> result.txt
py csvdata_extraction_tool_allfiles.py %file_path%  459 >> result.txt
py csvdata_extraction_tool_allfiles.py %file_path%  Brandon >> result.txt
py csvdata_extraction_tool_allfiles.py %file_path%  Jack >> result.txt