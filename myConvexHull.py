import numpy as np
from numpy.linalg import norm

pointsReference = []

def myConvexHull(nppoints):
    global pointsReference
    pointsReference = nppoints.tolist()
    points = nppoints.tolist()
    sortPoints(points)
    pointsAbove, pointsBelow = divideFirstPoints(points)
    hull = DCConvexHull(pointsAbove, []) + DCConvexHull(pointsBelow, [])
    return formatedOutput(hull)

def pointToOriginalIndex(point):
    return pointsReference.index(point)


def sortPoints(points):
    quickSort(points, 0, len(points) - 1)

def partition(arr, low, high):
    i = (low-1)		        # index of smaller element
    pivot = arr[high]	    # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j][0] < pivot[0] or (arr[j][0] == pivot[0] and arr[j][1] < pivot[1]):

            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)



def DCConvexHull(points,hull):
    if(len(points) == 2):
        return hull +[[pointToOriginalIndex(points[0]), pointToOriginalIndex(points[1])]]
    else:
        setOfPoints1,setOfPoints2 = dividePoints(points)
        return hull + DCConvexHull(setOfPoints1, hull) + DCConvexHull(setOfPoints2, hull)

def findPmaxIndex(points):
    p1 = points[0]
    p2 = points[-1]
    p1= np.array(points[0])
    p2= np.array(points[-1])
    dmax = 0
    dmaxi = 0
    for i in range(0, len(points)):
        p3 = np.array(points[i])
        d = norm(np.cross(p2-p1, p1-p3))/norm(p2-p1)
        if(d == dmax):
            if(angle(p1,p2, p3) > angle(p1, p2, points[dmaxi])):
                dmaxi = i
                dmax = d

        elif(d > dmax):
            dmaxi = i
            dmax = d
    return dmaxi

def angle(p1, p2, p3):
    v1 = (p2[0] - p1[0], p2[1] - p1[1])
    v2 = (p3[0] - p1[0], p3[1] - p1[1])
    unit_vector_1 = v1 / np.linalg.norm(v1)
    unit_vector_2 = v2 / np.linalg.norm(v2)
    dot_product = np.dot(unit_vector_1, unit_vector_2)
    angle = np.arccos(dot_product)
    return angle

def divideFirstPoints(points):
    return divideCustom(points[0],points[-1], points)

def dividePoints(points):
    p1 = points[0]
    p2 = points[-1]
    pmaxIndex = findPmaxIndex(points)
    pmax = points[pmaxIndex]

    pointsWithP1Above, pointsWithP1Below = divideCustom(p1, pmax, points)
    pointsWithP2Above, pointsWithP2Below = divideCustom(pmax, p2, points)
    if(crossProduct(p1, p2, pmax) > 0):
        return pointsWithP1Above, pointsWithP2Above
    else:
        return pointsWithP1Below, pointsWithP2Below

def divideCustom(p1, p2, points):
    pointsAbove = [p1,p2]
    pointsBelow = [p1,p2]
    for point in points:
        if(point != p1 and point != p2):
            checker = crossProduct(p1, p2, point)
            if checker < 0:
                pointsBelow.append(point)
            if checker > 0:
                pointsAbove.append(point)
    sortPoints(pointsAbove)
    sortPoints(pointsBelow)
    return pointsAbove, pointsBelow


def crossProduct(p1, p2, p3):
    v1 = (p2[0] - p1[0], p2[1] - p1[1])
    v2 = (p3[0] - p1[0], p3[1] - p1[1])
    x = np.cross(v1,v2)
    return x

class Hull:
    def __init__(self,simplices):
        self.simplices = simplices

def formatedOutput(hull):
    return Hull(hull)