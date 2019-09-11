@echo off
setlocal
set input=100q_source.md
set output=plain_square_output.md
set limitcount=100

set category_format=Å°@
set question_format=@@. @
set numbering_format=d
set category_mark=##
set ignore_blank=--opt-ignore-blank
rem set ignore_blank=

python %~dp0builder.py -i %input% -o %output% -l %limitcount% --opt-category-format "%category_format%" --opt-question-format "%question_format%" --opt-numbering-format "%numbering_format%" --opt-category-mark "%category_mark%" %ignore_blank%
