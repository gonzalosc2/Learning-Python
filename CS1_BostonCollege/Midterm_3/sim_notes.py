########################################
def hiCount(iterable):
    rtnVal = 0
    most = ''
    for item in iterable:
        num = iterable.count(item)
        if num > rtnVal:
            most = item
            rtnVal = num
    return (most,rtnVal)

lyric = "you don't own me"
print(hiCount(lyric))

########################################
notables = [['DMZ','Adele'],'LvB']
print((notables[1])[0])

########################################
jingle = {1:'money', 2:'show'}
print(jingle[0])

########################################
def property(t):
    tList = t.split()
    d = {}
    for word in tList:
        length = len(word)
        if len(word) not in d:
            d[length] = 1
        else:
            d[length] += 1
    return d

ben = 'Lost time is never found again'
print(len(property(ben)))

########################################
def sub_set(A):
    if A == []: return [A]
    X = sub_set(A[1:])
    result = []
    for L in X:
        result += [L,A[0:1]+L]
    return result

sub_set([1,2])
sub_set([1,2,3])

########################################
