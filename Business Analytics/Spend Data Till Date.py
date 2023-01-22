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
userpwd = "alphabetagamma7" # Obtain password string from a user prompt or environment variable
dsn = cx_Oracle.makedsn("amer8.corp.birchstreet.net", 1521, service_name="AMER8")

connection = cx_Oracle.connect(user="vhmir", password=userpwd, dsn=dsn,encoding="UTF-8")
cur = connection.cursor()
Total_Live_Purchasing_Locations = "SELECT count(distinct a.company_Id) as \"A\" FROM PBEACH.PPO_MASTER_HEADER a,PBEACH.psm_company_profile b WHERE a.SUBSCRIBER_ID=641 and a.creation_date between TO_DATE('2021-01-01', 'YYYY-MM-DD') and TO_DATE('2022-12-01', 'YYYY-MM-DD') and nvl(a.is_deleted,0)!='1' and a.company_id not in (SELECT COMPANY_ID FROM PBEACH.PSM_COMPANY_PROFILE WHERE SUBSCRIBER_ID=641 and is_buyer=1 and active=1 and BATTR_VAL15 is null) and a.subscriber_id=b.subscriber_id and a.company_id=b.company_id and B.IS_BUYER=1 and b.active=1 and b.BATTR_VAL14 is not null"

# dfe = cur.execute(query1)
# rows = cur.fetchall()
FileNameExcel = 'AmkAnalysis_' + str(TimeStamp) + '.xlsx'
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
'D':'Total Purchase Orders','E':'Total Invoices','F':'Total PO Lines','G':'Total AP Lines','H':'Total Spend in Purchase Orders','I':'Highest Value Purchase Order',
'J':'Total Spend in AP Invoices','K':'Highest Value AP Invoice','L':'Highest Valued Line Item ordered','M':'Highest Valued AP Line','N':'Total Catalog items',
'O':'Lowest Value Purchase Order','P':'PO Count Trend (8 Rows)','Q':'PO Spend Trend','R':'AP Count Trend','S':'AP Spend Trend','T':'BirchStreet Report Run Count',
'U':'PO Spend by Supplier (Last 15 Days)','V':'PO Spend by Supplier (Till Date)',
'W':'Total Units','X1':'Count of Live Profit Centers','X':'Non PO Invoices', 'XA':'Feed Correction Non-PO Inv','Y':'Non PO Supplier Portal AP',
'Z':'Non-PO EReceive','AB':'Manually Gen <>PO AP/Non-Elect',
'AC':'PO Invoices','AC1':'Feed Correction PO Inv','AD':'PO Supplier Portal Invoices','AE':'PO EReceive',
'AF':'Manually Generated PO Invoices','AG':'Purchase by LOB',
'AH':'Purchase by PC','AI':'Purchase by Site Names','AJ':'AP  Invoice by Site Names', 'AK': 'Total Live Sites'}, inplace=True)


with pd.ExcelWriter(FileNameExcel) as writer:  # doctest: +SKIP
    df2.to_excel(writer, sheet_name= 'Summary', index=False)
    # df3.to_excel(writer, sheet_name= 'List of AP for Live PCs', index=False)
    # df4.to_excel(writer, sheet_name= 'Feed Non PO Inv', index=False)
    # df5.to_excel(writer, sheet_name= 'Feed PO Inv', index=False)
    # df6.to_excel(writer, sheet_name= 'PO Sup Portal Inv', index=False)
    # df7.to_excel(writer, sheet_name= 'NonPO Sup Portal Inv', index=False)
    # df8.to_excel(writer, sheet_name= 'PO eReceiveInvoices', index=False)
    # df9.to_excel(writer, sheet_name= 'Non PO eReceiveInvoices', index=False)
    # df10.to_excel(writer, sheet_name= 'Manually Gen PO Inv', index=False)
    # df11.to_excel(writer, sheet_name= 'Manually Gen Non PO Inv', index=False)
    # df12.to_excel(writer, sheet_name= 'SQL STATEMENTS', index=False)

connection.close()

msg = EmailMessage()
msg['Subject'] = 'Aramark Spend Data'
msg['From'] = 'vakasmir@yahoo.com'
msg['To'] = 'abtiwari@birchstreet.net,vhmir@birchstreet.net'
msg.set_content("Attached file contains the details of Spend Data which includes the count of active locations/sites/Profit Centers.\nReach out to Vikaus for further clarity on data.")

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
