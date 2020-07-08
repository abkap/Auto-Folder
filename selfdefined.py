import os
import shutil
from constants import path_source,  target_directory



def moveTextFile(source,target):
    shutil.move(source,target)
def moveImageFile(source,target):
    shutil.move(source,target)
def movePdfFile(source,target):
    shutil.move(source,target)
def moveZipFile(source,target):
    shutil.move(source,target)
def moveDocxFile(source,target):
    shutil.move(source,target)
def moveFolderFile(source,target):
    shutil.move(source,target)
def moveSoftwareFile(source,target):
    shutil.move(source,target)


def forTextFile(extension, each_file):
    txt_target = f"{target_directory}\\text"
    txt_source = f"{path_source}\\{each_file}"
    special = 0
    if extension == '.txt':
        moveTextFile(txt_source,txt_target)
        print("text moved successfully !")
        
def forImageFile(extension, each_file):
    img_target = f"{target_directory}\\image"
    img_source = f"{path_source}\\{each_file}"
    special = 0
    if extension == '.jpg':
        moveImageFile(img_source,img_target)
        print("Image moved successfully !")
    if extension == '.jpeg':
        moveImageFile(img_source,img_target)
        print("Image moved successfully !")
    if extension == '.png':
        moveImageFile(img_source,img_target)
        print("Image moved successfully !")

def forPdfFile(extension, each_file):
    pdf_target = f"{target_directory}\\pdf"
    pdf_source = f"{path_source}\\{each_file}"
    special = 0
    if extension == '.pdf':
        movePdfFile(pdf_source,pdf_target)
        print("pdf moved successfully !")
def forZipFile(extension, each_file):
    zip_target = f"{target_directory}\\zip"
    zip_source = f"{path_source}\\{each_file}"
    special = 0
    if extension == '.zip':
        moveZipFile(zip_source,zip_target)
        print("zip moved successfully !")

def forDocxFile(extension,each_file):
    docx_target = f"{target_directory}\\docx"
    docx_source = f"{path_source}\\{each_file}"
    special = 0
    if extension == '.docx':
        moveDocxFile(docx_source, docx_target)
        print("docx moved successfully !")

def forFolderFile(extension,each_file):
    folder_target = f"{target_directory}\\folders"
    folder_source = f"{path_source}\\{each_file}"
    special = 0
    if extension == "":
        moveFolderFile(folder_source,folder_target)
        print('folder moved successfully ! ')


def forSoftwareFiles(extension, each_file):
    software_target = f"{target_directory}\\software"
    software_source = f"{path_source}\\{each_file}"
    special = 0
    if extension == '.exe':
        moveSoftwareFile(software_source,software_target)
        print("software moved successfully !")

def forExtraFiles(extension,each_file):
    extra_target = f"{target_directory}\\extra"
    extra_source = f"{path_source}\\{each_file}"
    possibleExtensions = ['.jpg',',jpeg','.png','.exe','.txt','.docx','.zip','.pdf','']
    special = 0
    if extension not in possibleExtensions:
        moveSoftwareFile(extra_source,extra_target)
        print("file moved to extra !")



def doTheWork(path_source):
    # checks each file in the path source folder 
    for each_file in os.listdir(path_source):
        if each_file != "MagicalPy":
            extension = ""
            special = 0
            # checks each letter
            for each_letter in each_file:
                #if the letter has '.' in it, with means it's not a folder and has an extension like txt
                #  then 'special' takes the value of 1 
                if each_letter == ".":
                    extension = ""
                    special = 1
                # if special have the value of 1 then we should get the next letters
                # which is used to determine the file type 
                if special == 1:
                    extension += each_letter
            # for moving files to its correct folder 
            try:
                forTextFile(extension,each_file)
                forImageFile(extension,each_file)
                forPdfFile(extension,each_file)
                forZipFile(extension,each_file)
                forDocxFile(extension,each_file)
                forSoftwareFiles(extension,each_file)
                forFolderFile(extension,each_file)
                forExtraFiles(extension,each_file)
            except:
                print(' Either of the files may alredy exists and can\'t be done twice')