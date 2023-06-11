def calc_percenatge(total_marks, obtained_marks):
    percentage=(obtained_marks/total_marks)*100
    return percentage

total=int(input("Enter the total amrks for all five subject:"))
obtained=int(input("Enter the total obtained marks in all five subject: "))
print(calc_percenatge(total, obtained))