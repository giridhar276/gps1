

print("hello python")

## read input from keyboard
name = input("Enter your name :")
print("You entered",name)

# display numbers from 1 to 10
# range(start,stop,increment)
print(list(range(1,11)))
print(list(range(1,11,2)))
print(list(range(1,11,2)))
print(list(range(10,0,-1)))

alist = [10,45,30]
print(sum(alist))
print(max(alist))
print(min(alist))

# display line by line
for val in range(1,11):
    print(val)


### list of builtin functions
print(dir(__builtins__))

name = "python"
print(len(name))

alist = [10,20,30]
print(len(alist))


