##Geneiva Ocampo
##CSCI 1470


##Prompt user to enter a file name
##readlines from the user file
##for each line in the file the average score is computed
##creates a new file with same data plus letter grade


input_file_name = input("Enter the name of the input file: ")


with open(input_file_name, 'r') as input_file:
    lines = input_file.readlines()
    output_file = open("report.txt", 'w')

    lineholder = ""

    for line in lines:
        values = line.split()

        if len(values) == 5:
            last_name = values[0]
            first_name = values[1]
            midterm1_score = int(values[2])
            midterm2_score = int(values[3])
            final_score = int(values[4])
            
            x = (midterm1_score + midterm2_score + final_score) / 3

            if x >= 90:
                letter_grade = 'A'
            elif x >= 80:
                letter_grade = 'B'
            elif x >= 70:
                letter_grade = 'C'
            elif x >= 60:
                letter_grade = 'D'
            elif x<=59:
                letter_grade = 'F'

        lineholder += first_name + " " + last_name + " " + str(midterm1_score) + " " + str(midterm2_score) + " " + str(final_score) + f" {letter_grade}" + " \n"
output_file.write(lineholder[:-25])        
output_file.close()



 









