
# Simple Password Length Checker for Today's Streak
def check_password(password):
    if len(password) >= 8:
        return "Strong Password!"
    else:
        return "Weak Password! Must be 8 characters long."

user_input = input("Enter password: ")
print(check_password(user_input))
