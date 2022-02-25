import numpy
from myConvexHull import myConvexHull 
from myConvexHull import crossProduct
from myConvexHull import angle
list = [[ 5.1 , 3.5 ],
[ 4.9 , 3.0 ],
[ 4.7 , 3.2 ],
[ 4.6 , 3.1 ],
[ 5.0 , 3.6 ],
[ 5.4 , 3.9 ],
[ 4.6 , 3.4 ],
[ 5.0 , 3.4 ],
[ 4.4 , 2.9 ],
[ 4.9 , 3.1 ],
[ 5.4 , 3.7 ],
[ 4.8 , 3.4 ],
[ 4.8 , 3.0 ],
[ 4.3 , 3.0 ],
[ 5.8 , 4.0 ]]
hull = myConvexHull(numpy.array(list))
print("hull.simplices")
print(hull.simplices)
x= angle([ 5.1 , 3.5 ],
[ 4.9 , 3.0 ],
[ 4.7 , 3.2 ])
print(x)
# isPointAbove([4.6, 3.4],[5.8, 4.0],  [2, 3])