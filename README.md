# PDFtoCSV
Read tables from pdf files and transcript to csv.

Nothing fancy, but some good starting point to learn using github (also piece of working code which look elegant enough to show it to the world ;) ).

## Purpose of script
During developing of UIPath robot, there was a need to read effectively (more effectively than OCR reading) tables from pdf file and save it as csv file.
Idea was:
 - UIPath robot store all pdf files we're interested in a folder. Location of folder can be set easily in config.txt 
 - Python Scrip open folder containing PDFs and one by one convert all tables in .pdf to a .csv file using tabula library. 
 - Tabula can run batch convert only for .pdf files and not .PDF files (yes, capittal letters in extension doesn't work for batch conversion). Due to security reasons (file name changing is a potential security breach) batch conversion was not used. But I'm leavig code for it, for future me, or for you.
 - instead . pdf files are read one by one and then converted. This is less efective solution, but more secure.
 - .csv file is stored in the same folder and then used by UIPath robot.

 In the end robot has been rethinked and script was not used.

## Useful links
 [Tabula official documentation](https://tabula-py.readthedocs.io/en/latest/getting_started.html)
