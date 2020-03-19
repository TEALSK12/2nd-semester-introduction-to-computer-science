@echo off & setlocal

robocopy /mir .\ .\docs
cd .\docs

@REM -- Remove unnecessary files that are copied
del "C:\Users\v-anspi\Documents\GitHub\2nd-semester-introduction-to-computer-science\docs\md-to-markdeep.cmd"
del "C:\Users\v-anspi\Documents\GitHub\2nd-semester-introduction-to-computer-science\docs\markdeep-footer.txt"
del "C:\Users\v-anspi\Documents\GitHub\2nd-semester-introduction-to-computer-science\docs\markdeep-header.txt"
del "C:\Users\v-anspi\Documents\GitHub\2nd-semester-introduction-to-computer-science\docs\docs\cert_assets"
del "C:\Users\v-anspi\Documents\GitHub\2nd-semester-introduction-to-computer-science\docs\docs\
@REM -- del "C:\Users\v-anspi\Documents\GitHub\2nd-semester-introduction-to-computer-science\docs\docs\.git"
rmdir "C:\Users\v-anspi\Documents\GitHub\2nd-semester-introduction-to-computer-science\docs\docs\cert_assets"

set sed="C:\Program Files\Git\usr\bin\sed.exe"


@REM -- Convert files at the root of the repo.
for %%f in (*.md) do (
    @echo %%f
    type >%%f.html markdeep-header.txt
    %sed% >>%%f.html "s/\.md/.md.html/g" %%f
    type >>%%f.html markdeep-footer.txt

    @REM -- pandoc -s -o geometry:margin=2cm "%%f" "%%~nf.pdf"
)

@REM -- Convert files in each unit

for /r . %%f in (*.md) do (
    @echo %%f
    type >%%f.html markdeep-header.txt
    %sed% >>%%f.html "s/\.md/.md.html/g" %%f
    type >>%%f.html markdeep-footer.txt

    @REM -- pandoc -s -o geometry:margin=2cm "%%f" "%%~nf.pdf"
)

rename summary.md.html index.html




Exit /B