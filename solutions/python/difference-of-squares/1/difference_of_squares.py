def square_of_sum(number):
    squareofsum = 0
    for i in range(1,number+1):
        squareofsum+=i
    return squareofsum**2
        
        
def sum_of_squares(number):
    sumofsquare = 0
    for i in range(1,number+1):
        sumofsquare += i**2
    return sumofsquare
        


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
