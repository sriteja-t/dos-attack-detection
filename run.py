# Script to run all the functions at once in sequential order
import parser
import geoLocation
import merge

print(parser.reader('access.log'))
print(geoLocation.getLocation())
print(merge.dropdf())
print(merge.mergedf())