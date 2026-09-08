# Password Strength Checker
# Checks a password's length, character variety, and whether it's a common/weak password.

userPass = input("Enter your password to check its strength:\n")

strengthPoint = 0

# -------------------------
# Length
# -------------------------

if len(userPass) >= 8:
    strengthPoint += 1
    print("Password has a good amount of characters! ✔️")
else:
    print("Password is not long enough! ❌")
    print("It is suggested that you increase the number of characters!")


# -------------------------
# Lowercase
# -------------------------

if any(c.islower() for c in userPass):
    strengthPoint += 1
    print("Password has at least one lowercase character! ✔️")
else:
    print("Password does not have a lowercase character! ❌")
    print("It is suggested to add at least one lowercase character!")


# -------------------------
# Uppercase
# -------------------------

if any(c.isupper() for c in userPass):
    strengthPoint += 1
    print("Password has at least one uppercase character! ✔️")
else:
    print("Password does not have an uppercase character! ❌")
    print("It is suggested to add at least one uppercase character!")


# -------------------------
# Number
# -------------------------

if any(c.isdigit() for c in userPass):
    strengthPoint += 1
    print("Password has at least one number! ✔️")
else:
    print("Password does not have a number! ❌")
    print("It is suggested to add at least one number!")


# -------------------------
# Special character
# -------------------------

specialChar = "!@#$%^&*,./;'`~()-_=+[]{}|:\"<>?"

if any(c in specialChar for c in userPass):
    strengthPoint += 1
    print("Password has at least one special character! ✔️")
else:
    print("Password does not have a special character! ❌")
    print("It is suggested to add at least one special character!")


# -------------------------
# Common password check
# -------------------------

commonPhrase = ["123456789", "qwerty", "password", "12345678", "admin"]

if any(phrase in userPass.lower() for phrase in commonPhrase):
    print("Password contains a predictable or commonly used phrase! ❌")
    print("It is recommended to change the password!")
else:
    strengthPoint += 1
    print("Password does not contain a common phrase! ✔️")


# -------------------------
# Strength score
# -------------------------

print("\n-------------------------")
print(f"Strength Score: {strengthPoint}/6")

if strengthPoint <= 2:
    print("Password Strength: WEAK ❌")
elif strengthPoint <= 4:
    print("Password Strength: MEDIUM ⚠️")
else:
    print("Password Strength: STRONG ✔️")



