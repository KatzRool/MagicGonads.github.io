def maximise(m=2000,b='௵Ỏ',l=['̿','̳'],e='ௌ'):
    n = int(m/len(''.join(l)))-len(b+e)
    for i in l:
        b += i*n
    return b+e
