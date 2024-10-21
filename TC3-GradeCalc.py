# Grade Point Calculator

# Create a console-based program that will take a letter grade, such as B+ or C, and convert it to its 
# corresponding numeric value. It will use two prompts, one for the letter grade and a second for the
# modifier, if any (+ or -), and calculate, then output the proper number grade.

# •	Possible letter grades are A, B, C, D, and F
# •	Possible numeric values are 4, 3, 2, 1, and 0, respective to the letters listed above.
# •	Possible modifiers are a plus (+), a minus (–) or nothing. 
# •	There is no F+ or F–. 
# •	Using the + sign increases the numeric value by 0.3, using the – sign decreases it by 0.3. However, an A+ has 
#       still has a value of only 4.0. 
# •	A valid letter grade can be either uppercase or lowercase.
# •	If an invalid value is entered, display a warning message.


def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    import sys

    #Intro message
    print("Grade Point Calculator\n\nValid letter grades that can be entered: A, B, C, D, F \nValid grade modifiers are +, - or nothing.\nAll letter grades except from F can include a + or - symbol.\nCalculated grade point value cannot exceed 4.0.")

    #Input variable - Letter
    letter = input("\nPlease enter a letter grade: ").lower()

    #Letter identification (A, B, C, D, F) and grades (4, 3, 2, 1, 0)
    if letter == "a":
        grade = 4
    elif letter == "b":
        grade = 3
    elif letter == "c":
        grade = 2
    elif letter == "d":
        grade = 1
    elif letter == "f":
        grade = 0
    else:
        print("You entered an invalid letter grade.")
        sys.exit()
    
    #Input variable - Modifier
    modifier = input("Please enter a modifier (+, - or nothing): ")

    # Modifiers (+, - or zero) + Grade total
    if modifier == "+":
        #Exceptions (A+ is still 4.0, F+ invalid grade)
        if letter == "a":
            value = float(grade)
        elif letter == "f":
            print("F+ is not a valid grade.")
            sys.exit()
        #Every other grade
        else:
            value = float(grade + 0.3)
    elif modifier == "-":
        #Normal grades
        value = float(grade - 0.3)
        #Exception (F- invalid grade)
        if letter == "f":
            print("F- is not a valid grade.")
            sys.exit()
    elif modifier == "" or modifier == " " or modifier == "nothing":
        value = float(grade)
    else:
        print("This is not a valid modifier (or lack thereof).")
        sys.exit()

    #Output message
    print("The numeric value is: ", round(value, 1))

    # YOUR CODE ENDS HERE

main()
