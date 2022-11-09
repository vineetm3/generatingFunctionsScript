import math 

'''
I simply made two methods for each of the two problems. There is probably a more efficient 
way of handeling this by using only one method but I didn't think it was needed for this hw. 
In this file I have 2 methods (computeSum and computeSum2) which compute the coefficients 
and 2 print methods to get our output in a table format. 
'''

def computeSum() -> int: 
    finalCoeff = 0
    counter = 0
    printTerms("Case #","1st Term", "2nd Term", "3rd Term", "Total(MP)")

    for i in range(3): 
        for j in range(6): 
            coeff1 = math.comb(2, i) * (-1)**i
            coeff2 = math.comb(5, j) * (-1)**j
            
            tempR = (29 - (6*i) - (5*j))

            if tempR >= 0: 
                coeff3 = math.comb(tempR + 6, tempR)
                counter += 1
            else: 
                continue

            finalCoeff += (coeff1 * coeff2 * coeff3)
            printTerms(counter, coeff1, coeff2, coeff3, coeff1 * coeff2 * coeff3)

    return finalCoeff

def computeSum2() -> int: 
    finalCoeff = 0
    counter = 0
    printTerms("Case #","1st Term", "2nd Term", "Total (MP)")

    for i in range(3): 
        for j in range(1): 
            coeff1 = math.comb(2, i) * (-1)**i
            
            tempR = (23 - (9*i))

            if tempR >= 0: 
                coeff3 = math.comb(tempR + 3, tempR)
                counter += 1
            else: 
                continue

            finalCoeff += (coeff1 * coeff3)
            printTerms(counter, coeff1, coeff3, coeff1 * coeff3)

    return finalCoeff

def printTerms(a, b, c, d, e) -> None: 
    print(f"{(a):>12}{(b):>12}{(c):>12}{(d):>12}{(e):>12}")

def printTerms2(a, b, c, d) -> None: 
    print(f"{(a):>12}{(b):>12}{(c):>12}{(d):>12}")

print("   The coefficient computed by summing the last column by AP is: " + str(computeSum()))