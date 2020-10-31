#CamelCase
def camelcase(s):
    x = 1
    for i in s:
        if i.isupper():
            x += 1
    return x


#Strong Password
def minimumNumber(n, password):
    n = l = u = s = 1
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    for i in password:
        if i in numbers:
            n = 0
        elif i in lower_case:
            l = 0
        elif i in upper_case:
            u = 0
        elif i in special_characters:
            s = 0

    x = n + l + u + s

    if (len(password) + x) < 6:
        return x + (6 - (len(password) + x))
    else:
        return x


#Caesar Cipher
def caesarCipher(s, k):
    lower_oa = 'abcdefghijklmnopqrstuvwxyz'
    upper_oa = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    l_loa = list(lower_oa)
    u_loa = list(upper_oa)
    lower_na = []
    upper_na = []
    temp = []
    while k > 26:
        k = k - 26

    for i in range(k, len(lower_oa)):
        l_loa.remove(lower_oa[i])
        u_loa.remove(upper_oa[i])
        lower_na.append(lower_oa[i])
        upper_na.append(upper_oa[i])

    for i in l_loa:
        lower_na.append(i)
    for i in u_loa:
        upper_na.append(i)

    for i in s:

        if i in lower_oa:
            temp.append(lower_na[lower_oa.index(i)])
        elif i in upper_oa:
            temp.append(upper_na[upper_oa.index(i)])
        else:
            temp.append(i)

    return ''.join(temp)


#Pangrams
def pangrams(s):
    a = list('abcdefghijklmnopqrstuvwxyz')
    for i in s.lower():
        if i in a:
            a.remove(i)
            print(a)
    if len(a) > 0:
        return 'not pangram'
    else:
        return 'pangram'


#Alternating Characters
def alternatingCharacters(s):
    c = 0
    for i in range(0, len(s) - 1):

        if s[i] == s[i + 1]:
            c += 1

    return c