import itertools


st = 'kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm'
n = 10
# st = 'aba'
# n = 10

def repeatedString(s, n):

    if len(s) == 1 and s == 'a':
        return n

    c = s.count('a')
    i = c * (n//len(s))
    i += s[:n % len(s)].count('a')

    return i




if __name__ == '__main__':
    print(repeatedString(st, n))