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
userpwd = "DBPwd" # Obtain password string from a user prompt or environment variable
dsn = cx_Oracle.makedsn("HOSTNAME", 'PORT', service_name="SERVICE NAME")

connection = cx_Oracle.connect(user="DBUserName", password=userpwd, dsn=dsn,encoding="UTF-8")
cur = connection.cursor()
Total_Live_Purchasing_Locations = "SELECT count(distinct a.COMP_ID) as \"A\" FROM PO_HEADER a,COMP_PRFLE b WHERE a.SUB_ID=@SUBID and a.GEN_DATE between TO_DATE('2021-01-01', 'YYYY-MM-DD') and TO_DATE('2022-12-01', 'YYYY-MM-DD') and nvl(a.is_deleted,0)!='1' and a.COMP_ID not in (SELECT COMP_ID FROM COMP_PRFLE WHERE SUB_ID=@SUBID and is_buyer=1 and active=1) and a.SUB_ID=b.SUB_ID and a.COMP_ID=b.COMP_ID and B.IS_BUYER=1 and b.active=1 and b.ATTR is not null"

# dfe = cur.execute(query1)
# rows = cur.fetchall()
FileNameExcel = 'SpendAnalysis_' + str(TimeStamp) + '.xlsx'
df2 = pd.read_sql(Total_Live_Purchasing_Locations, connection)
# with open('Spend Analysis.sql') as f:
#     newText=f.read().replace('2022-08-01', '2022-08-01')
# with open('Spend Analysis.sql', "w") as f:
#     f.write(newText)
with open('Spend Analysis.sql') as f:
    Lines = f.readlines()
    # print("File data in binary", file_data)
    # file_name = f.name
    # print("File Name is:", file_name)
for line in Lines:
    x= line.strip()
    df = pd.read_sql(x, connection)
    df = df.dropna()
    df2 = pd.concat([df2, df], axis=1)
    df2.dropna()
# print(df2)
df2.rename(columns={'A':'Number of Purchasing Locations Live','B':'Number of Invoicing Locations Live','C':'Total Credit Memos',
'D':'Total Purchase Orders','E':'Total Invoices','F':'Total Purchase Order Lines','G':'Total Accounts Payable Lines','H':'Total Spend in Purchase Orders','I':'Highest Value Purchase Order',
'J':'Total Spend in AP Invoices','K':'Highest Value AP Invoice','L':'Highest Valued Line Item ordered','M':'Highest Valued AP Line','N':'Total Catalog items',
'O':'Lowest Value Purchase Order','P':'PO Count Trend (8 Rows)','Q':'PO Spend Trend','R':'AP Count Trend','S':'AP Spend Trend','T':'Report Run Count',
'U':'PO Spend by Supplier (Last 15 Days)','V':'PO Spend by Supplier (Till Date)',
'W':'Total Units','X1':'Count of Live Customer Profit Sites','X':'Non PO Invoices', 'XA':'EDI Exchange Non-PO Invoices','Y':'Non PO Supplier App AP',
'Z':'Non-PO CSV','AB':'Manually Gen <>PO AP/Non-Elect',
'AC':'PO Invoices','AC1':'EDI Exchange PO Inv','AD':'PO Supplier App Invoices','AE':'PO CSV',
'AF':'Manually Generated PO Invoices','AG':'Purchase by Line of Business',
'AH':'Purchase by Profit Sites','AI':'Purchase by Area Site Names','AJ':'AP  Invoice by Area Site Names', 'AK': 'Total Live Area Site'}, inplace=True)


with pd.ExcelWriter(FileNameExcel) as writer:  # doctest: +SKIP
    df2.to_excel(writer, sheet_name= 'Summary', index=False)
    # df3.to_excel(writer, sheet_name= 'SQL STATEMENTS', index=False)

connection.close()

msg = EmailMessage()
msg['Subject'] = 'Customer Spend Data'
msg['From'] = 'username@domain.com'
msg['To'] = 'username@domain.net,username2@domain.net'
msg.set_content("Attached file contains the details of Spend Data which includes the count of active locations/sites/Profit Centers.\nReach out to me for further clarity on data.")

with open(FileNameExcel, "rb") as f:
    file_data = f.read()
    file_name = f.name
    print("File Name is:", file_name)
    msg.add_attachment(file_data,maintype="application", subtype= "xlsx", filename = file_name)
try:
    server = smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465)
    server.login("user@domain.com", "pwd")
    server.send_message(msg)
    print("Email Sent Sucessfully!")
except:
    print("Unknown Error")
server.quit()

