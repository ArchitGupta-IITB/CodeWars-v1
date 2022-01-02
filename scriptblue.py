import random
from random import randint
def ActRobot(robot):
         #if u need variables create here or uncomment them      
        #corner=["NE","SW","SE","NW"]
        #side=["UP","DW","RT","LT"]
        #commands=[]
        #dic={0:'UP',1:'NW',2:'LT',3:"SW",4:"DW",5:"SE",6:"RT",7:"NE"}
        robotSignalOld=robot.GetYourSignal()
        specialStructure=""
        (robotX,robotY) = robot.GetPosition()
        specialStructureX=-1
        specialStructureY=-1
        specialStructurestr=""
        isCollected=robotSignalOld[19]
        targetX=int(robotSignalOld[6:8])
        targetY=int(robotSignalOld[8:10])
        targetXStrNew=""
        targetYStrNew=""
        next_pos=0
        if robot.GetVirus() > 1000:
                robot.DeployVirus(200)
        l1=[]
        l1.append(robot.investigate_up())          
        l1.append(robot.investigate_nw())
        l1.append(robot.investigate_left())
        l1.append(robot.investigate_sw())   
        l1.append(robot.investigate_down())    
        l1.append(robot.investigate_se())
        l1.append(robot.investigate_right())
        l1.append(robot.investigate_ne())
        for i in range(0,8):
                if l1[i]=="enemy-base":
                        specialStructure="EB"
                        robot.DeployVirus(200)
                        (specialStructureX, specialStructureY, specialStructurestr) = generate(robot.GetPosition(),l1[i])
                        break

                if l1[i]=="enemy":
                        specialStructure="EN"                
        
        #attack strategy
        
        base_signal=robot.GetCurrentBaseSignal()
        if base_signal[4:8]!=" "*4:
        #rTX = robotSignalOld[6:8]
                bEX = base_signal[4:6]
                targetXStrNew+=bEX

        #rTY = robotSignalOld[8:10]
                bEY = base_signal[6:8]
                targetYStrNew+=bEY


        attrob=int(base_signal[8:10])
        shudAttack = False  
        
        if attrob<=certainvalue:    #archit look into this
                shudAttack=True
        else:
               #xxs1=int(robotSignalOld[0:2])
                #yys1=int(robotSignalOld[2:4])
                xxs2=int(base_signal[4:6])
                yys2=int(base_signal[6:8])
               

                xxdistance=abs(robotX,robotY)
                yydistance=abs(xxs2,yys2)

                distance=max(xxdistance,yydistance)
        
        
                if distance<=20:
                        #send robot
                        shudAttack=True
        
        if shudAttack:
                pass   


        if  specialStructure=="EB":
                
                targetXStrNew+=specialStructureX
                targetYStrNew+=specialStructureY
        '''
        Add your code here
                Robot Signal="XXYYSPTXTYSSPTGURLRT"; for blank keep space
                              01234567890123456789
                              t=reached yet? Y/N
                P=attacking or defense(A/D/Resorce collector)
                XXYY=coord SP= special position SS special Structure EB-enemy Base
                Base Signal="BXBYEXEYNANCND0001TR"
                             01234567890123456789
        '''
        #checking for enemy or b
        
        #lets spiral out        
        if(robotSignalOld[12]=="R"):
                if robotX==robotSignalOld[6:8] and robotY==robotSignalOld[8:10]:
                        isCollected="Y"
                if isCollected=="Y":
                        if robotX==targetX:
                                next_pos=2
                        elif robotX>targetX:
                                if robotY<=targetY:
                                        if (robotX-targetX)>(targetY-robotY):
                                                next_pos=3
                                        elif (robotX-targetX)==(targetY-robotY):
                                                next_pos=2
                                        else:
                                                next_pos=2
                                        
                                else:
                                        if (robotX-targetX)>(robotY-targetY):
                                                next_pos=3
                                        else:
                                                next_pos=4
                        else:
                                if robotY<=targetY:
                                        if (targetX-robotX)>(targetY-robotY):
                                                next_pos=1
                                        elif (targetX-robotX)==(targetY-robotY):
                                                next_pos=2
                                        else:
                                                next_pos=2
                                        
                                else:
                                        if (robotX-targetX)>=(robotY-targetY):
                                                next_pos=1
                                        else:
                                                next_pos=4
                                
                                
                                        
                                
                                
                


        """ 
                if (xx not equal to tx)
                #distance between xx and tx

                # for(xx,xx+distance)
                 return 
                 
                 """
        # After checking for any enemy bots, move to target
        # Check ur previous designation if RC, enemy base found, A of friendly base less than threshold, dist less then chg ur status A
        ##Robot Signal="XXYYSPTXTYSSPTGRDDI"; for blank keep space

def generate(s,t):#s=robot position tuple t= direction
                a,b = t
                aN,bN,abstr=""
                if s=="UP":
                        aN=a
                        bN=b-1
                if s=="NE":
                        aN=a+1
                        bN=b-1
                if s=="RT":
                        aN=a+1
                        bN=b
                if s=="SE":
                        aN=a+1
                        bN=b+1
                if s=="DW":
                        an=a
                        bN=b+1
                if s=="SW":
                        an=a-1
                        bN=b+1
                if s=="LT":
                        an=a-1
                        bN=b
                if s=="NW":
                        an=a-1
                        bN=b-1
                if aN<10:
                        abstr+="0"+str(aN)
                if aN>9:
                        abstr+=str(aN)
                if bN<10:
                        abstr+="0"+str(bN)
                if bN>9:
                        abstr+=str(bN)
                return (aN.bN,abstr) 
#complete this Drashti & Suranjan
def isNear(s1,s2,r):#"XXYY"
        import math
        xs1=int(s1[0:2])
        ys1=int(s1[2:4])
        xs2=int(s2[0:2])
        ys2=int(s2[2:4])

        xdistance =abs(xs1-xs2)
        ydistance=abs(ys1-ys2)

        distance=max(xdistance,ydistance)
        
        
        if distance<=r :
                return True
        else:
                return False

def distancebtw(s1,s2):#"XXYY"
        xs1=int(s1[0:2])
        ys1=int(s1[2:4])
        xs2=int(s2[0:2])
        ys2=int(s2[2:4])
        return max(abs(xs2-xs1),abs(ys1-ys2))

def nextmovement(s1,s2):#XXYY
                x=int(s1[0:2])
                y=int(s1[2:4])
                tx = int(s2[0:2])
                ty = int(s2[2:4])
                distx1=tx-x
                disty1=ty-y
                distx = abs(tx-x) 
                disty = abs(ty-y)
                """
                if distx==1 and disty==0:
                        robot.DeployVirus(robot.GetVirus()*0.75)
                        return 0
                elif disty==1 and distx==0:
                        robot.DeployVirus(robot.GetVirus()*0.75)
                        return 0 
                """
                poss=[]
                """
                if distx1>0 and disty<0:
                        a=randint(1,2)
                        return a
                elif distx1<0 and disty>0:
                        b=randint(3,4)    
                        return b  
                elif distx1>0 and disty>0:
                        c=randint(2,3)
                        return c
                elif distx1<0 and disty<0:
                        return random.choice([1,4])   
                """
                

                if x < tx:
                        poss.append(2)
                if x > tx:
                        poss.append(4) 
                if y < ty :
                        poss.append(3)
                if y > ty:
                        poss.append(1)
                return random.choice(poss)
        #return 0

def ActBase(base):
        '''
        Add your code here
                Robot Signal="XXYYSPTXTYSSPTGURLRT"; for blank keep space
                              01234567890123456789
                              t=reached yet? Y/N
                P=attacking or defense(A/D/Resorce collector)
                XXYY=coord SP= special position SS special Structure EB-enemy Base
                Base Signal="BXBYEXEYNANCND0001TR"
                             01234567890123456789
        '''
        #creating signal for the first time
        
        canvasX=base.GetDimensionX()
        canvasY=base.GetDimensionY()
        canvaspartitions=[]
        istr=""
        jstr=""
        for i in range(3,canvasX,5):
                yrange=[]
                
                for j in range(3,canvasY,5):
                        if i<10:
                                istr="0"+str(i)
                        if i>9:
                                istr=str(i)
                        if j<10:
                                jstr="0"+str(j)
                        if j>9:
                                jstr=str(j)
                        yrange.append(istr,jstr)
                canvaspartitions.append(yrange)
        base_X_int,base_Y_int=base.GetPosition()
        base_X_str=""
        base_Y_str=""
        if base_X_int<10:
                base_X_str="0"+str(base_X_int)
        if base_X_int>9:
                base_X_str=str(base_X_int)
        if base_Y_int<10:
                base_Y_str="0"+str(base_Y_int)
        if base_Y_int>9:
                base_Y_str=str(base_Y_int)
        #creating signal
        if base.GetYourSignal()=="":
                base_X_int,base_Y_int=base.GetPosition()
                base_X_str=""
                base_Y_str=""
                if base_X_int<10:
                        base_X_str="0"+str(base_X_int)
                if base_X_int>9:
                        base_X_str=str(base_X_int)
                if base_Y_int<10:
                        base_Y_str="0"+str(base_Y_int)
                if base_Y_int>9:
                        base_Y_str=str(base_Y_int)
                base.SetYourSignal(base_X_str+base_Y_str+" "*10+"0"*4+"  ")
                #create initial bots under here
                totalrobots=0
                #Resource collectors
                for i in range(0,len(canvaspartitions)):
                        for j in range(0,len(canvaspartitions[0])):
                                base.create_robots(base_X_str+base_Y_str+"  "+canvaspartitions[i][j]+"  "+"R"+"  "+"    "+"N")
                                #base.create_robots(base_X_str+base_Y_str+"  "+canvaspartitions[i][j]+"  "+"R"+"  "+"    "+"N")
                                totalrobots+=1
                '''
                base.create_robot(base_X_str+base_Y_str+"  "+" "*6+"R"+"UP"+"1510")
                base.create_robot(base_X_str+base_Y_str+"  "+" "*6+"R"+"NW"+"1510")
                base.create_robot(base_X_str+base_Y_str+"  "+" "*6+"R"+"LT"+"1510")
                base.create_robot(base_X_str+base_Y_str+"  "+" "*6+"R"+"SW"+"1510")
                base.create_robot(base_X_str+base_Y_str+"  "+" "*6+"R"+"DW"+"1510")
                base.create_robot(base_X_str+base_Y_str+"  "+" "*6+"R"+"SE"+"1510")
                base.create_robot(base_X_str+base_Y_str+"  "+" "*6+"R"+"RT"+"1510")
                base.create_robot(base_X_str+base_Y_str+"  "+" "*6+"R"+"NE"+"1510")
                base.create_robot(base_X_str+base_Y_str+"  "+" "*6+"R"+"UP"+"1005")
                base.create_robot(base_X_str+base_Y_str+"  "+" "*6+"R"+"NW"+"1005")
                base.create_robot(base_X_str+base_Y_str+"  "+" "*6+"R"+"LT"+"1005")
                base.create_robot(base_X_str+base_Y_str+"  "+" "*6+"R"+"SW"+"1005")
                base.create_robot(base_X_str+base_Y_str+"  "+" "*6+"R"+"DW"+"1005")
                base.create_robot(base_X_str+base_Y_str+"  "+" "*6+"R"+"SE"+"1005")
                base.create_robot(base_X_str+base_Y_str+"  "+" "*6+"R"+"RT"+"1005")
                base.create_robot(base_X_str+base_Y_str+"  "+" "*6+"R"+"NE"+"1005")               
                '''
                #DEFENSE
                #Review this with team
                base.create_robot(base_X_str+base_Y_str+"  "+base_X_str+base_Y_str+"  "+"D"+"NW"+"0500"+"Y")
                base.create_robot(base_X_str+base_Y_str+"  "+base_X_str+base_Y_str+"  "+"D"+"SW"+"0500"+"Y")
                base.create_robot(base_X_str+base_Y_str+"  "+base_X_str+base_Y_str+"  "+"D"+"SE"+"0500"+"Y")
                base.create_robot(base_X_str+base_Y_str+"  "+base_X_str+base_Y_str+"  "+"D"+"NE"+"0500"+"Y")
                
                totalrobots+=4
                
                a=robotSignalOld[4:6]
                x,y=robot.GetPosition()
                BX,BY=base.GetPosition() 
                distx=abs(BX-x)
                disty=abs(BY-y)
                
                
                
                possible=[]
                if a=="NE":
                        if (distx==0 or distx==1) and (disty==0 or disty==1):
                                possible=[1,2]
                        elif distx==2 and disty==0:
                                possible=[1,4]
                        elif distx==0 and disty==2:
                                possible=[3,2]
                        elif distx==1 and disty==1:
                                possible=[1,4,3,2]
                        if distx==1 and disty==2:
                                possible=[2,3,4]
                        elif distx==2 and disty==1:
                                possible=[1,3,4]
                        elif distx==2 and disty==2:
                                possible=[3,4]         
                        

                if a=="NW":
                        if (distx==0 or distx==1) and (disty==0 or disty==1):
                                possible=[1,4]
                        elif distx==2 and disty==0:
                                possible=[1,4]
                        elif distx==0 and disty==2:
                                possible=[3,2]
                        elif distx==1 and disty==1:
                                possible=[1,4,3,2]
                        if distx==1 and disty==2:
                                possible=[2,3,4]
                        elif distx==2 and disty==1:
                                possible=[1,3,2]
                        elif distx==2 and disty==2:
                                possible=[3,2]         
                        
                                       
                if a=="SW":
                        if (distx==0 or distx==1) and (disty==0 or disty==1):
                                possible=[1,2]
                        elif distx==2 and disty==0:
                                possible=[1,4]
                        elif distx==0 and disty==2:
                                possible=[3,2]
                        elif distx==1 and disty==1:
                                possible=[1,4,3,2]
                        if distx==1 and disty==2:
                                possible=[2,3,4]
                        elif distx==2 and disty==1:
                                possible=[1,3,4]
                        elif distx==2 and disty==2:
                                possible=[3,4]         
                        
                                
                if a=="SE":
                        if (distx==0 or distx==1) and (disty==0 or disty==1):
                                possible=[3,2]
                        elif distx==2 and disty==0:
                                possible=[3,4]
                        elif distx==0 and disty==2:
                                possible=[1,2]
                        elif distx==1 and disty==1:
                                possible=[1,4,3,2]
                        if distx==1 and disty==2:
                                possible=[2,1,4]
                        elif distx==2 and disty==1:
                                possible=[1,3,4]
                        elif distx==2 and disty==2:
                                possible=[1,4]         
                        
                return random.choice(possible)       

                
                 
                #creating signal
                base.SetYourSignal(base_X_str+base_Y_str+" "*10+"0"*4+str(totalrobots))
                
                #created bots
        
        #basic info recollection
        base_signal_Old=base.GetYourSignal()
        enemy_base_found=True
        if base_signal_Old[4:8]!=" "*4:
                enemy_base_found=False
        enemy_baseX=base_signal_Old[4:6]
        enemy_baseY=base_signal_Old[6:8]
        base_signal_New=""

        #timeframe renewal
        timestamp=base_signal_Old[14:18]
        timestamp_New=str(1+int(timestamp))
        
        #Remaking of bots in intervals
        if int(timestamp)%50==0:
                base.create_robot('')

        robot_signal_list=base.GetListOfSignals()
        robot_signal_list_distance_enemybase=[]
        if enemy_base_found==False:
                for w in robot_signal_list:
                        if w[10:12]=="EB":
                                enemy_baseX=w[6:8]
                                enemy_baseY=w[8:10]
        
        #Recounting Status of Robots
        resource_collectors=0
        for i in robot_signal_list:
                if i[12]=="R":
                        resource_collectors+=1
        defender=0
        for i in robot_signal_list:
                if i[12]=="D":
                        defender+=1

        #attack strategy implementation
        #Review Pending
        attacking_no_old=base_signal_Old[8:10]
        attacking_no_New=""
        attack_counter=0
        
        #Calculating the distance between 
        if enemy_base_found:

                for w in robot_signal_list:
                        robot_signal_list_distance_enemybase.append(distancebtw(w[0:4],enemy_baseX+enemy_baseY))
        
        
                for i in range(0,len(robot_signal_list)):
                        if robot_signal_list[i][12]=="A" and robot_signal_list_distance_enemybase[i]<base.GetCanvasX()/2:
                                attack_counter+=1



        if attack_counter<10:
                attacking_no_New="0"+str(attack_counter)
        if attack_counter>9:
                attacking_no_New=str(attack_counter)
                
        
        #Resource must be collected
        
        
        #Repeat 8 times in 8 dir
        
        
        
        
        
        #searching for enemy robots near base
        st = ""
        
        #enemy position
        
        if base.investigate_up()=="enemy":
                st="UP"                       
        if base.investigate_nw()=="enemy":
                st="NW"
        if base.investigate_left()=="enemy":
                st="LT"
        if base.investigate_sw()=="enemy":
                st="SW"
        if base.investigate_down()=="enemy":
                st="DW"
        if base.investigate_se()=="enemy":
                st="SE"
        if base.investigate_right()=="enemy":
                st="RT"
        if base.investigate_ne()=="enemy":
                st="NE"
        
        if st!=" ":
                base.DeployVirus(800)
        
        base_signal_New=base_signal_Old[0:4]+enemy_baseX+enemy_baseY+attacking_no_New+resource_collectors+defender+timestamp_New+totalrobots
        base.SetYourSignal(base_signal_New)
        
        #apply defense
        #checking for defense in 4 corners
        corner=["NE","SW","SE","NW"]
        corner_now=[]
        for i in robot_signal_list:
                if i[12]=="D":
                        for j in corner:
                                if i[13:15]==j:
                                        corner_now.append(j)
                                        break
        for i in range(0,len(corner)-len(corner_now)):
                if corner[i] not in corner_now:
                        base.create_robot(base_X_str+base_Y_str+"  "+base_X_str+base_Y_str+"  "+"D"+corner[i]+"0500"+"Y")
        
        defender=0
        for i in robot_signal_list:
                if i[12]=="D":
                        defender+=1

        if st!="  ":
                base.create_robot(base_X_str+base_Y_str+"  "+base_X_str+base_Y_str+"  "+"D"+st+"0500"+"Y")

        if int(timestamp)>500:
                if defender<12:
                        base.create_robot(base_X_str+base_Y_str+"  "+base_X_str+base_Y_str+"  "+"D"+"  "+"0500"+"Y")
        
        #Defense applied


        #return

        '''
        Add your code here
                Robot Signal="XXYYSPTXTYSSPTGURLRT"; for blank keep space
                              01234567890123456789
                              t=reached yet?
                P=attacking or defense(A/D/R)
                XXYY=coord SP= special position SS special Structure EB-enemy Base
                Base Signal="BXBYEXEYNANCND0001TR"
                             01234567890123456789
        '''
        return