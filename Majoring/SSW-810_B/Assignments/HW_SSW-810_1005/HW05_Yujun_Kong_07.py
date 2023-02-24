"""/*
School: Stevens Institute of Technology
-------------------
Course: SSW 810 - B
Instructor: Prof. Zhongyuan Yu
Teaching Assistant: Kavish Shanghvi
-----------------------------------
Homework: # 05 / Topic: Strings, Files and Coding Style
-------------------------------------------------------
Coder Name with The CWID: Name: Yujun Kong / CWID: 1046 6820
*/"""
# //

# # # Coding Begins # # #


# * import the potentially usable utilities *
import sys

# * import the supporting types *
from typing import Any, List, Sequence, Optional, Iterator, IO

# * import testing tool, target files and classes *
import unittest


""" # Global Objects Begin # """
# {format} for to print blank line:
def BL():
        print()

# {/format/}
""" # /Global Objects End # """


""" # Supporting Classes Begin # """
# <class> define supporting class"ezIO" for to reuse codes:
class ezIO:

    # ([constructor]) define a constructor for class itself:
    def __init__(self):
        pass
    
    # ((method)) define a method for to print out the welcoming words:
    def welcome(self):

        welcoming = "--- Welcome to String manipulation ---"
        print(welcoming)
        BL()

    # ((method)) define a method for to quit the main program:
    def quit_Main(self):

        BL()
        print("--- Thanks for your playing, Bye! ---")
        sys.exit()

    # ((method)) define a method for to get user's singular words sequence:
    def get_AnyType_Input(self, prompt) -> Optional[str]:
        
        illegal_Input_Set: str = '@#^-=_+'

        while True:
            raw_Input: Optional[str]

            try:
                raw_Input = input(prompt)
                
                for i in illegal_Input_Set:
                    if i in raw_Input:
                        print("Kidding?! Please don't input digit, try again.")
                        BL()
                        continue
                
                    elif raw_Input.isnumeric():
                        print("Kidding?! Please don't input digit, try again.")
                        BL()
                        continue
                    elif raw_Input.isspace():
                        print("Kidding?! Please don't only input space, try again.")
                        BL()
                        continue
                    elif raw_Input == "":
                        print("Kidding?! Please don't input nothing, try again.")
                        BL()
                        continue

            except ValueError:
                print(f"{raw_Input} is invalid! Please input again, thanks")
                continue

            return raw_Input
    # ((/method))

    # ((method)) define a method for to handle user's string input <- this example specifically adopts it as the program control:
    def get_String_Input(self, prompt) -> str:
        
        while True:
            raw_Input: str = ""
            try:
                raw_Input = input(prompt)
                return raw_Input
            except ValueError:
                print(f"{raw_Input} is a invalid input! Please try again, thanks")
                continue

# </class>
""" # /Supporting Classes End # """


""" # CORE DEFINING BEGINS HERE # """
# --------------------------------- #

""" # 01 function """
# (function) define a function for to reverse the order of a gotten string:
def my_Reverse(seq: str) -> str:

    max_Index: int = len(seq) - 1

    i = max_Index

    reversed_Seq: list = []

    while True:

        reversed_Seq.append(seq[i])
        i = i - 1

        if i < 0:
            break

    combined_Reversed_Seq = ' '.join(reversed_Seq)
    print (combined_Reversed_Seq)
        
# (/function)

""" # 02 function """
# (function) define a function for to find a target in a sequence to return its offset of the first index of the target:
def my_Substring(target: str, seq: str) -> str:

    tb: int = target[0]
    counter: int = 0

    for x_Letter in seq:

        if x_Letter != tb:
            counter = counter + 1

        elif x_Letter == tb:
            print (counter)

# (/function)

""" # 03 function """
# (function) define a function for to find the second occurrence content in a string matches the user input to return the offset:
def find_Second(key: str, seq: str) -> str:

    counter: int = -1
    finding_Iterator: int = 0

    temp_Stored_Slices: str = ''
    tss = temp_Stored_Slices

    out_Stack_Finding_Point: int = len(seq) - 1

    headOf_Slice_Index = 0
    tailOf_Slice_Index = len(key)

    hix = headOf_Slice_Index
    tix = tailOf_Slice_Index
    
    i = 0

    while (len(key) > 0) and (len(seq) > 0):

        tss = seq[hix : tix]
        counter = counter + 1

        if counter > out_Stack_Finding_Point:

            print ('Oops!')
            break

        elif tss != key:

            hix = hix + 1
            tix = tix + 1
            continue

        elif tss == key:

            hix = hix + 1
            tix = tix + 1

            finding_Iterator = finding_Iterator + 1

            if finding_Iterator == 1:
                continue

            elif finding_Iterator == 2:
                print (counter)
                break

# (/function)

""" # 04 function """
# (function) define a function for to find, and open a file and then read, write it:
def get_lines(target_FileName_withPath: str) -> Iterator[str]:

    try:
        target_file: IO = open(target_FileName_withPath, 'r')
    except FileNotFoundError:
        print (f'Not Found! {target_FileName_withPath} is not existed')
    else:
        with target_file:

            all_Lines: str = target_file.readlines()

            backslashFree_Lines: list = []
            for single_Line in all_Lines:

                first_IndexOf_SingleLine: int = single_Line[0]
                fix = first_IndexOf_SingleLine
                last_IndexOf_SingleLine: int = len(single_Line) - 1
                lax = last_IndexOf_SingleLine

                backslashChar_Index: int = single_Line.find('\\')
                commentsChar_Index: int = single_Line.find('\\')

          
                if fix == '#':
                    continue
                
                #elif '#' in single_Line and (fix == '<') and (lax == '\\'):
                    #single_Line = single_Line.split(single_Line[commentsChar_Index: ])
                    #backslashFree_Lines.append(single_Line)

                #elif (fix == '#') and (lax != '>') and (lax != '\\'):
                    #single_Line = single_Line[ : commentsChar_Index]

                elif (lax == '>') or (lax != '\\'):
                    single_Line = single_Line[: backslashChar_Index]
                    backslashFree_Lines.append(single_Line)

                #elif (fix == '<') and (lax == '>'):                    
                    #purified_Lines.append(single_Line)

                #elif (fix == '<') and (lax == '\\'):
                    #single_Line = single_Line[backslashChar_Index:]
                    #purified_Lines.append(single_Line)

            clear_Lines = ''.join(backslashFree_Lines)
            print (clear_Lines)

            leftArrow_Char_Index: int = clear_Lines.find('<')
            comments_Char_Index: int = clear_Lines.find('#')

            i: int = 0
            x: int = 0
            y: int = 0       

            for letter in clear_Lines:
                
                i = i + 1                

                if letter == '<':

                
                    
                    x = i                  

                elif letter == '>':

                    
                        
                    y = i

                    print (clear_Lines[x-1 : y ])
                        



            return

            print (clear_Lines.split (clear_Lines[ comments_Char_Index : leftArrow_Char_Index ]) )
                        
            return
            
            for i in clear_Lines:

                if i != '<' and i != '>':
                    continue

                elif i == '<' and i == '>':
                    print (i)

            return

            

            
            x: list = []
            for i in clear_Lines:
                    
                
                if i != '>':
                    x.append(i)
                    ''.join(x)

                elif i == '>':
                    x = x[leftArrow_Char_Index : ]
                

                
                    
                #x = x[leftArrow_Char_Index : rightArrow_char_Index]
            #'/'.join(x)
            print (x)
                
                    



                
                    


            
            
            #while True:
                #x = enumerate (clear_Lines)

                #if leftArrow_Char_Index and rightArrow_char_Index:
                    #print ( x[leftArrow_Char_Index : rightArrow_char_Index] )




            #x: str = ''
            #required_Slice = clear_Lines[leftArrow_Char_Index : rightArrow_char_Index]

            #purified_Line: list = []
            #for required_Slice in clear_Lines:

                #print (required_Slice)

                


            #no_Comments_Lines: list = []
            #for clean_Line in purified_Lines:

                #commentsChar_Index: int = clean_Line.find('#')



            #pl = ''.join(purified_Lines)
            #print (purified_Lines)
            #for lbl in pl:
                #print (lbl)


            


            #ckl = ''.join(commentsChar_Killed_Lines)
            #print (commentsChar_Killed_Lines)

            




                



            

            

                    

                    

                


                



                

# (/function)            
 
# ------------------------------- #
""" # CORE DEFINING ENDS HERE # """


"""///*** define main program and execute it below ***///"""

def main(): #!! <- Main Program Procedure Flow !!#

    e = ezIO() #! <- Supporting Input/Output Class !#

    #my_Reverse('abcde')

    #my_Substring('cc', 'abc')

    #find_Second('rosa', 'rosa knows another rosa')
    #find_Second('jason', 'jason beat kevin,yet kevin beat wrong jack')

    get_lines('hw05_given_file.txt')


"""///*** main program ends ***///"""


"""///*** main program execute below ***///"""

if __name__ == '__main__':
    main()

"""///*** main program ends ***///"""

# # # Coding Ends # # #