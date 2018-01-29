from crontab import CronTab
import ConfigParser
import os

def CRON_job():
    # config = ConfigParser.ConfigParser()
    # config.read(os.path.join(os.getcwd(), 'details.conf'))
    cron_job = CronTab(user='asadhussain')

    job = cron_job.new(command='python /Users/asadhussain/youtube-app/mail.py')
    # job = cron_job.new(command='python /Users/asadhussain/youtube-app/write_date.py')
    job.minute.every(1)
    # job.day.every(1)

    # first solution is to call mail.py and iterate through the list of videos and find a url with its flag=0 and
    # set its flag=1. SO in this way this cron job will keep on sending the mail till the flag of all URLs are set


    cron_job.write()

if __name__ == '__main__':
    CRON_job()