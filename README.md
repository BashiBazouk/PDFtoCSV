# PDFtoCSV
Read tables from pdf files and transcript to csv.

Nothing fancy, but some good starting point to learn using github (also piece of working code which look elegant enough to show it to the world ;) ).

## Purpose of script
During developing of UIPath robot, there was a need to read effectively (more effectively than OCR reading) tables from pdf file and save it as csv file.
Idea was:
 - UIPath robot store all pdf files we're interested in a folder. Location of folder can be set easily in config.txt 
 - Python Scrip open folder containing PDFs and one by one convert all tables in .PDF to a .csv file using tabula library. This is less efective solution, as tabula can run batch convert. Due to security reasons (file name changing) batch conversion has been declined. But I'm leavig code for it, for future me, or for you.

## Useful links
 (Tabula official documentation)[https://tabula-py.readthedocs.io/en/latest/getting_started.html]
