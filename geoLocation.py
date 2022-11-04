# from urllib import response
import pandas as pd
import csv
import geoip2.database

# To get the geolocation of every IP address in the log file

def getLocation():

# Read the initial output file created by the parser
    df = pd.read_csv('output.csv')
    print()

# Create dataframe ips and search in the IP database.
    ips = df['remote_host']
    with geoip2.database.Reader('GeoLite2-Country.mmdb') as geo:
         with open('output.csv', 'r') as csvin:
            with open('geoLocation.csv', 'w', newline='') as csvout:
                writer = csv.writer(csvout)
                reader = csv.reader(csvin)
                count = False

# For every ip in the dataframe search in the database for the country using the geoip2.database module            
                for ip in ips:
                    try:
                        response = geo.country(ip)
                        print(response.country.name)
                        if count == False:
                            writer.writerow(["Country"])
                            count = True
                        writer.writerow([response.country.name])
                        
# Catch exception if there exist no entry for the IP           
                    except Exception as e:
                        writer.writerow([e])
                        print(e)