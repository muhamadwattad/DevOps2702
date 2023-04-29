isTrue = False
a = 2
b = 2.5
strOne = "One"
strThree = "Three"


if a > b and (strOne == "One" or b > 1):
    print("a is greater than b")
elif a == b:  # or u can do a is b
    print("a equals b")
elif strOne != strThree:
    print("str are not the same")
else:
    print("a is not greater than b")