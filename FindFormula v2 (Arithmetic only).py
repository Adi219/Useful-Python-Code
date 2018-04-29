import math

class FindForm():

    def solve(Arr):

        formulaStr = ""
        maxPower = len(Arr)
        
        if Arr.count(Arr[0]) == len(Arr): ## All the terms are the same
            formulaStr +=  str(Arr[0])
        else:

            diffArr = Arr[0:]
            
            while len(diffArr) != 1 and Arr.count(Arr[0]) != maxPower:

                diffArr = Arr[0:]
                
                while len(diffArr) > 1 and diffArr.count(diffArr[0]) != len(diffArr):
                    newArr = []
                    for i in range(len(diffArr) - 1):
                        newArr.append(diffArr[i + 1] - diffArr[i])
                    diffArr = newArr[0:]

                
                if len(diffArr) != 1: ## It's not geometric
                    formulaStr += str(diffArr[0] / math.factorial(maxPower - len(diffArr)))
                    formulaStr += "n^" + str(maxPower - len(diffArr)) + " + "

                    tempArr = []
                    for j in range(maxPower):
                        tempArr.append(Arr[j] - ((diffArr[0] / math.factorial(maxPower - len(diffArr))) * ((j + 1) ** (maxPower - len(diffArr)))))
                    Arr = tempArr[0:]
            
            
            formulaStr += str(Arr[0])
            tempStr = ""
            
            for k in range(maxPower, 0, -1):
                
                if formulaStr.count("n^"+ str(k)):

                    totalCoeff = 0
                    for m in range(len(formulaStr)):

                        if formulaStr[m] == "n":

                            if formulaStr[m+2:m+2+len(str(k))] == str(k):

                                if "+" in formulaStr[:m+1]:
                                    coefficient = formulaStr[ : formulaStr[:m][::-1].index("+") -1]
                                else:
                                    coefficient = formulaStr[:m]
                                
                                if "n" not in coefficient and coefficient != "":

                                    try:
                                        totalCoeff += int(coefficient)
                                    except:
                                        totalCoeff += float(coefficient)
                                else:
                                    totalCoeff += 1
                    
                    tempStr += str(totalCoeff) + "n^" + str(k) + " + "
                    
            
            if tempStr[:2] == "1n":
                tempStr = tempStr[1:]
            
            if " +" in formulaStr:
                
                blah = formulaStr[len(formulaStr) - formulaStr[::-1].index(" +"):]

                if "n^" not in blah:
                    
                    if blah[0] != "-":
                        blah = " + " + blah
                    elif blah[0] == "-" :
                        blah = " - " + blah[1:]

                    tempStr += blah

            tempStr = ' '.join(tempStr.split())
            tempStr = tempStr.replace(" 1n", " n")
            tempStr = tempStr.replace("^1 ", " ")
            tempStr = tempStr.replace(" + 0.0", "")
            tempStr = tempStr.replace("+ +", "+")
            tempStr = tempStr.replace(".0n", "n")

            if tempStr[:2] == "1n":
                tempStr = tempStr[1:]

            if tempStr[-2:] == ".0" or tempStr[-2:] == " +":
                tempStr = tempStr[:-2]
            
            
            try:
                if tempStr[::-1].index(" + ") == 0:
                    tempStr = tempStr[: len(tempStr) - 3]
            except:
                pass
            
            formulaStr = tempStr[0:]
        
        return formulaStr

while True:
    TA = list(map(float, input("Space separated Sequence -->\t").split()))
    String = "                   Term(n) =    "
    input(String + FindForm.solve(TA))
