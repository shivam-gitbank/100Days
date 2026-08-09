def tital(fname, lname):
    first = fname.capitalize()
    last = lname.capitalize()
    fullname = first + ' ' + last
    return fullname

first_name = input("enter your firstname ")
last_name = input("enter your lastname ")

print(tital(first_name, last_name))