@REM echo off & setlocal
@REM md-to-pdf.cmd 1> out.txt 2>&1 
echo %time%

@REM software needed to build GitHub pages and .pdf
@REM sed http://gnuwin32.sourceforge.net/packages/sed.htm
@REM headless chrome https://www.google.com/chrome/
@REM pdftk https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/

@REM usage to capture output and errors: md-tomarkdeep > out.txt 2>&1

@REM -- Set up the GitHub pages directory structure by copying curriculum content.
@echo off & setlocal
@echo off & setlocal
echo %time%

robocopy /mir .\ .\docs
cd .\docs

@REM -- Remove unnecessary files that are copied
del "C:\Users\aspie\Documents\2nd-semester-introduction-to-computer-science\docs\md-to-markdeep.cmd"
del "C:\Users\aspie\Documents\2nd-semester-introduction-to-computer-science\docs\markdeep-footer.txt"
del "C:\Users\aspie\Documents\2nd-semester-introduction-to-computer-science\docs\markdeep-header.txt"
rmdir /Q /S nonemptydir "C:\Users\aspie\Documents\2nd-semester-introduction-to-computer-science\docs\docs\

set sed="C:\Program Files (x86)\GnuWin32\bin\sed"
set edge="C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Edge.lnk"

@REM -- Convert files in each unit

for /r %%f in (*.md) do (
    @echo %%f

    @REM -- Create .pdf version of markdown files with no toc
    type >%%f-pdf.html ../markdeep-header.txt
    %sed% >>%%f-pdf.html "s/\.md/.md.-pdf.html/g" %%f
    type >>%%f-pdf.html ../markdeep-footer-tocstyle-none.txt
    
    @REM --no-margins does not work, had to edit the javascript
    @REM %chrome% --headless --print-to-pdf="%%~pf%%~nf.pdf" --no-margins "%%f-pdf.html"
    %edge% --headless --print-to-pdf="%%~pf%%~nf.pdf" --no-margins %%f-pdf.html
    del %%f-pdf.html

    @REM -- remove original .md file
    del %%f

)

pdftk README.pdf curriculum_map.pdf units/1_unit/unit_1.pdf units/1_unit/01_lesson/lesson.pdf units/1_unit/02_lesson/lesson.pdf units/1_unit/02_lesson/lab.pdf units/1_unit/03_lesson/lesson.pdf units/1_unit/03_lesson/do_now.pdf ^
units/1_unit/03_lesson/lab.pdf units/1_unit/04_lesson/lesson.pdf units/1_unit/04_lesson/do_now.pdf units/1_unit/04_lesson/lab.pdf units/1_unit/05_lesson/lesson.pdf units/1_unit/06_lesson/lesson.pdf ^
units/1_unit/06_lesson/project.pdf units/1_unit/06_lesson/alternate_project.pdf units/2_unit/unit2_md.pdf units/2_unit/01_lesson/lesson.pdf units/2_unit/01_lesson/do_now.pdf units/2_unit/01_lesson/lab.pdf ^
units/2_unit/02_lesson/lesson.pdf units/2_unit/02_lesson/do_now.pdf units/2_unit/02_lesson/lab.pdf units/2_unit/03_lesson/lesson.pdf units/2_unit/03_lesson/do_now.pdf units/2_unit/03_lesson/lab.pdf ^
units/2_unit/04_lesson/lesson.pdf units/2_unit/04_lesson/do_now.pdf units/2_unit/04_lesson/lab.pdf units/2_unit/05_lesson/lesson.pdf units/2_unit/05_lesson/do_now.pdf units/2_unit/05_lesson/lab.pdf ^
units/2_unit/06_lesson/lesson.pdf units/2_unit/06_lesson/do_now.pdf units/2_unit/06_lesson/lab.pdf units/2_unit/07_lesson/lesson.pdf units/2_unit/07_lesson/project.pdf units/2_unit/07_lesson/alternate_project.pdf ^
units/3_unit/unit_3.pdf units/3_unit/01_lesson/lesson.pdf units/3_unit/01_lesson/do_now.pdf units/3_unit/01_lesson/lab.pdf units/3_unit/02_lesson/lesson.pdf units/3_unit/02_lesson/do_now.pdf ^
units/3_unit/02_lesson/lab.pdf units/3_unit/03_lesson/lesson.pdf units/3_unit/03_lesson/do_now.pdf units/3_unit/03_lesson/lab.pdf units/3_unit/04_lesson/lesson.pdf units/3_unit/04_lesson/do_now.pdf ^
units/3_unit/04_lesson/lab.pdf units/3_unit/05_lesson/lesson.pdf units/3_unit/05_lesson/project.pdf units/3_unit/05_lesson/alternate_project.pdf units/4_unit/unit4.pdf units/4_unit/01_lesson/lesson.pdf ^
units/4_unit/01_lesson/do_now.pdf units/4_unit/01_lesson/lab.pdf units/4_unit/02_lesson/lesson.pdf units/4_unit/02_lesson/do_now.pdf units/4_unit/02_lesson/lab.pdf units/4_unit/03_lesson/lesson.pdf ^
units/4_unit/03_lesson/do_now.pdf units/4_unit/03_lesson/lab.pdf units/4_unit/04_lesson/lesson.pdf units/4_unit/04_lesson/do_now.pdf units/4_unit/04_lesson/lab.pdf units/4_unit/05_lesson/lesson.pdf ^
units/4_unit/05_lesson/lab.pdf units/4_unit/06_lesson/lesson.pdf units/4_unit/06_lesson/project.pdf units/4_unit/06_lesson/alternate_project.pdf units/5_unit/unit5.pdf units/5_unit/01_lesson/lesson.pdf ^
units/5_unit/01_lesson/do_now.pdf units/5_unit/01_lesson/lab.pdf units/5_unit/02_lesson/lesson.pdf units/5_unit/02_lesson/do_now.pdf units/5_unit/02_lesson/lab.pdf units/5_unit/03_lesson/lesson.pdf ^
units/5_unit/03_lesson/do_now.pdf units/5_unit/03_lesson/lab.pdf units/5_unit/04_lesson/lesson.pdf units/5_unit/04_lesson/do_now.pdf units/5_unit/04_lesson/lab.pdf units/5_unit/05_lesson/lesson.pdf ^
units/5_unit/05_lesson/do_now.pdf units/5_unit/05_lesson/project.pdf units/6_unit/unit6.pdf units/6_unit/01_lesson/lesson.pdf units/6_unit/01_lesson/do_now.pdf units/6_unit/01_lesson/lab.pdf units/6_unit/02_lesson/lesson.pdf ^
units/6_unit/02_lesson/do_now.pdf units/6_unit/02_lesson/lab.pdf units/6_unit/03_lesson/lesson.pdf units/6_unit/03_lesson/do_now.pdf units/6_unit/03_lesson/lab.pdf units/6_unit/04_lesson/lesson.pdf ^
units/6_unit/04_lesson/do_now.pdf units/6_unit/04_lesson/lab.pdf units/6_unit/05_lesson/lesson.pdf units/6_unit/05_lesson/do_now.pdf units/6_unit/05_lesson/projectb.pdf units/6_unit/05_lesson/project.pdf ^
units/7_unit/unit7.pdf units/7_unit/01_lesson/lesson.pdf units/7_unit/01_lesson/do_now.pdf units/7_unit/01_lesson/example.pdf units/7_unit/01_lesson/lab.pdf units/7_unit/02_lesson/lesson.pdf ^
units/7_unit/02_lesson/do_now.pdf units/7_unit/02_lesson/lab.pdf units/7_unit/03_lesson/lesson.pdf units/7_unit/03_lesson/do_now.pdf units/7_unit/03_lesson/lab.pdf units/7_unit/04_lesson/lesson.pdf ^
units/7_unit/04_lesson/do_now.pdf units/7_unit/04_lesson/lab.pdf units/7_unit/05_lesson/lesson.pdf units/7_unit/05_lesson/project.pdf units/7_unit/05_lesson/alternate_project.pdf units/8_unit/unit8.pdf ^
units/8_unit/project.pdf units/8_unit/01_lesson/lesson.pdf units/8_unit/01_lesson/do_now.pdf units/8_unit/02_lesson/lesson.pdf units/8_unit/02_lesson/do_now.pdf units/8_unit/03_lesson/lesson.pdf ^
units/8_unit/03_lesson/do_now.pdf units/8_unit/04_lesson/lesson.pdf units/8_unit/04_lesson/do_now.pdf units/supplemental/01_lesson/lesson.pdf units/supplemental/01_lesson/do_now.pdf ^
readings.pdf cat output 2ndSemPython.pdf

@REM delete all temporary .pdf files  
move /Y 2ndSemPython.pdf 2ndSemPython.save
del /s *.pdf
move /Y 2ndSemPython.save 2ndSemPython.pdf

cd ..

echo %time%

Exit /B

