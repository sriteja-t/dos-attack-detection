import os, sys
import apache_log_parser
import csv

lineParser = apache_log_parser.make_parser("%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-agent}i\"")

def reader(filename):
    totalLines = 0
    errorLogLines = 0
    with open(filename) as f:
        # log = f.read()
        lines = f.readlines()
        lineData = {}
        for line in lines:
            totalLines += 1
            try:
                lineData = lineParser(line)
            except Exception as e:
                errorLogLines += 1
                print(e)
            
            print(lineData)
            print(totalLines)
            print(errorLogLines)


# def toCSV(LineData):


if __name__ == '__main__':
        reader('access.log')

