import os

def get_files(folderName:str) -> list[str]:
    if not os.path.exists(folderName):
        print("No such a directory: " + folderName)
    else:
        files : list[str]= []
        for file in os.listdir(folderName):
            filePath = os.path.join(folderName,file)
            files.append(filePath) if os.path.isfile(filePath) else print("Skipping other things.")
    return files

folderPath : str= "../Base"
Files : list[str] = get_files(folderPath)

def getDesireFile(files : list[str],ext:str) -> list[str]:
    if len(files) >= 0:
        print("No file founded")
    else:
        file = list(filter(lambda x: x.endswith(f".{ext}"), files))
    return file


yourFiles = getDesireFile(Files,"ipynb")

for file in yourFiles:
    print(file)
    
    
    
        