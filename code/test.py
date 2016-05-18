
"""Test to verify that even-ness of an odd base number can be calculated by
checking if there is even number of odd digits."""

def toStr(n,base):
    print("n", n)
    convertString = "0123456789ABCDEF"
    if n < base:
       return convertString[n]
    else:
       return toStr(n//base,base) + convertString[n%base]

print(toStr(10,3))

def test_odd_base():
    for base in (3,5,7,9,13,15):
        for x in range(30000):
            ev = x%2==0
            num = toStr(x, base)
            total = 0
            for d in [1,3,5,7,9,'B','D']:
                total += num.count(str(d))
            ev2 = total%2==0
            assert ev and ev2 or not (ev or ev2)
        print ("base %s Test passed.." % base)
# test_odd_base()
