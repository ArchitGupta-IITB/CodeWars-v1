from random import randint
def ActRobot(robot):
        '''        
        corner=["NE","SW","SE","NW"]
        side=["UP","DW","RT","LT"]
        commands=[]
        dic={0:'UP',1:'NW',2:'LT',3:"SW",4:"DW",5:"SE",6:"RT",7:"NE"}
        robotSignalOld=robot.GetYourSignal()
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
                        s=robot.GetYourSignal()
                        robot.setSignal(s[0:4]+dic.values(i)+s[6:10]+"EB")
                        robot.DeployVirus(200)
                        break

                if l1[i]=="enemy":
                        s=robot.GetYourSignal()
                        robot.setSignal(s[0:4]+dic.values(i)+s[6:10]+"EN")
                        
        
        #attack strategy Archit 
        
        base_signal=robot.GetCurrentBaseSignal()
        if base_signal[4:8]!=" "*4:
        '''
        



        up = robot.investigate_up()
        down = robot.investigate_down()
        left = robot.investigate_left()
        right = robot.investigate_right()
        x,y = robot.GetPosition()
        robot.setSignal('')
        if up == "enemy" and robot.GetVirus() > 1000:
                robot.DeployVirus(100)
        elif up == "enemy-base":
                if x < 10:
                        msg_x = '0' + str(x)
                else: 
                        msg_x = str(x)
                if y-1 < 10:
                        msg_y = '0' + str(y-1)
                else:
                        msg_y = str(y-1)
                msg = "base" + msg_x + msg_y
                robot.setSignal(msg)
                if robot.GetVirus() > 500:
                        robot.DeployVirus(500)
        if down == "enemy" and robot.GetVirus() > 1000:
                robot.DeployVirus(100)
        elif down == "enemy-base":
                
                if x < 10:
                        msg_x = '0' + str(x)
                else: 
                        msg_x = str(x)
                if y+1 < 10:
                        msg_y = '0' + str(y+1)
                else:
                        msg_y = str(y+1)
                msg = "base" + msg_x + msg_y
                robot.setSignal(msg)
                if robot.GetVirus() > 500:
                        robot.DeployVirus(500)
        
        if left == "enemy" and robot.GetVirus() > 1000:
                robot.DeployVirus(100)
        elif left == "enemy-base":
                if x - 1 < 10:
                        msg_x = '0' + str(x-1)
                else: 
                        msg_x = str(x-1)
                if y < 10:
                        msg_y = '0' + str(y)
                else:
                        msg_y = str(y)
                msg = "base" + msg_x + msg_y
                robot.setSignal(msg)
                if robot.GetVirus() > 500:
                        robot.DeployVirus(500)
                
        if right == "enemy" and robot.GetVirus() > 1000:
                robot.DeployVirus(100)
        elif right == "enemy-base":
                x,y = robot.GetPosition()
                if x+1 < 10:
                        msg_x = '0' + str(x+1)
                else: 
                        msg_x = str(x+1)
                if y < 10:
                        msg_y = '0' + str(y)
                else:
                        msg_y = str(y)
                msg = "base" + msg_x + msg_y
                robot.setSignal(msg)
                if robot.GetVirus() > 500:
                        robot.DeployVirus(500)
        
        
        if len(robot.GetCurrentBaseSignal()) > 0:
                s = robot.GetCurrentBaseSignal()[4:]
                sx = int(s[0:2])
                sy = int(s[2:4])
                dist = abs(sx-x) + abs(sy-y)
                if dist==1:
                        robot.DeployVirus(robot.GetVirus()*0.75)
                        return 0
                if x < sx:
                        return 2
                if x > sx:
                        return 4
                if y < sy :
                        return 3
                if y > sy:
                        return 1
        else:
                return randint(1,4)

        # After checking for any enemy bots, move to target
        # Check ur previous designation if RC, enemy base found, A of friendly base less than threshold, dist less then chg ur status A
        ##Robot Signal="XXYYSPTXTYSSPTGRDDI"; for blank keep space
def nextMove(robot):
        
                
        
        return randint(1,4)

def generate(s,t):
                a,b = t
                aN,bN,abstr=""
                if s=="UP":
                        aN=a
                        bN=b+1
                if s=="NE":
                        aN=a+1
                        bN=b+1
                if s=="RT":
                        aN=a+1
                        bN=b
                if s=="SE":
                        aN=a+1
                        bN=b-1
                if s=="DW":
                        an=a
                        bN=b-1
                if s=="SW":
                        an=a-1
                        bN=b-1
                if s=="LT":
                        an=a-1
                        bN=b
                if s=="NW":
                        an=a-1
                        bN=b+1
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
        return True

def distance_Btw(s1,s2):#XXYY
        
        return 0

def ActBase(base):
        '''
        Add your code here
                Robot Signal="XXYYSPTXTYSSPTGURLR"; for blank keep space
                              01234567890123456789
                P=attacking or defense(A/D/R)
                XXYY=coord SP= special position SS special Structure EB-enemy Base
                Base Signal="BXBYEXEYNANCND0001"
                             01234567890123456789
        '''
        #creating signal for the first time
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
                
                #Resource collectors
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
                
                #DEFENSE
                base.create_robot(base_X_str+base_Y_str+"  "+" "*6+"D"+"NW"+"0500")
                base.create_robot(base_X_str+base_Y_str+"  "+" "*6+"D"+"sW"+"0500")
                base.create_robot(base_X_str+base_Y_str+"  "+" "*6+"D"+"SE"+"0500")
                base.create_robot(base_X_str+base_Y_str+"  "+" "*6+"D"+"NE"+"0500")
                
                
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


        robot_signal_list=base.GetListOfSignals()
        robot_signal_list_distance_enemybase=[]
        if enemy_base_found==False:
                for w in robot_signal_list:
                        if w[10:12]=="EB":
                                enemy_baseX=w[6:8]
                                enemy_baseY=w[8:10]
        
        
        #attack strategy implementation
        
        attacking_no_old=base_signal_Old[8:10]
        attacking_no_New=""
        attack_counter=0
        #Calculating the distance between 
        if enemy_base_found:

                for w in robot_signal_list:
                        robot_signal_list_distance_enemybase.append(distance_Btw(w[0:4],enemy_baseX+enemy_baseY))
        
        
                for i in range(0,len(robot_signal_list)):
                        if robot_signal_list[i][12]=="A" and robot_signal_list_distance_enemybase[i]<10:
                                attack_counter+=1
        
        if attack_counter<10:
                attacking_no_New="0"+str(attack_counter)
        if attack_counter>9:
                attacking_no_New=str(attack_counter)
        
        #Apply Defense
        
        
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
        
        base_signal_New=base_signal_Old[0:4]+enemy_baseX+enemy_baseY+attacking_no_New+timestamp_New
        base.SetYourSignal(base_signal_New)
        
        return

        