#Brandon Schnedar
#25821724
# 11/15/2018
##This Program

#imports
import sys
import math
#FUNCTIONS??
class Howdy:

    
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
        
    def _MINI(GG,HH,JJ):
        s_GH = ((HH[0] - GG[0])**2 + (HH[1] - GG[1])**2)**0.5
        s_HJ = ((JJ[0] - HH[0])**2 + (JJ[1] - HH[1])**2)**0.5
        s_JG = ((GG[0] - JJ[0])**2 + (GG[1] - JJ[1])**2)**0.5

        a_GHJ = _SSS(s_GH,s_HJ,s_JG)
        a_JGH = _SSS(s_JG,s_GH,s_HJ)
        a_HJG = _SSS(s_HJ,s_JG,s_GH)

        VZ = 0.5 * (s_GH + s_HJ + s_JG)
        area_GHJ = (VZ*(VZ-s_GH) * (VZ-s_HJ)*(VZ-s_JG))**0.5

        return (s_GH, s_HJ, s_JG, a_GHJ, a_JGH, a_HJG, area_GHJ)

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
    print("#-----Triangle 1-----#")
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
    print("#-----Triangle 2-----#")
    #Make Sides
    sb1 = ((x2b - x1b)**2 + (y2b - y1b)**2)**0.5
    sb2 = ((x3b - x2b)**2 + (y3b - y2b)**2)**0.5
    sb3 = ((x1b - x3b)**2 + (y1b - y3b)**2)**0.5
    print(sb1)
    print(sb2)
    print(sb3)
    #angles
    ab1 = _SSS(sb1,sb2,sb3)
    ab2 = _SSS(sb2,sb3,sb1)
    ab3 = _SSS(sb3,sb1,sb2)

    print(ab1)
    print(ab2)
    print(ab3)

    #ab is area
    VS = 0.5 * (sb1 + sb2 + sb3)
    ab = (VS*(VS-sb1) * (VS-sb2)*(VS-sb3))**0.5
    print(ab)
    #PLOT BOTH TRIANGLES



    #-----GET INTERSECTION POINTS-----#
    print("#-----GET INTERSECTION POINTS-----#")
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



    ARR_INTER = [inter_a1,inter_a2,inter_a3,inter_b1, inter_b2, inter_b3,inter_c1,inter_c2,inter_c3]
    ARR_INTER = list(set(ARR_INTER))
    ARR_INTER.remove(False)
    print(ARR_INTER)

    #-----END INTERSECTION POINTS-----#



    print("\n")
    if(len(ARR_INTER) != 5):
        print("invalid inputs")
        sys.exit()

    print("#-----MINI TRIANGLES-----#")

    #if a interection is equal to a plotted point then it is the unique point. From here we can determine the rest of the triangle calculations.

    #The intersection lies on 1 and a
    print(PA)
    print(inter_a1)

    if(inter_a1[0] == PA[0] and  inter_a1[1] == PA[1]):##inter c1 == inter_a1
        if(inter_c3 == False):   #JUAN6     
            #P2, inter_a1, inter_c2
                print("#TRIANGLE 1")
                T1 = _MINI(P2,inter_a1,inter_c2)
                print(T1)
            #PC, inter_b2, inter_c2  *1*
                print("#TRIANGLE 2")
                T2 = _MINI(PC,inter_b2,inter_c2)
                print(T2)
            #P3, inter_b2, inter_b3
                print("#TRIANGLE 3")
                T3 = _MINI(P3,inter_b2,inter_b3)
                print(T3)
            #PB, inter_a3, inter_b3  *2*
                print("#TRIANGLE 4")
                T4 = _MINI(PB,inter_a3,inter_b3)
                print(T4)
            #P1, inter_a3, inter_a1
                print("#TRIANGLE 5")
                T5 = _MINI(P1,inter_a3,inter_a1)
                print(T5)
            #Big area = TRI_ABC - *1* - *2*
                BIGAREA =  aa - T2[6] - T4[6]
                print("big area")
                print(BIGAREA)
                
        elif(inter_a3 == False):  #KARL6
            #P2, inter_a1, inter_a2
                print("#TRIANGLE 1")
                T1 = _MINI(P2,inter_a1,inter_a2)
                print(T1)
            #PB,inter_b2,inter_a2 *1*
                print("#TRIANGLE 2")
                T2 = _MINI(PB,inter_b2,inter_a2)
                print(T2)
            #P3, b2, b3
                print("#TRIANGLE 3")
                T3 = _MINI(P3,inter_b2,inter_b3)
                print(T3)
            #pc , b3,c3  *2*
                print("#TRIANGLE 4")
                T4 = _MINI(PC,inter_c3,inter_b3)
                print(T4)
            #p1, c3, 1c
                print("#TRIANGLE 5")
                T5 = _MINI(P1,inter_c3,inter_c1)
                print(T5)

            #Big area = TRI_ABC - *1* - *2*
                BIGAREA =  aa - T2[6] - T4[6]
                print("big area")
                print(BIGAREA)
        else:
            print("JUAN-KARL")
            #return("error 6")
        
    elif(inter_a1 == PB): ##inter_b1 == inter_a1
        if(inter_b3 == False): #SEB12
            #p2, inter_a1,inter_b2
                print("#TRIANGLE 1")
                T1 = _MINI(P2,inter_a1,inter_b2)
                print(T1)
            #pc c2 inter_b2*1*
                print("#TRIANGLE 2")
                T2 = _MINI(PC,inter_c2,inter_b2)
                print(T2)
            #p3 c2 c3
                print("#TRIANGLE 3")
                T3 = _MINI(P3,inter_c2,inter_c3)
                print(T3)
            #pa  c3 3a*2*
                print("#TRIANGLE 4")
                T4 = _MINI(PA,inter_a3,inter_c3)
                print(T4)
            #p1 a3 a1
                print("#TRIANGLE 5")
                T5 = _MINI(P1,inter_a3,inter_a1)
                print(T5)
            #Big area = TRI_ABC - *1* - *2*
                BIGAREA =  aa - T2[6] - T4[6]
                print("big area")
                print(BIGAREA)
                 
        elif(inter_a3 == False): #LARRY12
            #p2 inter_a1, inter_a2
                print("#TRIANGLE 1")
                T1 = _MINI(P2,inter_a1,inter_a2)
                print(T1)
            #pa inter_a2 inter_c2 *1*
                print("#TRIANGLE 2")
                T2 = _MINI(PA,inter_c2,inter_a2)
                print(T2)
            #p3 inter_c2 inter_c3
                print("#TRIANGLE 3")
                T3 = _MINI(P3,inter_c2,inter_c3)
                print(T3)
            #pc inter_b3 inter_c3 *2*
                print("#TRIANGLE 4")
                T4 = _MINI(PC,inter_b3,inter_c3)
                print(T4)
            #p1
                print("#TRIANGLE 5")
                T5 = _MINI(P1,inter_b3,inter_b1)
                print(T5)
            #Big area = TRI_ABC - *1* - *2*
                BIGAREA =  aa - T2[6] - T4[6]
                print("big area")
                print(BIGAREA)
        else:
            print("SEB-LARRY")
            #return("error 12")
    elif(inter_b1 == PC): ##inter_b1 == inter_c1
        if(inter_c3 == False):   #JACK18     
            #P2,inter_b1, inter_c2
                print("#TRIANGLE 1")
                T1 = _MINI(P2,inter_b1 ,inter_c2)
                print(T1)
            #PA,  inter_c2, inter_a2
                print("#TRIANGLE 2")
                T2 = _MINI(PA,inter_a2,inter_c2)
                print(T2)
            #P3, inter_a2 inter_a3
                print("#TRIANGLE 3")
                T3 = _MINI(P3,inter_a2,inter_a3)
                print(T3)
            #PB, inter_a3 inter_b3
                print("#TRIANGLE 4")
                T4 = _MINI(PB,inter_b3,inter_a3)
                print(T4)
            #P1, inter_b1 inter_b3
                print("#TRIANGLE 5")
                T5 = _MINI(P1,inter_b3 ,inter_b1)
                print(T5)
            #Big area = TRI_ABC - *1* - *2*
                BIGAREA =  aa - T2[6] - T4[6]
                print("big area")
                print(BIGAREA)
                
        elif(inter_b3 == False):  #SARA18
            #P2,  inter_b1  inter_b2
                print("#TRIANGLE 1")
                T1 = _MINI(P2,inter_b1,inter_b2)
                print(T1)
            #PB, inter_b2 inter_a2
                print("#TRIANGLE 2")
                T2 = _MINI(PB,inter_a2,inter_b2)
                print(T2)
            #P3,  inter_a2 inter_a3
                print("#TRIANGLE 3")
                T3 = _MINI(P3,inter_a2,inter_a3)
                print(T3)
            #pa , inter_a3 inter_c3
                print("#TRIANGLE 4")
                T4 = _MINI(PA,inter_c3,inter_a3)
                print(T4)
            #p1, inter_c3 inter_c1
                print("#TRIANGLE 5")
                T5 = _MINI(P1,inter_c3,inter_c1)
                print(T5)
            #Big area = TRI_ABC - *1* - *2*
                BIGAREA =  aa - T2[6] - T4[6]
                print("big area")
                print(BIGAREA)
        else:
            print("SARA-JACK")
            #return("error 18")
        
    elif(inter_a1 == P1):
        ####
        if(inter_c1 == False):        
            #Pb a1 b1
                print("#TRIANGLE 1")
                T1 = _MINI(PB,inter_a1,inter_b1)
                print(T1)
            #P2 b2 inter_b1
                print("#TRIANGLE 2")
                T2 = _MINI(P2,inter_b2,inter_b1)
                print(T2)
            #P3, 
                print("#TRIANGLE 3")
                T3 = _MINI(PC,inter_b2,inter_c2)
                print(T3)
            #PB,
                print("#TRIANGLE 4")
                T4 = _MINI(P3,inter_c3,inter_c2)
                print(T4)
            #P1,
                print("#TRIANGLE 5")
                T5 = _MINI(PA,inter_a3,inter_c3)
                print(T5)
            #Big area = TRI_ABC - *1* - *2*
                BIGAREA =  aa - T2[6] - T4[6]
                print("big area")
                print(BIGAREA)
                
        elif(inter_c3 == False):  #KARL6
            #P2, 
                print("#TRIANGLE 1")
                T1 = _MINI(PB,inter_a3,inter_b3)
                print(T1)
            #PB,
                print("#TRIANGLE 2")
                T2 = _MINI(P3,inter_b2,inter_b3)
                print(T2)
            #P3, 
                print("#TRIANGLE 3")
                T3 = _MINI(PC,inter_b2,inter_c2)
                print(T3)
            #pc ,
                print("#TRIANGLE 4")
                T4 = _MINI(P2,inter_c1,inter_c2)
                print(T4)
            #p1,
                print("#TRIANGLE 5")
                T5 = _MINI(PA,inter_a1,inter_c1)
                print(T5)

            #Big area = TRI_ABC - *1* - *2*
                BIGAREA =  aa - T2[6] - T4[6]
                print("big area")
                print(BIGAREA)
        else:
            print("JUAN-KARL")
            #return("error 6")
        ####
    elif(inter_a1 == P2):
        ####
        if(inter_c1 == False):        
            #Pb a1 b1
                print("#TRIANGLE 1")
                T1 = _MINI(PB,inter_a1,inter_b1)
                print(T1)
            #P2 b2 inter_b1
                print("#TRIANGLE 2")
                T2 = _MINI(P1,inter_b3,inter_b1)
                print(T2)
            #P3, 
                print("#TRIANGLE 3")
                T3 = _MINI(PC,inter_b3,inter_c3)
                print(T3)
            #PB,
                print("#TRIANGLE 4")
                T4 = _MINI(P3,inter_c3,inter_c2)
                print(T4)
            #P1,
                print("#TRIANGLE 5")
                T5 = _MINI(PA,inter_a2,inter_c2)
                print(T5)
            #Big area = TRI_ABC - *1* - *2*
                BIGAREA =  aa - T2[6] - T4[6]
                print("big area")
                print(BIGAREA)
                
        elif(inter_c2 == False):  #KARL6
            #P2, 
                print("#TRIANGLE 1")
                T1 = _MINI(PB,inter_a2,inter_b2)
                print(T1)
            #PB,
                print("#TRIANGLE 2")
                T2 = _MINI(P3,inter_b2,inter_b3)
                print(T2)
            #P3, 
                print("#TRIANGLE 3")
                T3 = _MINI(PC,inter_b3,inter_c3)
                print(T3)
            #pc ,
                print("#TRIANGLE 4")
                T4 = _MINI(P1,inter_c1,inter_c3)
                print(T4)
            #p1,
                print("#TRIANGLE 5")
                T5 = _MINI(PA,inter_a2,inter_c1)
                print(T5)

            #Big area = TRI_ABC - *1* - *2*
                BIGAREA =  aa - T2[6] - T4[6]
                print("big area")
                print(BIGAREA)
        else:
            print("JUAN-KARL")
            #return("error 6")
        ####
    elif(inter_a2 == P3):
        ####
        if(inter_c2 == False):        
            #Pb a1 b1
                print("#TRIANGLE 1")
                T1 = _MINI(PB,inter_a2,inter_b2)
                print(T1)
            #P2 b2 inter_b1
                print("#TRIANGLE 2")
                T2 = _MINI(P2,inter_b2,inter_b1)
                print(T2)
            #P3, 
                print("#TRIANGLE 3")
                T3 = _MINI(PC,inter_b1,inter_c1)
                print(T3)
            #PB,
                print("#TRIANGLE 4")
                T4 = _MINI(P1,inter_c3,inter_c1)
                print(T4)
            #P1,
                print("#TRIANGLE 5")
                T5 = _MINI(PA,inter_a3,inter_c3)
                print(T5)
            #Big area = TRI_ABC - *1* - *2*
                BIGAREA =  aa - T2[6] - T4[6]
                print("big area")
                print(BIGAREA)
                
        elif(inter_c3 == False):  #Bill7
            #P2, 
                print("#TRIANGLE 1")
                T1 = _MINI(PB,inter_a3,inter_b3)
                print(T1)
            #PB,
                print("#TRIANGLE 2")
                T2 = _MINI(P1,inter_b1,inter_b3)
                print(T2)
            #P3, 
                print("#TRIANGLE 3")
                T3 = _MINI(PC,inter_b1,inter_c1)
                print(T3)
            #pc ,
                print("#TRIANGLE 4")
                T4 = _MINI(P2,inter_c2,inter_c1)
                print(T4)
            #p1,
                print("#TRIANGLE 5")
                T5 = _MINI(PA,inter_c2,inter_a2)
                print(T5)

            #Big area = TRI_ABC - *1* - *2*
                BIGAREA =  aa - T2[6] - T4[6]
                print("big area")
                print(BIGAREA)
        else:
            print("JUAN-KARL")
            #return("error 6")
        ####
    else:
        print("wtf")

    print("called")
    ##repeat for a2 and a3




    '''''old code''''''
    s_pa = ((inter_a1[0] - P2[0])**2 + (inter_a1[1] - P2[1])**2)**0.5
                s_pa = ((inter_c2[0] - inter_a1[0])**2 + (inter_c2[1] - inter_a1[1])**2)**0.5
                s_cp = ((P2[0] - inter_c2[0])**2 + (P2[1] - inter_c2[1])**2)**0.5

                a_pac = _SSS(s_pa,s_ac,s_cp)
                a_cpa = _SSS(s_cp,s_pa,s_ac)
                a_acp = _SSS(s_ac,s_cp,s_pa)

                VZ = 0.5 * (s_pa + s_pa + s_cp)
                area_pac = (VZ*(VZ-s_pa) * (VZ-s_pa)*(VZ-s_cp))**0.5


    ////


    elif(inter_b1 == PC): ##inter_b1 == inter_c1
        if(inter_c3 == False):   #JACK18     
            #P2,inter_b1, inter_c2
                print("#TRIANGLE 1")
                T1 = _MINI(P2,inter_b1 ,inter_c2)
                print(T1)
            #PA,  inter_c2, inter_a2
                print("#TRIANGLE 2")
                T2 = _MINI(PA,inter_a2,inter_c2)
                print(T2)
            #P3, inter_a2 inter_a3
                print("#TRIANGLE 3")
                T3 = _MINI(P3,inter_a2,inter_a3)
                print(T3)
            #PB, inter_a3 inter_b3
                print("#TRIANGLE 4")
                T4 = _MINI(PB,inter_b3,inter_a3)
                print(T4)
            #P1, inter_b1 inter_b3
                print("#TRIANGLE 5")
                T5 = _MINI(P1,inter_b3 ,inter_b1)
                print(T5)
            #Big area = TRI_ABC - *1* - *2*
                BIGAREA =  aa - T2[6] - T4[6]
                print("big area")
                print(BIGAREA)
                
        elif(inter_b3 == False):  #SARA18
            #P2,  inter_b1  inter_b2
                print("#TRIANGLE 1")
                T1 = _MINI(P2,inter_b1,inter_b2)
                print(T1)
            #PB, inter_b2 inter_a2
                print("#TRIANGLE 2")
                T2 = _MINI(PB,inter_a2,inter_b2)
                print(T2)
            #P3,  inter_a2 inter_a3
                print("#TRIANGLE 3")
                T3 = _MINI(P3,inter_a2,inter_a3)
                print(T3)
            #pa , inter_a3 inter_c3
                print("#TRIANGLE 4")
                T4 = _MINI(PA,inter_c3,inter_a3)
                print(T4)
            #p1, inter_c3 inter_c1
                print("#TRIANGLE 5")
                T5 = _MINI(P1,inter_c3,inter_c1)
                print(T5)
            #Big area = TRI_ABC - *1* - *2*
                BIGAREA =  aa - T2[6] - T4[6]
                print("big area")
                print(BIGAREA)
        else:
            print("SARA-JACK")
            #return("error 18")
        
    elif(inter_a1 == P1):
        ####
        if(inter_c3 == False):   #SARA18     
            #P2, 
                print("#TRIANGLE 1")
                T1 = _MINI(P2,inter_a1,inter_c2)
                print(T1)
            #PC, 
                print("#TRIANGLE 2")
                T2 = _MINI(PC,inter_b2,inter_c2)
                print(T2)
            #P3, 
                print("#TRIANGLE 3")
                T3 = _MINI(P3,inter_b2,inter_b3)
                print(T3)
            #PB,
                print("#TRIANGLE 4")
                T4 = _MINI(PB,inter_a3,inter_b3)
                print(T4)
            #P1,
                print("#TRIANGLE 5")
                T5 = _MINI(P1,inter_a3,inter_a1)
                print(T5)
            #Big area = TRI_ABC - *1* - *2*
                BIGAREA =  aa - T2[6] - T4[6]
                print("big area")
                print(BIGAREA)
                
        elif(inter_a3 == False):  #KARL6
            #P2, 
                print("#TRIANGLE 1")
                T1 = _MINI(P2,inter_a1,inter_a2)
                print(T1)
            #PB,
                print("#TRIANGLE 2")
                T2 = _MINI(PB,inter_b2,inter_a2)
                print(T2)
            #P3, 
                print("#TRIANGLE 3")
                T3 = _MINI(P3,inter_b2,inter_b3)
                print(T3)
            #pc ,
                print("#TRIANGLE 4")
                T4 = _MINI(PC,inter_c3,inter_b3)
                print(T4)
            #p1,
                print("#TRIANGLE 5")
                T5 = _MINI(P1,inter_c3,inter_c1)
                print(T5)

            #Big area = TRI_ABC - *1* - *2*
                BIGAREA =  aa - T2[6] - T4[6]
                print("big area")
                print(BIGAREA)
        else:
            print("JUAN-KARL")
            #return("error 6")
        ####


    ////


                

    '''''






