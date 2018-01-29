import smtplib
import traceback
import os
# def main():
import ConfigParser
try:

    config = ConfigParser.ConfigParser()
    config.read(os.path.join(os.getcwd(), 'details.conf'))
    # config.read(r'./details.conf')
    fromaddr = config.get('credentials', 'from_email_id')
    toaddrs = config.get('credentials', 'to_email_id')

    msg= 'sample message latest'
    # server = smtplib.SMTP('smtp.gmail.com', 587)
    with open(os.path.join(os.getcwd(), 'stats.txt'), 'a') as f:
        f.write('sending mail ')
    server = smtplib.SMTP(config.get('smtp-server-info', 'smtp_server'), config.get('smtp-server-info', 'port_number'))
    # server.ehlo()
    server.starttls()
    # To fix that the recepint does not have to enable "Less secure apps " setting on his gmail account
    # And also make it such that mail can be sent to any server

    server.login(fromaddr, config.get('credentials','from_passwd'))
    server.sendmail(from_addr=fromaddr, to_addrs=toaddrs, msg=msg)
    # print server
    print "inside mail.py"
    server.quit()
except:
    print traceback.print_exc()

    # server.set_debuglevel(1)
    # server.sendmail(fromaddr, toaddrs, msg)
    # server.quit()

# if  __name__ == '__main__':
#     main()
