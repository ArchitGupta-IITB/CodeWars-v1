
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
                if s=="UP":
                        return(a,b+1)
                if s=="NE":
                        return(a+1,b+1)
                if s=="RT":
                        return(a+1,b)
                if s=="SE":
                        return(a+1,b-1)
                if s=="DW":
                        return(a,b-1)
                if s=="SW":
                        return(a-1,b-1)
                if s=="LT":
                        return(a-1,b)
                if s=="NW":
                        return(a-1,b+1)



def ActBase(base):
        '''
        Archit made changes
        '''
        ebx="  "
        eby="  "
        basiN=" "*20
        st="  "#enemy position
        baso=base.GetYourSignal()
        sigli=base.GetListOfSignals()
        c,d=base.GetPosition()
        if c<10:
                e="0"+str(c)
        if c>9:
                e=str(c)
        if d<10:
                f="0"+str(d)
        if d>9:
                f=str(d)       
                basiN+=e+f
                basiN+=st
                basiN+=ebx+eby
        if baso[6:10]!=" "*4:
                basiN=basiN[0:6]+baso[6:10]+basiN[10:]
        
        for w in sigli:
                if w[10:12]=="EB":
                        ebx=w[6:8]
                        eby=w[8:10]
        if base.GetElixir() > 500:
                base.create_robot('')
        
        #Repeat 8 times in 8 dir
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
        c,d=base.GetPosition()
        temps=""
        e="  "
        f="  "
        if st!="  ":
                if c<10:
                        e="0"+str(c)
                if c>9:
                        e=str(c)
                if d<10:
                        f="0"+str(d)
                if d>9:
                        f=str(d)       
                basiN+=e+f
                basiN+=st
                basiN+=ebx+eby
                
                base.create_robot(temps)
        return

        