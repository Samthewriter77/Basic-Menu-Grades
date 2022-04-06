#Samuel Smith , A201, Chapter 5 Project, smithsawch5project.py, Due 4/10/22
# Create a menu that asks what you would like to see from scores you're asked to enter.

def launch_menu(): #decided to do a launch menu to add the header and creator info and call for the scores to avoid zero value errors
    print("Functions") #title
    print("by Sam Smith") #author credit
    menu() #calls the actual menu
    get_Scores() #initial request for scores so functions below are guaranteed to work
    global menu_Choice #this is global so we do not have a zero value in menu_Choice and so it isn't necessary to call it again
    menu_Choice = input("Please enter the number of your selection: ") #initial call for menu_Choice to fill global value
def menu(): #defines the initial menu of options
    print("Option 1: Input Three Scores")
    print("Option 2: Print the Sum and Average of the Scores")
    print("Option 3: Find the Minimum Score")
    print("Option 4: Find the Maximum Score")
    print("Option 5: Exit") #Option 5 can be called with either 5 or Exit
def get_Scores():
    global score_1 #global scores so they stay put when called each time and we don't have a hanging value somewhere
    global score_2
    global score_3
    score_1=int(input("Score 1: ")) #converts to integer type in order to perform mathematical functions on the values
    score_2=int(input("Score 2: "))
    score_3=int(input("Score 3: "))
    return #to prevent looping and to return values
def score_Total():
    score_Total_Value=int(score_1+score_2+score_3) #builds the sum / total of the scores
    print("The total score is: "+str(score_Total_Value)) #provides context for the printed value and converts to string for easy printing
    return
def avg_score():
    avg_score_Value=(score_1+score_2+score_3)/3 #builds the average score from the base variables
    print("The average is: "+str(avg_score_Value)) #converts to string for easy printing
    return
def low_Score():
    low_Score_Value=int(min(score_1,score_2,score_3)) #performs minimum mathematical equation to determine smallest of the numbers
    print("The minimum score is "+str(low_Score_Value)) #converts to string to provide context for the printed value
    return
def high_Score():
    high_Score_Value=int(max(score_1,score_2,score_3)) #function to find the maximum of the input scores
    print("The maximum score is "+str(high_Score_Value)) #converts to string for clarity
    return

launch_menu() #calls the menu list
while menu_Choice !="5": #we start at !=5 so it will exit at 5 if that is the first option chosen but will cycle through other options from there.
    if menu_Choice=="1":
        get_Scores() #since option 1 is to read in 3 new scores, we call the get_Scores function
        menu_Choice = input("Please enter the number of your selection: ")    #we use an input here to update the variable directly
    elif menu_Choice=="2":
        score_Total() #option 2 calls both the score total and the avg score so we call two functions when 2 is selected from the menu
        avg_score() #calculates the average and prints it
        menu_Choice = input("Please enter the number of your selection: ")
    elif menu_Choice=="3":
        low_Score() #calls minimum function with stored score values from this nested while loop
        menu_Choice = input("Please enter the number of your selection: ")
    elif menu_Choice=="4":
        high_Score() #pulls the high score and prints it with context, see function comment above.
        menu_Choice = input("Please enter the number of your selection: ")
    else:
        print("Oops, check your formatting for your answer and try again! Only the numbers 1-5 are accepted.") #error handling phrase and guidance
        menu() #calls the menu again to provide clear options
        menu_Choice = input("Please enter the number of your selection: ") #gives the user another chance to select