from urllib import response
import pandas as pd
import csv
import geoip2.database

def getLocation():
    df = pd.read_csv('output.csv')
    print()
    ips = df['remote_host']
    with geoip2.database.Reader('GeoLite2-Country.mmdb') as reader, open('output.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        count = False
        for ip in ips:
            try:
                response = reader.country(ip)
                # print (response.country.name)
                if count == False:
                    writer.writerows(["Country"])
                    count = True
                writer.writerows([response.country.name])
                # print()
            except Exception as e:
                print(e)
print(getLocation())
# getLocation()