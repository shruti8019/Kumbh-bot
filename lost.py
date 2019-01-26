import sys, os, zulip
sys.path.insert(0,os.getcwd())
import smtplib
def send_email(bot_handler,*params)->str:
	sender_name = params[0][0]
	sender_aadhar = params[0][1]
	lost_name = params[0][2]
	lost_aadhar = params[0][3]
	subject = "***URGENT-MISSING PERSON***"
	content="Sender's name:" + sender_name + "\nSender's aadhar number:" + sender_aadhar +"\nMissing person's name:" + lost_name +"\nMissing person's aadhar number:" + lost_aadhar;
	message = 'Subject: {}\n\n{}'.format(subject, content)
	mail=smtplib.SMTP('smtp.gmail.com',587)
	mail.ehlo()
	mail.starttls()
	mail.login('<sender id>','sender-password')
	receiver="receiver's-id"
	mail.sendmail('sender-id',receiver,message)
	mail.close()
	return "Noted dear user!"
	
	
	
	
	
	
