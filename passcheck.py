import re

def check_password_strength(password):
    remarks = []

    # Length check
    if len(password) < 8:
        remarks.append("Password must be at least 8 characters long.")

    # Uppercase check
    if not re.search(r"[A-Z]", password):
        remarks.append("Add at least one uppercase letter.")

    # Lowercase check
    if not re.search(r"[a-z]", password):
        remarks.append("Add at least one lowercase letter.")

    # Digit check
    if not re.search(r"\d", password):
        remarks.append("Add at least one number.")

    # Special character check
    if not re.search(r"[@$!%*?&^#_=+\-]", password):
        remarks.append("Add at least one special character.")

    return remarks


if __name__ == "__main__":
    while True:
        pwd = input("Enter a password to check: ")
        feedback = check_password_strength(pwd)

        if not feedback:  # means no issues found
            print("\n✅ Password accepted: Strong password!")
            break
        else:
            print("\n❌ Weak password. Please fix the following:")
            for tip in feedback:
                print("-", tip)
            print("\nPlease try again.\n")

