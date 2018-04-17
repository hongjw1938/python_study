from string import whitespace
class number11:
    def __init__(self, numFile):
        self.numFile = open(numFile, 'r')
        self.fileNum = number11.make2DList([ nums  for line in self.numFile.readlines() for nums in line if nums not in whitespace ])
    
    @classmethod
    def make2DList(cls, numberList):
        temp = []
        numbers = []
        for i in range(0,len(numberList),2):
            temp.append(int(numberList[i])*10 + int(numberList[i+1]))
        
        for line in range(0,len(temp),20):
            numbers.append(list(temp[line:line+20]))
            
        return numbers
            
            
            
            
    #This method is for initial step to start
    def initialDfs(self, x, y):
        
        #This value is for first step pass by
        passed = 1
        
        #return value
        retVal = self.fileNum[x][y]
        
        #Possible ex 1 : if initial point stays at left - top side
        if x < 3 and y < 3:
            retVal = max(self.searchDfs(x, y+1, passed+1, 'right', retVal), self.searchDfs(x+1, y+1, passed+1, 'rd_diagonal', retVal)
                        , self.searchDfs(x+1, y, passed+1, 'down', retVal))
        
        #Possible ex2 : if initial point stays at top side
        elif x < 3 and 3 <= y and y < len(self.fileNum[x])-3 : 
            retVal = max(self.searchDfs(x, y+1, passed+1, 'right', retVal), self.searchDfs(x+1, y+1, passed+1, 'rd_diagonal', retVal)
                           , self.searchDfs(x+1, y, passed+1, 'down', retVal) ,self.searchDfs(x+1, y-1, passed+1, 'ld_diagonal', retVal)
                           , self.searchDfs(x, y-1, passed+1, 'left', retVal))
        
        #Possible ex3 : if initial point stays at right - top side
        elif x < 3 and y >= len(self.fileNum[x])-3:
            retVal = max(self.searchDfs(x, y-1, passed+1, 'left', retVal), self.searchDfs(x+1, y-1, passed+1, 'ld_diagonal', retVal)
                        , self.searchDfs(x+1, y, passed+1, 'down', retVal))
                        
        #Possible ex4 : if initial point stays at left - bar side
        elif 3 <= x and x < len(self.fileNum)-3 and y < 3:
            retVal = max(self.searchDfs(x, y+1, passed+1, 'right', retVal), self.searchDfs(x+1, y+1, passed+1, 'rd_diagonal', retVal)
                        , self.searchDfs(x+1, y, passed+1, 'down', retVal), self.searchDfs(x-1, y, passed+1, 'top', retVal)
                        , self.searchDfs(x-1, y+1, passed+1, 'rt_diagonal', retVal))
                        
        #Possible ex5 : if initial point stays at center
        elif 3 <= x and x < len(self.fileNum)-3 and 3 <= y and y < len(self.fileNum[x])-3:
            retVal = max(self.searchDfs(x, y+1, passed+1, 'right', retVal), self.searchDfs(x+1, y+1, passed+1, 'rd_diagonal', retVal)
                        , self.searchDfs(x+1, y, passed+1, 'down', retVal), self.searchDfs(x-1, y, passed+1, 'top', retVal)
                        , self.searchDfs(x-1, y+1, passed+1, 'rt_diagonal', retVal), self.searchDfs(x-1, y-1, passed+1, 'lt_diagonal', retVal)
                        , self.searchDfs(x, y-1, passed+1, 'left', retVal), self.searchDfs(x+1, y-1, passed+1, 'ld_diagonal', retVal))
                        
        #Possible ex6 : if initial point stays at right - bar side
        elif 3 <= x and x < len(self.fileNum)-3 and y >= len(self.fileNum[x])-3:
            retVal = max(self.searchDfs(x+1, y, passed+1, 'down', retVal), self.searchDfs(x-1, y, passed+1, 'top', retVal)
                        , self.searchDfs(x-1, y-1, passed+1, 'lt_diagonal', retVal), self.searchDfs(x, y-1, passed+1, 'left', retVal)
                        , self.searchDfs(x+1, y-1, passed+1, 'ld_diagonal', retVal))
        
        #Possible ex7 : if initial point stays at left - bottom side
        elif x >= len(self.fileNum)-3 and y < 3:
            retVal = max(self.searchDfs(x, y+1, passed+1, 'right', retVal), self.searchDfs(x-1, y, passed+1, 'top', retVal)
                        , self.searchDfs(x-1, y+1, passed+1, 'rt_diagonal', retVal))
                        
        #Possible ex8 : if initial point stays at center - bottom side
        elif x >= len(self.fileNum)-3 and 3 <= y and y < len(self.fileNum[x])-3:
            retVal = max(self.searchDfs(x, y+1, passed+1, 'right', retVal),  self.searchDfs(x-1, y, passed+1, 'top', retVal)
                        , self.searchDfs(x-1, y+1, passed+1, 'rt_diagonal', retVal), self.searchDfs(x-1, y-1, passed+1, 'lt_diagonal', retVal)
                        , self.searchDfs(x, y-1, passed+1, 'left', retVal))
            
        #Possible ex9 : if initial point stays at right - bottom side
        else:
            retVal =  max(self.searchDfs(x-1, y, passed+1, 'top', retVal), self.searchDfs(x-1, y-1, passed+1, 'lt_diagonal', retVal)
                        , self.searchDfs(x, y-1, passed+1, 'left', retVal))
        
        return retVal
        
    def searchDfs(self, x, y, passing, way, retv):
        
        #check how many injacent i've been through
        #Return previous if I've been through maximum 4 steps
        passed = passing
        
        if passed > 4:
            return retv
        else:
             retVal = retv * self.fileNum[x][y]
            
        #Possible way1 : left
        if way == 'left':
            retVal = self.searchDfs(x, y-1, passed+1, 'left', retVal)
        
        #Possible way2 : left top diagonal
        elif way == 'lt_diagonal':
            retVal = self.searchDfs(x-1, y-1, passed+1, 'lt_diagonal', retVal)
        
        #Possible way3 : top
        elif way == 'top':
            retVal = self.searchDfs(x-1, y, passed+1, 'top', retVal)
        
        #Possible way4 : right top diagonal
        elif way == 'rt_diagonal':
            retVal = self.searchDfs(x-1, y+1, passed+1, 'rt_diagonal', retVal)
        
        #Possible way5 : right
        elif way == 'right':
            retVal = self.searchDfs(x, y+1, passed+1, 'right', retVal)
            
        #Possible way6 : right bottom diagonal
        elif way == 'rd_diagonal':
            retVal = self.searchDfs(x+1, y+1, passed+1, 'rd_diagonal', retVal)
            
        #Possible way7 : bottom
        elif way == 'down':
            retVal = self.searchDfs(x+1, y, passed+1, 'down', retVal)
        
        #Possible way8 : left bottom diagonal
        else:
            retVal = self.searchDfs(x+1, y-1, passed+1, 'ld_diagonal', retVal)
            
        
        return retVal
        
    
    
ques11 = number11("Q11numbers.txt")
#for i in range(len(ques11.fileNum)):
#    print(ques11.fileNum[i])

Q11results = [0]

for i in range(len(ques11.fileNum)):
    for j in range(len(ques11.fileNum[i])):
        Q11results.append(ques11.initialDfs(i,j))
        Q11results.sort()
        del Q11results[0]
        
print(Q11results.pop())


grid = [[0]*23]*3 + [[int(x) for x in line.split()]+[0,0,0] for line in
'''08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'''.split('\n')
] + [[0]*23]*3

#print(grid)
import operator

for n in (0,1,2,3):
    for d in ((0,1),(1,0),(1,1),(-1,1)):
        print(grid[n*d[0]][n*d[1]], 'row : ', n*d[0], 'col : ', n*d[1])

print([[grid[n*d[0]][n*d[1]] for n in (0,1,2,3)]
        #for x in range(0,20) for y in range(3,23)
       for d in ((0,1),(1,0),(1,1),(-1,1))])
       
       
print(grid[-1][1])
print max([reduce(operator.mul, [grid[y+n*d[0]][x+n*d[1]] for n in (0,1,2,3)])
        for x in xrange(0,20) for y in xrange(3,23)
        for d in ((0,1),(1,0),(1,1),(-1,1))])
        
        
#grid[0*0][0*1] grid[0*1][0*0] grid[0*1][0*1] grid[0*-1][0*1] 1 --> grid[0][0] grid[0][0] grid[0][0] grid[0][0] 0 0 0 0
#grid[1*0][1*1] grid[1*1][1*0] grid[1*1][1*1] grid[1*-1][1*1] 2 --> grid[0][1] grid[1][0] grid[1][1] grid[-1][1] 0 0 0 0
#grid[2*0][2*1] grid[2*1][2*0] grid[2*1][2*1] grid[2*-1][2*1] 3 --> grid[0][2] grid[2][0] grid[2][2] grid[-2][2] 0 0 0 0
#grid[3*0][3*1] grid[3*1][3*0] grid[3*1][3*1] grid[3*-1][3*1] 4 --> grid[0][3] grid[3][0] grid[3][3] grid[-3][3] 0 8 97 0