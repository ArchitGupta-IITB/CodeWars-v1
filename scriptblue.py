from random import randint
corner=["NE","SW","SE","NW"]
side=["UP","DW","RT","LT"]
commands=[]
dic={0:'UP',1:'NW',2:'LT',3:"SW",4:"DW",5:"SE",6:"RT",7:"NE"}


def ActRobot(robot):
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
                if l1[i]=="enemy":
                        s=robot.GetYourSignal()
                        robot.setSignal(s[0:4]+print(dic.values(i))+s[6:10]+"EN")
                        
                if l1[i]=="enemy-base":
                        s=robot.GetYourSignal()
                        robot.setSignal(s[0:4]+print(dic.values(i))+s[6:10]+"EB")   
                        
        
                
        
        return randint(1,4)


def ActBase(base):
    '''
    
    Add your code here
    Signal="XXYYSPTXTYSS enemy base at XXYY"; for blank keep space
    XXYY=coord SP= special position SS special Structure EB-enemy Base
    '''
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
        
        if base.GetElixir() > 500:
                base.create_robot('')
        sigli=base.GetListOfSignals()
        ebx=00
        eby=00
        for w in sigli:
                if w[10:12]=="EB":
                        =w[8:10]

        st="  "
        temp=""
        temps=""
        #Repeat 8 times in 8 dir
        if base.investigate_up()=="enemy":
                st="UP"
        
        if st!="  ":
                temp=base.GetPosition()
                temps+=(string)temp[0]+(string)temp[1]
                temps+=st
                
                base.create_robot(temps)
        return
        