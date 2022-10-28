import main
import geoLocation
import merge

print(main.reader('access.log'))
print(geoLocation.getLocation())
print(merge.dropdf())
print(merge.mergedf())