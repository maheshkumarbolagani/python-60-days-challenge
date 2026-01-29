name = input("Enter your Full Name: ")
email = input("Enter your Email ID: ")
mobile = input("Enter your Mobile Number: ")
age = int(input("Enter your Age: "))

valid = True

if name.count(" ") < 1 or name[0] == " " or name[-1] == " ":
    valid = False

if email.count("@") != 1 or email.count(".") < 1 or email[0] == "@":
    valid = False

if len(mobile) != 10 or mobile[0] == '0' or not mobile.isdigit():
    valid = False

if age < 18 or age > 60:
    valid = False

if valid:
    print("User Profile is VALID")
else:
    print("User Profile is INVALID")