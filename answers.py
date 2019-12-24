


################################################################################
# Zadanie 4



def revers_sentence(inStr):
    outStr = ''
    for x in range(len(inStr)-1,-1,-1):
        if (x == len(inStr)-1) or (inStr[x+1] == ' '):
            outStr = outStr + inStr[x].upper()
        else:
            outStr = outStr + inStr[x].lower()
    return outStr



# a = input('\n>')
# n = count_char(a,'A')
# print(n)



################################################################################
# Zadanie 5



def count_char(inStr,char):
    inStr = inStr.lower()
    char = char.lower()
    outCount = 0                #
    for x in inStr:             # This could be achieved by simple inStr.count(char)
        if x == char:           # but in that case why build a new function in the first place
            outCount += 1       #
    return outCount



# a = input('\n>')
# rev = revers_sentence(a)
# print(rev)



################################################################################
# Zadanie 6



def list_filter(int_values,*dividers):
    outList = []
    for x in int_values:
        if type(x) != int:
            continue
        divChk = True
        for y in dividers:
            if (type(y) != int) or (y < 2):
                continue
            x = int(x)
            y = int(y)
            if (x % y) == 0:
                divChk = False
        if divChk:
            outList.append(x)
    return outList



# result = list_filter([1,0,8,15,20,11], 20)
# print(result) # [1,8,15,11]
# result = list_filter([1,8,'aa',1.1,15,20,11], 20,4,0)
# print(result) # [1,15,11]
# result = list_filter([1,8,15,20,11], 2, 5, 31,1,1.1,'aa')
# print(result) # [1,11]



################################################################################
# Zadanie 7



import random

def get_random_elements(inList,randVal = 1):
    if (type(randVal) != int) or (randVal < 1) or (randVal > len(inList)):
        raise ValueError('No way to do this!')
    outList = []
    for x in range(randVal):
        randItem = inList[random.randint(0,len(inList)-1)]
        outList.append(randItem)
        inList.remove(randItem)
    return outList



# n = get_random_elements([1,2,6,3,7]) # [2]
# print(n)
# n = get_random_elements([1,2,6,3,7],3) # [6,2,7]
# print(n)
# n = get_random_elements([1,2,6,3,7],16) # Wyjątek!
# print(n)



################################################################################
# Zadanie 8



from flask import Flask, request
from jd_library import jd_htmlops
from my_phonebook import pb



app = Flask(__name__)



@app.route('/pbk', methods=['GET', 'POST'])
def pbk():
    if request.method == 'POST':
        nameFilter = request.form['nameFilter']
        numFilter = request.form['numFilter']
    else:
        nameFilter = ''
        numFilter = ''
    tabContent = ''
    for x in pb:
        if (nameFilter.lower() in x['nickname'].lower()) and (numFilter in x['number']):
            tabContent += f'''
                <tr>
                    <td>{x['nickname']}</td>
                    <td>{x['number']}</td>
                </tr>'''
        if tabContent == '':
            tabContent = '''
                <tr>
                    <td colspan="2">No record!</td>
                </tr>'''
    siteContent = f'''
        <h3>Moja książka telefoniczna:</h3>
        <form method="POST">
            <table>
                <tr>
                    <th>Nickname</th>
                    <th>Number</th>
                </tr>
                <tr>
                    <td>
                        <input type="text" name="nameFilter" value="{nameFilter}" placeholder="filter">
                    </td>
                    <td>
                        <input type="text" name="numFilter" value="{numFilter}" placeholder="filter">
                    </td>
                </tr>
                {tabContent}
            </table>
            <input type="submit" hidden />
        </form>'''
    outHtml = jd_htmlops.buildHtmlPage('My Phone Book', siteContent)
    return outHtml



if __name__ == "__main__":
    app.run()
