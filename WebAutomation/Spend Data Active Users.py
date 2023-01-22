import cx_Oracle
import pandas as pd
import datetime
import smtplib
from email.message import EmailMessage
# import numpy as np
# import matplotlib.pyplot as plt

year = datetime.date.today().year
month = datetime.date.today().month
day = datetime.date.today().day
TimeStamp = str(year)+str(month)+str(day)
# TimeStamp = datetime.date.today()

cx_Oracle.init_oracle_client(lib_dir=r"C:/instantclient_19_12")
userpwd = "alphabetagamma8" # Obtain password string from a user prompt or environment variable
dsn = cx_Oracle.makedsn("repos8.gdiindia.com", 1521, service_name="repos8.birchstreet.net")

connection = cx_Oracle.connect(user="vhmir", password=userpwd, dsn=dsn,encoding="UTF-8")
cur = connection.cursor()
Total_Active_Users = "SELECT count(distinct(LOGINNAME)) as \"User Count\" FROM PBEACH_REPOS_B.LOGINHISTORY_SYN WHERE SUBSCRIBER_ID=641 and LOGINDATE>TO_DATE('2021-01-01', 'YYYY-MM-DD') and loginname not like 'bss_%'"

FileNameExcel = 'AmkAnalysis_UserData' + str(TimeStamp) + '.xlsx'
df2 = pd.read_sql(Total_Active_Users, connection)

with pd.ExcelWriter(FileNameExcel) as writer:  # doctest: +SKIP
    df2.to_excel(writer, sheet_name= 'Active Users Count', index=False)

connection.close()

msg = EmailMessage()
msg['Subject'] = 'Aramark Active Users Count'
msg['From'] = 'vakasmir@yahoo.com'
msg['To'] = 'abtiwari@birchstreet.net,vhmir@birchstreet.net'
msg.set_content("Attached file contains the number of active Users.\nReach out to Vikaus for further clarity on data.\n")

with open(FileNameExcel, "rb") as f:
    file_data = f.read()
    file_name = f.name
    print("File Name is:", file_name)
    msg.add_attachment(file_data,maintype="application", subtype= "xlsx", filename = file_name)
try:
    server = smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465)
    server.login("vakasmir@yahoo.com", "uorxxuctvgepoyso")
    server.send_message(msg)
    print("Email Sent Sucessfully!")
except:
    print("Unknown Error")
server.quit()
#Version - 1/22/2023 - Post Code to the Git Repos