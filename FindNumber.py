#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from itertools import permutations 

def judge(A,B,C,D,E,F,G,H,I,K):
    num=B+H+D+K+B+C+C+D
    if num%10!=D:
        return False
    num=int(num/10)+K+G+I+H+I+C+E
    if num%10!=E:
        return False
    num=int(num/10)+C+A+D+D+C+D
    if num%10!=G:
        return False
    num=int(num/10)+A+E+K+D+F
    if num%10!=K:
        return False
    num=int(num/10)+D+F+F+A
    if num%10!=K:
        return False
    num=int(num/10)+F+A+E
    if num%10!=D:
        return False
    num=int(num/10)+G+K
    if num%10!=B:
        return False
    return True

if __name__ == '__main__':
    digit=[0,1,2,3,4,5,6,7,8,9]
    perm=permutations(digit)
    flag=False
    count=0
    for i in list(perm):
    #    count+=1
    #    if count%10000==0:
    #        print(count)

        l=list(i)
        if not l[9]>l[1] and not l[6]>l[1]:
            for j in range(len(l)):
                A=l[0]
                B=l[1]
                C=l[2]
                D=l[3]
                E=l[4]
                F=l[5]
                G=l[6]
                H=l[7]
                I=l[8]
                K=l[9]

                if judge(A,B,C,D,E,F,G,H,I,K):
                    print("The number is",A,B,C,D,E,F,G,H,I,K)
                    flag=True
                    break
        if flag:
            break

