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

alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

for x in range(int(MatrixSize)):
    
    flags=[]
    for i in range(26):
        flags.append(0)

    EquationLines.append(f.readline())
    #print(EquationLines[x])

    for k in range(26):
        if (alphabet[k] in EquationLines[x])==0:
            flags[k]=1

    i=poly(EquationLines[x])
    Temp=i.coeffs()
        
    for j in range(26):
        if flags[j]:
            Temp.insert(j,0)
    if (len(Temp)<(26)):
        Temp.append(0)
    coefficientList.append(Temp)
InitialPointList=f.readline()
f.close()

indicestopop=[]
for u in range(27):
    zeroflags=[]
    for x in range(int(MatrixSize)):
        zeroflags.append(0)
    for y in range(int(MatrixSize)):
        if coefficientList[y][u]==0:
            zeroflags[y]=1
        else: break
    zeroflags.insert(0,1)
    if all(elem == zeroflags[0] for elem in zeroflags):
        indicestopop.append(u)


newCoefficentList=[[] for i in range(int(MatrixSize))]

for i in range(int(MatrixSize)):
    for x in range(27):
        if (x in indicestopop)==0:
            newCoefficentList[i].append(coefficientList[i][x])

           
print(int(MatrixSize))
print(Method)
for j in newCoefficentList:    
    print(j)
print (InitialPointList)


