from __future__ import generators

def xcombinations(items, n):
    if n==0: yield []
    else:
        for i in range(len(items)):
            for cc in xcombinations(items[:i]+items[i+1:],n-1):
                yield [items[i]]+cc

def xuniqueCombinations(items, n):
    if n==0: yield []
    else:
        for i in range(len(items)):
            for cc in xuniqueCombinations(items[i+1:],n-1):
                yield [items[i]]+cc
            
def xselections(items, n):
    if n==0: yield []
    else:
        for i in range(len(items)):
            for ss in xselections(items, n-1):
                yield [items[i]]+ss

def xpermutations(items):
    return xcombinations(items, len(items))

def get_perms(hand, n):
    handlist = []
    for key in hand:
        for i in range(hand[key]):
            handlist.append(key)
    l = []  
    toret = []
    for c in xuniqueCombinations(handlist,n):
        l.append(c)
    for j in l:
        for p in xpermutations(j): 
            toret.append("".join(p))
    return toret	

if __name__=="__main__":
    print ("Permutations of 'love'")
    for p in xpermutations(['l','o','v','e']): print (str(''.join(p)))

    print
    print ("Combinations of 2 letters from 'love'")
    for c in xcombinations(['l','o','v','e','h','j'],6 ): print (str(''.join(c)))
     
    print
    print ("Unique Combinations of 2 letters from 'love'")
    for uc in xuniqueCombinations(['l','o','v','e'],2): print (str(''.join(uc)))

    print
    print ("Selections of 2 letters from 'love'")
    for s in xselections(['l','o','v','e'],2): print (str(''.join(s)))
 
    print
    print (str(map(''.join, list(xpermutations('done')))))
    print 
    print ("testing stuff for 6.00")
    print (str(len(get_perms({"a":2, "b":3, "c":1 , "e":1, "f":1}, 5))))
    print (get_perms({"a":2, "b":3, "c":1 , "e":1, "f":1}, 5)) 
