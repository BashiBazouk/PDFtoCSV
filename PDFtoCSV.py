
import tabula
import os

# hardcoding
configFile = 'config.txt' # location of pdfs in folders

def readConfig():
    # read folders from config file and iterate over them to read from pdf to write to csv
    configFileContent = open(configFile, 'r')

    Lines = configFileContent.readlines()
    for line in Lines:
        # run subroutine which reads all content of folder
        readFolder(line.rstrip('\n')) # remove 'new line' characters

def readFolder(path_to_pdfs):
    for filename in os.listdir(path_to_pdfs):
        if filename.endswith(".pdf") or filename.endswith(".PDF"):
            # this will return a tuple of root and extension
            split_tup = os.path.splitext(filename)

            # extract the file name and extension
            file_name=split_tup[0]
            # print(path_to_pdfs+file_name)
            readPDFwriteToCsv(path_to_pdfs + '/' + filename, path_to_pdfs + '/' + file_name+'.csv')

def readPDFwriteToCsv(pdfFile, csvFile):
    # convert pdf to csv with the same name
    tabula.convert_into(pdfFile, csvFile, output_format="csv", pages='all')

    # batch version, but it doesn't work with .PDF and I shouldn't change extension on files - security issue
    #tabula.convert_into_by_batch(pDFsPath, output_format='csv', java_options=None, pages="all")

if __name__ == '__main__':
    readConfig()

