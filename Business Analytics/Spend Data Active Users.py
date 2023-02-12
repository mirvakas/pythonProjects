import datetime
import smtplib
from email.message import EmailMessage

import cx_Oracle
import pandas as pd

# import numpy as np
# import matplotlib.pyplot as plt

year = datetime.date.today().year
month = datetime.date.today().month
day = datetime.date.today().day
TimeStamp = str(year) + str(month) + str(day)
# TimeStamp = datetime.date.today()

cx_Oracle.init_oracle_client(lib_dir=r"C:/instantclient_19_12")
userpwd = "enter your password"  # Obtain password string from a user prompt or environment variable
dsn = cx_Oracle.makedsn("host name", 1521, service_name="SERVICE_NAME")

connection = cx_Oracle.connect(user="DBusername", password=userpwd, dsn=dsn, encoding="UTF-8")
cur = connection.cursor()
Total_Active_Users = "SELECT count(distinct(LOGIN_NAME)) as \"User Count\" FROM DBSCHEMA.LOGIN_HISTORY WHERE SUB_ID=@CUST_ID and LOGINDATE>TO_DATE('2021-01-01', 'YYYY-MM-DD') and LOGIN_NAME not like 'SUPERUSER_%'"

FileNameExcel = 'Analysis_UserData' + str(TimeStamp) + '.xlsx'
df2 = pd.read_sql(Total_Active_Users, connection)

with pd.ExcelWriter(FileNameExcel) as writer:  # doctest: +SKIP
    df2.to_excel(writer, sheet_name='Active Users Count', index=False)

connection.close()

msg = EmailMessage()
msg['Subject'] = 'Customer Active Users Count'
msg['From'] = 'username@domain.com'
msg['To'] = 'abc@domain.com,abc@domain.com'
msg.set_content(
    "Attached file contains the number of active Users.\nReach out to me for further clarity on data.\n")

with open(FileNameExcel, "rb") as f:
    file_data = f.read()
    file_name = f.name
    print("File Name is:", file_name)
    msg.add_attachment(file_data, maintype="application", subtype="xlsx", filename=file_name)
try:
    server = smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465)
    server.login("username@domain.com", "uorxxuctvgepoyso")
    server.send_message(msg)
    print("Email Sent Sucessfully!")
except:
    print("Unknown Error")
server.quit()
# Version - 1/22/2023 - Post Code to the Git Repos
