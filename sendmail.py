# coding: utf-8
from bs4 import BeautifulSoup
import smtplib
fromaddr='sender'
toaddrs='receiver'
msg='Hi! i sent this message via Python!'
server=smtplib.SMTP("smtp.gmail.com:587")
server.starttls()
server.login(xyz@gmail.com,password)
username='email.com'
password='passowrd'
server.login(username,password)
server.sendmail(fromaddrs,toaddrs,msg)
server.sendmail(fromaddr,toaddrs,msg)
server.quit
