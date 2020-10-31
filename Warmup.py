#Solve Me First
def solveMeFirst(a,b):
	return a + b


num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1,num2)
print(res)


#Simple Array Sum
def simpleArraySum(ar):
    t = 0
    for i in ar:
        t += i
    return t


#Compare The Triplets
def compareTriplets(a, b):
    A = 0
    B = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            A += 1
        elif a[i] < b[i]:
            B += 1
    return A, B


#A Very Big Sum
def aVeryBigSum(ar):
    x = 0
    for i in ar:
        x += i
    return x


#Diagonal Difference
def diagonalDifference(arr):
    ld = 0
    rd = 0

    for i in range(n):
        ld += arr[i][i]
        rd += arr[i][-(i + 1)]

    return abs(ld - rd)


#Plus Minus
def plusMinus(arr):
    pos = 0
    neg = 0
    O = 0

    for i in arr:
        if i < 0:
            neg += 1
        elif i > 0:
            pos += 1
        elif i == 0:
            O += 1

    pos = pos / n
    neg = neg / n
    O = O / n
    print(pos)
    print(neg)
    print(O)


#Staircase
def staircase(n):
    for i in range(n):
        print(('#'*(i+1)).rjust(n,' '), end='\n')


#Mini-Max Sum
def miniMaxSum(arr):
    m = 0
    M = 0

    arr.sort(key = int)
    for i in arr[:-1]:
        m += i
    for i in arr[1:]:
        M += i
    print(m, M)


#Birthday Cake Candles
def birthdayCakeCandles(candles):
    M = max(candles)
    l = 0
    for i in candles:
        if i == M:
            l += 1
    return l


#Time Conversion
def timeConversion(s):
    if s[-2:] == 'AM' and s[:2] != '12':
        return s[:-2]

    elif s[-2:] == 'AM' and s[:2] == '12':
        return '00' + s[2:-2]

    elif s[-2:] == 'PM' and s[:2] != '12':
        return str(int(s[:2]) + 12) + s[2:-2]

    elif s[-2:] == 'PM' and s[:2] == '12':
        return '12' + s[2:-2]