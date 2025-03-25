#Timothy Foster, 3/21/25, Average Numbers Project

#Define function.
def sum_numbers_from_file():

    #Import the os module.
    import os

    #Assign the file path.
    numbers_path = "numbers.txt"

    #Check if the file exists and quit if not.
    if os.path.exists(numbers_path):
        file = open("numbers.txt", "r")
    else:
        print("No such file exists. Sorry!")
        quit()

    #Assign the file contents to the numberFile variable.
    with open("numbers.txt", "r") as file:
        numberFile = " ".join(line.rstrip() for line in file)

    #Get the number of characters in the file.
    file_length = len(numberFile)

    #Define the total variable.
    total = 0

    #Use a for loop for each character in the duplicate of the file's contents.
    for counter in range(file_length):

        #Assign each character to a new variable
        num = numberFile[counter]

        #Ensure there are no decimals, negative numbers, nor fractions in the file. Quit if there are.
        if num == "." or num == "-" or num == "/":
            print("There must be only positive integers in the file. Sorry!")
            quit()

        #Check if the character is a number and add it to the total if so.
        elif num.isnumeric() == True:
            total = total + int(num)

    #Print the results.
    print(f'All of the values in the numbers.txt file added together are equal to {total}.')

#Call the above function.
if __name__ == '__main__':
    sum_numbers_from_file()
