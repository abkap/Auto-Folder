import os
import shutil
from constants import path_source,  target_directory
from time import sleep

# combining unwanted functions
def forPerticularFile(extension,each_file):
    # choosing folder_name

    file_source = f"{path_source}\\{each_file}"
    if extension == '.pptx':
        file_target = f"{target_directory}\\ppt"
        shutil.move(file_source,file_target)
        print(f"ppt moved successfully !")
    elif extension == '.txt':
        file_target = f"{target_directory}\\text"
        shutil.move(file_source,file_target)
        print("text moved successfully !")
    # for img files
    elif extension == '.jpg':
        file_target = f"{target_directory}\\image"
        shutil.move(file_source,file_target)
        print("Image moved successfully !")
    elif extension == '.jpeg':
        file_target = f"{target_directory}\\image"
        shutil.move(file_source,file_target)
        print("Image moved successfully !")
    elif extension == '.png':
        file_target = f"{target_directory}\\image"
        shutil.move(file_source,file_target)
        print("Image moved successfully !")
    # for pdf
    elif extension == '.pdf' or extension == '.PDF':
        file_target = f"{target_directory}\\pdf"
        shutil.move(file_source,file_target)
        print("pdf moved successfully !")

    elif extension == '.zip':
        file_target = f"{target_directory}\\zip"
        shutil.move(file_source,file_target)
        print("zip moved successfully !")
    elif extension == '.docx':
        file_target = f"{target_directory}\\docx"
        shutil.move(file_source, file_target)
        print("docx moved successfully !")

    elif extension == "":
        file_target = f"{target_directory}\\folders"
        shutil.move(file_source,file_target)
        print('folder moved successfully ! ')
    elif extension == '.exe':
        file_target = f"{target_directory}\\software"
        shutil.move(file_source,file_target)
        print("software moved successfully !")
    else:
        file_target = f"{target_directory}\\extra"
        shutil.move(file_source,file_target)
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
                forPerticularFile(extension,each_file);
            except Exception as e:
                print(e)
                sleep(1)
