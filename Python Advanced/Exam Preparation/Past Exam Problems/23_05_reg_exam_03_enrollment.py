# You are planning to study at Software University.
# You need to choose classes so that you gather enough credits to graduate successfully.
# Write a function called gather_credits that receives information about credits needed, courses, and their credits,
# and returns the result. The function will receive a different number of arguments.
# The arguments will be passed as follows:
# •	The first argument will be the number of credits you need - an integer in the range [0, 200];
# •	The following arguments will be the tuples with two elements - the first one is the course name (string),
# and the second one is the course credits (integer);
# After receiving the information and calling the function, the program should start tracking the enrollment process:
# •	Take the course’s name from each tuple successively and if you need more credits, enroll in it,
# and proceed to the next one.
# •	If a course has already been enrolled in, ignore it, and proceed to the next one.
# •	If you have reached the needed number of credits, STOP enrolling!
#  In the end:
# •	If you’ve managed to gather the needed credits, return the message, including the enrolled courses on a new line:
# "Enrollment finished! Maximum credits: {gathered_credits}.
# Courses: {course1, course2, …, courseN}"
# o	return the courses’ names sorted alphabetically, in ascending order.
# •	Otherwise, return the message:
# "You need to enroll in more courses! You have to gather {credits_shortage} credits more."
# Note: Submit only the function in the judge system
# Input
# •	There will be no input from the console, just parameters passed to your function.
# Output
# •	Return one of the strings shown above depending on the result.
# Constraints
# •	The first argument will always be an integer.
# •	Each tuple given will always contain the course name with its credits.


def gather_credits(needed_credits, *args):

    credits_sum = 0
    taken_courses = []

    for course_name, course_credits in args:
        if credits_sum >= needed_credits:
            break

        if course_name not in taken_courses:
            taken_courses.append(course_name)
            credits_sum += course_credits

        else:
            continue

    if credits_sum >= needed_credits:
        return f"Enrollment finished! Maximum credits: {credits_sum}.\nCourses: {', '.join(x for x in sorted(taken_courses))}"

    return f"You need to enroll in more courses! You have to gather {needed_credits-credits_sum} credits more."



# --- Tests: ---
# Test1:
print(gather_credits(
    80,
    ("Basics", 27),
))

# Test2:
print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))

# Test3:
print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))

#
# --- Outputs: ---
# Test1:
# You need to enroll in more courses! You have to gather 53 credits more.
# Test2:
# Enrollment finished! Maximum credits: 84.
# Courses: Advanced, Basics, Fundamentals
#
# Test3:
# Enrollment finished! Maximum credits: 84.
# Courses: Advanced, Basics, Fundamentals
