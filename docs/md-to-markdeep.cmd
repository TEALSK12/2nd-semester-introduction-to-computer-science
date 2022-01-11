@REM -- This file is no longer in use to convert curiculum to Markdeep. Changes need to be made directly in /docs/ folder.

@echo off & setlocal
echo %time%

robocopy /E .\ .\docs /XD %CD%\docs
cd .\docs

@REM -- Remove unnecessary files that are copied
del ".\docs\md-to-markdeep.cmd"
del ".\docs\markdeep-footer.txt"
del ".\docs\markdeep-header.txt"

set sed="C:\Program Files\Git\usr\bin\sed.exe"

@REM -- Convert files at the root of the repo.
for %%f in (*.md) do (
    @echo %%f
    type >%%f.html markdeep-header.txt
    %sed% >>%%f.html "s/\.md/.md.html/g" %%f
    type >>%%f.html markdeep-footer.txt
   
)

@REM -- Convert files at the Units of the repo.
for /r . %%f in (*.md) do (
    @echo %%f
    type >%%f.html ..\markdeep-header.txt
    %sed% >>%%f.html "s/\.md/.md.html/g" %%f
    type >>%%f.html ..\markdeep-footer.txt 
 
    del %%f
    
)

MOVE /Y README.md.html index.html

echo %time%

Exit /B