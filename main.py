from crontab import CronTab

cron = CronTab(user='farman_ali')
job = cron.new(command='python3 /home/farman_ali/ide/bubbel-project/sample/helpers.py')
job.minute.every(1)

cron.write()
print(job.enable())
