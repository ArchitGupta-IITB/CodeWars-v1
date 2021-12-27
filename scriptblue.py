
def ActRobot(robot):
        corner=["NE","SW","SE","NW"]
        side=["UP","DW","RT","LT"]
        commands=[]
        dic={0:'UP',1:'NW',2:'LT',3:"SW",4:"DW",5:"SE",6:"RT",7:"NE"}
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

                if l1[i]=="enemy":
                        s=robot.GetYourSignal()
                        robot.setSignal(s[0:4]+dic.values(i)+s[6:10]+"EN")

def nextMove(robot):
        friend_positions = ["friend", "friend-base"]
        enemy_positions = ["enemy","enemy-base"]
        empty_positions =  ["blank"]
        safe_positions = []
        up = robot.investigate_up()
        down = robot.investigate_down()
        left = robot.investigate_left()
        right = robot.investigate_right()
        ne = robot.investigate_ne()
        nw = robot.investigate_nw()
        se = robot.investigate_se()
        sw = robot.investigate_sw()
        resultant_step = {
                "release_virus" : 0,
                "enemy_base" : (-1,-1),
        }
        
        if up in enemy_positions:
                if up == "enemy":
                        resultant_step["release_virus"] = 1
                else:
                        t = robot.GetPosition()
                        resultant_step["enemy_base"] = (t[0], t[1]-1)
                        return resultant_step
        else:
                safe_positions.append("up")

        if down in enemy_positions:
                if down == "enemy":
                        resultant_step["release_virus"] = 1
                else:
                        t = robot.GetPosition()
                        resultant_step["enemy_base"] = (t[0], t[1]+1)
                        return resultant_step
        else:
                safe_positions.append("down")
        if left in enemy_positions:
                if left == "enemy":
                        resultant_step["release_virus"] = 1
                else:
                        t = robot.GetPosition()
                        resultant_step["enemy_base"] = (t[0]-1, t[1])
                        return resultant_step
        else:
                safe_positions.append("left")
        if right in enemy_positions:
                if right == "enemy":
                        resultant_step["release_virus"] = 1
                else:
                        t = robot.GetPosition()
                        resultant_step["enemy_base"] = (t[0]+1, t[1])
                        return resultant_step
        else:
                safe_positions.append("right")
        
        if ne in enemy_positions:
                if ne == "enemy":
                        resultant_step["release_virus"] = 1
                else:
                        t = robot.GetPosition()
                        resultant_step["enemy_base"] = (t[0]+1, t[1]-1)
                        return resultant_step
        # else:
        #         safe_positions.append("ne")
        if nw in enemy_positions:
                if nw == "enemy":
                        resultant_step["release_virus"] = 1
                else:
                        t = robot.GetPosition()
                        resultant_step["enemy_base"] = (t[0]-1, t[1]-1)
                        return resultant_step
        # else:
        #         safe_positions.append("nw")
        if se in enemy_positions:
                if se == "enemy":
                        resultant_step["release_virus"] = 1
                else:
                        t = robot.GetPosition()
                        resultant_step["enemy_base"] = (t[0]+1, t[1]+1)
                        return resultant_step
        # else:
        #         safe_positions.append("se")
        if sw in enemy_positions:
                if sw == "enemy":
                        resultant_step["release_virus"] = 1
                else:
                        t = robot.GetPosition()
                        resultant_step["enemy_base"] = (t[0]-1, t[1]+1)
                        return resultant_step
        # else:
        #         safe_positions.append("sw")

        return (safe_positions,resultant_step)
                
        
        #return randint(1,4)

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
                



def ActBase(base):
        '''
        Archit made changes
        '''
        '''
    
        Add your code here
        Robot Signal="XXYYSPTXTYSSP"; for blank keep space
        P=attacking or defense(A/D)
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
               
        if enemy_base_found==False:
                for w in robot_signal_list:
                        if w[10:12]=="EB":
                                enemy_baseX=w[6:8]
                                enemy_baseY=w[8:10]
        
        if base.GetElixir() > 500:
                base.create_robot('')
        
        #Repeat 8 times in 8 dir
        #searching for enemy robots near base
        st="  "#enemy position
        if base.investigate_up()=="enemy":
                st="UP"
                base.DeployVirus(800)
        if base.investigate_nw()=="enemy":
                st="NW"
                base.DeployVirus(800)
        if base.investigate_left()=="enemy":
                st="LT"
                base.DeployVirus(800)
        if base.investigate_sw()=="enemy":
                st="SW"
                base.DeployVirus(800)
        if base.investigate_down()=="enemy":
                st="DW"
                base.DeployVirus(800)
        if base.investigate_se()=="enemy":
                st="SE"
                base.DeployVirus(800)
        if base.investigate_right()=="enemy":
                st="RT"
                base.DeployVirus(800)
        if base.investigate_ne()=="enemy":
                st="NE"
                base.DeployVirus(800)
        
        base_signal_New=base_signal_Old[0:4]+enemy_baseX+enemy_baseY+timestamp_New
        base.SetYourSignal(base_signal_New)
        return

        