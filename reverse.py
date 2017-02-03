#Write a script for reverting the string in any language

def ReverseS(str):
    str=list(str)
    spl_str=''
    n=len(str)-1
    m=0
    while m<n:
        c = str[m]
        str[m] = str[n]
        str[n] = c
        m=m+1
        n=n-1
    return spl_str.join(str)
    
s=raw_input('Enter a string: ')
s=ReverseS(s)
print(s)
