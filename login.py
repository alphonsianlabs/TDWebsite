def filter_school_email(email, is_time_allowed=False):
    # Clean the input by stripping extra spaces and making it lowercase
    email = email.strip().lower()

    # Step 1: Check if the email ends with the school domain
    if email.endswith("@sacs.edu.ph"):
        # Split the email to get the part before the '@' symbol (the username)
        local_part = email.split("@")[0]

        # Step 2: Check if the first 7 characters are numbers (Student pattern)
        if len(local_part) >= 7 and local_part[:7].isdigit():
            print("Access Granted! Welcome to the website.")
            return "student"

        # Step 3: Check if the first character is a letter (Teacher pattern)
        elif local_part and local_part[0].isalpha():
            # Check your timeline condition
            if is_time_allowed:
                print("Access Granted! Welcome, Teacher.")
                return "teacher"
            else:
                print("It ain't your time yet. Come back later.")
                return "locked"
        
        else:
            print("Invalid email structure.")
            return "invalid_format"

    # Step 4: Fallback for non-school emails
    else:
        print("Aww, we only use sacs edu accounts")
        return "rejected_domain"

# --- Example Testing ---
# Try running these tests to see how the logic reacts:
print("--- Test 1: Student Email ---")
filter_school_email("2024123@sacs.edu.ph")

print("\n--- Test 2: Teacher Email (Before time window) ---")
filter_school_email("m.cruz@sacs.edu.ph", is_time_allowed=False)

print("\n--- Test 3: Teacher Email (After time window) ---")
filter_school_email("m.cruz@sacs.edu.ph", is_time_allowed=True)

print("\n--- Test 4: External Email ---")
filter_school_email("student@gmail.com")