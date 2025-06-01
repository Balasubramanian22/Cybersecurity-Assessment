import re

def check_password_strength(password):
    strength = 0
    remarks = ""

    # Length check
    if len(password) < 6:
        remarks = "Password is too short."
        return strength, remarks
    elif len(password) >= 8:
        strength += 1

    # Lowercase check
    if re.search("[a-z]", password):
        strength += 1

    # Uppercase check
    if re.search("[A-Z]", password):
        strength += 1

    # Digits check
    if re.search("[0-9]", password):
        strength += 1

    # Special characters check
    if re.search("[@#$%^&+=!]", password):
        strength += 1

    # Final remarks
    if strength <= 2:
        remarks = "Weak password"
    elif strength == 3 or strength == 4:
        remarks = "Moderate password"
    elif strength == 5:
        remarks = "Strong password"

    return strength, remarks

if __name__ == "__main__":
    pwd = input("Enter your password: ")
    score, comment = check_password_strength(pwd)
    print(f"\nPassword Score: {score}/5")
    print(f"Assessment: {comment}")
