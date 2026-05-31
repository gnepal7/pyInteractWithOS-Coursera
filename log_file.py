import sys
# if len(sys.argv) < 2:
#     print("Usage: python log_file.py <logfile>")
#     exit(1)
# logfile = sys.argv[1]
# with open(logfile) as f:
#   for line in f:
#     print(line.strip())

# if len(sys.argv) < 2:
#     print("Usage: python log_file.py <logfile>")
#     exit(1)
# logfile = sys.argv[1]
# with open(logfile) as f:
#   for line in f:
#     if "CRON" not in line:
#       continue
#     print(line.strip())

# import re
# pattern = r"USER \((\w+)\)$"
# line = "Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)"
# result = re.search(pattern, line)
# print(result[1])

# if len(sys.argv) < 2:
#   print("Usage: python log_file.py <logfile>")
#   exit(1)
# logfile = sys.argv[1]
# with open(logfile) as f:
#   for line in f:
#     if "CRON" not in line:
#       continue
#     pattern = r"USER \((.+)\)$"
#     result = re.search(pattern, line)
#     print(result[1])

# Making Sense of Data
# usernames = {}
# name = "good_user"
# usernames[name] = usernames.get(name, 0) + 1
# print(usernames)
# usernames[name] = usernames.get(name, 0) + 1
# print(usernames)

import re
import sys

if len(sys.argv) < 2:
  print("Usage: python log_file.py <logfile>")
  exit(1)

logfile = sys.argv[1]
usernames = {}
with open(logfile) as f:
  for line in f:
    if "CRON" not in line:
      continue
    pattern = r"USER \((\w+)\)$"
    result = re.search(pattern, line)

    if result is None:
      continue
    name = result[1]
    usernames[name] = usernames.get(name, 0) + 1

print(usernames)
