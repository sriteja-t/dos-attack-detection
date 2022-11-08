import pandas as pd

# Filter data
def dropdf():
    df = pd.read_csv('output.csv')
    drdf = df.drop(['remote_logname', 'remote_user', 'time_received', 'time_received_datetimeobj', 'time_received_isoformat', 'time_received_tz_datetimeobj', 'time_received_tz_isoformat', 'time_received_utc_datetimeobj', 'time_received_utc_isoformat', 'request_url_scheme'], axis=1)
    drdf.to_csv('dOutput.csv', index=False)
    print(drdf)
    print("-----------------------Successfully droped the columns!------------------------------------")

# Merging the geoLocation to IP addresses
def mergedf():
    csv1 = pd.read_csv('dOutput.csv')
    csv2 = pd.read_csv('geoLocation.csv')
    csv1['Country'] = csv2
    csv1.to_csv('final.csv', index=False)
    # print(csv1[['Country']])
    print("-------------------------------------Merge successful!-------------------------------------")