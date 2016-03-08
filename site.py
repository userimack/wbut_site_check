from requests import get
from time import sleep
from datetime import datetime
import smtplib
import difflib
import os
import sys

# Website to monitor
url ='http://wbutech.net'
#url = 'http://google.com' #for testing purpose
# Your Email
sender = os.environ['email_id']
# Your Password
password = os.environ['email_passwd']
# Recipient of the 'Website Changed' email.
recipient = 'mahendra.k12@gmail.com'
# Subject of the Email
subject = 'The Website has changed'
# Body of the Email
body = 'The website %s has changed' % (url)
message = 'Subject: %s\n\n%s' % (subject, body)
interval = 900  # 15 minutes
# To count the instances
count = 0

def isSiteChanged():
    '''Returns True if the site has change and False otherwise.'''  
    print("Running instance #%s") % (count)
    first = get(url)
    sleep(interval)
    second=get(url)
    now = datetime.now()
    time = now.strftime("%a %m/%d at %I:%M %P")

    print("\nChecked at %s") % (time)
    if first.text != second.text:
        print("\n\n Website Changed \n\n")
        diff = difflib.ndiff(first.text.splitlines(1), second.text.splitlines(1))
        diff = list(diff)
        print ''.join(diff)
        return True
    else:
        print ("\nWebsite not chnaged\n")
        return False



def sendEmail(sender, recipient, message, password):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, recipient, message)
    server.quit()

while True:
    count += 1
    if isSiteChanged():
        print("\nSending Email to %s\n") % (recipient)
        sendEmail(sender, recipient, message, password)
        print ("Running VLC")
        os.system('vlc "/home/imack/Downloads/Moves Like Jagger - Maroon 5 featuring Christina Aguilera.mp4"')        
        #os.system('vlc "https://www.youtube.com/watch?v=pIOOwhmkoLo"')

        sys.exit()

