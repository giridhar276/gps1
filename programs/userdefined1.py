

### fixed arguments
def display(a,b):
    c = a + b
    return c


total = display(10,20)
print(total)

###################
# variable length arguments
def display(*data):  # tuple
    for val in data:
        print(val)

display(10,20,30,56,43,63,"info")

###################



def display(**kwargs):
    print(kwargs)

display(chap1=10 , chap2 = 20)


