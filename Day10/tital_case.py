def tital(fname, lname):
    first = fname.capitalize() # tital is also a function that can be of help here as it capitalize fisrt letter of a string sentence
    last = lname.capitalize()
    fullname = first + ' ' + last
    return fullname

first_name = input("enter your firstname ")
last_name = input("enter your lastname ")

print(tital(first_name, last_name))