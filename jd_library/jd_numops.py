##############################
#     jd_numops library      #
#----------------------------#
# Various Numbers Operations #
#============================#
# Ver. 0.4 (2019-12-04)      #
# (C) 2019 Przemyslaw Zbroch #
##############################





#######################################################################################
#                                                                                     #
# isNumber(inStr, numType, numSign)                                                   #
#                                                                                     #
# Function that checks if any string is a proper number.                              #
#                                                                                     #
# Returns True if the input string is a number that meets the requirements.           #
#                                                                                     #
# Parameters:                                                                         #
#   - inStr - any string                                                              #
#   - numType (optional) - string representing the expected number:                   #
#       - any - any number will be accepted (integer or float / positive or negative) #
#               (This is a default setting).                                          #
#       - int - only integers will be accepted                                        #
#   - numSign (optional) - string representing the allowed sign of the numer:         #
#       - any - any sign will be accepted (positive or negative) (this is a default). #
#       - pos - only positive numbers will be accepted                                #
#       - neg - only negative numbers will be accepted                                #
#                                                                                     #
#######################################################################################



def isNumber(inStr, numType = 'any', numSign = 'any'):
    if inStr == '':                                                             # If input string is empty
        return False                                                            #   then the string is not a number so the whole function can return False
    numList = ['-', '.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']      # Chars allowed in integers or floats
    if numType == 'int':                                                        # If only integers are accepted
        numList.remove('.')                                                     #   then remove '.' from allowed chars, as it can't occur in an integer
    if numSign == 'pos':                                                        # If only positive numbers are accepted
        numList.remove('-')                                                     #   then remove '-' from allowed chars, as it can't occur in a positive number
    for x in inStr:                                                             # Iterate through the whole string
        if x in numList:                                                        # If the current char is proper (in the list)
            if '-' in numList:                                                  #   then check if this is the first iteration - if so
                if (numSign == 'neg') and (x != '-'):                           #   then if only negative numbers are accepted check if first char is '-'
                    return False                                                #   if not, then input is not a negative number, so return False
                numList.remove('-')                                             #   else remove '-' from list as '-' can only be at the beginning of the number
            if x == '.':                                                        # Also check if the current char is '.' - if so
                numList.remove('.')                                             #   then remove '.' from list as '.' can only occur once in the whole number
            continue                                                            # If the current char of the number is proper then move to next char
        else:                                                                   # If this char is improper
            return False                                                        #   then the string is not a number so the whole function can return False
    if ((numSign == 'pos') or (numSign == 'neg')) and (float(inStr) == 0):      # If only negative or positive numbers are accepted then check if input was '0'
        return False                                                            #   if so, then it is not considered as a negative or positive, so return False
    return True                                                                 # If all chars are proper (in the numlist) then the string is a proper number





#######################################################################################
#                                                                                     #
# inputNum(message, numType, numSign)                                                 #
#                                                                                     #
# Function similar to input(), but accepts only numbers and keeps looping with        #
# accordant message on any other input. Can allow any number, or only integers, also  #
# a sign can be verified depending on the parameters used.                            #
#                                                                                     #
# Returns user input if it meets the requirements in a string format same as input(). #
#                                                                                     #
# Parameters:                                                                         #
#   - message (optional) - any message shown before user input                        #
#                          if not specified shows no message just like input()        #
#   - numType (optional) - string representing the expected number:                   #
#       - any - any number will be accepted (integer or float / positive or negative) #
#               (This is a default setting).                                          #
#       - int - only integers will be accepted                                        #
#   - numSign (optional) - string representing the allowed sign of the numer:         #
#       - any - any sign will be accepted (positive or negative) (this is a default). #
#       - pos - only positive numbers will be accepted                                #
#       - neg - only negative numbers will be accepted                                #
#                                                                                     #
# Required functions:                                                                 #
#   - isNumber() from jd_numops library                                               #
#                                                                                     #
#######################################################################################



def inputNum(message = '', numType = 'any', numSign = 'any'):
    while True:
        userStr = input(message)
        if isNumber(userStr, numType, numSign):
            return userStr
        print('Możesz podać tylko liczbę', end = '')
        if numType == 'int':
            print(' całkowitą', end = '')
        if numSign == 'pos':
            print(' dodatnią', end = '')
        if numSign == 'neg':
            print(' ujemną', end = '')
        print('!')
