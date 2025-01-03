"""
File:    ab_verify.py
Author:  SETH LESLIE
Date:    11/5/24
Description:
  This program counts if a string has more a's than (or an equal amount of) b's. If it does, it retur\
ns True. If not, it returns False.
"""
"""
Funciton to check if there are more a's than b's in a string.
:param string: The string passed by the user.
:param index: Keeps track of the first index of the string.
:param a_counter: Keeps track of the number of a's in the string.
:param b_counter: Keeps track of the number of b's in the string.
"""
def ab_verify(string, index = 0, a_counter = 0, b_counter = 0):
    #If the string length is equal to 1, the a and b counters are evaluated.
    if len(string) == 0:

        if a_counter >= b_counter:
            return True
        elif a_counter <= b_counter:
            return False

    if string[index] == "a":
        return ab_verify(string[1:], index = 0, a_counter = a_counter + 1, b_counter = b_counter)

    if string[index] == "b":
        return ab_verify(string[1:], index = 0, a_counter = a_counter, b_counter = b_counter + 1)




if __name__ == '__main__':
   print(ab_verify("aab"))
   print(ab_verify("abba"))
   print(ab_verify("aabbbbbaaaaabbbabaabababa"))
   print(ab_verify("abb"))
   print(ab_verify("ababab"))
