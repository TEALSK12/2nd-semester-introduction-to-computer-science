@echo off & setlocal

robocopy /mir .\ .\docs
cd .\docs

@REM -- Remove unnecessary files that are copied
del "C:\Users\v-anspi\Documents\GitHub\2nd-semester-introduction-to-computer-science\docs\md-to-markdeep.cmd"
del "C:\Users\v-anspi\Documents\GitHub\2nd-semester-introduction-to-computer-science\docs\markdeep-footer.txt"
del "C:\Users\v-anspi\Documents\GitHub\2nd-semester-introduction-to-computer-science\docs\markdeep-header.txt"
rmdir /Q /S nonemptydir "C:\Users\v-anspi\Documents\GitHub\2nd-semester-introduction-to-computer-science\docs\docs\

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
)

rename summary.md.html index.html


Exit /B