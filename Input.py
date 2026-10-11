NUM1 = int(input("Give value of NUM1:"))
NUM2 = int(input("Give value of NUM2:"))
operator = input("Give the operator:")
if operator == "+":
    print(NUM1+NUM2)
elif operator == "-":
    print(NUM1-NUM2)
elif operator == "*":
    print("NUM1*NUM2")
elif operator == "/":
    print(NUM1/NUM2)
else:
    print("It is invalid operator")        

