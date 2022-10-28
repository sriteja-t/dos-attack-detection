import os, sys
import apache_log_parser
import csv

lineParser = apache_log_parser.make_parser("%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-agent}i\"")

def reader(filename):
    totalLines = 0
    errorLogLines = 0
    with open(filename) as f, open('output.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        lines = f.readlines()
        lineData = {}
        count = False
        for line in lines:
            totalLines += 1
            try:
                lineData = lineParser(line)
                if count == False:
                    writer.writerow(list(lineData.keys()))
                    count = True
                writer.writerow(list(lineData.values()))
            except Exception as e:
                errorLogLines += 1
                print(e)
            
            print(lineData)
            print(totalLines)
            print(errorLogLines)

if __name__ == '__main__':
    reader('access.log')
