from urllib import response
import pandas as pd
import csv
import geoip2.database

def getLocation():
    df = pd.read_csv('output.csv')
    print()
    ips = df['remote_host']
    with geoip2.database.Reader('GeoLite2-Country.mmdb') as geo:
         with open('output.csv', 'r') as csvin:
            with open('final.csv', 'w') as csvout:
                writer = csv.writer(csvout)
                reader = csv.reader(csvin)
                count = False
                for ip in ips:
                    try:
                        response = geo.country(ip)
                        # print (response.country.name)
                        if count == False:
                            writer.writerow(["Country"])
                            count = True
                        writer.writerow([response.country.name])
                        # print()
                    except Exception as e:
                        print(e)

print(getLocation())
# getLocation()