f=[i for i in range(7)]
prec = 7



def prochain(l) :
    ok=False
    a=[l[0]]
    for i in range(1, len(l)) :
        if i+len(a) < len(l) and l[i:i+len(a)] == a :
            ok=True
            break
        a.append(l[i])
    if ok :
        if l[len(l)-len(a):] == a :
            return a[0]
        for i in range(1, len(a)) :
            if l[len(l)+i-len(a):] == a[:-i] :
                return a[-i]
    #Sinon on a 1,x le motif a avec 1,x < 2
    #On prends un seuil d'acceptation à 4 chiffres
    for i in range(1, len(a)) :
        tmp = a[i:]
        if tmp == a[:len(tmp)] :
            if len(tmp) > 3 :
                return a[len(tmp)]
            else :
                return None
    return None

def guess(f) :
    m=[]
    for k in range(2, prec*len(f)) :
        m.append([i%k for i in f])
        if prochain(m[-1]) == None :
            m.pop()
            break
    proch = [prochain(i) for i in m]
    probable=[]
    for i in range(1, prec*f[-1]) :
        if [i%k for k in range(2, len(m)+2)] == proch :
            probable.append(i)
    return(probable)


def bis(f) :
    return [f[i]-f[i-1] for i in range(1, len(f))]


def solve(f, t) :
    m=[[0 for i in range(len(f))], f]
    for i in range(t) :
        m.append(bis(m[-1]))
    
    final=[]
    for i in range(1, len(m)) :
        final.append([sum([m[k-1][-1] for k in range(1, i+1)])+ii for ii in guess(m[i])])
    
    
    guessFinal = []
    for i in final[0] :
        ok = True
        for k in final :
            if not i in k :
                ok = False
        if ok :
            guessFinal.append(i)
    
    return(guessFinal)


for t in range(len(f)) :
    kappa = len(f)-1-t
    tmp = solve(f, kappa)
    if not tmp == [] :
        print(tmp)
        break
