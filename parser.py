import csv
import apache_log_parser

logParser = apache_log_parser.make_parser("%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-agent}i\"")

# To read the log file   
def reader(filename):
   
# Creating a increment counter for debugging purpose 
    errorLogLines = 0
    totalLines = 0 

# Opening the log file and writing the parsed data in new csv file
    with open(filename) as f, open('output.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        lines = f.readlines()
        lineData = {}
        count = False
        
# Passing every line of log file in the logParser to parse the data.  
        for line in lines:
            try:
                lineData = logParser(line)
                totalLines = totalLines + 1 
                if count == False:
                    writer.writerow(list(lineData.keys()))
                    count = True
                writer.writerow(list(lineData.values()))
            except Exception as e:
                errorLogLines += 1
                print(e)

# LineData is the parsed data, totalLines is the number of parsed lines and errorLogLines are failed to parse log lines.
            print(lineData)
    print("-----Total number of lines parsed: " + str(totalLines))
    print("-----Total number of lines failed: "+ str(errorLogLines))

if __name__ == '__main__':
    reader('access.log')