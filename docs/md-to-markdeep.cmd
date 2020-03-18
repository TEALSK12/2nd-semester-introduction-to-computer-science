@echo off & setlocal

robocopy /mir .\ .\docs
robocopy /mir .\ .\docs /E /Z /ZB /R:5 /W:5 /TBD /NP /V /XD .\docs
cd .\docs

set sed="C:\Program Files\Git\usr\bin\sed.exe"

@REM -- Convert files at the root of the repo.
for %%f in (*.md) do (
    @echo %%f
    type >%%f.html markdeep-header.txt
    %sed% >>%%f.html "s/\.md/.md.html/g" %%f
    type >>%%f.html markdeep-footer.txt

    pandoc -s -o geometry:margin=2cm "%%`nf.pdf" "%%f"
)

@REM -- Convert files in each unit

for /r . %%f in (*.md) do (
    @echo %%f
    type >%%f.html markdeep-header.txt
    %sed% >>%%f.html "s/\.md/.md.html/g" %%f
    type >>%%f.html markdeep-footer.txt

    pandoc -s -o geometry:margin=2cm "%%`nf.pdf" "%%f"
)

rename summary.md.html index.html

Exit /B