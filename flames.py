boy = input("If you want to know about your relationship \nThen enter YOUR NAME : ").lower()
girl = input("enter your PARTNER NAME : ").lower()
p = list("".join(boy.split(' ')))
q = list("".join(girl.split(' ')))
r = ['f','l','a','m','e','s']
z = len(p) + len(q)
for a in range(0,len(p)):
    for b in range(0,len(q)):
        if p[a] == q[b]:
            z -= 2
            q[b] = 'x'
            break
        
i = 6
if z >= 1:
    for j in range(0,5):
        x = []
        if z % i == 0:
            r.pop(i-1)
        else:
            if z%i-1 != 0:
                for k in range(z%i,len(r)):
                    x.append(r[k])
                for l in range(0,z%i-1):
                    x.append(r[l])
                r = x
            else:
                r.pop((z%i-1))
        i -= 1
    h = {
            "f":"may be you are the BEST FRIENDS in the world",
            "l":"may be you are LOVERS forever and ever",
            "a":"may be your AFFECTION is precious",
            "m":"may be your MARRIAGE was fixed in the heaven",
            "e":"may be you are ENEMIES",
            "s":"may be she is your one and only SISTER"
        }
    print(h[r[0]])
    f = open('flames.txt','a')
    f.write("%s\t--->%s\t--->%s\n" %(boy,girl,h[r[0]]))
    f.close()
else:
    print("You love yourself, you fool  !!")
    f = open('flames.txt','a')
    f.write("%s\t--->%s\t--->You love yourself you fool!!\n" %(boy,girl))
    f.close()
