from sys import path

#Add a path to your file
path.append('C:\\Users\\LiekeCeton\\Projects\\Education\\modules')

#import module
from module import suml, prodl

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))

