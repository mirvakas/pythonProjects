import datetime

import cx_Oracle
import pandas as pd

# import numpy as np
# import matplotlib.pyplot as plt

year = datetime.date.today().year
month = int(datetime.date.today().month) - 1
if month <= 0:
    year = year - 1
    month = 12
day = datetime.date.today().day
TimeStamp = str(month) + str(year)

cx_Oracle.init_oracle_client(lib_dir=r"C:/instantclient_19_12")
userpwd = "alphabetagamma4"  # Obtain password string from a user prompt or environment variable
dsn = cx_Oracle.makedsn("amer8.corp.birchstreet.net", 1521, service_name="AMER8")

connection = cx_Oracle.connect(user="vhmir", password=userpwd, dsn=dsn,
                               encoding="UTF-8")
cur = connection.cursor()
Total_Live_Purchasing_Locations = "SELECT count(distinct a.company_Id) as \"A\" FROM PBEACH.PPO_MASTER_HEADER a,PBEACH.psm_company_profile b WHERE a.SUBSCRIBER_ID=641 and a.creation_date between TO_DATE('2022-01-01', 'YYYY-MM-DD') and TO_DATE('2022-02-01', 'YYYY-MM-DD') and nvl(a.is_deleted,0)!='1' and a.company_id not in (SELECT COMPANY_ID FROM PBEACH.PSM_COMPANY_PROFILE WHERE SUBSCRIBER_ID=641 and is_buyer=1 and active=1 and BATTR_VAL15 is null) and a.subscriber_id=b.subscriber_id and a.company_id=b.company_id and B.IS_BUYER=1 and b.active=1 and b.BATTR_VAL14 is not null"

FileNameExcel = 'AmkAnalysisTEST' + '.xlsx'
df2 = pd.read_sql(Total_Live_Purchasing_Locations, connection)
# with open('Spend AnalysisMONTHLY.sql') as f:
#     newText=f.read().replace('2021-11-01', '2022-01-01')
# with open('Spend AnalysisMONTHLY.sql', "w") as f:
#     f.write(newText)
# with open('Spend AnalysisMONTHLY.sql') as f:
#     newText=f.read().replace('2021-01-01', '2021-11-01')
# with open('Spend AnalysisMONTHLY.sql', "w") as f:
#     f.write(newText)


with pd.ExcelWriter(FileNameExcel) as writer:  # doctest: +SKIP
    df2.to_excel(writer, sheet_name='Summary', index=False)

connection.close()
