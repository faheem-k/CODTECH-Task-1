import re

def check_password_strength(password):
    # Initialize strength variables
    length_criteria = False
    lower_criteria = False
    upper_criteria = False
    digit_criteria = False
    special_criteria = False
    common_patterns = ["password", "123456", "qwerty", "letmein"]
    
    # Check length
    if len(password) >= 8:
        length_criteria = True

    # Check for lowercase, uppercase, digits, and special characters
    if re.search(r"[a-z]", password):
        lower_criteria = True
    if re.search(r"[A-Z]", password):
        upper_criteria = True
    if re.search(r"\d", password):
        digit_criteria = True
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        special_criteria = True

    # Check for common patterns
    uniqueness_criteria = not any(pattern in password.lower() for pattern in common_patterns)
    
    # Determine strength
    strength = "Weak"
    criteria_met = sum([length_criteria, lower_criteria, upper_criteria, digit_criteria, special_criteria, uniqueness_criteria])
    
    if criteria_met >= 4:
        strength = "Moderate"
    if criteria_met >= 5:
        strength = "Strong"

    feedback = {
        "length_criteria": length_criteria,
        "lower_criteria": lower_criteria,
        "upper_criteria": upper_criteria,
        "digit_criteria": digit_criteria,
        "special_criteria": special_criteria,
        "uniqueness_criteria": uniqueness_criteria
    }

    return strength, feedback

def main():
    # Prompt the user for a password
    password = input("Enter a password to check its strength: ")
    
    # Check the password strength
    strength, feedback = check_password_strength(password)
    
    # Display the result
    print(f"\nPassword Strength: {strength}")
    print("Feedback:")
    for criteria, met in feedback.items():
        print(f"  {criteria}: {'Met' if met else 'Not Met'}")

# Run the main function
if __name__ == "__main__":
    main()
