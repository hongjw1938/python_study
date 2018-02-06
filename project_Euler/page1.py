#############################3#Problem1



#Multiples of 3 and 5
def mul():
    result = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return result






######################################problem2




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








##########################problem3



def isPrime(num):
    retval = False
    if num<2:
        retval = False
    elif num==2 or num==3 or num==5 or num==7 or num==11 or num==13 or num==17 or num==19 or num==23:
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
    print(dlist)
    for j in dlist:
        boolval = isPrime(j)
        if boolval == True:
            dlist2.append(j)
        else:
            continue
    largest = dlist2[-1]
    return largest




########################Problem4




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


#print(getBigPal(3))






#################Question 5



#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def getNum(ran):
    
    retNum = 1
    temp = ran
    #To go out with better performance, make it even number
    if ran % 2 == 0:
        pass
    else:
        ran += 1
    
    #First of all, multiply every prime number
    #To implement performance, multiply 2 before try for~loop
    retNum *= 2
    
    for i in range(3,ran,2):
        if isPrime(i):
            retNum *= i
        else:
            continue
    
    #Secondly, make it back to original number to go further
    #And save the number into temporary variable
    if temp%2 !=0:
        ran -=1
    plusNum = retNum
    
    
    #Lastly, check if the number is the targeted one.
    while True:
        
        for j in range(2,ran+1):
            if retNum % j == 0:
                if j==ran:
                    return retNum
                continue
            
            else:
                break
        retNum += plusNum
        

#print(getNum(30))

#Question6


sqrsSum = 0
sumSqr = 0
for i in range(1,101):
    sqrsSum += i ** 2

for i in range(1,101):
    sumSqr += i

#result = (sumSqr ** 2) - sqrsSum
#print(result)








################Question7


#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?

class getTargetP:
    def __init__(self):
        self.targetNo = 2
        self.intervNum = 3
    
    def getPr(self):
        while self.targetNo <= 10001:
            self.intervNum += 2
            if isPrime(self.intervNum):
                self.targetNo += 1
                if self.targetNo == 10001:
                    print(self.intervNum)
            else:   
                continue
    
        
        
        
        
##################Question8



numbers = '''7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'''


targetList = [0]

for i in range(0,len(numbers)-13):
    for j in range(i,i+13):
        if numbers[j] ==0:
            i += 1

    targetNum = 1
    for j in range(i,i+13):
        targetNum *= int(numbers[j])
    targetList.append(targetNum)
    
        
    if targetList[0] <= targetList[1]:
        del targetList[0]
    else:
        targetList.pop()
        
#print(targetList.pop())



#another way to solve

from string import whitespace

class anotherSolve:
    def __init__(self):
        self.numFile = open('numbers.txt','r')
        self.numbers2 = [int(nums) for lines in self.numFile for nums in lines if nums not in whitespace]
        
    def targetNum(self, n):
        numList = self.numbers2
        targetList = [0]
        targetNum2 = 1
        for i in range(0, len(numList)-n):
            for j in range(i, i+n):
                if numList[j] == 0:
                    break
                targetNum2 *= numList[j]
            targetList.append(targetNum2)
            
            if targetList[0] > targetList[1]:
                targetList.pop()
                
            else:
                del targetList[0]
                
            targetNum2 = 1
        return targetList.pop()


#test = anotherSolve()
#print(test.targetNum(13))
                
                
                


##################################Question9




#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

#a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.





#Because they say there exactly exist 1000 that meet the condition...
#It means that we can use aliquot of 1000 like under this ex
#(25*a)^2 + (25*b)^2 = (25^c)^2



#Get the aliquotes of 1000

def getAliquot(num):
    sqrtNum = int(num ** 0.5)
    alList = []
    for i in range(1, sqrtNum):
        if num%i == 0:
            if i != 1:
                alList.append(i)
        else:
            continue
        i += 1
    alList.sort()
    return alList
    
def findTriplet(QNum):
    divide = 0
    alList = getAliquot(QNum)
    retNum = 0
    
    for i in alList:
        divide = QNum / i
        a, b = 1, 2
        c = divide - a - b
        
        while a>0 and b>0 and c >0 and b >= a:
            if (a ** 2) + (b ** 2) == (c ** 2):
                retNum = a*i*b*i*c*i
                print(a, b, c ,i)
                return retNum
            else:
                if c <=  b:
                    a += 1
                    b = a+1
                    c = divide - a - b
                else:
                    b += 1
                    c -= 1
                    
            
        
print(findTriplet(1000))
