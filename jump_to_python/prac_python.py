##Selection Sort Algorithm

def s_sort(a):
    n = len(a)
    for i in range(0,n-1):
        for j in range(i+1, n):
            if a[j] < a[i]:
                #min_idx = j
                a[i], a[j] = a[j], a[i]
                
selectionTest = [2,65,7,5,1,7,845,0,90,86]
s_sort(selectionTest)
print('selection sorted list : ' , selectionTest)



##Insert sort

def i_sort(list1):
    changeVal = 0;
    for i in range(0,len(list1)-1):
        for j in range(i+1, len(list1)):
            if list1[j] < list1[i]:
                changeVal = list1[j]
                list1.remove(changeVal)
                list1.insert(i,changeVal)
            #print(insertionTest)

insertionTest = [2,65,7,5,1,7,845,0,90,86]
i_sort(insertionTest)
print('insertion sort : ', insertionTest)



##Merge sort

def m_sort(list1):
    if len(list1) <= 1:
        return list1
    
    m = len(list1) // 2
    formerHalf = m_sort(list1[:m])
    latterHalf = m_sort(list1[m:])
    
    i=0
    while formerHalf or latterHalf:
        if len(formerHalf) == 0:
            list1[i] = latterHalf.pop(0)
        elif len(latterHalf) == 0:
            list1[i] = formerHalf.pop(0)
        else:
            if formerHalf[0] >= latterHalf[0]:
                list1[i] = latterHalf.pop(0)
            else:
                list1[i] = formerHalf.pop(0)
        i += 1
        if len(formerHalf) == 0 and len(latterHalf) == 0:
            #print(result)
            return list1
            
mergeTest = [2,65,7,5,1,7,845,0,90,86]
print('merge sort : ',m_sort(mergeTest))


##Quick sort
def q_sort(a):
    if len(a) <= 1:
        return a
    q_sort_sub(a, 0, len(a)-1)
    return a
    
def q_sort_sub(a, start, end):
    if end-start <= 0:
        return
    
    i = start
    pivot = a[end]
    
    for j in range(start, end):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
        #print(a, i ,j, a[j])
    a[i], a[end] = a[end], a[i]
    q_sort_sub(a, 0, i-1)
    q_sort_sub(a, i+1, end)
    
QuickTest = [1000,960,7,5,1,7,55,0,84,86]
print('quick sort : ', q_sort(QuickTest))


##Binary search
def b_search(mylist, f_val):
    q_sort(mylist)
    
    result = b_search_sub(mylist, 0, len(mylist)-1, f_val)
    return result
    
    
def b_search_sub(mylist, start, end, f_val):
    f_pos = (start+end) // 2
    while end-start >= 0 and mylist[f_pos] != f_val:
        f_pos = (start+end) // 2
        if mylist[f_pos] > f_val:
            end = f_pos - 1
        elif mylist[f_pos] < f_val:
            start = f_pos + 1
    
    if mylist[f_pos] == f_val:
        result = f_pos
    else:
        result = -1
        
    return result
    
searchTest = [1000,960,7,5,1,7,55,0,84,86]
print('location of 84 : ', b_search(searchTest, 84))


##Easy way of Binary search

def b_search2(mylist, f_val):
    q_sort(mylist)
    start = 0
    end = len(mylist)-1
    
    f_idx = -1
    
    while end >= start:
        f_idx = (start + end) // 2
        if mylist[f_idx] > f_val:
            end = f_idx - 1
        elif mylist[f_idx] < f_val:
            start = f_idx + 1
        else:
            return f_idx
    return f_idx
    
searchTest2 = [1000,960,7,5,1,7,55,0,84,86]
print('location of 84 : ', b_search(searchTest2, 84))


##Check palindrome

def checkPal(string):
    stack_array = []
    queue_array = []
    
    for i in string:
        if i.isalpha():
            stack_array.append(i.lower())
            queue_array.append(i.lower())
    i=0
    result = None
    while i < len(stack_array):
        if stack_array.pop() != queue_array.pop(0):
            return "This is not palindrome!"
        else:
            result = "This is palindrome!"
            i += 1
    return result
    
print(checkPal('Wow'))
print(checkPal('Madam, I''m Adam.'))
print(checkPal('Madam I am Adam.'))


##Looking for same named people with dic

def find_same_name(name_list):
    name_dict = {}
    
    for name in name_list:
        if name in name_dict:
            name_dict[name] += 1
        else:
            name_dict[name] = 1
    result = set()
    for name in name_dict:
        if name_dict[name] >= 2:
            result.add(name)
    return result

name = ['Tom', 'Jerry', 'Mike', 'Tom'] 
print(find_same_name(name))

name2 = ['Tom', 'Jerry', 'Mike', 'Tom', 'Mike']
print(find_same_name(name2))

print("------------------")
##Graph data structure

fr_info = {
    'Summer': ['John', 'Justin', 'Mike'],
    'John': ['Summer', 'Justin'],
    'Justin': ['John', 'Summer', 'Mike', 'May'],
    'Mike': ['Summer', 'Justin'],
    'May': ['Justin', 'Kim'],
    'Kim': ['May'],
    'Tom': ['Jerry'],
    'Jerry': ['Tom']
}

#Try to find every friends including myself

def every_fr(info, me):

    qu = []
    done = set()
    qu.append(me)
    done.add(me)
    
    while qu:
        for fr in qu:
            for friend in info[fr]:
                if friend in done:
                    if fr in qu:
                        qu.remove(fr)
                    else:
                        pass
                else:
                    qu.append(friend)
                    done.add(friend)
                    if fr in qu:
                        qu.remove(fr)
    return done


print(every_fr(fr_info, 'Summer'))

#Easier way with f_level

def every_fr2(info, start):
    qu = []
    done = set()
    
    qu.append((start, 0))
    done.add(start)
        
    while qu:
        (p, d) = qu.pop(0)
        print(p,d)
        for friend in info[p]:
            if friend not in done:
                qu.append((friend, d+1))
                done.add(friend)
            
every_fr2(fr_info, 'Summer')


##Maze Solve Problem
print("Let's solve maze!")

maze = {
    'a': ['e'],
    'b': ['c', 'f'],
    'c': ['b', 'd'],
    'd': ['c'],
    'e': ['a', 'i'],
    'f': ['b', 'g', 'j'],
    'g': ['f', 'h'],
    'h': ['g', 'l'],
    'i': ['e', 'm'],
    'j': ['f', 'k', 'n'],
    'k': ['j', 'o'],
    'l': ['h', 'p'],
    'm': ['i', 'n'],
    'n': ['m', 'j'],
    'o': ['k'],
    'p': ['l']
}

#print ', '.join(maze['a'])

def maze_solve(maze, start, end):
    qu = []
    done = set()
    
    qu.append(start)
    done.add(start)
    while qu:
        print(qu)
        p = qu.pop(0)
        v = p[-1]
        if v == end:
            return p
        for x in maze[v]:
            if x not in done:
                qu.append(p+x)
                done.add(x)
    return "?"
        
print(maze_solve(maze, 'a', 'p'))


##looking for fake coin algorithm
def weigh(a, b, c, d):
  fake = 29
  
  if a <= fake and fake <= b:
    return -1
  elif c <= fake and fake <= d:
    return 1
  return 0


def find_fake(left, right):
  if left == right:
    return left
  half = (right-left + 1) // 2
  				
  g1_left = left
  g1_right = left + half -1 
  g2_left = left + half
  g2_right = g2_left + half - 1

  result = weigh(g1_left, g1_right, g2_left, g2_right)
  if result == -1:
    find_fake(g1_left, g1_right)
  elif result == 1:
    find_fake(g2_left, g2_right)
  return right


import operator
##Stock value 
stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]

import copy
def max_revenue(a):
    prices = copy.deepcopy(a)
    maxVal = 0
    while prices:
        buy = prices.pop(0)
        for i in prices:

            maxVal = max(i-buy, maxVal)
            #Max function should have comparable value. If I only give list as an argument for the function
            #That can make result but could not insert it into a value
    return maxVal
print(max_revenue(stock))

## Get max revenue with less repeating
def max_revenue_revised(prices):
    max_profit = 0
    min_price = prices[0]
    
    n = len(prices)
    for i in range(1, n-1):
        profit = prices[i] - min_price
        if profit > max_profit:
            max_profit = profit
        if prices[i] < min_price:
            min_price = prices[i]
    return max_profit
        
print(max_revenue_revised(stock))






