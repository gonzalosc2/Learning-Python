####################################
# author: Gonzalo Salazar
# course: 2020 Complete Python Bootcamps: From Zero to Hero in Python
# purpose: lecture notes
# description: Section 18 - Emails
# other: N/A
####################################

# Sending or checking emails will absolutely rely on both our local computer,
# internet and our email (admin permissions). In gmail we need 2-factor
# authentication, otherwise it won't allow us to set an app password

# Provider and SMTP server domain name
# Gmail:                        smtp.gmail.com      (requires an app password)
# Yahoo Mail:                   smtp.mail.yahoo.com
# Outlook.com/Hotmail.com:      smtp-mail.outlook.com

import smtplib  # for sending emails
import getpass  # similar to input, but typed text is not visible

# if port 587 does not work, try 465, othewise, do not provide a port
# check that the firewall is blocking us from connecting to the server
smtp_object = smtplib.SMTP('smtp.gmail.com',587)
smtp_object.ehlo()  # tells us the state of our connection

# port 587 uses TLS encryption, which means that nobody but the recipient can read
# the email. Note we have to initiate the encryption ourselves if we are using
# a port different from 587
smtp_object.starttls()  # in this case, this command is unnecessary

#  prevents us from revealing our pass
email = getpass.getpass('Email: ')
password = getpass.getpass('Password: ')   # here we should use our APP PASSWORD
smtp_object.login(email,password)

# Sending Emails
from_address = email
to_address = email  # can be any other email address
subject = input('enter the subject line: ')
message = input('enter the body message: ')

# format required in order to work; basically it requires one giant string
# indicating both Subject and message body. To diff them we use a new line (\n)
msg = 'Subject: ' + subject + '\n' + message

smtp_object.sendmail(from_address,to_address,msg)   # {} means success
smtp_object.quit()

# Receiving emails
import imaplib  # has a special syntax for searching our inbox
import email

M = imaplib.IMAP4_SSL('imap.gmail.com')
email = getpass.getpass("Email: ")
password = getpass.getpass('Password: ')   # here we should use our APP PASSWORD

M.login(email,password)
M.list()  # all what we can check in
M.select('inbox')

#typ, data = M.search(None,'ON 22-Oct-2020')   # tuple & packing, result is a tuple
#typ, data = M.search(None,'SUBJECT "string"')
typ, data = M.search(None,'SUBJECT "Hello world"')
typ
data   # if no number is shown here, then it found no messages
email_id = data[0]
result, email_data = M.fetch(email_id,'(RFC822)')  # RFC822 is a protocol
#email_data

raw_email = email_data[0][1]
raw_email_string = raw_email.decode('utf-8')

# using email module to get the actual message. We can code it ourselves

email_message = email.message_from_string(raw_email_string)

for part in email_message.walk():
        # try 'text/html' if a link is provided
    if part.get_content_type() == 'text/plain':
        body = part.get_payload(decode = True)
        print(body)
