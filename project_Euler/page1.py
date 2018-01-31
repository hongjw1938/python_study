#Multiples of 3 and 5
def mul():
    result = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return result

#problem2
#get fibonacci and plus the number which is even
def fibonacci():
    flist = [1,2]
    retval = 0
    while flist[1] < 4000000:
        flist.append(flist[0]+flist[1])
        if flist[1] % 2 ==0:
            retval += flist[1]
        flist.remove(flist[0])
    return retval        



#problem3

def isPrime(num):
    retval = False
    if num<2:
        retval = False
    elif num==2 or num==3 or num==5:
        retval = True
    elif num%2 == 0 or num%3 == 0:
        retval = False
    else:
        for i in range(5,int(round(num ** 0.5))+1,6):
            if num%i == 0 or num%(i+2) == 0:
                retval = False
                break
            else:
                retval = True
                continue
    return retval

def getPrimeNum(num):
    dlist = []
    dlist2 = []
    largest = 0
    snum = int(round(num ** 0.5))
    for i in range(1, snum+1):
        if num % i == 0:
            dlist.append(i)
            dlist.append(int(num/i))
        else:
            continue
    dlist.sort()
    
    for j in dlist:
        boolval = isPrime(j)
        if boolval == True:
            dlist2.append(j)
        else:
            continue
    largest = dlist2[-1]
    return largest


#Problem4
#Making palindrome

def makePal(tranNum):
    retval = 0
    number = tranNum
    boolFlag = False
    while not boolFlag:
        
        digit = len(str(number-1))
        numList = list(str(number-1))
        for i in range(digit):
            numList[digit-1-i] = numList[i]
    
        for j in range(digit):
            retval += int(numList[j]) * (10 ** (digit-1-j))
        
        if retval > tranNum:
            if digit % 2 != 0:
                number -= (10 ** int(digit/2+1))
            else:
                number -= (10 ** digit/2)
            retval = 0
        
        else:
            boolFlag = True
        
    return retval

def isPal(num):
    numL = list(str(num))
    
    comp = []
    compared = 0
    for j in range(0,len(numL)):
        comp.append(numL[len(numL)-1-j])

    retval = False
    for i in range(len(numL)):
        if int(numL[i]) == int(comp[i]):
            compared += 1
            if compared == len(numL):
                retval = True
            else:
                retval = False
        else:
            retval = False

    return retval


def getBigPal(digP):
    digit = (10 ** digP) -1
    palNum = []
    for i in range(digit,(digit+1)-(digit+1)/10,-1):
        for j in range(digit,(digit+1)-(digit+1)/10, -1):
            if isPal(i*j) == True:
                palNum.append(i*j)
                
            else:
                continue
    palNum.sort()
    return palNum[-1]


print(getBigPal(3))
