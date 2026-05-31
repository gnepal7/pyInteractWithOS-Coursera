import csv
import pandas as pd

data = pd.read_csv('german_credit_data.csv')
# print(data.columns)

file = open('german_credit_data.csv')
csv_file = csv.reader(file)
next(csv_file)
for row in csv_file:
  # print(row)
  break
# csv_file.close()


# Generate own csv file
# hosts = [['workstation.local', '192.168.25.46'], ['workstation.cloud', '10.2.5.6']]
# with open('hosts.csv', 'w') as hosts_csv:
#   writer = csv.writer(hosts_csv)
#   writer.writerows(hosts)

# with open('hosts.csv') as read_file:
#     lines = read_file.readlines()
#     for line in lines:
#         print(line.strip())

# with open('hosts.csv') as read_file:
#     lines = read_file.readlines()
#     print(lines)

# Read and write with dictionaries
# with open('hosts.csv') as host:
#   reader = csv.DictReader(host)
#   for row in reader:
#     print(("{} has {} users").format(row["name"], row["ip"]))

with open ('german_credit_data.csv') as german:
   for row in german:
      print(row)
      break
  #  lines = german.readlines()
  #  print(lines)

# DictWriter

users = [ {"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"}, 
 {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"}, 
  {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]
keys = ["name", "username", "department"]
with open('by_department.csv', 'w') as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)

with open('by_department.csv') as dr:
   for row in dr:
      print(row)
      break











