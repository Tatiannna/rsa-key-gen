from random import *

def getRandomInt():
    #generates pseudorandom integer by taking least significant bit of random number(1,1000000)
    string = ''
    for i in range(25):
        string += '0'
    string += '1'
    for i in range(5):
        num = randint(1,1000000)
        print (str(num) + " mod 2 = " + str(num%2))
        string += str(num % 2)
    string += '1'
    
    print(string) 
    print(int(string, 2))
    return int(string, 2)


def testPrimality(n):
    # tests if random number is prime. 
    count = 0
    arr = []
    while count < 20:
        a = 0
        # to ensure a !=0
        while a == 0:
            a = randint(1, 1000000) % n
        #to ensure this value of a has not been checked already. Each value must be UNIQUE
        if a > 0 and a not in arr:
            print ("\na = " + str(a))
            arr.append(a)
            count += 1
            if fastExp(a,n-1,n) != 1:
                print ( str(a) + '^' +str(n-1) + '(mod' + str(n) + ") != 1")
                print ( "\n" + str(n) + " is not prime. Fails primality test when a = " + str(a) +"\n\n")
                return 0
    #if we have found 20 values of a that pass primality test, return the prime number
    if count == 20:
        print( str(n) + " is possibly prime")
        print("------------------------------")
        return n
            
def fastExp( a, x, n):
    string = (bin(x)[2:])
    print ("Binary exponent: " + string + "\n")
    ans = a
    temp = ans
    
    print ( string[0] + "        1        " + str(a))
    
    for char in string[1:]:
        mult = 1 #for display purposes only. new variable has to be created to keep track of values in columns
        ans = (ans**2) % n
        
        if char == "1":
            mult = a 
            ans = (ans * a) % n
        print (char + "   " + str(temp) + "^2(mod" + str(n) + ")   " + str(ans) + " x " + str(mult))
        temp = ans
    return ans

def euclid(a, b):
    high = max(a,b)
    low = min(a,b)
    remainder = high % low
    i = 0

    #variables for extended euclidean are kept in arrays so that s[i-2] can be referenced
    qi = []
    si = [1,0]
    ti = [0,1]
 
    
    if remainder > 0:
        while remainder != 0:
            i +=1
            temp = remainder
            mult = high / low
            #for extended, need to keep track of previous mults(qi), and also si and ti
            qi.append(mult)

            #EXTENDED
            if i >= 2:
                si.append(si[len(si)-2] - qi[len(qi)-2] * si[len(si)-1])
                ti.append(ti[len(ti)-2] - qi[len(qi)-2] * ti[len(ti)-1])
            remainder = high - (mult * low)
            print(str(high) + " = " + str(mult) + " x " + str(low) + " + " + str(remainder) + "  ......s[i]: " + str(si[i-1]) + "  t[i]: " + str(ti[i-1]))
            high = low
            low = remainder
        print ("s(n): " + str(si[len(si)-1]) + "   t(n): " + str(ti[len(ti)-1]))
        #return the remainder and the last value of ti 
        return (temp, ti[len(ti)-1])
    else:
        print ( str(high) + " = " + str(low) + " x " + str(high/low) + " + 0 ")
        return (low, 0)
    
def eFinder(phi):
    e = 3
    
    #use fast euclidean to get the gcd and ti
    gcd, ti = euclid(e, phi)
    while gcd != 1:
        print("gcd of e = " + str(e) + " and " + str(phi) + " is not 1\n")
        e += 1
        gcd, ti = euclid(e, phi) 
    return (e, ti)

    
def display(string):
    newString = ''

    while len(string)  + len(newString) < 32:
        newString += '0'
    return newString + string

def main():
    p = 0
    q = 0
    
    print("---------------------------------------------------------------------------------------------------")
    print("---------------------------------------------------------------------------------------------------")
    print("---------------------------------------------------------------------------------------------------")
    while p == 0:
        num = getRandomInt()
        p = testPrimality(num)
    while q == 0 or q == p:
        num = getRandomInt()
        q = testPrimality(num)
        
    print("p and q are: " + str(p) + ", " + str(q))
    n = p*q
    print("n = p x q = " + str(p) + " x " + str(q) + " = " + str(n) + "\n")
    
    phi = (p-1) * (q -1)
    print ("(p-1)(q-1)= " + str(phi) + "\n\nCalculating e: \n")
    e, ti = eFinder(phi)

    #normalize d if negative
    if ti < 0:
        d = ti + n
    else:
        d = ti
    print ('e = ' + str(e) + "   d = " + str(d))
    
    #print("p: " + bin(p)[2:])
    #print("q: " + bin(q)[2:])
    #print("n: " + bin(n)[2:])
    #print("e: " + bin(e)[2:])
    #print("d: " + bin(d)[2:])

    print("\np: " +display(bin(p)[2:]))
    print("q: " +display(bin(q)[2:]))
    print("n: " +display(bin(n)[2:]))
    print("e: " +display(bin(e)[2:]))
    print("d: " +display(bin(d)[2:]))   
main()