#Timothy Foster, 3/24/25, Item Counter Program

#Define the function.
def count_file_lines():

    #Duplicate the contents of the file to a variable.
    with open('names.txt', 'r') as file:
        names = " ".join(line.rstrip() for line in file)

    #Get the number of characters in the file.
    file_length = len(names)

    #Define the variable to keep track of the number of names.
    number_of_names = 0

    #Use a for loop to check each character in the file.
    for counter in range(file_length):

        #Assign the character to a new variable.
        character = names[counter]

        #Check if the character is a letter.
        if character.isalpha() == True:

            #Check if it's the last character of the file.
            if counter == file_length:

                #Add to the total.
                number_of_names += 1

            #Check if there's a space before the letter or if it's the first character of the file.
            elif names[counter - 1] == " " or counter == 0:

                #Add to the total.
                number_of_names += 1

    #Print the results.
    print(f"There are {number_of_names} names in the names.txt file.")

#Call the above function.
if __name__ == '__main__':
    count_file_lines()
