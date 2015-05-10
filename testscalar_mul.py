from vec import *

zero = Vec({'x','y','z','w'}, {})
u = Vec({'x','y','z','w'},{'x':1,'y':2,'z':3,'w':4})
assert 0*u == zero

assert 1*u == u

assert 0.5*u == Vec({'x','y','z','w'},{'x':0.5,'y':1,'z':1.5,'w':2})

assert u == Vec({'x','y','z','w'},{'x':1,'y':2,'z':3,'w':4})
