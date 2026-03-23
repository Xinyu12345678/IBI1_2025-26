a=5.08
b=5.33
c=5.55
d=b-a
e=c-b
if d>e:
    print("decelerating")
elif d<e:
    print("celerating")#d is larger. decelerating.
X=True
Y=False
W=X or Y
print(W)
#X     Y     W
#True True True
#True False True
#False True True 
#False False False