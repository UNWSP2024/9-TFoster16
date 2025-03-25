#Timothy Foster, 3/21/25, Random Number File Writer

#Define the function to get a random number between 1 and 500.
def get_random_number():

    #Import the random module.
    import random

    #Get a random number.
    rand_num = random.randint(1,500)

    #Return the value.
    return rand_num

#Define the function to get the user's desired number of random numbers.
def get_user_number():

    #Get user input and instruct the user.
    desired_num = input("Enter how many random numbers you would like the file to hold, up to 1000.")

    #Check if the input is a positive integer.
    if desired_num.isnumeric() == False:

        #Instruct the user again and rerun another iteration while quitting this one.
        print("You must enter a positive integer.")
        write_numbers_to_file()
        quit()

    #Check if the number is bigger than 1000.
    elif int(desired_num) > 1000:

        #Instruct the user again and rerun another iteration while quitting this one.
        print("You must enter a positive integer that is less than 1000.")
        write_numbers_to_file()
        quit()

        #Return the number.
    else:
        return desired_num

#Define the function to write the numbers to a file.
def write_numbers_to_file():

    #Get user input, make it an integer, and assign it to a variable.
    number_of_numbers = int(get_user_number())

    #Create a file.
    write_file = open('example.txt', 'w')

    #Run a for loop to write the random numbers to a file.
    for counter in range(number_of_numbers):

        #Call the above function to get a random number.
        num = get_random_number()

        #Write the random number to the file.
        write_file.write(f'{num}, ')

#Call the above function.
if __name__ == "__main__":
    write_numbers_to_file()
