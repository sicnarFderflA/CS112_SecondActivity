name = input("Your Name:")
idnum = int(input("Your ID Number:"))
coursec = input("Your Course and Section:")
grad1 = eval(input("Your 1st  Quarter Grade:"))
grad2 = eval(input("Your 2nd  Quarter Grade:"))
grad3 = eval(input("Your 3rd  Quarter Grade:"))
grad4 = eval(input("Your 4th  Quarter Grade:"))

finalgrad = (grad1 + grad2 + grad3 + grad4 )/ 4

print("Name:" , name)
print("ID Number:" , idnum)
print("Course and Setion:" , coursec)
print("1st Quarter Grade:" , grad1)
print("2nd Quarter Grade:" , grad2)
print("3rd Quarter Grade:" , grad3)
print("4th Quarter Grade:" , grad4)
print("Your Average Grade:" , finalgrad)
