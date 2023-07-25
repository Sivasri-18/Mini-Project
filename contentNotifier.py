# importing necessary libraries

import urllib.request
import re
import smtplib
from functools import partial
import schedule

file_path = r"C:\Users\SIVASRI\Desktop\emails.txt"
with open(file_path, 'r') as file:
        f = file.read()
def check(web_src,required,r_mail):
    if(f'{r_mail}-{required}' not in f):
        try:
            page=urllib.request.urlopen(web_src)
            data=page.read().decode("UTF-8")
            data=data.lower()
            results = re.findall(required.lower(),data)
            if (len(results)!=0):
                # Sender and recipient email addresses
                sender_email = 'xxxxxx@gmil.com'
                recipient_email = r_mail
                # SMTP server settings for Gmail
                smtp_server = 'smtp.gmail.com'
                smtp_port = 587

                # Login credentials for the sender email address
                sender_password = '...........'

                # Create a secure connection to the SMTP server
                server = smtplib.SMTP(smtp_server, smtp_port)
                server.starttls()
                server.login(sender_email, sender_password)

                # Send the email
                server.sendmail(sender_email, recipient_email, f'The data {required}, you are looking for is just arrived. Check now here: {web_src}')
                print("Emil sent successfully")
                with open(file_path, 'w') as file:
                    file.write(f'{recipient_email}-{required}')
                # Close the connection to the SMTP server
                server.quit()
            else:
                    print('not found')
        except:
            print("Website can't be accessed")
check("https://rguktsklm.ac.in","Welcome","johndoe@gmail.com")