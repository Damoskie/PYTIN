def check_exam_eligibility():
    # Input details from the user
    age = int(input("Enter your age: "))
    education = input("Enter your highest level of education (e.g., High School, Bachelor's, etc.): ").lower()
    attempts = int(input("Enter the number of previous attempts you have made (0-3): "))

    # Check eligibility conditions
    if age < 18 or age > 30:
        print("Sorry, you are not eligible based on your age.")
    elif education not in ["high school", "12th grade", "bachelor's", "master's", "doctorate"]:
        print("Sorry, you are not eligible based on your education level.")
    elif attempts > 3:
        print("Sorry, you have exceeded the maximum number of attempts.")
    else:
        print("Congratulations! You are eligible for the exam.")

# Call the function to check eligibility
check_exam_eligibility()
