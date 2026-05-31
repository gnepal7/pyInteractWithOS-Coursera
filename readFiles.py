# file = open('text.txt')

# print(file.readline())
# print(file.read())
# file.close()

# with open('text.txt') as file2:  
#   pass
  # print(file2)

# with open('text.txt') as file2:  
#   for line in file2:   
#     pass 
    # print(line.upper())

# using line strip
# with open('text.txt') as file3:  
#   for line in file3:    
#     print(line.strip().upper())

# display in line
# file4 = open('text.txt')
# line = file4.readlines()
# file4.close()
# line.sort()
# print(line)

# write in file : includes 2 parameters => file and mode
# with open('text2.txt', 'w') as file5:
#   file5.write("This is sample writing from python script.")

# file paths
# absolute path can change as computer
# relative file path is useful for 

# Writing file paths in python
# windows = starts with drive name
# c:/my-directory/filename.extension
# c:\\my-directory\\filename.extension
# os.getcwd()
# outputs['current_directory_before'] = os.getcwd()
# outputs['file_and_directories'] = os.listdir()
# outputs['path_value'] = os.environ.get('PATH')

# import os
# os.remove('text3.txt')
# os.rename('text2.txt', 'text2New.txt')
# cheekPath = os.path.exists("text2New.txt")
# print(cheekPath)

# getting the file size
# print(os.path.getsize("main.py"))
# print(os.path.getsize("areas.py"))

# show when file was created
# print(os.path.getmtime('text.txt'))
# import datetime
# timestamp = os.path.getmtime('areas.py')
# check_time = datetime.datetime.fromtimestamp(timestamp)
# print(check_time)

# finding absolute path
# abspath = os.path.abspath('main.py')
# print(abspath)

# Directories
# get current working directory: cwd
# print(os.getcwd())
# os.mkdir('createdWithScr')
# os.chdir('createdWithScr')
# print(os.getcwd())
# os.rmdir('createdWithScr')
# os.mkdir('newDir')
# os.rmdir('newdir')

# print(os.getcwd())
# print(os.listdir("pyInteractWithOS-Coursera"))

# import os
# for name in os.listdir(dir):
#   fullname = os.path.join(dir, name)
#   if os.path.isdir(fullname):
#     print(f"{fullname} is a directory")
#   else:
#     print(f"{fullname} is a file")


import os
folder = "."    
for name in os.listdir(folder):
    fullname = os.path.join(folder, name)
    if os.path.isdir(fullname):
        print(f"{fullname} is a directory")
    else:
        print(f"{fullname} is a file")






