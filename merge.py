import pandas as pd
import csv

def mergedf():
    csv1 = pd.read_csv('nice.csv')
    csv2 = pd.read_csv('final.csv')
    # output = csv1.append(csv2)
    # output.to_csv('ush.csv', index=False)
    # print(output[['Country']])
    # print(output.head())
    # print(csv1.info())
    # print(csv2.info())

def dropdf():
    df = pd.read_csv('output.csv')
    drdf = df.drop(['remote_logname', 'remote_user', 'time_received', 'time_received_datetimeobj', 'time_received_isoformat', 'time_received_tz_datetimeobj', 'time_received_tz_isoformat', 'time_received_utc_datetimeobj', 'time_received_utc_isoformat', 'request_url_scheme'], axis=1)
    drdf.to_csv('nice.csv', index=False)
    print(drdf)

# print(mergedf())
print(dropdf())