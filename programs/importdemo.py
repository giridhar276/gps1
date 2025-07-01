
# method1:   all the methods are imported to your program space
import math
print(math.tan(1))
print(math.log(1))


#  method2:  using alis name
import math as m
print(m.log(1))
print(m.sin(2))

# method3: importing required methods only
from math import tan,log
print(tan(1))
print(log(1))