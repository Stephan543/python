
import itertools
    
# def getPermutations(s):
#     perms = itertools.permutations(s)
#     unique_perms = {''.join(p) for p in perms}
#     return unique_perms

    
def checkPermutation(s1: str, s2: str):
    
    # permSet = getPermutations(s1)
        
    # left,right = 0, len(s1)-1
    
    # while right <= len(s2)-1:
    #     window = s2[left:right+1]
        
    #     if window in permSet:
    #         return True
    #     else:
    #         left +=1
    #         right +=1
    
    # return False
    
    
        m = {}
        s1List = []
        for c in s1:
            m[c] = 0
            s1List.append(c)
        
        
        left,right = 0, len(s1)-1
        
        while right <= len(s2)-1:        
            hits = []
            for c in s2[left:right+1]:
                if c in m:
                    hits.append(c)
                    if hits == s1List:
                        return True
                else:
                    left +=1
                    right +=1
            
        return False






# print(getPermutations("ab"))

print(checkPermutation("aba", "xay3aba"))