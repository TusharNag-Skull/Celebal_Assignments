# Create lower triangular, upper triangular and pyramid containing the "*" character.

#I will create a menu driven program to create lower triangular, upper triangular and pyramid containing the "*" character.
#1. Lower triangular
#2. Upper triangular
#3. Pyramid
#4.Exit

class Triangle:                        #This is the Triangle class which will contain methods to print different patterns
    def lower_triangular(self, rows):  #This method will print a lower triangular pattern
        for i in range(1, rows + 1):   #This loop will iterate from 1 to the number of rows
            for j in range(1, i + 1):  #This inner loop will iterate from 1 to the current row number
                print("*", end=" ")    #Printing "*" character with a space at the end
            print()

    def upper_triangular(self, rows):  #This method will print an upper triangular pattern
        for i in range(rows, 0, -1):   #This loop will iterate from the number of rows to 1
            for j in range(1, i + 1):  #This inner loop will iterate from 1 to the current row number
                print("*", end=" ")    #Printing "*" character with a space at the end
            print()

    def pyramid(self, rows):           #This method will print a pyramid pattern
        for i in range(1, rows + 1):   #This loop will iterate from 1 to the number of rows
            print(" " * (rows - i), end="") # Printing spaces for pyramid alignment
            for j in range(1, i + 1):     #This inner loop will iterate from 1 to the current row number
                print("* ", end="")       #Printing "*" character with a space at the end
            print()

t1 = Triangle()     # Create an instance of the Triangle class
# Start a loop to display the menu and perform actions based on user input

while True:  # This will create a menu driven program to create lower triangular, upper triangular and pyramid containing the "*" character.
    print("Menu:")
    print("1. Lower Triangular")
    print("2. Upper Triangular")
    print("3. Pyramid")
    print("4. Exit")
    
    choice = int(input("Enter your choice: ")) # Taking input from the user for the choice of operation
    # Based on the user's choice, call the appropriate method from the Triangle class
    
    if choice == 1: # If the user chooses 1, we will call the lower_triangular method
        rows = int(input("Enter the number of rows for Lower Triangular: "))
        t1.lower_triangular(rows)  #Calling the lower_triangular method to print the pattern
    elif choice == 2: # If the user chooses 2, we will call the upper_triangular method
        rows = int(input("Enter the number of rows for Upper Triangular: "))
        t1.upper_triangular(rows) # Calling the upper_triangular method to print the pattern
    elif choice == 3: # If the user chooses 3, we will call the pyramid method
        rows = int(input("Enter the number of rows for Pyramid: "))
        t1.pyramid(rows) # Calling the pyramid method to print the pattern
    elif choice == 4: # If the user chooses 4, we will exit the program
        break    # Exit the loop and end the program
    else:
        print("Invalid choice, please try again.")
    
    print()  # Print a newline for better readability   
    


