from crontab import CronTab
import os
import getpass
currentPath=os.path.dirname(os.path.abspath(__file__))
getUser=getpass.getuser()
command1 = currentPath+"/venv/bin/python3 "+currentPath+"/module/helpers.py"
cron=CronTab(user=getUser)
job = cron.new(command=command1)
job.minute.every(1)

cron.write()
print(job.enable())
