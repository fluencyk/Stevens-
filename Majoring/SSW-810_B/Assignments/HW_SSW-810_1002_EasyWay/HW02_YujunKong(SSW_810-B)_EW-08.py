"""
/*
School: Stevens Institute of Technology
Course: SSW 540 - A
Topic: Fractions Calculation
Coder with CWID: Name: Yujun Kong / CWID: 1046 6820
Stevens Tech CWID: 1046 6820
*/
"""

import sys,types,fractions

""" define glob vars, cons, lists, dicts, and others """

test = 0

"""/* define vcldo ends */"""


""" define print format method """

# <define blank line>
def BL():

    print()
# <>

"""/* define pf-m ends */"""


"""/* define preset class and method */"""

# <define support-class="KG_IO">
class ezIO:

    def __init__(self):
        pass

    #def pl(*args):print(*args,end='')

    def get_Valid_InputVal(self,pmpt,cvtType):

        while True:
            rawVal = input(pmpt)    
            if rawVal.isalpha():
                print("Invalid input, please try again.")
                break
            elif cvtType == 'Int':
                cvtedVal = int(float(rawVal))
                return cvtedVal
                continue

# <>

# <define main-class="Fraction"> 
class Fraction():

    def __init__(self) -> None:
        pass

    
    def welcome(self):

        welcoming = "# Welcome to Fractions Calculation #"
        print(welcoming)
        BL()


    def get_Frac_Calcu(self):

        t = ezIO()

        #...
        def get_Frac():
        
            f = []

            print("Please set a fraction...")
            BL()
            n = t.get_Valid_InputVal("Input the numerator: ",'Int')
            d = t.get_Valid_InputVal("Input the denominator: ",'Int')

            f.append(n)
            f.append(d)

            print("This Fraction is: " + str(n) + '/' + str(d))
            BL()

            return f

        def calcu_Frac():

            nF = []
            print(nF)

            a = get_Frac()
              
            while True:
                altCMD = input("Type one of '+','-','*','/','=' to start: ")
                lawfulCMD = ['+','-','*','/','=']
                if altCMD == '+':

                    b = get_Frac()

                    nu = (a[0]*b[1])+(b[0]*a[1])
                    de = (a[1]*b[1])

                    print("The result is: " + str(nu) + "/" + str(de) +",")

                    for i in range(2,nu):
                        while (nu % i == 0 and de % i == 0):
                            nu = nu//i
                            de = de//i

                    print("and simplified as: " + str(nu) + "/" + str(de))

                    nF.append(nu)
                    nF.append(de)

                    


                    #print(nF)
                    calcu_Frac()
                    return nF
                    break
                
                else: 
                    altCMD not in lawfulCMD
                    print("Invalid calculation commond! please input again, thanks.")
                    continue



        

            


        #get_Frac()
        calcu_Frac()




class Operation:

    def __init__(self):
        pass



        
# <>

"""/* define class and method ends */"""



"""///*** define main program and execute it below ***///"""

def mainTest():

    x = Fraction()
    #y = Operation()

    x.welcome()
    x.get_Frac_Calcu()




mainTest()

"""///*** main program ends ***///"""