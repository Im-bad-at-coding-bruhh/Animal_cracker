def palindrome(s):
    ss = s.replace(" ",'')
    return ss == ss[::-1]

palindrome('kkk')