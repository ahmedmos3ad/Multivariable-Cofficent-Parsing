import numpy as np
import sympy as sp
from sympy import Eq, Matrix, poly
from sympy.abc import a, b, c

x,y,z = sp.symbols('x y z')
a,b,c = sp.symbols('a b c')

coefficientList=[]
EquationLines=[]
InitialPointList=[]


f=open("Equations.txt","r")
MatrixSize=f.readline()
Method=f.readline()
for x in range(int(MatrixSize)):
    
    aflag=0
    bflag=0
    cflag=0

    EquationLines.append(f.readline())
    #print(EquationLines[x])
    if ("a" in EquationLines[x]) & ("b" in EquationLines[x]) & ("c" in EquationLines[x]):
        i= poly(EquationLines[x])
        k= i.coeffs()
        if (len(k)<4):
            k.append(0)
        coefficientList.append(k)
    else:
        if ("a" in EquationLines[x])==0:
            aflag=1
        if ("b" in EquationLines[x])==0:
            bflag=1
        if ("c" in EquationLines[x])==0:
            cflag=1
        i=poly(EquationLines[x])
        Temp=i.coeffs()
        if (Temp.count(x)<4):
            if aflag:
                Temp.insert(0,0)
            if bflag:
                Temp.insert(1,0)
            if cflag:
                Temp.insert(2,0)
            if (len(Temp)<4):
                Temp.append(0)
        coefficientList.append(Temp)
InitialPointList=f.readline()
f.close()
print(int(MatrixSize))
print(Method)
for j in coefficientList:    
    print(j)
print (InitialPointList)


