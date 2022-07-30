# encoding=utf-8

"""
__project_ = 'py-worksapce'
__file_name__ = 'testSTMP'
__author__ = 'li.jiang'
__time__ = '2019/7/16 17:47'
__product_name = PyCharm
# Keep calm and carry on 
"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send_email_by_datayes():
    sender = 'li.jiang@datayes.com'
    receiver = ['li.jiang@datayes.com']

    message = MIMEText('This is my first email send by python!', 'plain', 'utf-8')
    message['From'] = Header('testSMTP')
    message['To'] = Header('测试', 'utf-8')

    subject = '邮件测试'
    message['subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP('smtp.datayes.com')
        smtpObj.sendmail(sender, receiver, message.as_string())
        print('success')
    except smtplib.SMTPException:
        print('send fail!')


def send_email_by_163():
    mail_host="smtp.163.com"
    mail_user="jianglixiaomeili@163.com"
    mail_password="JLasdfg13345679"

    sender="jianglixiaomeili@163.com"
    receivers = ['li.jiang@datayes.com']

    message=MIMEText("send by 163 email service!",'plain','utf-8')
    message['From']= "{}".format(sender)
    message['To']=",".join(receivers)

    subject="Just for test! Don't reply!"
    message['subject']=Header(subject,'utf-8')

    try:
        smtpObj=smtplib.SMTP()
        smtpObj.connect(mail_host,25)
        smtpObj.login(mail_user,mail_password)
        smtpObj.sendmail(sender,receivers,message.as_string())
        print('success 2')
    except smtplib.SMTPException:
        print('send fail!')

send_email_by_163()