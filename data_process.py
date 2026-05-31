# basic input style
# name = input("Please enter your name: ")
# print("Hello, " + name)

# def to_seconds(hours, minutes, seconds):
#     return hours*3600+minutes*60+seconds

# print("Welcome to this time converter")
# cont = "y"
# while(cont.lower() == "y"):
#     hours = int(input("Enter the number of hours: "))
#     minutes = int(input("Enter the number of minutes: "))
#     seconds = int(input("Enter the number of seconds: "))

#     print("That's {} seconds".format(to_seconds(hours, minutes, seconds)))
#     print()
#     cont = input("Do you want to do another conversion? [y to continue] ")
    
# print("Goodbye!")

# standard streams
# data = input("This will come from STDIN: ")
# print("Now we write it to STDOUT: " + data)
# print("Now we generate an error to STDERR: " + data + 1)

# Environment Variables
import os
# print("HOME: " + os.environ.get("HOME", ""))
# print("SHELL: " + os.environ.get("SHELL", ""))
# print("FRUIT: " + os.environ.get("FRUIT", ""))

# Command-line Arguments and exit status
import sys
print(sys.argv)

# filename = sys.argv[1]
# if not os.path.exists(filename):
#     with open(filename, "w") as f:
#         f.write("New file created\n")
# else:
#     print("Error, the file {} already exists!".format(filename))
#     sys.exit(1)

# More About Input Functions
# my_number = raw_input('Please Enter a Number: \n')
# print(my_number)
# my_input = input('Please Enter a Number: \n')
# print(raw_input)
# print(my_input)
# my_number = input('Please Enter a Number: \n')
# print(my_number)
# type(my_number)

# Running System Commands in Python
# import subprocess
# subprocess.run(["powershell", "Get-Date"])
# subprocess.run(["cmd", "/c", "date /t"])

# Obtaining the output of s System Command
# result = subprocess.run(["nslookup", "8.8.8.8"], capture_output=True, text=True)
# print(result.returncode)
# print(result.stdout)

# import os
# import subprocess
# my_env = os.environ.copy()
# my_env["PATH"] = os.pathsep.join([
#     r"D:\MSCITM\5th-Python\pyInteractWithOS-Coursera",
#     my_env["PATH"]
# ])
# result = subprocess.run(["myapp"], env=my_env)







