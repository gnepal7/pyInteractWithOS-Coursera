# command for creating virtual environment
# python -m venv myenv

# use requirements 
# pip freeze > requirements.txt 
# pip install -r requirements.txt.

from areas import traingle, rectangle, circle

# import areas

# print(str(traingle(5.5, 6.8)) + " cm")
# print(str(rectangle(13.6, 18.2)) + " inch")
# print(str(circle(160)) + " px")

# command for checking disk status
# import shutil
# du = shutil.disk_usage("/")
# print(du)
# remaining_space = du.free/du.total * 100
# print(remaining_space)

# command for checking CPU usage
# import psutil
# cp = psutil.cpu_percent(0.1)
# print(cp)

# command for checking health of OS
import shutil
import psutil
def check_disk_usage(disk):
  du = shutil.disk_usage(disk)
  free = du.free / du.total * 100
  return free
  # return free > 20
# print(check_disk_usage("D:\\"))

def check_cpu_usage():
  usage = psutil.cpu_percent(1)
  # return usage < 75
  return usage
# print(check_cpu_usage())

if not check_disk_usage("/") or not check_cpu_usage():
  print("ERROR!")
else:
  print("Everything is OK.")

