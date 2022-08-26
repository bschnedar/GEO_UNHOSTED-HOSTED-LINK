#Brandon Schnedar
#25821724
# 11/15/2018
##This Program

#imports
import sys
import math
#FUNCTIONS??
__NUM_INTER = 0

def _SEG(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0]*p2[1] - p2[0]*p1[1])

    return A, B, -C 

def _INTER(L1, L2,p1,p2,p3,p4):
    D  = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        if(x > max(p1[0],p2[0],p3[0],p4[0] ) or y > max(p1[1],p2[1],p3[1],p4[1] ) or x < min(p1[0],p2[0],p3[0],p4[0] ) or y < min(p1[1],p2[1],p3[1],p4[1])):
            return False
        else:
            global __NUM_INTER
            __NUM_INTER =  __NUM_INTER +1
            return x,y
    else:
        return False
    

def _AAA(a,b):
    return (180 - a - b)

def _SSS(a, b, c):
    try:
        ret = (math.degrees(math.acos((c**2 - b**2 - a**2)/(-2.0 * a * b))))
        return ret
    except:
        print("invalid triangle")
        return 0 
         

#------VARIABLES------#
int_num = 0;
    
#Triangle A
sa1 = None#Sides
sa2 = None
sa3 = None

aa1 = None #Angles
aa2 = None
aa3 = None

aa = None #Area

x1a = None #Cordinates
y1a = None

x2a = None
y2a = None

x3a = None
y3a = None

#Triangle B
sb1 = None #Sides
sb2 = None 
sb3 = None

ab1 = None #Angles
ab2 = None
ab3 = None

ab = None #Area

x1b = None #Cordinates
y1b = None

x2b = None
y2b = None

x3b = None
y3b = None
#------END VARIABLES-------#

#------VAR INPUT-----#
print("If the information is missing leave blank")
### Triangle A ###
#Coordinates 
try:
    x1a = float(input("X1 Triangle A"))  ##replace with et input from webinterface
except (SyntaxError, ValueError):
    print("need to fill value")
try:
    y1a = float(input("y1 for Triangle A"))  ##replace with et input from webinterface
except (SyntaxError, ValueError):
    print("need to fill value")
try:
    x2a = float(input("X2 Triangle A"))  ##replace with et input from webinterface
except (SyntaxError, ValueError):
    print("need to fill value")
try:
    y2a = float(input("y2 for Triangle A"))  ##replace with et input from webinterface
except (SyntaxError, ValueError):
    print("need to fill value")
try:
    x3a = float(input("X3 Triangle A"))  ##replace with et input from webinterface
except (SyntaxError, ValueError):
   print("need to fill value")
try:
    y3a = float(input("y3 for Triangle A"))  ##replace with et input from webinterface
except (SyntaxError, ValueError):
    print("need to fill value")
### Triangle B ###
#Coordinates 
try:
    x1b = float(input("X1 Triangle B"))  ##replace with et input from webinterface
except (SyntaxError, ValueError):
    print("need to fill value")
try:
    y1b = float(input("y1 for Triangle B"))  ##replace with et input from webinterface
except (SyntaxError, ValueError):
    print("need to fill value")
try:
    x2b = float(input("X2 Triangle B"))  ##replace with et input from webinterface
except (SyntaxError, ValueError):
    print("need to fill value")
try:
    y2b = float(input("y2 for Triangle B"))  ##replace with et input from webinterface
except (SyntaxError, ValueError):
    print("need to fill value")
try:
    x3b = float(input("X3 Triangle B"))  ##replace with et input from webinterface
except (SyntaxError, ValueError):
   print("need to fill value")
try:
    y3b = float(input("y3 for Triangle B"))  ##replace with et input from webinterface
except (SyntaxError, ValueError):
    print("need to fill value")
#-----END OF VAR INPUT-----#
#Solve Regular Triangle :)
#Triangle 1
#Make Sides

sa1 = ((x2a - x1a)**2 + (y2a - y1a)**2)**0.5
sa2 = ((x3a - x2a)**2 + (y3a - y2a)**2)**0.5
sa3 = ((x1a - x3a)**2 + (y1a - y3a)**2)**0.5
print(sa1)
print(sa2)
print(sa3)
aa1 = _SSS(sa1,sa2,sa3)
aa2 = _SSS(sa2,sa3,sa1)
aa3 = _SSS(sa3,sa1,sa2)

print(aa1)
print(aa2)
print(aa3)

VS = 0.5 * (sa1 + sa2 + sa3)
aa = (VS*(VS-sa1) * (VS-sa2)*(VS-sa3))**0.5
print(aa)

#Triangle two
#Make Sides
sb1 = ((x2b - x1b)**2 + (y2b - y1b)**2)**0.5
sb2 = ((x3b - x2b)**2 + (y3b - y2b)**2)**0.5
sb3 = ((x1b - x3b)**2 + (y1b - y3b)**2)**0.5
print(sb1)
print(sb2)
print(sb3)
ab1 = _SSS(sb1,sb2,sb3)
ab2 = _SSS(sb2,sb3,sb1)
ab3 = _SSS(sb3,sb1,sb2)

print(ab1)
print(ab2)
print(ab3)

VS = 0.5 * (sb1 + sb2 + sb3)
ab = (VS*(VS-sb1) * (VS-sb2)*(VS-sb3))**0.5
print(ab)
#PLOT BOTH TRIANGLES



#-----GET INTERSECTION POINTS-----#
#sb1 and sb2
PA = [x1a,y1a]
PB = [x2a,y2a]
PC = [x3a,y3a]

P1 = [x1b,y1b]
P2 = [x2b,y2b]
P3 = [x3b,y3b]

lineA = _SEG(PA,PB)
lineB = _SEG(PB,PC)
lineC = _SEG(PC,PA)

line1 = _SEG(P1,P2)
line2 = _SEG(P2,P3)
line3 = _SEG(P3,P1)

inter_a1 = _INTER(line1, lineA,P1,P2,PA,PB)
inter_a2 = _INTER(line2, lineA,P2,P3,PA,PB)
inter_a3 = _INTER(line3, lineA,P3,P1,PA,PB)

inter_b1 = _INTER(line1, lineB,P1,P2,PB,PC)
inter_b2 = _INTER(line2, lineB,P2,P3,PB,PC)
inter_b3 = _INTER(line3, lineB,P3,P1,PB,PC)

inter_c1 = _INTER(line1, lineC,P1,P2,PC,PA)
inter_c2 = _INTER(line2, lineC,P2,P3,PC,PA)
inter_c3 = _INTER(line3, lineC,P3,P1,PC,PA)


print("\n A")
if(inter_a1 != False):
    print(inter_a1[0], "," , inter_a1[1])
if(inter_a2 != False):
    print(inter_a2[0], "," , inter_a2[1])
if(inter_a3 != False):
    print(inter_a3[0], "," , inter_a3[1])
print("B")
if(inter_b1 != False):
    print(inter_b1[0], "," , inter_b1[1])
if(inter_b2 != False):
    print(inter_b2[0], "," , inter_b2[1])
if(inter_b3 != False):
    print(inter_b3[0], "," , inter_b3[1])
print("C")
if(inter_c1 != False):
    print(inter_c1[0], "," , inter_c1[1])
if(inter_c2 != False):
    print(inter_c2[0], "," , inter_c2[1])
if(inter_c3 != False):
    print(inter_c3[0], "," , inter_c3[1])

ARR_INTER = [inter_a1,inter_a2,inter_a3,inter_b1, inter_b2, inter_b3,inter_c1,inter_c2,inter_c3]
ARR_INTER = list(set(ARR_INTER))
ARR_INTER.remove(False)
print(ARR_INTER)


print("\n /n")
if(len(ARR_INTER) != 5):
    print("invalid inputs")
    sys.exit()


#if a interection is equal to a plotted point then it is the unique point. From here we can determine the rest of the triangle calculations. 
if(inter_a1 == PA):

elif(inter_a1 == PB):

elif(inter_a1 == PC):

elif(inter_a1 == P1):
    if(inter_a1 == inter_a2):  ##inter c1 == false
        #triangles
        #p1, pb, inter_b1
        #P2,inter_b1, inter_b3  *****sub from p1, p2, p3 for area of middle shape
        #inter_b3 inter_c3 PCl
        #inter_c3, P3,inter_c2*******
        #PA, inter_2a, inter_c2
    elif(inter_a1 == inter_a3):
       
    else:
        print("error 16")
        
elif(inter_a1 == P2):

elif(inter_a1 == P3):




"""    
##a1  A and 1
if(inter_a1 != False and (inter_a1 == inter_a2 or inter_a1 == inter_a3)):  #inter a is the singler intersection
    print(inter_a1)
    print("new triagle",inter_a1,PA
elif(inter_a1 != False and (inter_a1 != inter_a2 and inter_a1 != inter_a3) ): # inter a is one point of a new triangle
    print("unique point")
    print(inter_a1)
    
##a2  A and 2
if(inter_a2 != False and (inter_a1 == inter_a2 or inter_a2 == inter_a3)):  #inter a is the singler intersection
    print("your singel is this:")
    print(inter_a2)
elif(inter_a2 != False and (inter_a1 != inter_a2 and inter_a2 != inter_a3) ): # inter a is one point of a new triangle
    print("unique point")
    print(inter_a2)

##a3  A and 3
if(inter_a3 != False and (inter_a3 == inter_a2 or inter_a1 == inter_a3)):  #inter a is the singler intersection
    print("your singel is this:")
    print(inter_a3)
elif(inter_a3 != False and (inter_a3 != inter_a2 and inter_a1 != inter_a3) ): # inter a is one point of a new triangle
    print("unique point")
    print(inter_a3)
    
    
   

    
    

##USE 5 intersection points to get SAS of all the new sides and angles.

##Use new intersections and angles to get Areas

##Graph new monstrocity and call python code from jsp




#-----GET MISSING VALUES-----#

 







