

def pmaxOnLine(p1, p2, pmax):
     x1, y1 = p1
     x2, y2 = p2
     x3, y3 = pmax
     dx, dy = x2-x1, y2-y1
     det = dx*dx + dy*dy
     a = (dy*(y3-y1)+dx*(x3-x1))/det
     return x1+a*dx, y1+a*dy

def isPmaxAboveLine(p1, p2, pmax):
    checker = (p1[0] * p2[1]) + (pmax[0] * p1[1]) + (p2[0] * pmax[1]) - (pmax[0] * p2[1]) - (p2[0] * p1[1]) - (p1[0] * pmax[1])
    return checker>0
    onLine = pmaxOnLine(p1, p2, pmax)
    print("pmax = ", pmax)
    print("pmax on line = ", onLine)
    return (onLine[1] > pmax[1] or (onLine[1] == pmax[1] and onLine[0] < pmax[1]))