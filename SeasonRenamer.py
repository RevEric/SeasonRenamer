import os

directory = ""
#if directory not specified above use current directory
if directory == "":
    directory = os.getcwd()

filesInDirectory = os.listdir(directory)
filesInDirectory.sort()

season = input("Enter season number: ")

#I define the index here because it needs to strt at 1,
#   and I only want to iterate it for movie files
index = 1 
for filename in filesInDirectory:
    if filename.endswith('.avi') or filename.endswith('.mp4'):
        extension = os.path.splitext(filename)[1]
        episodeName = "s" + str(season).zfill(2) + "e" + str(index).zfill(2) + extension
        os.rename(os.path.join(directory, filename), os.path.join(directory, episodeName))
        index += 1
        
print("Done!")