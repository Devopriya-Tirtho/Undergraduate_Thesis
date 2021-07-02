# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 23:27:56 2020

@author: Hp
"""


''' Libraries which we are using '''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
from sklearn import linear_model

#################################
''' Importing Dataset '''
##################################
dataset=pd.read_csv('Yuzvendra Chahal.csv')

###############################
'''Number of Rows'''
############################
b=dataset.shape
print(b[0])
columnNumber=b[0]

#############################
'''Venue Indexing'''
#############################
for i in range(0,columnNumber):
    y=dataset.at[i,'Ground']
    if(y=="M Chinnaswamy Stadium"):
        
        dataset.at[i,'VenueIndex']=1
    elif(y=="MA Chidambaram Stadium"):
     
        dataset.at[i,'VenueIndex']=2
    elif(y=="Punjab Cricket Association IS Bindra Stadium"):
     
        dataset.at[i,'VenueIndex']=3
    elif(y=="Sawai Mansingh Stadium"):
      
        dataset.at[i,'VenueIndex']=4
    elif(y=="Eden Gardens"):
       
        dataset.at[i,'VenueIndex']=5
    elif(y=="Wankhede Stadium"):
     
        dataset.at[i,'VenueIndex']=6
    elif(y=="Maharashtra Cricket Association Stadium"):
  
        dataset.at[i,'VenueIndex']=7
    elif(y=="Arun Jaitley Stadium"):
     
        dataset.at[i,'VenueIndex']=8
    elif(y=="Rajiv Gandhi International Stadium"):
  
        dataset.at[i,'VenueIndex']=9
    elif(y=="JSCA International Stadium Complex"):
   
        dataset.at[i,'VenueIndex']=10
    elif(y=="Sharjah Cricket Stadium"):
    
        dataset.at[i,'VenueIndex']=11
    elif(y=="Dubai International Cricket Stadium"):
      
        dataset.at[i,'VenueIndex']=12
    elif(y=="Sheikh Zayed Stadium"):
      
        dataset.at[i,'VenueIndex']=13
    elif(y=="Sardar Patel Stadium"):
      
        dataset.at[i,'VenueIndex']=14
    elif(y=="Shaheed Veer Narayan Sing International Stadium"):
    
        dataset.at[i,'VenueIndex']=15
    elif(y=="Saurashtra Cricket Association Stadium"):
      
        dataset.at[i,'VenueIndex']=16
    elif(y=="Holkar Cricket Stadium"):
      
        dataset.at[i,'VenueIndex']=17
    elif(y=="ACA-VDCA" or y=="Dr YS Rajasekhara Reddy Cricket Stadium"):
      
        dataset.at[i,'VenueIndex']=18
    elif(y=="Barabati Stadium"):
      
        dataset.at[i,'VenueIndex']=19
    elif(y=="Brabourne Stadium"):
      
        dataset.at[i,'VenueIndex']=20
    elif(y=="DY Patil Stadium"):
      
        dataset.at[i,'VenueIndex']=21
    elif(y=="Feroz Shah Kotla Ground"):
      
        dataset.at[i,'VenueIndex']=22
    elif(y=="Green Park Stadium" or y=="Green Park"):
      
        dataset.at[i,'VenueIndex']=23
    elif(y=="HPCA Stadium" or y=="Himachal Pradesh Cricket Association Stadium"):
      
        dataset.at[i,'VenueIndex']=24
    elif(y=="Jawaharlal Nehru Stadium"):
      
        dataset.at[i,'VenueIndex']=25
        
    elif(y=="VCA Stadium"):      
        dataset.at[i,'VenueIndex']=26
                
    else:
        dataset.at[i,'VenueIndex']=27

################################
'''Calculation of Venue-wise Experience'''
################################
cnt1=0
cnt2=0
cnt3=0
cnt4=0
cnt5=0
cnt6=0
cnt7=0
cnt8=0
cnt9=0
cnt10=0
cnt11=0
cnt12=0
cnt13=0
cnt14=0
cnt15=0
cnt16=0
cnt17=0
cnt18=0
cnt19=0
cnt20=0
cnt21=0
cnt22=0
cnt23=0
cnt24=0
cnt25=0
cnt26=0
cnt27=0



for i in range(0,columnNumber):
    x=dataset.at[i,'VenueIndex']
    if(x==1):
        cnt1=cnt1+1
        dataset.at[i,'VenueExp']=cnt1
    elif(x==2):
        cnt2=cnt2+1
        dataset.at[i,'VenueExp']=cnt2
    elif(x==3):
        cnt3=cnt3+1
        dataset.at[i,'VenueExp']=cnt3
    elif(x==4):
        cnt4=cnt4+1
        dataset.at[i,'VenueExp']=cnt4
    elif(x==5):
        cnt5=cnt5+1
        dataset.at[i,'VenueExp']=cnt5
    elif(x==6):
        cnt6=cnt6+1
        dataset.at[i,'VenueExp']=cnt6
    elif(x==7):
        cnt7=cnt7+1
        dataset.at[i,'VenueExp']=cnt7
    elif(x==8):
        cnt8=cnt8+1
        dataset.at[i,'VenueExp']=cnt8
    elif(x==9):
        cnt9=cnt9+1
        dataset.at[i,'VenueExp']=cnt9
    elif(x==10):
        cnt10=cnt10+1
        dataset.at[i,'VenueExp']=cnt10
    elif(x==11):
        cnt11=cnt11+1
        dataset.at[i,'VenueExp']=cnt11
    elif(x==12):
        cnt12=cnt12+1
        dataset.at[i,'VenueExp']=cnt12
    elif(x==13):
        cnt13=cnt13+1
        dataset.at[i,'VenueExp']=cnt13
    elif(x==14):
        cnt14=cnt14+1
        dataset.at[i,'VenueExp']=cnt14
    elif(x==15):
        cnt15=cnt15+1
        dataset.at[i,'VenueExp']=cnt15
    elif(x==16):
        cnt16=cnt16+1
        dataset.at[i,'VenueExp']=cnt16
    elif(x==17):
        cnt17=cnt17+1
        dataset.at[i,'VenueExp']=cnt17
    elif(x==18):
        cnt18=cnt18+1
        dataset.at[i,'VenueExp']=cnt18
    elif(x==19):
        cnt19=cnt19+1
        dataset.at[i,'VenueExp']=cnt19
    elif(x==20):
        cnt20=cnt20+1
        dataset.at[i,'VenueExp']=cnt20
    elif(x==21):
        cnt21=cnt21+1
        dataset.at[i,'VenueExp']=cnt21
    elif(x==22):
        cnt22=cnt22+1
        dataset.at[i,'VenueExp']=cnt22
    elif(x==23):
        cnt23=cnt23+1
        dataset.at[i,'VenueExp']=cnt23
    elif(x==24):
        cnt24=cnt24+1
        dataset.at[i,'VenueExp']=cnt24
    elif(x==25):
        cnt25=cnt25+1
        dataset.at[i,'VenueExp']=cnt25
    elif(x==26):
        cnt26=cnt26+1
        dataset.at[i,'VenueExp']=cnt26
    elif(x==27):
        cnt27=cnt27+1
        dataset.at[i,'VenueExp']=cnt27
    else:
        dataset.at[i,'VenueExp']=1







################################
"""Opposition Indexing"""
################################

for i in range(0,columnNumber):
    y=dataset.at[i,'Vs']
    if(y=="Delhi Capitals" or y=="Delhi Daredevils"):
        
        dataset.at[i,'OppositionIndex']=1
    elif(y=="Kolkata Knight Riders"):
     
        dataset.at[i,'OppositionIndex']=2
    elif(y=="Chennai Super Kings"):
     
        dataset.at[i,'OppositionIndex']=3
    elif(y=="Rajasthan Royals"):
      
        dataset.at[i,'OppositionIndex']=4
    elif(y=="Pune Warriors"):
       
        dataset.at[i,'OppositionIndex']=5
    elif(y=="Kings XI Punjab"):
     
        dataset.at[i,'OppositionIndex']=6
    elif(y=="Deccan Chargers"):
  
        dataset.at[i,'OppositionIndex']=7
    elif(y=="Mumbai Indians"):
     
        dataset.at[i,'OppositionIndex']=8
    elif(y=="Sunrisers Hyderabad"):
  
        dataset.at[i,'OppositionIndex']=9
    elif(y=="Rising Pune Supergiant"):
   
        dataset.at[i,'OppositionIndex']=10
    elif(y=="Gujarat Lions"):
    
        dataset.at[i,'OppositionIndex']=11
    elif(y=="Royal Challengers Bengaluru" or y=="Royal Challengers Bangalore"):
    
        dataset.at[i,'OppositionIndex']=12
    else:
        dataset.at[i,'OppositionIndex']=0






######################
        """Creatiing New Dataframe"""
df=pd.DataFrame(dataset,columns=['Match','VenueIndex','VenueExp','OppositionIndex','Date','WicketsCric','Overs','Runs'
                                ])
df['Date']=pd.to_datetime(df['Date'].astype(str), format='%Y/%m/%d')

################################
################################

#Number of Rows
a=df.shape
print(a[0])
columnNum=a[0]


#####################################
######################################
#########################################
'''Calculation of balls from over'''

import math

Balls=[]   

for i in range(0,columnNum):
    overnum=math.floor(df.at[i,'Overs'])
    Balls.append((df.at[i,'Overs']-overnum)*10+overnum*6)

df["Balls"] = Balls  

#####################################
######################################
#########################################


'''Calculation of Cumulative Runs, Overs, Wickets,Balls'''


#####################################
######################################
#########################################

TotalRuns=[]   
run=0
for i in range(0,columnNum):
        run=run+df.at[i,'Runs']
        TotalRuns.append(run)

df["TotalRuns"] = TotalRuns   


TotalOvers=[]   
over=0
for i in range(0,columnNum):
        over=over+df.at[i,'Overs']
        TotalOvers.append(over)

df["TotalOvers"] = TotalOvers   


TotalWickets=[]   
wicket=0
for i in range(0,columnNum):
        wicket=wicket+df.at[i,'WicketsCric']
        TotalWickets.append(wicket)

df["TotalWickets"] = TotalWickets   


TotalBalls=[]   
ball=0
for i in range(0,columnNum):
        ball=ball+df.at[i,'Balls']
        TotalBalls.append(ball)

df["TotalBalls"] = TotalBalls  


#####################################
######################################
#########################################



'''Calculation of Career Average'''


BowlingAverage=[]   

for i in range(0,columnNum):
    if(df.at[i,'TotalWickets']!=0):
        BowlingAverage.append(df.at[i,'TotalRuns']/df.at[i,'TotalWickets'])
    else:
         BowlingAverage.append(100)

df["BowlingAverage"] = BowlingAverage  


'''Calculation of Match-wise Economy Rate change'''


EconomyRateMatch=[]   

for i in range(0,columnNum):
    if(df.at[i,'Overs']!=0):
        EconomyRateMatch.append(df.at[i,'Runs']/df.at[i,'Overs']) 
    else:
        EconomyRateMatch.append(10)
         
df["EconomyRateMatch"] = EconomyRateMatch  


'''Calculation of Career-wise Economy Rate'''


EconomyRateTotal=[]   

for i in range(0,columnNum):
    if (df.at[i,'TotalOvers']!=0):
        EconomyRateTotal.append(df.at[i,'TotalRuns']/df.at[i,'TotalOvers'])
    else:
         EconomyRateTotal.append(10)
df["EconomyRateTotal"] = EconomyRateTotal  



'''Calculation of Career SR'''


SRTotal=[]   

for i in range(0,columnNum):
    if(df.at[i,'TotalWickets']!=0):
        SRTotal.append(df.at[i,'TotalBalls']/df.at[i,'TotalWickets'])
    else:
        SRTotal.append(100)

df["SRTotal"] = SRTotal  





'''Calculation of Match-wise SR'''


SRMatch=[]   

for i in range(0,columnNum):
    if(df.at[i,'WicketsCric']):
        SRMatch.append(df.at[i,'Balls']/df.at[i,'WicketsCric'])
    else:
        SRMatch.append(100)

df["SRMatch"] = SRMatch  

#####################################
######################################
#########################################
#####################################
######################################
#########################################
#####################################
######################################
#########################################


########################################################################
        ########################
        ########################
        ########################
########Opposition Experience########
########################

ex1=0
ex2=0
ex3=0
ex4=0
ex5=0
ex6=0
ex7=0
ex8=0
ex9=0
ex10=0
ex11=0
ex12=0
OppositionExp=[]   
for i in range(0,columnNum):
    val=df.at[i,'OppositionIndex']
    if(val==1):
            ex1=ex1+1
            OppositionExp.append(ex1)
    elif(val==2):
            ex2=ex2+1
            OppositionExp.append(ex2)
    elif(val==3):
            ex3=ex3+1
            OppositionExp.append(ex3)
    elif(val==4):
            ex4=ex4+1
            OppositionExp.append(ex4)
    elif(val==5):
            ex5=ex5+1
            OppositionExp.append(ex5)
    elif(val==6):
            ex6=ex6+1
            OppositionExp.append(ex6)
    elif(val==7):
            ex7=ex7+1
            OppositionExp.append(ex7)
    elif(val==8):
            ex8=ex8+1
            OppositionExp.append(ex8)
    elif(val==9):
            ex9=ex9+1
            OppositionExp.append(ex9)
    elif(val==10):
            ex10=ex10+1
            OppositionExp.append(ex10)
    elif(val==11):
            ex11=ex11+1
            OppositionExp.append(ex11)
    elif(val==12):
            ex12=ex12+1
            OppositionExp.append(ex12)
    else:
            OppositionExp.append(0)
df["OppositionExp"] = OppositionExp   
#####################################
######################################
#########################################
#####################################
######################################
#########################################
#####################################
######################################
##############################################################################

''' Calculation of 3+ Wickets in Career'''


TotalThreeOutNumber=0
ThreeWicketHaul=[]
for i in range(0,columnNum):
    if (df.at[i,'WicketsCric']>=3):
        TotalThreeOutNumber=TotalThreeOutNumber+1
        ThreeWicketHaul.append(TotalThreeOutNumber)
    else:
        ThreeWicketHaul.append(TotalThreeOutNumber)

df["ThreeWicketHaul"]=ThreeWicketHaul


####################################
####################################

''' Calculation of 3+ Wickets in Match'''


ThreeWicketHaulMatch=[]
for i in range(0,columnNum):
    if (df.at[i,'WicketsCric']>=3):

        ThreeWicketHaulMatch.append(1)
    else:
        ThreeWicketHaulMatch.append(0)

df["ThreeWicketHaulMatch"]=ThreeWicketHaulMatch
####################################
'''Matches played in a single season'''
################################


SMatch=[]
count=0
for i in range (a[0]):
    if(i!=a[0]-1):

        x=pd.to_datetime(df.at[i+1,'Date'])
        z=pd.to_datetime(df.at[i,'Date'])
        m=(x-z).days
        if m>=100:
            SMatch.append(count+1)
            count=0
        else:
            count=count+1
            SMatch.append(count)
    else:
        SMatch.append(count)
    
df["SMatch"] = SMatch  
##############################
################################

'''Seasonwise Over,Ball,Wicket,Avg,SR,Economy'''
##############################
#################################


SRun=[]
SOut=[]
SBall=[]
SThreeHaul=[]
SOver=[]
SZero=[]
run=0
ball=0
out=0
threehaul=0
over=0
zero=0
count=2

for i in range (b[0]):
    if(i!=b[0]-1):
        
        if  (df.at[i,'SMatch']- df.at[i+1,'SMatch'])<0 :
            run+=df.at[i,'Runs']
            SRun.append(run)
            
            ball+=df.at[i,'Balls']
            SBall.append(ball)
            
            over+=df.at[i,'Overs']
            SOver.append(over)
            
            out+=df.at[i,'WicketsCric']
            SOut.append(out)
            
            if df.at[i,'WicketsCric']>=3:
                threehaul=threehaul+1
                SThreeHaul.append(threehaul)
            else:
                SThreeHaul.append(threehaul)
            
    

        else:
            run+=df.at[i,'Runs']
            SRun.append(run)
            run=0
            ball+=df.at[i,'Balls']
            SBall.append(ball)
            ball=0
            out+=df.at[i,'WicketsCric']
            SOut.append(out)
            out=0 
            over+=df.at[i,'Overs']
            SOver.append(over)
            over=0
            if df.at[i,'WicketsCric']>=3:
                threehaul=threehaul+1
                SThreeHaul.append(threehaul)
                threehaul=0
            else:
               SThreeHaul.append(threehaul)
               threehaul=0
 
               
               
               
    else:

        SRun.append(SRun[i-1]+df.at[i,'Runs'])
           
       
        SBall.append(SBall[i-1]+df.at[i,'Balls'])
           
        
        SOut.append(SOut[i-1]+df.at[i,'WicketsCric'])
        
        SOver.append(SOver[i-1]+df.at[i,'Overs'])
        
        
        if df.at[i,'WicketsCric']>=3:
                threehaul=threehaul+1
                SThreeHaul.append(threehaul)
                
        else:
             SThreeHaul.append(threehaul)
         

                                               
df["SRun"] = SRun  
df["SBall"] = SBall  
df["SOut"] = SOut  
df["SThreeHaul"] = SThreeHaul  
df["SOver"] = SOver  





#####################################
######################################
#########################################



'''Calculation of SeasonWise Average'''


SAvg=[]   



for i in range(0,columnNum):
    if(df.at[i,'SOut']!=0):
        SAvg.append(df.at[i,'SRun']/df.at[i,'SOut'])
    else:
        SAvg.append(100)

df["SAvg"] = SAvg  


'''Calculation of Season-wise Economy Rate'''


SEr=[]   

for i in range(0,columnNum):
    if(df.at[i,'SOver']!=0):
        SEr.append(df.at[i,'SRun']/df.at[i,'SOver'])
    else:
        SEr.append(10)

df["SEr"] = SEr  





'''Calculation of SeasonWise SR'''


SSr=[]   

for i in range(0,columnNum):
    if(df.at[i,'SOut']!=0):
        SSr.append(df.at[i,'SBall']/df.at[i,'SOut'])
    else:
        SSr.append(100)

df["SSr"] = SSr  



#####################################
######################################
#########################################
#####################################
######################################
#########################################
#####################################
######################################
#########################################

#For NoOfInningsConsistency###############
############################

MatchCon=[]
for value in df["Match"]:
    if value>=0 and value<=16:
        MatchCon.append(1)
    elif value>=17 and value<=31:
        MatchCon.append(2)
    elif value>=32 and value<=75:
        MatchCon.append(3)
    elif value>=76 and value<=119:
        MatchCon.append(4)
    elif value>=119 :
        MatchCon.append(5)
df["MatchCon"] = MatchCon   




################################
################################




#For NoOfInnings Form############
############################

MatchForm=[]
for value in df["SMatch"]:
    if value>=0 and value<=3:
        MatchForm.append(1)
    elif value>=4 and value<=8:
        MatchForm.append(2)
    elif value>=9 and value<=10:
        MatchForm.append(3)
    elif value>=11 and value<=13:
        MatchForm.append(4)
    elif value>=14 :
        MatchForm.append(5)
df["MatchForm"] = MatchForm   





################################
################################



#For NoOfInnings Venue############
####################

MatchVen=[]
for value in df["VenueExp"]:
    if value>=0 and value<=11:
        MatchVen.append(1)
    elif value>=12 and value<=19:
        MatchVen.append(2)
    elif value>=20 and value<=34:
        MatchVen.append(3)
    elif value>=35 and value<=49:
        MatchVen.append(4)
    elif value>=50 :
        MatchVen.append(5)
df["MatchVen"] = MatchVen 


################################
################################



#For NoOfInnings Opposition ########
####################

MatchOpp=[]
for value in df["OppositionExp"]:
    if value>=0 and value<=7:
        MatchOpp.append(1)
    elif value>=8 and value<=12:
        MatchOpp.append(2)
    elif value>=13 and value<=18:
        MatchOpp.append(3)
    elif value>=19 and value<=24:
        MatchOpp.append(4)
    elif value>=25 :
        MatchOpp.append(5)
df["MatchOpp"] = MatchOpp 


################################
################################





#For Overs Consistency###############
############################

OverCon=[]
for value in df["TotalOvers"]:
    if value>=0 and value<=52.9:
        OverCon.append(1)
    elif value>=53 and value<=101.9:
        OverCon.append(2)
    elif value>=102 and value<=499.9:
        OverCon.append(3)
    elif value>=500 and value<=255.9:
        OverCon.append(4)
    elif value>=256 :
        OverCon.append(5)
df["OverCon"] = OverCon   




################################
################################




#For NoOfInnings Form############
############################

OverForm=[]
for value in df["SOver"]:
    if value>=1 and value<=9.5:
        OverForm.append(1)
    elif value>=10 and value<=24.5:
        OverForm.append(2)
    elif value>=25 and value<=49.5:
        OverForm.append(3)
    elif value>=50 and value<=99.5:
        OverForm.append(4)
    elif value>=100 :
        OverForm.append(5)
df["OverForm"] = OverForm   





################################
################################



#For NoOfInnings Venue############
####################
################################
################################
## TotalOvers in a particular venue
overven1=0
overven2=0
overven3=0
overven4=0
overven5=0
overven6=0
overven7=0
overven8=0
overven9=0
overven10=0
overven11=0
overven12=0
overven13=0
overven14=0
overven15=0
overven16=0
overven17=0
overven18=0
overven19=0
overven20=0
overven21=0
overven22=0
overven23=0
overven24=0
overven25=0
overven26=0
overven27=0


VenueOver=[]   

for i in range(0,columnNum):
    val=df.at[i,'VenueIndex']
    if(val==1):
        overven1=overven1+df.at[i,'Overs']
        VenueOver.append(overven1)
    elif(val==2):
        overven2=overven2+df.at[i,'Overs']
        VenueOver.append(overven2)
    elif(val==3):
        overven3=overven3+df.at[i,'Overs']
        VenueOver.append(overven3)
    elif(val==4):
        overven4=overven4+df.at[i,'Overs']
        VenueOver.append(overven4)
    elif(val==5):
        overven5=overven5+df.at[i,'Overs']
        VenueOver.append(overven5)
    elif(val==6):
        overven6=overven6+df.at[i,'Overs']
        VenueOver.append(overven6)
    elif(val==7):
        overven7=overven7+df.at[i,'Overs']
        VenueOver.append(overven7)
    elif(val==8):
        overven8=overven8+df.at[i,'Overs']
        VenueOver.append(overven8)
    elif(val==9):
        overven9=overven9+df.at[i,'Overs']
        VenueOver.append(overven9)
    elif(val==10):
        overven10=overven10+df.at[i,'Overs']
        VenueOver.append(overven10)
    elif(val==11):
        overven11=overven11+df.at[i,'Overs']
        VenueOver.append(overven11)
    elif(val==12):
        overven12=overven12+df.at[i,'Overs']
        VenueOver.append(overven12)
    elif(val==13):
        overven13=overven13+df.at[i,'Overs']
        VenueOver.append(overven13)
    elif(val==14):
        overven14=overven14+df.at[i,'Overs']
        VenueOver.append(overven14)
    elif(val==15):
        overven15=overven15+df.at[i,'Overs']
        VenueOver.append(overven15)
    elif(val==16):
        overven16=overven16+df.at[i,'Overs']
        VenueOver.append(overven16)
    elif(val==17):
        overven17=overven17+df.at[i,'Overs']
        VenueOver.append(overven17)
    elif(val==18):
        overven18=overven18+df.at[i,'Overs']
        VenueOver.append(overven18)
    elif(val==19):
        overven19=overven19+df.at[i,'Overs']
        VenueOver.append(overven19)
    elif(val==20):
        overven20=overven20+df.at[i,'Overs']
        VenueOver.append(overven20)
    elif(val==21):
        overven21=overven21+df.at[i,'Overs']
        VenueOver.append(overven21)
    elif(val==22):
        overven22=overven22+df.at[i,'Overs']
        VenueOver.append(overven22)
    elif(val==23):
        overven23=overven23+df.at[i,'Overs']
        VenueOver.append(overven23)
    elif(val==24):
        overven24=overven24+df.at[i,'Overs']
        VenueOver.append(overven24)
    elif(val==25):
        overven25=overven25+df.at[i,'Overs']
        VenueOver.append(overven25)
    elif(val==26):
        overven26=overven26+df.at[i,'Overs']
        VenueOver.append(overven26)
    elif(val==27):
        overven27=overven27+df.at[i,'Overs']
        VenueOver.append(overven27)
    else:
        VenueOver.append(0)
   
df["VenueOver"]=VenueOver


################################
################################
## TotalRuns in A particular venue
runven1=0
runven2=0
runven3=0
runven4=0
runven5=0
runven6=0
runven7=0
runven8=0
runven9=0
runven10=0
runven11=0
runven12=0
runven13=0
runven14=0
runven15=0
runven16=0
runven17=0
runven18=0
runven19=0
runven20=0
runven21=0
runven22=0
runven23=0
runven24=0
runven25=0
runven26=0
runven27=0


VenueRun=[]   

for i in range(0,columnNum):
    val=df.at[i,'VenueIndex']
    if(val==1):
        runven1=runven1+df.at[i,'Runs']
        VenueRun.append(runven1)
    elif(val==2):
        runven2=runven2+df.at[i,'Runs']
        VenueRun.append(runven2)
    elif(val==3):
        runven3=runven3+df.at[i,'Runs']
        VenueRun.append(runven3)
    elif(val==4):
        runven4=runven4+df.at[i,'Runs']
        VenueRun.append(runven4)
    elif(val==5):
        runven5=runven5+df.at[i,'Runs']
        VenueRun.append(runven5)
    elif(val==6):
        runven6=runven6+df.at[i,'Runs']
        VenueRun.append(runven6)
    elif(val==7):
        runven7=runven7+df.at[i,'Runs']
        VenueRun.append(runven7)
    elif(val==8):
        runven8=runven8+df.at[i,'Runs']
        VenueRun.append(runven8)
    elif(val==9):
        runven9=runven9+df.at[i,'Runs']
        VenueRun.append(runven9)
    elif(val==10):
        runven10=runven10+df.at[i,'Runs']
        VenueRun.append(runven10)
    elif(val==11):
        runven11=runven11+df.at[i,'Runs']
        VenueRun.append(runven11)
    elif(val==12):
        runven12=runven12+df.at[i,'Runs']
        VenueRun.append(runven12)
    elif(val==13):
        runven13=runven13+df.at[i,'Runs']
        VenueRun.append(runven13)
    elif(val==14):
        runven14=runven14+df.at[i,'Runs']
        VenueRun.append(runven14)
    elif(val==15):
        runven15=runven15+df.at[i,'Runs']
        VenueRun.append(runven15)
    elif(val==16):
        runven16=runven16+df.at[i,'Runs']
        VenueRun.append(runven16)
    elif(val==17):
        runven17=runven17+df.at[i,'Runs']
        VenueRun.append(runven17)
    elif(val==18):
        runven18=runven18+df.at[i,'Runs']
        VenueRun.append(runven18)
    elif(val==19):
        runven19=runven19+df.at[i,'Runs']
        VenueRun.append(runven19)
    elif(val==20):
        runven20=runven20+df.at[i,'Runs']
        VenueRun.append(runven20)
    elif(val==21):
        runven21=runven21+df.at[i,'Runs']
        VenueRun.append(runven21)
    elif(val==22):
        runven22=runven22+df.at[i,'Runs']
        VenueRun.append(runven22)
    elif(val==23):
        runven23=runven23+df.at[i,'Runs']
        VenueRun.append(runven23)
    elif(val==24):
        runven24=runven24+df.at[i,'Runs']
        VenueRun.append(runven24)
    elif(val==25):
        runven25=runven25+df.at[i,'Runs']
        VenueRun.append(runven25)
    elif(val==26):
        runven26=runven26+df.at[i,'Runs']
        VenueRun.append(runven26)
    elif(val==27):
        runven27=runven27+df.at[i,'Runs']
        VenueRun.append(runven27)
    else:
        VenueRun.append(0)
   
df["VenueRun"]=VenueRun


######## Venue Total Out
outven1=0
outven2=0
outven3=0
outven4=0
outven5=0
outven6=0
outven7=0
outven8=0
outven9=0
outven10=0
outven11=0
outven12=0
outven13=0
outven14=0
outven15=0
outven16=0
outven17=0
outven18=0
outven19=0
outven20=0
outven21=0
outven22=0
outven23=0
outven24=0
outven25=0
outven26=0
outven27=0
VenueTotalOut=[]  
 

for i in range(0,columnNum):
    val=df.at[i,'VenueIndex']
    if(val==1):
        outven1=outven1+df.at[i,'WicketsCric']
        VenueTotalOut.append(outven1)
    elif(val==2):
        outven2=outven2+df.at[i,'WicketsCric']
        VenueTotalOut.append(outven2)
    elif(val==3):
        outven3=outven3+df.at[i,'WicketsCric']
        VenueTotalOut.append(outven3)
    elif(val==4):
        outven4=outven4+df.at[i,'WicketsCric']
        VenueTotalOut.append(outven4)
    elif(val==5):
        outven5=outven5+df.at[i,'WicketsCric']
        VenueTotalOut.append(outven5)
    elif(val==6):
        outven6=outven6+df.at[i,'WicketsCric']
        VenueTotalOut.append(outven6)
    elif(val==7):
        outven7=outven7+df.at[i,'WicketsCric']
        VenueTotalOut.append(outven7)
    elif(val==8):
        outven8=outven8+df.at[i,'WicketsCric']
        VenueTotalOut.append(outven8)
    elif(val==9):
        outven9=outven9+df.at[i,'WicketsCric']
        VenueTotalOut.append(outven9)
    elif(val==10):
        outven10=outven10+df.at[i,'WicketsCric']
        VenueTotalOut.append(outven10)
    elif(val==11):
        outven11=outven11+df.at[i,'WicketsCric']
        VenueTotalOut.append(outven11)
    elif(val==12):
        outven12=outven12+df.at[i,'WicketsCric']
        VenueTotalOut.append(outven12)
    elif(val==13):
        outven13=outven13+df.at[i,'WicketsCric']
        VenueTotalOut.append(outven13)
    elif(val==14):
        outven14=outven14+df.at[i,'WicketsCric']
        VenueTotalOut.append(outven14)
    elif(val==15):
        outven15=outven15+df.at[i,'WicketsCric']
        VenueTotalOut.append(outven15)
    elif(val==16):
        outven16=outven16+df.at[i,'WicketsCric']
        VenueTotalOut.append(outven16)
    elif(val==17):
        outven17=outven17+df.at[i,'WicketsCric']
        VenueTotalOut.append(outven17)
    elif(val==18):
        outven18=outven18+df.at[i,'WicketsCric']
        VenueTotalOut.append(outven18)
    elif(val==19):
        outven19=outven19+df.at[i,'WicketsCric']
        VenueTotalOut.append(outven19)
    elif(val==20):
        outven20=outven20+df.at[i,'WicketsCric']
        VenueTotalOut.append(outven20)
    elif(val==21):
        outven21=outven21+df.at[i,'WicketsCric']
        VenueTotalOut.append(outven21)
    elif(val==22):
        outven22=outven22+df.at[i,'WicketsCric']
        VenueTotalOut.append(outven22)
    elif(val==23):
        outven23=outven23+df.at[i,'WicketsCric']
        VenueTotalOut.append(outven23)
    elif(val==24):
        outven24=outven24+df.at[i,'WicketsCric']
        VenueTotalOut.append(outven24)
    elif(val==25):
        outven25=outven25+df.at[i,'WicketsCric']
        VenueTotalOut.append(outven25)
    elif(val==26):
        outven26=outven26+df.at[i,'WicketsCric']
        VenueTotalOut.append(outven26)
    elif(val==27):
        outven27=outven27+df.at[i,'WicketsCric']
        VenueTotalOut.append(outven27)
    else:
        VenueTotalOut.append(0)
   
df["VenueTotalOut"]=VenueTotalOut


######## Venue Total Balls
ballven1=0
ballven2=0
ballven3=0
ballven4=0
ballven5=0
ballven6=0
ballven7=0
ballven8=0
ballven9=0
ballven10=0
ballven11=0
ballven12=0
ballven13=0
ballven14=0
ballven15=0
ballven16=0
ballven17=0
ballven18=0
ballven19=0
ballven20=0
ballven21=0
ballven22=0
ballven23=0
ballven24=0
ballven25=0
ballven26=0
ballven27=0
VenueTotalBall=[]  
 

for i in range(0,columnNum):
    val=df.at[i,'VenueIndex']
    if(val==1):
        ballven1=ballven1+df.at[i,'Balls']
        VenueTotalBall.append(ballven1)
    elif(val==2):
        ballven2=ballven2+df.at[i,'Balls']
        VenueTotalBall.append(ballven2)
    elif(val==3):
        ballven3=ballven3+df.at[i,'Balls']
        VenueTotalBall.append(ballven3)
    elif(val==4):
        ballven4=ballven4+df.at[i,'Balls']
        VenueTotalBall.append(ballven4)
    elif(val==5):
        ballven5=ballven5+df.at[i,'Balls']
        VenueTotalBall.append(ballven5)
    elif(val==6):
        ballven6=ballven6+df.at[i,'Balls']
        VenueTotalBall.append(ballven6)
    elif(val==7):
        ballven7=ballven7+df.at[i,'Balls']
        VenueTotalBall.append(ballven7)
    elif(val==8):
        ballven8=ballven8+df.at[i,'Balls']
        VenueTotalBall.append(ballven8)
    elif(val==9):
        ballven9=ballven9+df.at[i,'Balls']
        VenueTotalBall.append(ballven9)
    elif(val==10):
        ballven10=ballven10+df.at[i,'Balls']
        VenueTotalBall.append(ballven10)
    elif(val==11):
        ballven11=ballven11+df.at[i,'Balls']
        VenueTotalBall.append(ballven11)
    elif(val==12):
        ballven12=ballven12+df.at[i,'Balls']
        VenueTotalBall.append(ballven12)
    elif(val==13):
        ballven13=ballven13+df.at[i,'Balls']
        VenueTotalBall.append(ballven13)
    elif(val==14):
        ballven14=ballven14+df.at[i,'Balls']
        VenueTotalBall.append(ballven14)
    elif(val==15):
        ballven15=ballven15+df.at[i,'Balls']
        VenueTotalBall.append(ballven15)
    elif(val==16):
        ballven16=ballven16+df.at[i,'Balls']
        VenueTotalBall.append(ballven16)
    elif(val==17):
        ballven17=ballven17+df.at[i,'Balls']
        VenueTotalBall.append(ballven17)
    elif(val==18):
        ballven18=ballven18+df.at[i,'Balls']
        VenueTotalBall.append(ballven18)
    elif(val==19):
        ballven19=ballven19+df.at[i,'Balls']
        VenueTotalBall.append(ballven19)
    elif(val==20):
        ballven20=ballven20+df.at[i,'Balls']
        VenueTotalBall.append(ballven20)
    elif(val==21):
        ballven21=ballven21+df.at[i,'Balls']
        VenueTotalBall.append(ballven21)
    elif(val==22):
        ballven22=ballven22+df.at[i,'Balls']
        VenueTotalBall.append(ballven22)
    elif(val==23):
        ballven23=ballven23+df.at[i,'Balls']
        VenueTotalBall.append(ballven23)
    elif(val==24):
        ballven24=ballven24+df.at[i,'Balls']
        VenueTotalBall.append(ballven24)
    elif(val==25):
        ballven25=ballven25+df.at[i,'Balls']
        VenueTotalBall.append(ballven25)
    elif(val==26):
        ballven26=ballven26+df.at[i,'Balls']
        VenueTotalBall.append(ballven26)
    elif(val==27):
        ballven27=ballven27+df.at[i,'Balls']
        VenueTotalBall.append(ballven27)
    else:
        VenueTotalBall.append(0)
   
df["VenueTotalBall"]=VenueTotalBall



############## Venuewise Three wicket Haul
TotalThreeOutNumber1=0
TotalThreeOutNumber2=0
TotalThreeOutNumber3=0
TotalThreeOutNumber4=0
TotalThreeOutNumber5=0
TotalThreeOutNumber6=0
TotalThreeOutNumber7=0
TotalThreeOutNumber8=0
TotalThreeOutNumber9=0
TotalThreeOutNumber10=0
TotalThreeOutNumber11=0
TotalThreeOutNumber12=0
TotalThreeOutNumber13=0
TotalThreeOutNumber14=0
TotalThreeOutNumber15=0
TotalThreeOutNumber16=0
TotalThreeOutNumber17=0
TotalThreeOutNumber18=0
TotalThreeOutNumber19=0
TotalThreeOutNumber20=0
TotalThreeOutNumber21=0
TotalThreeOutNumber22=0
TotalThreeOutNumber23=0
TotalThreeOutNumber24=0
TotalThreeOutNumber25=0
TotalThreeOutNumber26=0
TotalThreeOutNumber27=0
VenThreeWicketHaul=[]  
 

for i in range(0,columnNum):
    val=df.at[i,'VenueIndex']
    if(val==1):
        if (df.at[i,'WicketsCric']>=3):
            TotalThreeOutNumber1=TotalThreeOutNumber1+1
            VenThreeWicketHaul.append(TotalThreeOutNumber1)
        else:
            VenThreeWicketHaul.append(TotalThreeOutNumber1)

    elif(val==2):
        if (df.at[i,'WicketsCric']>=3):
            TotalThreeOutNumber2=TotalThreeOutNumber2+1
            VenThreeWicketHaul.append(TotalThreeOutNumber2)
        else:
            VenThreeWicketHaul.append(TotalThreeOutNumber2)
    elif(val==3):
        if (df.at[i,'WicketsCric']>=3):
            TotalThreeOutNumber3=TotalThreeOutNumber3+1
            VenThreeWicketHaul.append(TotalThreeOutNumber3)
        else:
            VenThreeWicketHaul.append(TotalThreeOutNumber3)
    elif(val==4):
        if (df.at[i,'WicketsCric']>=3):
            TotalThreeOutNumber4=TotalThreeOutNumber4+1
            VenThreeWicketHaul.append(TotalThreeOutNumber4)
        else:
            VenThreeWicketHaul.append(TotalThreeOutNumber4)
    elif(val==5):
        if (df.at[i,'WicketsCric']>=3):
            TotalThreeOutNumber5=TotalThreeOutNumber5+1
            VenThreeWicketHaul.append(TotalThreeOutNumber5)
        else:
            VenThreeWicketHaul.append(TotalThreeOutNumber5)
    elif(val==6):
        if (df.at[i,'WicketsCric']>=3):
            TotalThreeOutNumber6=TotalThreeOutNumber6+1
            VenThreeWicketHaul.append(TotalThreeOutNumber6)
        else:
            VenThreeWicketHaul.append(TotalThreeOutNumber6)
    elif(val==7):
        if (df.at[i,'WicketsCric']>=3):
            TotalThreeOutNumber7=TotalThreeOutNumber7+1
            VenThreeWicketHaul.append(TotalThreeOutNumber7)
        else:
            VenThreeWicketHaul.append(TotalThreeOutNumber7)
    elif(val==8):
        if (df.at[i,'WicketsCric']>=3):
            TotalThreeOutNumber8=TotalThreeOutNumber8+1
            VenThreeWicketHaul.append(TotalThreeOutNumber8)
        else:
            VenThreeWicketHaul.append(TotalThreeOutNumber8)
    elif(val==9):
        if (df.at[i,'WicketsCric']>=3):
            TotalThreeOutNumber9=TotalThreeOutNumber9+1
            VenThreeWicketHaul.append(TotalThreeOutNumber9)
        else:
            VenThreeWicketHaul.append(TotalThreeOutNumber9)
    elif(val==10):
        if (df.at[i,'WicketsCric']>=3):
            TotalThreeOutNumber10=TotalThreeOutNumber10+1
            VenThreeWicketHaul.append(TotalThreeOutNumber10)
        else:
            VenThreeWicketHaul.append(TotalThreeOutNumber10)
    elif(val==11):
        if (df.at[i,'WicketsCric']>=3):
            TotalThreeOutNumber11=TotalThreeOutNumber11+1
            VenThreeWicketHaul.append(TotalThreeOutNumber11)
        else:
            VenThreeWicketHaul.append(TotalThreeOutNumber11)
    elif(val==12):
        if (df.at[i,'WicketsCric']>=3):
            TotalThreeOutNumber12=TotalThreeOutNumber12+1
            VenThreeWicketHaul.append(TotalThreeOutNumber12)
        else:
            VenThreeWicketHaul.append(TotalThreeOutNumber12)
    elif(val==13):
        if (df.at[i,'WicketsCric']>=3):
            TotalThreeOutNumber13=TotalThreeOutNumber13+1
            VenThreeWicketHaul.append(TotalThreeOutNumber13)
        else:
            VenThreeWicketHaul.append(TotalThreeOutNumber13)
    elif(val==14):
        if (df.at[i,'WicketsCric']>=3):
            TotalThreeOutNumber14=TotalThreeOutNumber14+1
            VenThreeWicketHaul.append(TotalThreeOutNumber14)
        else:
            VenThreeWicketHaul.append(TotalThreeOutNumber14)
    elif(val==15):
        if (df.at[i,'WicketsCric']>=3):
            TotalThreeOutNumber15=TotalThreeOutNumber15+1
            VenThreeWicketHaul.append(TotalThreeOutNumber15)
        else:
            VenThreeWicketHaul.append(TotalThreeOutNumber15)
    elif(val==16):
        if (df.at[i,'WicketsCric']>=3):
            TotalThreeOutNumber16=TotalThreeOutNumber16+1
            VenThreeWicketHaul.append(TotalThreeOutNumber16)
        else:
            VenThreeWicketHaul.append(TotalThreeOutNumber16)
    elif(val==17):
        if (df.at[i,'WicketsCric']>=3):
            TotalThreeOutNumber17=TotalThreeOutNumber17+1
            VenThreeWicketHaul.append(TotalThreeOutNumber17)
        else:
            VenThreeWicketHaul.append(TotalThreeOutNumber17)
    elif(val==18):
        if (df.at[i,'WicketsCric']>=3):
            TotalThreeOutNumber18=TotalThreeOutNumber18+1
            VenThreeWicketHaul.append(TotalThreeOutNumber18)
        else:
            VenThreeWicketHaul.append(TotalThreeOutNumber18)
    elif(val==19):
        if (df.at[i,'WicketsCric']>=3):
            TotalThreeOutNumber19=TotalThreeOutNumber19+1
            VenThreeWicketHaul.append(TotalThreeOutNumber19)
        else:
            VenThreeWicketHaul.append(TotalThreeOutNumber19)
    elif(val==20):
        if (df.at[i,'WicketsCric']>=3):
            TotalThreeOutNumber20=TotalThreeOutNumber20+1
            VenThreeWicketHaul.append(TotalThreeOutNumber20)
        else:
            VenThreeWicketHaul.append(TotalThreeOutNumber20)
    elif(val==21):
        if (df.at[i,'WicketsCric']>=3):
            TotalThreeOutNumber21=TotalThreeOutNumber21+1
            VenThreeWicketHaul.append(TotalThreeOutNumber21)
        else:
            VenThreeWicketHaul.append(TotalThreeOutNumber21)
    elif(val==22):
        if (df.at[i,'WicketsCric']>=3):
            TotalThreeOutNumber22=TotalThreeOutNumber22+1
            VenThreeWicketHaul.append(TotalThreeOutNumber22)
        else:
            VenThreeWicketHaul.append(TotalThreeOutNumber22)
    elif(val==23):
        if (df.at[i,'WicketsCric']>=3):
            TotalThreeOutNumber23=TotalThreeOutNumber23+1
            VenThreeWicketHaul.append(TotalThreeOutNumber23)
        else:
            VenThreeWicketHaul.append(TotalThreeOutNumber23)
    elif(val==24):
        if (df.at[i,'WicketsCric']>=3):
            TotalThreeOutNumber24=TotalThreeOutNumber24+1
            VenThreeWicketHaul.append(TotalThreeOutNumber24)
        else:
            VenThreeWicketHaul.append(TotalThreeOutNumber24)
    elif(val==25):
        if (df.at[i,'WicketsCric']>=3):
            TotalThreeOutNumber25=TotalThreeOutNumber25+1
            VenThreeWicketHaul.append(TotalThreeOutNumber25)
        else:
            VenThreeWicketHaul.append(TotalThreeOutNumber25)
    elif(val==26):
        if (df.at[i,'WicketsCric']>=3):
            TotalThreeOutNumber26=TotalThreeOutNumber26+1
            VenThreeWicketHaul.append(TotalThreeOutNumber26)
        else:
            VenThreeWicketHaul.append(TotalThreeOutNumber26)
    elif(val==27):
        if (df.at[i,'WicketsCric']>=3):
            TotalThreeOutNumber27=TotalThreeOutNumber27+1
            VenThreeWicketHaul.append(TotalThreeOutNumber27)
        else:
            VenThreeWicketHaul.append(TotalThreeOutNumber27)
    else:
        VenThreeWicketHaul.append(0)
   
df["VenThreeWicketHaul"]=VenThreeWicketHaul




######################################
#########################################



'''Calculation of Venuewise Average'''


VAvg=[]   

for i in range(0,columnNum):
    if df.at[i,'VenueTotalOut']!=0:
    
        VAvg.append(df.at[i,'VenueRun']/df.at[i,'VenueTotalOut'])
    else:
        VAvg.append(100)

df["VAvg"] = VAvg  


'''Calculation of Venue-wise Economy Rate'''


VEr=[]   

for i in range(0,columnNum):
    if df.at[i,'VenueOver']!=0:
        VEr.append(df.at[i,'VenueRun']/df.at[i,'VenueOver'])
    else: 
        VEr.append(10)

df["VEr"] = VEr  





'''Calculation of VenueWise SR'''


VSr=[]   

for i in range(0,columnNum):
    if df.at[i,'VenueTotalOut']!=0:
        VSr.append(df.at[i,'VenueTotalBall']/df.at[i,'VenueTotalOut'])
    else:
        VSr.append(100)

df["VSr"] = VSr  



#####################################

#####################################



################################
################################
## TotalRuns against a particular Opposition
runopp1=0
runopp2=0
runopp3=0
runopp4=0
runopp5=0
runopp6=0
runopp7=0
runopp8=0
runopp9=0
runopp10=0
runopp11=0
runopp12=0


OppRun=[]   

for i in range(0,columnNum):
    val=df.at[i,'OppositionIndex']
    if(val==1):
        runopp1=runopp1+df.at[i,'Runs']
        OppRun.append(runopp1)
    elif(val==2):
        runopp2=runopp2+df.at[i,'Runs']
        OppRun.append(runopp2)
    elif(val==3):
        runopp3=runopp3+df.at[i,'Runs']
        OppRun.append(runopp3)
    elif(val==4):
        runopp4=runopp4+df.at[i,'Runs']
        OppRun.append(runopp4)
    elif(val==5):
        runopp5=runopp5+df.at[i,'Runs']
        OppRun.append(runopp5)
    elif(val==6):
        runopp6=runopp6+df.at[i,'Runs']
        OppRun.append(runopp6)
    elif(val==7):
        runopp7=runopp7+df.at[i,'Runs']
        OppRun.append(runopp7)
    elif(val==8):
        runopp8=runopp8+df.at[i,'Runs']
        OppRun.append(runopp8)
    elif(val==9):
        runopp9=runopp9+df.at[i,'Runs']
        OppRun.append(runopp9)
    elif(val==10):
        runopp10=runopp10+df.at[i,'Runs']
        OppRun.append(runopp10)
    elif(val==11):
        runopp11=runopp11+df.at[i,'Runs']
        OppRun.append(runopp11)
    elif(val==12):
        runopp12=runopp12+df.at[i,'Runs']
        OppRun.append(runopp12)

    else:
        OppRun.append(0)
   
df["OppRun"]=OppRun


######## Opposition Total Out
outopp1=0
outopp2=0
outopp3=0
outopp4=0
outopp5=0
outopp6=0
outopp7=0
outopp8=0
outopp9=0
outopp10=0
outopp11=0
outopp12=0

OppTotalOut=[]  
 

for i in range(0,columnNum):
    val=df.at[i,'OppositionIndex']
    if(val==1):
        outopp1=outopp1+df.at[i,'WicketsCric']
        OppTotalOut.append(outopp1)
    elif(val==2):
        outopp2=outopp2+df.at[i,'WicketsCric']
        OppTotalOut.append(outopp2)
    elif(val==3):
        outopp3=outopp3+df.at[i,'WicketsCric']
        OppTotalOut.append(outopp3)
    elif(val==4):
        outopp4=outopp4+df.at[i,'WicketsCric']
        OppTotalOut.append(outopp4)
    elif(val==5):
        outopp5=outopp5+df.at[i,'WicketsCric']
        OppTotalOut.append(outopp5)
    elif(val==6):
        outopp6=outopp6+df.at[i,'WicketsCric']
        OppTotalOut.append(outopp6)
    elif(val==7):
        outopp7=outopp7+df.at[i,'WicketsCric']
        OppTotalOut.append(outopp7)
    elif(val==8):
        outopp8=outopp8+df.at[i,'WicketsCric']
        OppTotalOut.append(outopp8)
    elif(val==9):
        outopp9=outopp9+df.at[i,'WicketsCric']
        OppTotalOut.append(outopp9)
    elif(val==10):
        outopp10=outopp10+df.at[i,'WicketsCric']
        OppTotalOut.append(outopp10)
    elif(val==11):
        outopp11=outopp11+df.at[i,'WicketsCric']
        OppTotalOut.append(outopp11)
    elif(val==12):
        outopp12=outopp12+df.at[i,'WicketsCric']
        OppTotalOut.append(outopp12)

    else:
        OppTotalOut.append(0)
   
df["OppTotalOut"]=OppTotalOut


######## Opposition Total Balls
ballopp1=0
ballopp2=0
ballopp3=0
ballopp4=0
ballopp5=0
ballopp6=0
ballopp7=0
ballopp8=0
ballopp9=0
ballopp10=0
ballopp11=0
ballopp12=0

OppTotalBall=[]  
 

for i in range(0,columnNum):
    val=df.at[i,'OppositionIndex']
    if(val==1):
        ballopp1=ballopp1+df.at[i,'Balls']
        OppTotalBall.append(ballopp1)
    elif(val==2):
        ballopp2=ballopp2+df.at[i,'Balls']
        OppTotalBall.append(ballopp2)
    elif(val==3):
        ballopp3=ballopp3+df.at[i,'Balls']
        OppTotalBall.append(ballopp3)
    elif(val==4):
        ballopp4=ballopp4+df.at[i,'Balls']
        OppTotalBall.append(ballopp4)
    elif(val==5):
        ballopp5=ballopp5+df.at[i,'Balls']
        OppTotalBall.append(ballopp5)
    elif(val==6):
        ballopp6=ballopp6+df.at[i,'Balls']
        OppTotalBall.append(ballopp6)
    elif(val==7):
        ballopp7=ballopp7+df.at[i,'Balls']
        OppTotalBall.append(ballopp7)
    elif(val==8):
        ballopp8=ballopp8+df.at[i,'Balls']
        OppTotalBall.append(ballopp8)
    elif(val==9):
        ballopp9=ballopp9+df.at[i,'Balls']
        OppTotalBall.append(ballopp9)
    elif(val==10):
        ballopp10=ballopp10+df.at[i,'Balls']
        OppTotalBall.append(ballopp10)
    elif(val==11):
        ballopp11=ballopp11+df.at[i,'Balls']
        OppTotalBall.append(ballopp11)
    elif(val==12):
        ballopp12=ballopp12+df.at[i,'Balls']
        OppTotalBall.append(ballopp12)

    else:
        OppTotalBall.append(0)
   
df["OppTotalBall"]=OppTotalBall



############## Oppwise Three wicket Haul
TotalThreeOutNumberOpp1=0
TotalThreeOutNumberOpp2=0
TotalThreeOutNumberOpp3=0
TotalThreeOutNumberOpp4=0
TotalThreeOutNumberOpp5=0
TotalThreeOutNumberOpp6=0
TotalThreeOutNumberOpp7=0
TotalThreeOutNumberOpp8=0
TotalThreeOutNumberOpp9=0
TotalThreeOutNumberOpp10=0
TotalThreeOutNumberOpp11=0
TotalThreeOutNumberOpp12=0

OppThreeWicketHaul=[]  
 

for i in range(0,columnNum):
    val=df.at[i,'OppositionIndex']
    if(val==1):
        if (df.at[i,'WicketsCric']>=3):
            TotalThreeOutNumberOpp1=TotalThreeOutNumberOpp1+1
            OppThreeWicketHaul.append(TotalThreeOutNumberOpp1)
        else:
            OppThreeWicketHaul.append(TotalThreeOutNumberOpp1)

    elif(val==2):
        if (df.at[i,'WicketsCric']>=3):
            TotalThreeOutNumberOpp2=TotalThreeOutNumberOpp2+1
            OppThreeWicketHaul.append(TotalThreeOutNumberOpp2)
        else:
            OppThreeWicketHaul.append(TotalThreeOutNumberOpp2)
    elif(val==3):
        if (df.at[i,'WicketsCric']>=3):
            TotalThreeOutNumberOpp3=TotalThreeOutNumberOpp3+1
            OppThreeWicketHaul.append(TotalThreeOutNumberOpp3)
        else:
            OppThreeWicketHaul.append(TotalThreeOutNumberOpp3)
    elif(val==4):
        if (df.at[i,'WicketsCric']>=3):
            TotalThreeOutNumberOpp4=TotalThreeOutNumberOpp4+1
            OppThreeWicketHaul.append(TotalThreeOutNumberOpp4)
        else:
            OppThreeWicketHaul.append(TotalThreeOutNumberOpp4)
    elif(val==5):
        if (df.at[i,'WicketsCric']>=3):
            TotalThreeOutNumberOpp5=TotalThreeOutNumberOpp5+1
            OppThreeWicketHaul.append(TotalThreeOutNumberOpp5)
        else:
            OppThreeWicketHaul.append(TotalThreeOutNumberOpp5)
    elif(val==6):
        if (df.at[i,'WicketsCric']>=3):
            TotalThreeOutNumberOpp6=TotalThreeOutNumberOpp6+1
            OppThreeWicketHaul.append(TotalThreeOutNumberOpp6)
        else:
            OppThreeWicketHaul.append(TotalThreeOutNumberOpp6)
    elif(val==7):
        if (df.at[i,'WicketsCric']>=3):
            TotalThreeOutNumberOpp7=TotalThreeOutNumberOpp7+1
            OppThreeWicketHaul.append(TotalThreeOutNumberOpp7)
        else:
            OppThreeWicketHaul.append(TotalThreeOutNumberOpp7)
    elif(val==8):
        if (df.at[i,'WicketsCric']>=3):
            TotalThreeOutNumberOpp8=TotalThreeOutNumberOpp8+1
            OppThreeWicketHaul.append(TotalThreeOutNumberOpp8)
        else:
            OppThreeWicketHaul.append(TotalThreeOutNumberOpp8)
    elif(val==9):
        if (df.at[i,'WicketsCric']>=3):
            TotalThreeOutNumberOpp9=TotalThreeOutNumberOpp9+1
            OppThreeWicketHaul.append(TotalThreeOutNumberOpp9)
        else:
            OppThreeWicketHaul.append(TotalThreeOutNumberOpp9)
    elif(val==10):
        if (df.at[i,'WicketsCric']>=3):
            TotalThreeOutNumberOpp10=TotalThreeOutNumberOpp10+1
            OppThreeWicketHaul.append(TotalThreeOutNumberOpp10)
        else:
            OppThreeWicketHaul.append(TotalThreeOutNumberOpp10)
    elif(val==11):
        if (df.at[i,'WicketsCric']>=3):
            TotalThreeOutNumberOpp11=TotalThreeOutNumberOpp11+1
            OppThreeWicketHaul.append(TotalThreeOutNumberOpp11)
        else:
            OppThreeWicketHaul.append(TotalThreeOutNumberOpp11)
    elif(val==12):
        if (df.at[i,'WicketsCric']>=3):
            TotalThreeOutNumberOpp12=TotalThreeOutNumberOpp12+1
            OppThreeWicketHaul.append(TotalThreeOutNumberOpp12)
        else:
            OppThreeWicketHaul.append(TotalThreeOutNumberOpp12)

    else:
        OppThreeWicketHaul.append(0)
   
df["OppThreeWicketHaul"]=OppThreeWicketHaul


################################
################################
## TotalOvers against a particular oppotent
overOpp1=0
overOpp2=0
overOpp3=0
overOpp4=0
overOpp5=0
overOpp6=0
overOpp7=0
overOpp8=0
overOpp9=0
overOpp10=0
overOpp11=0
overOpp12=0



OppOver=[]   

for i in range(0,columnNum):
    val=df.at[i,'OppositionIndex']
    if(val==1):
        overOpp1=overOpp1+df.at[i,'Overs']
        OppOver.append(overOpp1)
    elif(val==2):
        overOpp2=overOpp2+df.at[i,'Overs']
        OppOver.append(overOpp2)
    elif(val==3):
        overOpp3=overOpp3+df.at[i,'Overs']
        OppOver.append(overOpp3)
    elif(val==4):
        overOpp4=overOpp4+df.at[i,'Overs']
        OppOver.append(overOpp4)
    elif(val==5):
        overOpp5=overOpp5+df.at[i,'Overs']
        OppOver.append(overOpp5)
    elif(val==6):
        overOpp6=overOpp6+df.at[i,'Overs']
        OppOver.append(overOpp6)
    elif(val==7):
        overOpp7=overOpp7+df.at[i,'Overs']
        OppOver.append(overOpp7)
    elif(val==8):
        overOpp8=overOpp8+df.at[i,'Overs']
        OppOver.append(overOpp8)
    elif(val==9):
        overOpp9=overOpp9+df.at[i,'Overs']
        OppOver.append(overOpp9)
    elif(val==10):
        overOpp10=overOpp10+df.at[i,'Overs']
        OppOver.append(overOpp10)
    elif(val==11):
        overOpp11=overOpp11+df.at[i,'Overs']
        OppOver.append(overOpp11)
    elif(val==12):
        overOpp12=overOpp12+df.at[i,'Overs']
        OppOver.append(overOpp12)
   
    else:
        OppOver.append(0)
   
df["OppOver"]=OppOver




######## OpponentWise Total Balls
ballOpp1=0
ballOpp2=0
ballOpp3=0
ballOpp4=0
ballOpp5=0
ballOpp6=0
ballOpp7=0
ballOpp8=0
ballOpp9=0
ballOpp10=0
ballOpp11=0
ballOpp12=0

OppTotalBall=[]  
 

for i in range(0,columnNum):
    val=df.at[i,'OppositionIndex']
    if(val==1):
        ballOpp1=ballOpp1+df.at[i,'Balls']
        OppTotalBall.append(ballOpp1)
    elif(val==2):
        ballOpp2=ballOpp2+df.at[i,'Balls']
        OppTotalBall.append(ballOpp2)
    elif(val==3):
        ballOpp3=ballOpp3+df.at[i,'Balls']
        OppTotalBall.append(ballOpp3)
    elif(val==4):
        ballOpp4=ballOpp4+df.at[i,'Balls']
        OppTotalBall.append(ballOpp4)
    elif(val==5):
        ballOpp5=ballOpp5+df.at[i,'Balls']
        OppTotalBall.append(ballOpp5)
    elif(val==6):
        ballOpp6=ballOpp6+df.at[i,'Balls']
        OppTotalBall.append(ballOpp6)
    elif(val==7):
        ballOpp7=ballOpp7+df.at[i,'Balls']
        OppTotalBall.append(ballOpp7)
    elif(val==8):
        ballOpp8=ballOpp8+df.at[i,'Balls']
        OppTotalBall.append(ballOpp8)
    elif(val==9):
        ballOpp9=ballOpp9+df.at[i,'Balls']
        OppTotalBall.append(ballOpp9)
    elif(val==10):
        ballOpp10=ballOpp10+df.at[i,'Balls']
        OppTotalBall.append(ballOpp10)
    elif(val==11):
        ballOpp11=ballOpp11+df.at[i,'Balls']
        OppTotalBall.append(ballOpp11)
    elif(val==12):
        ballOpp12=ballOpp12+df.at[i,'Balls']
        OppTotalBall.append(ballOpp12)
    else:
        OppTotalBall.append(0)
   
df["OppTotalBall"]=OppTotalBall




######################################
#########################################



'''Calculation of Opponent wise Average'''


OpAvg=[]   

for i in range(0,columnNum):
    if df.at[i,'OppTotalOut']!=0:
        OpAvg.append(df.at[i,'OppRun']/df.at[i,'OppTotalOut'])
    else:
        OpAvg.append(100)

df["OpAvg"] = OpAvg  


'''Calculation of Opponent-wise Economy Rate'''


OpEr=[]   

for i in range(0,columnNum):
    if(df.at[i,'OppOver']!=0):
        OpEr.append(df.at[i,'OppRun']/df.at[i,'OppOver'])
    else:
        OpEr.append(10)

df["OpEr"] = OpEr  





'''Calculation of OpponentWise SR'''


OpSr=[]   

for i in range(0,columnNum):
    if(df.at[i,'OppTotalOut']!=0):
        OpSr.append(df.at[i,'OppTotalBall']/df.at[i,'OppTotalOut'])
    else:
         OpSr.append(100)

df["OpSr"] = OpSr  




#For Overs Opposition ############
############################

OverCon=[]
for value in df["Overs"]:
    if value>=0 and value<=99.6:
        OverCon.append(1)
    elif value>=100 and value<=199.9:
        OverCon.append(2)
    elif value>=200 and value<=299.6:
        OverCon.append(3)
    elif value>=300 and value<=399.6:
        OverCon.append(4)
    elif value>=400 :
        OverCon.append(5)
df["OverCon"] = OverCon 

#For Overs Opposition ############
############################

OverOpp=[]
for value in df["OppOver"]:
    if value>=0 and value<=5.9:
        OverOpp.append(1)
    elif value>=6 and value<=10.9:
        OverOpp.append(2)
    elif value>=11 and value<=35.9:
        OverOpp.append(3)
    elif value>=36 and value<=60.9:
        OverOpp.append(4)
    elif value>=61 :
        OverOpp.append(5)
df["OverOpp"] = OverOpp   

#ForOvers Venue ############
############################

OverVen=[]
for value in df["VenueOver"]:
    if value>=0 and value<=5.6:
        OverVen.append(1)
    elif value>=6 and value<=10.6:
        OverVen.append(2)
    elif value>=11 and value<=65.6:
        OverVen.append(3)
    elif value>=66 and value<=131.6:
        OverVen.append(4)
    elif value>=132 :
        OverVen.append(5)
df["OverVen"] = OverVen   



#For Avg Consistency ############
############################

AvgCon=[]

for value in df["BowlingAverage"]:
    if value>=0 and value<=20.99:
        AvgCon.append(5)
    elif value>=21 and value<=27.99:
        AvgCon.append(4)
    elif value>=28 and value<=38.99:
        AvgCon.append(3)
    elif value>=39 and value<=49.99:
        AvgCon.append(2)
    elif value>=50 :
        AvgCon.append(1)
df["AvgCon"] = AvgCon   


#For Avg Form ############
############################

AvgForm=[]
for value in df["SAvg"]:
    if value>=0.0 and value<=24.99:
        AvgForm.append(5)
    elif value>=25.0 and value<=29.99:
        AvgForm.append(4)
    elif value>=30.00 and value<=34.99:
        AvgForm.append(3)
    elif value>=35.00 and value<=49.99:
        AvgForm.append(2)
    elif value>=50.00 :
        AvgForm.append(1)
df["AvgForm"] = AvgForm   



#For Average Opponent ############
############################

AvgOpp=[]
for value in df["OpAvg"]:
    if value>=2.0 and value<=13.99:
        AvgOpp.append(5)
    elif value>=14.0 and value<=25.99:
        AvgOpp.append(4)
    elif value>=26.00 and value<=69.99:
        AvgOpp.append(3)
    elif value>=70.00 and value<=113.99:
        AvgOpp.append(2)
    elif value>=114.00 :
        AvgOpp.append(1)
df["AvgOpp"] = AvgOpp   




#For Average Ven ############
############################

AvgVen=[]
for value in df["VAvg"]:
    if value>=2.0 and value<=15.99:
        AvgVen.append(5)
    elif value>=16.0 and value<=31.99:
        AvgVen.append(4)
    elif value>=32.00 and value<=71.99:
        AvgVen.append(3)
    elif value>=72.00 and value<=111.99:
        AvgVen.append(2)
    elif value>=112.00 :
        AvgVen.append(1)
df["AvgVen"] = AvgVen   



##########################
##########################
##########################
##########################
##########################
##########################
##########################
##########################

##########################
##########################
##########################
##########################
##########################
##########################
##########################
##########################
##########################
##########################
##########################
##########################
##########################
##########################
##########################
##########################



#For SR Consistency ############
############################

SRCon=[]
for value in df["SRTotal"]:
    if value>=0.0 and value<=13.999999:
        SRCon.append(5)
    elif value>=14.0 and value<=19.9999999:
        SRCon.append(4)
    elif value>=20.00 and value<=27.9999999:
        SRCon.append(3)
    elif value>=28.00 and value<=36.9999999:
        SRCon.append(2)
    elif value>=37.00 :
        SRCon.append(1)
df["SRCon"] = SRCon   


#For SR Form ############
############################

SRForm=[]
for value in df["SSr"]:
    if value>=0.0 and value<=29.99:
        SRForm.append(5)
    elif value>=30.0 and value<=39.99:
        SRForm.append(4)
    elif value>=40.00 and value<=49.99:
        SRForm.append(3)
    elif value>=50.00 and value<=59.99:
        SRForm.append(2)
    elif value>=60.00 :
        SRForm.append(1)
df["SRForm"] = SRForm   



#For SR Opponent ############
############################

SROpp=[]
for value in df["OpSr"]:
    if value>=0 and value<=21.99:
        SROpp.append(5)
    elif value>=22.0 and value<=39.99:
        SROpp.append(4)
    elif value>=40.00 and value<=67.99:
        SROpp.append(3)
    elif value>=68.00 and value<=96.99:
        SROpp.append(2)
    elif value>=97.00 :
        SROpp.append(1)
df["SROpp"] = SROpp   




#For SR Ven ############
############################

SRVen=[]
for value in df["VSr"]:
    if value>=3.0 and value<=10.999:
        SRVen.append(5)
    elif value>=11.0 and value<=21.999:
        SRVen.append(4)
    elif value>=22.00 and value<=54.999:
        SRVen.append(3)
    elif value>=55.00 and value<=87.999:
        SRVen.append(2)
    elif value>=88.00 :
        SRVen.append(1)
df["SRVen"] = SRVen   







##########################
##########################
##########################
##########################
##########################
##########################
##########################
##########################

##########################
##########################
##########################
##########################
##########################
##########################
##########################
##########################
##########################
##########################
##########################
##########################
##########################
##########################
##########################
##########################



#For 3 wickets+ Consistency ############
############################

WikCon=[]
for value in df["ThreeWicketHaul"]:
    if value>=1 and value<=2:
        WikCon.append(3)
    elif value>=3 and value<=4:
        WikCon.append(4)

    elif value>=5 :
        WikCon.append(5)
    else:
        WikCon.append(0)
df["WikCon"] = WikCon   


#For 3 wickets+ Form ############
############################

WikForm=[]
for value in df["SThreeHaul"]:
    if value>=1 and value<=2:
        WikForm.append(4)

    elif value>=3:
        WikForm.append(5)
    else:
        WikForm.append(0)
df["WikForm"] = WikForm   



#For 3 wickets+ Opponent ############
############################

WikOpp=[]
for value in df["OppThreeWicketHaul"]:
    if value>=1 and value<=2:
        WikOpp.append(4)

    elif value>=3 :
        WikOpp.append(5)
    else:
        WikOpp.append(0)
df["WikOpp"] = WikOpp   




#For 3 wickets+ Ven ############
############################

WikVen=[]
for value in df["VenThreeWicketHaul"]:
    if value>=1 and value<=2:
        WikVen.append(4)

    elif value>=3 :
        WikVen.append(5)
    else:
        WikVen.append(0)
df["WikVen"] = WikVen   




##########################
##########################
##########################

########### Rating for consistency for Economy rate #########
EconomyConRating=[]
for value in df["EconomyRateTotal"]:

    if value>=0.00 and value<=4.999999:
        EconomyConRating.append(5)

    elif value>=5.00 and value<=6.9999999 :
        EconomyConRating.append(4)
    elif value>=7.00 and value<=8.999999 :
        EconomyConRating.append(3)
    elif value>=9.00 and value<=10.999999 :
        EconomyConRating.append(2)
    elif value>=11.00:
        EconomyConRating.append(1)
df["EconomyConRating"] = EconomyConRating  


########### Rating for form Economy rate #########
EconomyFormRating=[]
for value in df["SEr"]:

    if value>=0.00 and value<=4.999999:
        EconomyFormRating.append(5)

    elif value>=5.00 and value<=6.999999 :
        EconomyFormRating.append(4)
    elif value>=7.00 and value<=8.99999 :
        EconomyFormRating.append(3)
    elif value>=9.00 and value<=10.999999 :
        EconomyFormRating.append(2)
    elif value>=11.00:
        EconomyFormRating.append(1)
df["EconomyFormRating"] = EconomyFormRating  

########### Rating for opposition Economy rate #########
EconomyOppRating=[]
for value in df["OpEr"]:

    if value>=0.00 and value<=4.9999999:
        EconomyOppRating.append(5)

    elif value>=5.00 and value<=6.999999 :
        EconomyOppRating.append(4)
    elif value>=7.00 and value<=8.999999 :
        EconomyOppRating.append(3)
    elif value>=9.00 and value<=10.999999 :
        EconomyOppRating.append(2)
    elif value>=11.00:
        EconomyOppRating.append(1)
df["EconomyOppRating"] = EconomyOppRating  


########### Rating for form Ven Economy rate #########
EconomyVenRating=[]
for value in df["VEr"]:

    if value>=0.00 and value<=4.99999:
        EconomyVenRating.append(5)

    elif value>=5.00 and value<=6.99999 :
        EconomyVenRating.append(4)
    elif value>=7.00 and value<=8.99999 :
        EconomyVenRating.append(3)
    elif value>=9.00 and value<=10.99999 :
        EconomyVenRating.append(2)
    elif value>=11.00:
        EconomyVenRating.append(1)
df["EconomyVenRating"] = EconomyVenRating  

##########################
##########################
##########################
##########################

##########################
##########################
##########################
##########################
##########################
##########################
##########################
####################################################


####################### Wickets Rating ##############################
WicketRating=[]
for value in df["WicketsCric"]:
    if value>=0 and value<=1:
        WicketRating.append(1)

    elif value==2 :
        WicketRating.append(2)
        
    elif value==3  :
        WicketRating.append(3)
    elif value==4  :
        WicketRating.append(4)
        
    elif value>=5:
        WicketRating.append(5)
df["WicketRating"] = WicketRating   


################################################################################
########################################

#######################################
####              Calculation of Consistency      ############
####################################

ConValue=[]
ConValue.append(0)
df.at[0,'Consistency']=0

for i in range(1,columnNum):
      ConValue.append(4*(df.at[i-1,'AvgCon'])+3*(df.at[i-1,'MatchCon'])+2*(df.at[i-1,'SRCon'])+0.3*(df.at[i-1,'OverCon'])+0.5*(df.at[i-1,'WikCon'])+0.2*(df.at[i-1,'EconomyConRating']))  

df["Consistency"] = ConValue  

#######################################
####              Calculation of Form      ############
####################################

FormValue=[]
FormValue.append(0)
df.at[0,'Form']=0

for i in range(1,columnNum):
    if(df.at[i,'SMatch']!=1):
        FormValue.append(4*(df.at[i-1,'AvgForm'])+3*(df.at[i-1,'MatchForm'])+2*(df.at[i-1,'SRForm'])+0.3*(df.at[i-1,'OverForm'])+0.5*(df.at[i-1,'WikForm'])+0.2*(df.at[i-1,'EconomyFormRating']))  
    else:
        FormValue.append(0)
        #FormValue.append(df.at[i,'Consistency'])
df["Form"] = FormValue  



###############

###############
##################
######   List for match numbers against an opposition ##########

OppositionNumberList1=[]
OppositionNumberList2=[]
OppositionNumberList3=[]
OppositionNumberList4=[]
OppositionNumberList5=[]
OppositionNumberList6=[]
OppositionNumberList7=[]
OppositionNumberList8=[]
OppositionNumberList9=[]
OppositionNumberList10=[]
OppositionNumberList11=[]
OppositionNumberList12=[]

for i in range(0,columnNum):
    if(df.at[i,'OppositionIndex']==1):
        OppositionNumberList1.append(df.at[i,'Match'])
    elif(df.at[i,'OppositionIndex']==2):
        OppositionNumberList2.append(df.at[i,'Match'])
    elif(df.at[i,'OppositionIndex']==3):
        OppositionNumberList3.append(df.at[i,'Match'])
    elif(df.at[i,'OppositionIndex']==4):
        OppositionNumberList4.append(df.at[i,'Match'])
    elif(df.at[i,'OppositionIndex']==5):
        OppositionNumberList5.append(df.at[i,'Match'])
    elif(df.at[i,'OppositionIndex']==6):
        OppositionNumberList6.append(df.at[i,'Match'])
    elif(df.at[i,'OppositionIndex']==7):
        OppositionNumberList7.append(df.at[i,'Match'])
    elif(df.at[i,'OppositionIndex']==8):
        OppositionNumberList8.append(df.at[i,'Match'])
    elif(df.at[i,'OppositionIndex']==9):
        OppositionNumberList9.append(df.at[i,'Match'])
    elif(df.at[i,'OppositionIndex']==10):
        OppositionNumberList10.append(df.at[i,'Match'])
    elif(df.at[i,'OppositionIndex']==11):
        OppositionNumberList11.append(df.at[i,'Match'])
    elif(df.at[i,'OppositionIndex']==12):
        OppositionNumberList12.append(df.at[i,'Match'])

print(OppositionNumberList1)



############################
###############################
###### Calculation for Opposition Feature's Value #############
   
if len(OppositionNumberList1)>0:
    df.at[OppositionNumberList1[0]-1,"OppositionValue"]=0
    for i in range(1,len(OppositionNumberList1)):
        df.at[OppositionNumberList1[i]-1,"OppositionValue"]=(4*(df.at[OppositionNumberList1[i-1]-1,'AvgOpp'])+3*(df.at[OppositionNumberList1[i-1]-1,'MatchOpp'])+2*(df.at[OppositionNumberList1[i-1]-1,'SROpp'])+0.3*(df.at[OppositionNumberList1[i-1]-1,'OverOpp'])+0.5*(df.at[OppositionNumberList1[i-1]-1,'WikOpp'])+0.2*df.at[OppositionNumberList1[i-1]-1,'EconomyOppRating'])
        
if len(OppositionNumberList2)>0:
    df.at[OppositionNumberList2[0]-1,"OppositionValue"]=0
    for i in range(1,len(OppositionNumberList2)):
        df.at[OppositionNumberList2[i]-1,"OppositionValue"]=(4*(df.at[OppositionNumberList2[i-1]-1,'AvgOpp'])+3*(df.at[OppositionNumberList2[i-1]-1,'MatchOpp'])+2*(df.at[OppositionNumberList2[i-1]-1,'SROpp'])+0.3*(df.at[OppositionNumberList2[i-1]-1,'OverOpp'])+0.5*(df.at[OppositionNumberList2[i-1]-1,'WikOpp'])+0.2*df.at[OppositionNumberList2[i-1]-1,'EconomyOppRating'])
        
        
if len(OppositionNumberList3)>0:
    df.at[OppositionNumberList3[0]-1,"OppositionValue"]=0
    for i in range(1,len(OppositionNumberList3)):
        df.at[OppositionNumberList3[i]-1,"OppositionValue"]=(4*(df.at[OppositionNumberList3[i-1]-1,'AvgOpp'])+3*(df.at[OppositionNumberList3[i-1]-1,'MatchOpp'])+2*(df.at[OppositionNumberList3[i-1]-1,'SROpp'])+0.3*(df.at[OppositionNumberList3[i-1]-1,'OverOpp'])+0.5*(df.at[OppositionNumberList3[i-1]-1,'WikOpp'])+0.2*df.at[OppositionNumberList3[i-1]-1,'EconomyOppRating'])
        
        
if len(OppositionNumberList4)>0:
    df.at[OppositionNumberList4[0]-1,"OppositionValue"]=0
    for i in range(1,len(OppositionNumberList4)):
        df.at[OppositionNumberList4[i]-1,"OppositionValue"]=(4*(df.at[OppositionNumberList4[i-1]-1,'AvgOpp'])+3*(df.at[OppositionNumberList4[i-1]-1,'MatchOpp'])+2*(df.at[OppositionNumberList4[i-1]-1,'SROpp'])+0.3*(df.at[OppositionNumberList4[i-1]-1,'OverOpp'])+0.5*(df.at[OppositionNumberList4[i-1]-1,'WikOpp'])+0.2*df.at[OppositionNumberList4[i-1]-1,'EconomyOppRating'])
        
        
if len(OppositionNumberList5)>0:
    df.at[OppositionNumberList5[0]-1,"OppositionValue"]=0
    for i in range(1,len(OppositionNumberList5)):
        df.at[OppositionNumberList5[i]-1,"OppositionValue"]=(4*(df.at[OppositionNumberList5[i-1]-1,'AvgOpp'])+3*(df.at[OppositionNumberList5[i-1]-1,'MatchOpp'])+2*(df.at[OppositionNumberList5[i-1]-1,'SROpp'])+0.3*(df.at[OppositionNumberList5[i-1]-1,'OverOpp'])+0.5*(df.at[OppositionNumberList5[i-1]-1,'WikOpp'])+0.2*df.at[OppositionNumberList5[i-1]-1,'EconomyOppRating'])
        
        
if len(OppositionNumberList6)>0:
    df.at[OppositionNumberList6[0]-1,"OppositionValue"]=0
    for i in range(1,len(OppositionNumberList6)):
        df.at[OppositionNumberList6[i]-1,"OppositionValue"]=(4*(df.at[OppositionNumberList6[i-1]-1,'AvgOpp'])+3*(df.at[OppositionNumberList6[i-1]-1,'MatchOpp'])+2*(df.at[OppositionNumberList6[i-1]-1,'SROpp'])+0.3*(df.at[OppositionNumberList6[i-1]-1,'OverOpp'])+0.5*(df.at[OppositionNumberList6[i-1]-1,'WikOpp'])+0.2*df.at[OppositionNumberList6[i-1]-1,'EconomyOppRating'])
        
        
if len(OppositionNumberList7)>0:
    df.at[OppositionNumberList7[0]-1,"OppositionValue"]=0
    for i in range(1,len(OppositionNumberList7)):
        df.at[OppositionNumberList7[i]-1,"OppositionValue"]=(4*(df.at[OppositionNumberList7[i-1]-1,'AvgOpp'])+3*(df.at[OppositionNumberList7[i-1]-1,'MatchOpp'])+2*(df.at[OppositionNumberList7[i-1]-1,'SROpp'])+0.3*(df.at[OppositionNumberList7[i-1]-1,'OverOpp'])+0.5*(df.at[OppositionNumberList7[i-1]-1,'WikOpp'])+0.2*df.at[OppositionNumberList7[i-1]-1,'EconomyOppRating'])
        
if len(OppositionNumberList8)>0:
    df.at[OppositionNumberList8[0]-1,"OppositionValue"]=0
    for i in range(1,len(OppositionNumberList8)):
        df.at[OppositionNumberList8[i]-1,"OppositionValue"]=(4*(df.at[OppositionNumberList8[i-1]-1,'AvgOpp'])+3*(df.at[OppositionNumberList8[i-1]-1,'MatchOpp'])+2*(df.at[OppositionNumberList8[i-1]-1,'SROpp'])+0.3*(df.at[OppositionNumberList8[i-1]-1,'OverOpp'])+0.5*(df.at[OppositionNumberList8[i-1]-1,'WikOpp'])+0.2*df.at[OppositionNumberList8[i-1]-1,'EconomyOppRating'])
        
        
if len(OppositionNumberList9)>0:
    df.at[OppositionNumberList9[0]-1,"OppositionValue"]=0
    for i in range(1,len(OppositionNumberList9)):
        df.at[OppositionNumberList9[i]-1,"OppositionValue"]=(4*(df.at[OppositionNumberList9[i-1]-1,'AvgOpp'])+3*(df.at[OppositionNumberList9[i-1]-1,'MatchOpp'])+2*(df.at[OppositionNumberList9[i-1]-1,'SROpp'])+0.3*(df.at[OppositionNumberList9[i-1]-1,'OverOpp'])+0.5*(df.at[OppositionNumberList9[i-1]-1,'WikOpp'])+0.2*df.at[OppositionNumberList9[i-1]-1,'EconomyOppRating'])
        
        
if len(OppositionNumberList10)>0:
    df.at[OppositionNumberList10[0]-1,"OppositionValue"]=0
    for i in range(1,len(OppositionNumberList10)):
        df.at[OppositionNumberList10[i]-1,"OppositionValue"]=(4*(df.at[OppositionNumberList10[i-1]-1,'AvgOpp'])+3*(df.at[OppositionNumberList10[i-1]-1,'MatchOpp'])+2*(df.at[OppositionNumberList10[i-1]-1,'SROpp'])+0.3*(df.at[OppositionNumberList10[i-1]-1,'OverOpp'])+0.5*(df.at[OppositionNumberList10[i-1]-1,'WikOpp'])+0.2*df.at[OppositionNumberList10[i-1]-1,'EconomyOppRating'])
        
        
if len(OppositionNumberList11)>0:
    df.at[OppositionNumberList11[0]-1,"OppositionValue"]=0
    for i in range(1,len(OppositionNumberList11)):
        df.at[OppositionNumberList11[i]-1,"OppositionValue"]=(4*(df.at[OppositionNumberList11[i-1]-1,'AvgOpp'])+3*(df.at[OppositionNumberList11[i-1]-1,'MatchOpp'])+2*(df.at[OppositionNumberList11[i-1]-1,'SROpp'])+0.3*(df.at[OppositionNumberList11[i-1]-1,'OverOpp'])+0.5*(df.at[OppositionNumberList11[i-1]-1,'WikOpp'])+0.2*df.at[OppositionNumberList11[i-1]-1,'EconomyOppRating'])
        
        
if len(OppositionNumberList12)>0:
    df.at[OppositionNumberList12[0]-1,"OppositionValue"]=0
    for i in range(1,len(OppositionNumberList12)):
        df.at[OppositionNumberList12[i]-1,"OppositionValue"]=(4*(df.at[OppositionNumberList12[i-1]-1,'AvgOpp'])+3*(df.at[OppositionNumberList12[i-1]-1,'MatchOpp'])+2*(df.at[OppositionNumberList12[i-1]-1,'SROpp'])+0.3*(df.at[OppositionNumberList12[i-1]-1,'OverOpp'])+0.5*(df.at[OppositionNumberList12[i-1]-1,'WikOpp'])+0.2*df.at[OppositionNumberList12[i-1]-1,'EconomyOppRating'])
        

    





######   List for match numbers in a particular venue ##########

VenueNumberList1=[]
VenueNumberList2=[]
VenueNumberList3=[]
VenueNumberList4=[]
VenueNumberList5=[]
VenueNumberList6=[]
VenueNumberList7=[]
VenueNumberList8=[]
VenueNumberList9=[]
VenueNumberList10=[]
VenueNumberList11=[]
VenueNumberList12=[]
VenueNumberList13=[]
VenueNumberList14=[]
VenueNumberList15=[]
VenueNumberList16=[]
VenueNumberList17=[]
VenueNumberList18=[]
VenueNumberList19=[]
VenueNumberList20=[]
VenueNumberList21=[]
VenueNumberList22=[]
VenueNumberList23=[]
VenueNumberList24=[]
VenueNumberList25=[]
VenueNumberList26=[]
VenueNumberList27=[]
  

for i in range(0,columnNum):
    if(df.at[i,'VenueIndex']==1):
        VenueNumberList1.append(df.at[i,'Match'])
    elif(df.at[i,'VenueIndex']==2):
        VenueNumberList2.append(df.at[i,'Match'])
    elif(df.at[i,'VenueIndex']==3):
        VenueNumberList3.append(df.at[i,'Match'])
    elif(df.at[i,'VenueIndex']==4):
        VenueNumberList4.append(df.at[i,'Match'])
    elif(df.at[i,'VenueIndex']==5):
        VenueNumberList5.append(df.at[i,'Match'])
    elif(df.at[i,'VenueIndex']==6):
        VenueNumberList6.append(df.at[i,'Match'])
    elif(df.at[i,'VenueIndex']==7):
        VenueNumberList7.append(df.at[i,'Match'])
    elif(df.at[i,'VenueIndex']==8):
        VenueNumberList8.append(df.at[i,'Match'])
    elif(df.at[i,'VenueIndex']==9):
        VenueNumberList9.append(df.at[i,'Match'])
    elif(df.at[i,'VenueIndex']==10):
        VenueNumberList10.append(df.at[i,'Match'])
    elif(df.at[i,'VenueIndex']==11):
        VenueNumberList11.append(df.at[i,'Match'])
    elif(df.at[i,'VenueIndex']==12):
        VenueNumberList12.append(df.at[i,'Match'])
    elif(df.at[i,'VenueIndex']==13):
        VenueNumberList13.append(df.at[i,'Match'])
    elif(df.at[i,'VenueIndex']==14):
        VenueNumberList14.append(df.at[i,'Match'])
    elif(df.at[i,'VenueIndex']==15):
        VenueNumberList15.append(df.at[i,'Match'])
    elif(df.at[i,'VenueIndex']==16):
        VenueNumberList16.append(df.at[i,'Match'])
    elif(df.at[i,'VenueIndex']==17):
        VenueNumberList17.append(df.at[i,'Match'])
    elif(df.at[i,'VenueIndex']==18):
        VenueNumberList18.append(df.at[i,'Match'])
    elif(df.at[i,'VenueIndex']==19):
        VenueNumberList19.append(df.at[i,'Match'])
    elif(df.at[i,'VenueIndex']==20):
        VenueNumberList20.append(df.at[i,'Match'])
    elif(df.at[i,'VenueIndex']==21):
        VenueNumberList21.append(df.at[i,'Match'])
    elif(df.at[i,'VenueIndex']==22):
        VenueNumberList22.append(df.at[i,'Match'])
    elif(df.at[i,'VenueIndex']==23):
        VenueNumberList23.append(df.at[i,'Match'])
    elif(df.at[i,'VenueIndex']==24):
        VenueNumberList24.append(df.at[i,'Match'])
    elif(df.at[i,'VenueIndex']==25):
        VenueNumberList25.append(df.at[i,'Match'])
    elif(df.at[i,'VenueIndex']==26):
        VenueNumberList26.append(df.at[i,'Match'])
    elif(df.at[i,'VenueIndex']==27):
        VenueNumberList27.append(df.at[i,'Match'])
    
    
###### Calculation for Venue Feature's Value #############
   
if len(VenueNumberList1)>0:
    df.at[VenueNumberList1[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList1)):
        df.at[VenueNumberList1[i]-1,"VenueValue"]=(4*(df.at[VenueNumberList1[i-1]-1,'AvgVen'])+3*(df.at[VenueNumberList1[i-1]-1,'MatchVen'])+2*(df.at[VenueNumberList1[i-1]-1,'SRVen'])+0.3*(df.at[VenueNumberList1[i-1]-1,'OverVen'])+0.5*(df.at[VenueNumberList1[i-1]-1,'WikVen'])+0.2*(df.at[VenueNumberList1[i-1]-1,'EconomyVenRating']))
        
if len(VenueNumberList2)>0:
    df.at[VenueNumberList2[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList2)):
        df.at[VenueNumberList2[i]-1,"VenueValue"]=(4*(df.at[VenueNumberList2[i-1]-1,'AvgVen'])+3*(df.at[VenueNumberList2[i-1]-1,'MatchVen'])+2*(df.at[VenueNumberList2[i-1]-1,'SRVen'])+0.3*(df.at[VenueNumberList2[i-1]-1,'OverVen'])+0.5*(df.at[VenueNumberList2[i-1]-1,'WikVen'])+0.2*(df.at[VenueNumberList2[i-1]-1,'EconomyVenRating']))
        
if len(VenueNumberList3)>0:
    df.at[VenueNumberList3[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList3)):
        df.at[VenueNumberList3[i]-1,"VenueValue"]=(4*(df.at[VenueNumberList3[i-1]-1,'AvgVen'])+3*(df.at[VenueNumberList3[i-1]-1,'MatchVen'])+2*(df.at[VenueNumberList3[i-1]-1,'SRVen'])+0.3*(df.at[VenueNumberList3[i-1]-1,'OverVen'])+0.5*(df.at[VenueNumberList3[i-1]-1,'WikVen'])+0.2*(df.at[VenueNumberList3[i-1]-1,'EconomyVenRating']))
        
if len(VenueNumberList4)>0:
    df.at[VenueNumberList4[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList4)):
        df.at[VenueNumberList4[i]-1,"VenueValue"]=(4*(df.at[VenueNumberList4[i-1]-1,'AvgVen'])+3*(df.at[VenueNumberList4[i-1]-1,'MatchVen'])+2*(df.at[VenueNumberList4[i-1]-1,'SRVen'])+0.3*(df.at[VenueNumberList4[i-1]-1,'OverVen'])+0.5*(df.at[VenueNumberList4[i-1]-1,'WikVen'])+0.2*(df.at[VenueNumberList4[i-1]-1,'EconomyVenRating']))
        
if len(VenueNumberList5)>0:
    df.at[VenueNumberList5[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList5)):
        df.at[VenueNumberList5[i]-1,"VenueValue"]=(4*(df.at[VenueNumberList5[i-1]-1,'AvgVen'])+3*(df.at[VenueNumberList5[i-1]-1,'MatchVen'])+2*(df.at[VenueNumberList5[i-1]-1,'SRVen'])+0.3*(df.at[VenueNumberList5[i-1]-1,'OverVen'])+0.5*(df.at[VenueNumberList5[i-1]-1,'WikVen'])+0.2*(df.at[VenueNumberList5[i-1]-1,'EconomyVenRating']))
        
if len(VenueNumberList6)>0:
    df.at[VenueNumberList6[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList6)):
        df.at[VenueNumberList6[i]-1,"VenueValue"]=(4*(df.at[VenueNumberList6[i-1]-1,'AvgVen'])+3*(df.at[VenueNumberList6[i-1]-1,'MatchVen'])+2*(df.at[VenueNumberList6[i-1]-1,'SRVen'])+0.3*(df.at[VenueNumberList6[i-1]-1,'OverVen'])+0.5*(df.at[VenueNumberList6[i-1]-1,'WikVen'])+0.2*(df.at[VenueNumberList6[i-1]-1,'EconomyVenRating']))
        
if len(VenueNumberList7)>0:
    df.at[VenueNumberList7[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList7)):
        df.at[VenueNumberList7[i]-1,"VenueValue"]=(4*(df.at[VenueNumberList7[i-1]-1,'AvgVen'])+3*(df.at[VenueNumberList7[i-1]-1,'MatchVen'])+2*(df.at[VenueNumberList7[i-1]-1,'SRVen'])+0.3*(df.at[VenueNumberList7[i-1]-1,'OverVen'])+0.5*(df.at[VenueNumberList7[i-1]-1,'WikVen'])+0.2*(df.at[VenueNumberList7[i-1]-1,'EconomyVenRating']))


if len(VenueNumberList8)>0:
    df.at[VenueNumberList8[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList8)):
        df.at[VenueNumberList8[i]-1,"VenueValue"]=(4*(df.at[VenueNumberList8[i-1]-1,'AvgVen'])+3*(df.at[VenueNumberList8[i-1]-1,'MatchVen'])+2*(df.at[VenueNumberList8[i-1]-1,'SRVen'])+0.3*(df.at[VenueNumberList8[i-1]-1,'OverVen'])+0.5*(df.at[VenueNumberList8[i-1]-1,'WikVen'])+0.2*(df.at[VenueNumberList8[i-1]-1,'EconomyVenRating']))
        
if len(VenueNumberList9)>0:
    df.at[VenueNumberList9[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList9)):
        df.at[VenueNumberList9[i]-1,"VenueValue"]=(4*(df.at[VenueNumberList9[i-1]-1,'AvgVen'])+3*(df.at[VenueNumberList9[i-1]-1,'MatchVen'])+2*(df.at[VenueNumberList9[i-1]-1,'SRVen'])+0.3*(df.at[VenueNumberList9[i-1]-1,'OverVen'])+0.5*(df.at[VenueNumberList9[i-1]-1,'WikVen'])+0.2*(df.at[VenueNumberList9[i-1]-1,'EconomyVenRating']))
        
if len(VenueNumberList10)>0:
    df.at[VenueNumberList10[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList10)):
        df.at[VenueNumberList10[i]-1,"VenueValue"]=(4*(df.at[VenueNumberList10[i-1]-1,'AvgVen'])+3*(df.at[VenueNumberList10[i-1]-1,'MatchVen'])+2*(df.at[VenueNumberList10[i-1]-1,'SRVen'])+0.3*(df.at[VenueNumberList10[i-1]-1,'OverVen'])+0.5*(df.at[VenueNumberList10[i-1]-1,'WikVen'])+0.2*(df.at[VenueNumberList10[i-1]-1,'EconomyVenRating']))
        
if len(VenueNumberList11)>0:
    df.at[VenueNumberList11[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList11)):
        df.at[VenueNumberList11[i]-1,"VenueValue"]=(4*(df.at[VenueNumberList11[i-1]-1,'AvgVen'])+3*(df.at[VenueNumberList11[i-1]-1,'MatchVen'])+2*(df.at[VenueNumberList11[i-1]-1,'SRVen'])+0.3*(df.at[VenueNumberList11[i-1]-1,'OverVen'])+0.5*(df.at[VenueNumberList11[i-1]-1,'WikVen'])+0.2*(df.at[VenueNumberList11[i-1]-1,'EconomyVenRating']))
        
if len(VenueNumberList12)>0:
    df.at[VenueNumberList12[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList12)):
        df.at[VenueNumberList12[i]-1,"VenueValue"]=(4*(df.at[VenueNumberList12[i-1]-1,'AvgVen'])+3*(df.at[VenueNumberList12[i-1]-1,'MatchVen'])+2*(df.at[VenueNumberList12[i-1]-1,'SRVen'])+0.3*(df.at[VenueNumberList12[i-1]-1,'OverVen'])+0.5*(df.at[VenueNumberList12[i-1]-1,'WikVen'])+0.2*(df.at[VenueNumberList12[i-1]-1,'EconomyVenRating']))
        
    
if len(VenueNumberList13)>0:
    df.at[VenueNumberList13[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList13)):
        df.at[VenueNumberList13[i]-1,"VenueValue"]=(4*(df.at[VenueNumberList13[i-1]-1,'AvgVen'])+3*(df.at[VenueNumberList13[i-1]-1,'MatchVen'])+2*(df.at[VenueNumberList13[i-1]-1,'SRVen'])+0.3*(df.at[VenueNumberList13[i-1]-1,'OverVen'])+0.5*(df.at[VenueNumberList13[i-1]-1,'WikVen'])+0.2*(df.at[VenueNumberList13[i-1]-1,'EconomyVenRating']))
            
if len(VenueNumberList14)>0:
    df.at[VenueNumberList14[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList14)):
        df.at[VenueNumberList14[i]-1,"VenueValue"]=(4*(df.at[VenueNumberList14[i-1]-1,'AvgVen'])+3*(df.at[VenueNumberList14[i-1]-1,'MatchVen'])+2*(df.at[VenueNumberList14[i-1]-1,'SRVen'])+0.3*(df.at[VenueNumberList14[i-1]-1,'OverVen'])+0.5*(df.at[VenueNumberList14[i-1]-1,'WikVen'])+0.2*(df.at[VenueNumberList14[i-1]-1,'EconomyVenRating']))
        
if len(VenueNumberList15)>0:
    df.at[VenueNumberList15[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList15)):
        df.at[VenueNumberList15[i]-1,"VenueValue"]=(4*(df.at[VenueNumberList15[i-1]-1,'AvgVen'])+3*(df.at[VenueNumberList15[i-1]-1,'MatchVen'])+2*(df.at[VenueNumberList15[i-1]-1,'SRVen'])+0.3*(df.at[VenueNumberList15[i-1]-1,'OverVen'])+0.5*(df.at[VenueNumberList15[i-1]-1,'WikVen'])+0.2*(df.at[VenueNumberList15[i-1]-1,'EconomyVenRating']))
        
if len(VenueNumberList16)>0:
    df.at[VenueNumberList16[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList16)):
        df.at[VenueNumberList16[i]-1,"VenueValue"]=(4*(df.at[VenueNumberList16[i-1]-1,'AvgVen'])+3*(df.at[VenueNumberList16[i-1]-1,'MatchVen'])+2*(df.at[VenueNumberList16[i-1]-1,'SRVen'])+0.3*(df.at[VenueNumberList16[i-1]-1,'OverVen'])+0.5*(df.at[VenueNumberList16[i-1]-1,'WikVen'])+0.2*(df.at[VenueNumberList16[i-1]-1,'EconomyVenRating']))
        
if len(VenueNumberList17)>0:
    df.at[VenueNumberList17[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList17)):
        df.at[VenueNumberList17[i]-1,"VenueValue"]=(4*(df.at[VenueNumberList17[i-1]-1,'AvgVen'])+3*(df.at[VenueNumberList17[i-1]-1,'MatchVen'])+2*(df.at[VenueNumberList17[i-1]-1,'SRVen'])+0.3*(df.at[VenueNumberList17[i-1]-1,'OverVen'])+0.5*(df.at[VenueNumberList17[i-1]-1,'WikVen'])+0.2*(df.at[VenueNumberList17[i-1]-1,'EconomyVenRating']))


if len(VenueNumberList18)>0:
    df.at[VenueNumberList18[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList18)):
        df.at[VenueNumberList18[i]-1,"VenueValue"]=(4*(df.at[VenueNumberList18[i-1]-1,'AvgVen'])+3*(df.at[VenueNumberList18[i-1]-1,'MatchVen'])+2*(df.at[VenueNumberList18[i-1]-1,'SRVen'])+0.3*(df.at[VenueNumberList18[i-1]-1,'OverVen'])+0.5*(df.at[VenueNumberList18[i-1]-1,'WikVen'])+0.2*(df.at[VenueNumberList18[i-1]-1,'EconomyVenRating']))


if len(VenueNumberList19)>0:
    df.at[VenueNumberList19[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList19)):
        df.at[VenueNumberList19[i]-1,"VenueValue"]=(4*(df.at[VenueNumberList19[i-1]-1,'AvgVen'])+3*(df.at[VenueNumberList19[i-1]-1,'MatchVen'])+2*(df.at[VenueNumberList19[i-1]-1,'SRVen'])+0.3*(df.at[VenueNumberList19[i-1]-1,'OverVen'])+0.5*(df.at[VenueNumberList19[i-1]-1,'WikVen'])+0.2*(df.at[VenueNumberList19[i-1]-1,'EconomyVenRating']))
    
    
if len(VenueNumberList20)>0:
    df.at[VenueNumberList20[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList20)):
        df.at[VenueNumberList20[i]-1,"VenueValue"]=(4*(df.at[VenueNumberList20[i-1]-1,'AvgVen'])+3*(df.at[VenueNumberList20[i-1]-1,'MatchVen'])+2*(df.at[VenueNumberList20[i-1]-1,'SRVen'])+0.3*(df.at[VenueNumberList20[i-1]-1,'OverVen'])+0.5*(df.at[VenueNumberList20[i-1]-1,'WikVen'])+0.2*(df.at[VenueNumberList20[i-1]-1,'EconomyVenRating']))
    
if len(VenueNumberList21)>0:
    df.at[VenueNumberList21[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList21)):
        df.at[VenueNumberList21[i]-1,"VenueValue"]=(4*(df.at[VenueNumberList21[i-1]-1,'AvgVen'])+3*(df.at[VenueNumberList21[i-1]-1,'MatchVen'])+2*(df.at[VenueNumberList21[i-1]-1,'SRVen'])+0.3*(df.at[VenueNumberList21[i-1]-1,'OverVen'])+0.5*(df.at[VenueNumberList21[i-1]-1,'WikVen'])+0.2*(df.at[VenueNumberList21[i-1]-1,'EconomyVenRating']))

if len(VenueNumberList22)>0:
    df.at[VenueNumberList22[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList22)):
        df.at[VenueNumberList22[i]-1,"VenueValue"]=(4*(df.at[VenueNumberList22[i-1]-1,'AvgVen'])+3*(df.at[VenueNumberList22[i-1]-1,'MatchVen'])+2*(df.at[VenueNumberList22[i-1]-1,'SRVen'])+0.3*(df.at[VenueNumberList22[i-1]-1,'OverVen'])+0.5*(df.at[VenueNumberList22[i-1]-1,'WikVen'])+0.2*(df.at[VenueNumberList22[i-1]-1,'EconomyVenRating']))

if len(VenueNumberList23)>0:
    df.at[VenueNumberList23[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList23)):
        df.at[VenueNumberList23[i]-1,"VenueValue"]=(4*(df.at[VenueNumberList23[i-1]-1,'AvgVen'])+3*(df.at[VenueNumberList23[i-1]-1,'MatchVen'])+2*(df.at[VenueNumberList23[i-1]-1,'SRVen'])+0.3*(df.at[VenueNumberList23[i-1]-1,'OverVen'])+0.5*(df.at[VenueNumberList23[i-1]-1,'WikVen'])+0.2*(df.at[VenueNumberList23[i-1]-1,'EconomyVenRating']))


if len(VenueNumberList24)>0:
    df.at[VenueNumberList24[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList24)):
        df.at[VenueNumberList24[i]-1,"VenueValue"]=(4*(df.at[VenueNumberList24[i-1]-1,'AvgVen'])+3*(df.at[VenueNumberList24[i-1]-1,'MatchVen'])+2*(df.at[VenueNumberList24[i-1]-1,'SRVen'])+0.3*(df.at[VenueNumberList24[i-1]-1,'OverVen'])+0.5*(df.at[VenueNumberList24[i-1]-1,'WikVen'])+0.2*(df.at[VenueNumberList24[i-1]-1,'EconomyVenRating']))

if len(VenueNumberList25)>0:
    df.at[VenueNumberList25[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList25)):
       df.at[VenueNumberList25[i]-1,"VenueValue"]=(4*(df.at[VenueNumberList25[i-1]-1,'AvgVen'])+3*(df.at[VenueNumberList25[i-1]-1,'MatchVen'])+2*(df.at[VenueNumberList25[i-1]-1,'SRVen'])+0.3*(df.at[VenueNumberList25[i-1]-1,'OverVen'])+0.5*(df.at[VenueNumberList25[i-1]-1,'WikVen'])+0.2*(df.at[VenueNumberList25[i-1]-1,'EconomyVenRating']))
       
if len(VenueNumberList26)>0:
    df.at[VenueNumberList26[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList26)):
       df.at[VenueNumberList26[i]-1,"VenueValue"]=(4*(df.at[VenueNumberList26[i-1]-1,'AvgVen'])+3*(df.at[VenueNumberList26[i-1]-1,'MatchVen'])+2*(df.at[VenueNumberList26[i-1]-1,'SRVen'])+0.3*(df.at[VenueNumberList26[i-1]-1,'OverVen'])+0.5*(df.at[VenueNumberList26[i-1]-1,'WikVen'])+0.2*(df.at[VenueNumberList26[i-1]-1,'EconomyVenRating']))
       
if len(VenueNumberList27)>0:
    df.at[VenueNumberList27[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList27)):
        df.at[VenueNumberList27[i]-1,"VenueValue"]=(4*(df.at[VenueNumberList27[i-1]-1,'AvgVen'])+3*(df.at[VenueNumberList27[i-1]-1,'MatchVen'])+2*(df.at[VenueNumberList27[i-1]-1,'SRVen'])+0.3*(df.at[VenueNumberList27[i-1]-1,'OverVen'])+0.5*(df.at[VenueNumberList27[i-1]-1,'WikVen'])+0.2*(df.at[VenueNumberList27[i-1]-1,'EconomyVenRating']))


############################################
######### Detection of Travelling hour and distance #############
######################


### Readind the traveldata.csv and save it to a dataframe named Travel##########

                
Travel = pd.read_csv('venue_data.csv')


###### Calculating the number of rows in TravelData.csv#######

TravelRows=Travel.shape
print(TravelRows[0])
TravelRows=TravelRows[0]



###### Calculating the Travel Distance and Travel Hour #######


Venue_Distance=[]
Venue_Hour=[]

##### Setting the First value of travel distance and travel hour to zero#####


df.at[0,'Venue_Distance']=0
df.at[0,'Venue_Hour']=0

for i in range (1,columnNum):
    x=df.at[i,'VenueIndex'] 
    y=df.at[(i-1),'VenueIndex'] 
    
    if(x==y):
        df.at[i,'Venue_Distance']=0
        df.at[i,'Venue_Hour']=0
        
    else:
        if(df.at[i,'SMatch']!=1):
            for j in range(0,TravelRows):
                if((x==Travel.at[j,'venue1'] or x==Travel.at[j,'venue2']) and (y==Travel.at[j,'venue1'] or y==Travel.at[j,'venue2'])):
                    df.at[i,'Venue_Distance']=(Travel.at[j,'Distance(km)'])
                    df.at[i,'Venue_Hour']=(Travel.at[j,'Time(hr)'])
        else:
           df.at[i,'Venue_Distance']=0
           df.at[i,'Venue_Hour']=0

        
df.fillna( method ='ffill', inplace = True)






############################
#####################
######################
"""Creatiing Final Dataframe"""
finaldf=pd.DataFrame(df,columns=['VenueIndex',
                                 'OppositionIndex',
                                 'Venue_Distance',
                                 'Consistency',
                                 'Form',
                                 'OppositionValue',
                                 'VenueValue',
                                 'WicketRating'])
finaldf=finaldf.fillna(0)

##########################
############### Prediction ###################
            
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="white", color_codes=True)
import warnings # current version of seaborn generates a bunch of warnings that we'll ignore
warnings.filterwarnings("ignore")

from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split



X = finaldf[['VenueIndex',
             'OppositionIndex',
             'Venue_Distance',
             'Consistency',
             'Form',
             'OppositionValue',
             'VenueValue']]

y = finaldf['WicketRating']




# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)


 #random_state = 0
# Decision Tree's
from sklearn.tree import DecisionTreeClassifier

classifier = DecisionTreeClassifier()

classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

# Summary of the predictions made by the classifier
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
# Accuracy score
from sklearn.metrics import balanced_accuracy_score
print('Decision Tree Balanced accuracy is',balanced_accuracy_score(y_pred,y_test))

from sklearn.metrics import accuracy_score
print('accuracy Score is',accuracy_score(y_pred,y_test))


##############################
####################################
############ Custom Accuracy of Decision Tree with True Positive, True Negative, FP, FN ####################

confusion_matrix_list=[]

confusion_matrix_list=confusion_matrix(y_test, y_pred,labels=[1,2,3,4,5])

# print(confusion_matrix_list)
true_positive=[]
true_negative=[]
false_positive=[]
false_negative=[]


for row_element in range(len(confusion_matrix_list)):
    for col_element in range(len(confusion_matrix_list[row_element])):
        if(row_element==col_element):
            true_positive.append((confusion_matrix_list[row_element][col_element])*100)
            if(row_element==0):
                false_negative.append((confusion_matrix_list[1][col_element])*25)
                false_negative.append((confusion_matrix_list[2][col_element])*50)
                false_negative.append((confusion_matrix_list[3][col_element])*75)
                false_negative.append((confusion_matrix_list[4][col_element])*100)
                
                ####### True Negatives of 0,0 ######
                true_negative.append((confusion_matrix_list[1][1])*100)
                true_negative.append((confusion_matrix_list[1][2])*100)
                true_negative.append((confusion_matrix_list[1][3])*100)
                true_negative.append((confusion_matrix_list[1][4])*100)
                true_negative.append((confusion_matrix_list[2][1])*100)
                true_negative.append((confusion_matrix_list[2][2])*100)
                true_negative.append((confusion_matrix_list[2][3])*100)
                true_negative.append((confusion_matrix_list[2][4])*100)
                true_negative.append((confusion_matrix_list[3][1])*100)
                true_negative.append((confusion_matrix_list[3][2])*100)
                true_negative.append((confusion_matrix_list[3][3])*100)
                true_negative.append((confusion_matrix_list[3][4])*100)
                true_negative.append((confusion_matrix_list[4][1])*100)
                true_negative.append((confusion_matrix_list[4][2])*100)
                true_negative.append((confusion_matrix_list[4][3])*100)
                true_negative.append((confusion_matrix_list[4][4])*100)
                
                
                
                
                
                
            elif(row_element==1):
                false_negative.append((confusion_matrix_list[0][col_element])*25)
                false_negative.append((confusion_matrix_list[2][col_element])*25)
                false_negative.append((confusion_matrix_list[3][col_element])*50)
                false_negative.append((confusion_matrix_list[4][col_element])*75)
                
                
                                ####### True Negatives of 1,1 ######
                true_negative.append((confusion_matrix_list[0][0])*100)
                true_negative.append((confusion_matrix_list[0][2])*100)
                true_negative.append((confusion_matrix_list[0][3])*100)
                true_negative.append((confusion_matrix_list[0][4])*100)
                true_negative.append((confusion_matrix_list[2][0])*100)
                true_negative.append((confusion_matrix_list[2][2])*100)
                true_negative.append((confusion_matrix_list[2][3])*100)
                true_negative.append((confusion_matrix_list[2][4])*100)
                true_negative.append((confusion_matrix_list[3][0])*100)
                true_negative.append((confusion_matrix_list[3][2])*100)
                true_negative.append((confusion_matrix_list[3][3])*100)
                true_negative.append((confusion_matrix_list[3][4])*100)
                true_negative.append((confusion_matrix_list[4][0])*100)
                true_negative.append((confusion_matrix_list[4][2])*100)
                true_negative.append((confusion_matrix_list[4][3])*100)
                true_negative.append((confusion_matrix_list[4][4])*100)
                
            elif(row_element==2):
                false_negative.append((confusion_matrix_list[1][col_element])*25)
                false_negative.append((confusion_matrix_list[0][col_element])*50)
                false_negative.append((confusion_matrix_list[3][col_element])*25)
                false_negative.append((confusion_matrix_list[4][col_element])*50)
                
                                ####### True Negatives of 2,2 ######
                true_negative.append((confusion_matrix_list[0][0])*100)
                true_negative.append((confusion_matrix_list[0][1])*100)
                true_negative.append((confusion_matrix_list[0][3])*100)
                true_negative.append((confusion_matrix_list[0][4])*100)
                true_negative.append((confusion_matrix_list[1][0])*100)
                true_negative.append((confusion_matrix_list[1][1])*100)
                true_negative.append((confusion_matrix_list[1][3])*100)
                true_negative.append((confusion_matrix_list[1][4])*100)
                true_negative.append((confusion_matrix_list[3][0])*100)
                true_negative.append((confusion_matrix_list[3][1])*100)
                true_negative.append((confusion_matrix_list[3][3])*100)
                true_negative.append((confusion_matrix_list[3][4])*100)
                true_negative.append((confusion_matrix_list[4][0])*100)
                true_negative.append((confusion_matrix_list[4][1])*100)
                true_negative.append((confusion_matrix_list[4][3])*100)
                true_negative.append((confusion_matrix_list[4][4])*100)
                
            elif(row_element==3):
                false_negative.append((confusion_matrix_list[2][col_element])*25)
                false_negative.append((confusion_matrix_list[1][col_element])*50)
                false_negative.append((confusion_matrix_list[0][col_element])*75)
                false_negative.append((confusion_matrix_list[4][col_element])*25)
                
                
                
                    ####### True Negatives of 3,3 ######
                true_negative.append((confusion_matrix_list[0][0])*100)
                true_negative.append((confusion_matrix_list[0][1])*100)
                true_negative.append((confusion_matrix_list[0][2])*100)
                true_negative.append((confusion_matrix_list[0][4])*100)
                true_negative.append((confusion_matrix_list[1][0])*100)
                true_negative.append((confusion_matrix_list[1][1])*100)
                true_negative.append((confusion_matrix_list[1][2])*100)
                true_negative.append((confusion_matrix_list[1][4])*100)
                true_negative.append((confusion_matrix_list[2][0])*100)
                true_negative.append((confusion_matrix_list[2][1])*100)
                true_negative.append((confusion_matrix_list[2][2])*100)
                true_negative.append((confusion_matrix_list[2][4])*100)
                true_negative.append((confusion_matrix_list[4][0])*100)
                true_negative.append((confusion_matrix_list[4][1])*100)
                true_negative.append((confusion_matrix_list[4][2])*100)
                true_negative.append((confusion_matrix_list[4][4])*100)
                
            elif(row_element==4):
                false_negative.append((confusion_matrix_list[3][col_element])*25)
                false_negative.append((confusion_matrix_list[2][col_element])*50)
                false_negative.append((confusion_matrix_list[1][col_element])*75)
                false_negative.append((confusion_matrix_list[0][col_element])*100)
                
                
                    ####### True Negatives of 4,4 ######
                true_negative.append((confusion_matrix_list[0][0])*100)
                true_negative.append((confusion_matrix_list[0][1])*100)
                true_negative.append((confusion_matrix_list[0][2])*100)
                true_negative.append((confusion_matrix_list[0][3])*100)
                true_negative.append((confusion_matrix_list[1][0])*100)
                true_negative.append((confusion_matrix_list[1][1])*100)
                true_negative.append((confusion_matrix_list[1][2])*100)
                true_negative.append((confusion_matrix_list[1][3])*100)
                true_negative.append((confusion_matrix_list[2][0])*100)
                true_negative.append((confusion_matrix_list[2][1])*100)
                true_negative.append((confusion_matrix_list[2][2])*100)
                true_negative.append((confusion_matrix_list[2][3])*100)
                true_negative.append((confusion_matrix_list[3][0])*100)
                true_negative.append((confusion_matrix_list[3][1])*100)
                true_negative.append((confusion_matrix_list[3][2])*100)
                true_negative.append((confusion_matrix_list[3][3])*100)
            
        
            
        elif(abs(row_element-col_element)==1):
            true_positive.append((confusion_matrix_list[row_element][col_element])*75)
            false_positive.append((confusion_matrix_list[row_element][col_element])*25)
            
        elif(abs(row_element-col_element)==2):
            true_positive.append((confusion_matrix_list[row_element][col_element])*50)
            false_positive.append((confusion_matrix_list[row_element][col_element])*25)
            
        elif(abs(row_element-col_element)==3):
            true_positive.append((confusion_matrix_list[row_element][col_element])*25)
            false_positive.append((confusion_matrix_list[row_element][col_element])*75)
            
        elif(abs(row_element-col_element)==4):
            true_positive.append((confusion_matrix_list[row_element][col_element])*0)
            false_positive.append((confusion_matrix_list[row_element][col_element])*100)





divident= sum(true_positive)+sum(true_negative)

divisor= sum(true_positive)+sum(true_negative)+sum(false_positive)+sum(false_negative)

custom_accuracy_value=divident/divisor

print(custom_accuracy_value*100)







##########################
################################
###### Decision Tree Custom Accuracy ##############
print(y_pred)

PredList = y_pred.tolist()

print(PredList)

print(type(y_test))

test_df = y_test.to_frame()

TestList = test_df['WicketRating'].tolist()

print(TestList)


AccuracyPercent=[]
for (TrueVal,PredVal) in zip(TestList, PredList): 
    if(abs(TrueVal-PredVal)==0):
        AccuracyPercent.append(100)
    elif(abs(TrueVal-PredVal)==1):
        AccuracyPercent.append(75)
    elif(abs(TrueVal-PredVal)==2):
        AccuracyPercent.append(50)
    elif(abs(TrueVal-PredVal)==3):
        AccuracyPercent.append(25)
    elif(abs(TrueVal-PredVal)==4):
        AccuracyPercent.append(0)


TotalAccuracyPercent=sum(AccuracyPercent)

print(TotalAccuracyPercent)

TotalInstances=len(TestList)

CustomAccuracy=TotalAccuracyPercent/TotalInstances

print(CustomAccuracy)

#################################
########################################
##### Automating Prediction Model         ###
#################################
########################################


predictdf= pd.DataFrame(df,columns=['VenueIndex',
                                 'OppositionIndex',
                                 'Consistency',
                                 'Form',
                                 'OppositionValue',
                                 'VenueValue',
                                 'WicketRating'])

VenValue1_Pred=0
VenValue2_Pred=0
VenValue3_Pred=0
VenValue4_Pred=0
VenValue5_Pred=0
VenValue6_Pred=0
VenValue7_Pred=0
VenValue8_Pred=0
VenValue9_Pred=0
VenValue10_Pred=0
VenValue11_Pred=0
VenValue12_Pred=0
VenValue13_Pred=0
VenValue14_Pred=0
VenValue15_Pred=0
VenValue16_Pred=0
VenValue17_Pred=0
VenValue18_Pred=0
VenValue19_Pred=0
VenValue20_Pred=0
VenValue21_Pred=0
VenValue22_Pred=0
VenValue23_Pred=0
VenValue24_Pred=0
VenValue25_Pred=0
VenValue26_Pred=0
VenValue27_Pred=0



for i in range(0,columnNum):
## For finding the last performance in particular venue
    
    if(predictdf.at[i,'VenueIndex']==1):
      VenValue1_Pred= predictdf.at[i,'VenueValue']
      
    elif(predictdf.at[i,'VenueIndex']==2):
        VenValue2_Pred= predictdf.at[i,'VenueValue']
        
    elif(predictdf.at[i,'VenueIndex']==3):
        VenValue3_Pred= predictdf.at[i,'VenueValue']
        
    elif(predictdf.at[i,'VenueIndex']==4):
        VenValue4_Pred= predictdf.at[i,'VenueValue']
        
    elif(predictdf.at[i,'VenueIndex']==5):
        VenValue5_Pred= predictdf.at[i,'VenueValue']
        
    elif(predictdf.at[i,'VenueIndex']==6):
        VenValue6_Pred= predictdf.at[i,'VenueValue']
        
    elif(predictdf.at[i,'VenueIndex']==7):
        VenValue7_Pred= predictdf.at[i,'VenueValue']
        
    elif(predictdf.at[i,'VenueIndex']==8):
        VenValue8_Pred= predictdf.at[i,'VenueValue']
        
    elif(predictdf.at[i,'VenueIndex']==9):
        VenValue9_Pred= predictdf.at[i,'VenueValue']
        
    elif(predictdf.at[i,'VenueIndex']==10):
        VenValue10_Pred= predictdf.at[i,'VenueValue']
        
    elif(predictdf.at[i,'VenueIndex']==11):
        VenValue11_Pred= predictdf.at[i,'VenueValue']
        
    elif(predictdf.at[i,'VenueIndex']==12):
        VenValue12_Pred= predictdf.at[i,'VenueValue']
        
    elif(predictdf.at[i,'VenueIndex']==13):
        VenValue13_Pred= predictdf.at[i,'VenueValue']
        
    elif(predictdf.at[i,'VenueIndex']==14):
        VenValue14_Pred= predictdf.at[i,'VenueValue']
        
    elif(predictdf.at[i,'VenueIndex']==15):
        VenValue15_Pred= predictdf.at[i,'VenueValue']
        
    elif(predictdf.at[i,'VenueIndex']==16):
        VenValue16_Pred= predictdf.at[i,'VenueValue']
        
    elif(predictdf.at[i,'VenueIndex']==17):
        VenValue17_Pred= predictdf.at[i,'VenueValue']
        
    elif(predictdf.at[i,'VenueIndex']==18):
        VenValue18_Pred= predictdf.at[i,'VenueValue']
        
    elif(predictdf.at[i,'VenueIndex']==19):
        VenValue19_Pred= predictdf.at[i,'VenueValue']
        
    elif(predictdf.at[i,'VenueIndex']==20):
        VenValue20_Pred= predictdf.at[i,'VenueValue']
        
    elif(predictdf.at[i,'VenueIndex']==21):
        VenValue21_Pred= predictdf.at[i,'VenueValue']
        
    elif(predictdf.at[i,'VenueIndex']==22):
        VenValue22_Pred= predictdf.at[i,'VenueValue']
        
    elif(predictdf.at[i,'VenueIndex']==23):
        VenValue23_Pred= predictdf.at[i,'VenueValue']
        
    elif(predictdf.at[i,'VenueIndex']==24):
        VenValue24_Pred= predictdf.at[i,'VenueValue']
        
    elif(predictdf.at[i,'VenueIndex']==25):
        VenValue25_Pred= predictdf.at[i,'VenueValue']
        
    elif(predictdf.at[i,'VenueIndex']==26):
        VenValue26_Pred= predictdf.at[i,'VenueValue']

    elif(predictdf.at[i,'VenueIndex']==27):
        VenValue27_Pred= predictdf.at[i,'VenueValue']
   









OppValue_Pred1=0
OppValue_Pred2=0
OppValue_Pred3=0
OppValue_Pred4=0
OppValue_Pred5=0
OppValue_Pred6=0
OppValue_Pred7=0
OppValue_Pred8=0
OppValue_Pred9=0
OppValue_Pred10=0
OppValue_Pred11=0
OppValue_Pred12=0

for i in range(0,columnNum):
## For finding the last performance in particular venue
    if(predictdf.at[i,'OppositionIndex']==1):
      OppValue_Pred1= predictdf.at[i,'OppositionValue']
      
    elif(predictdf.at[i,'OppositionIndex']==2):
        OppValue_Pred2= predictdf.at[i,'OppositionValue']
        
    elif(predictdf.at[i,'OppositionIndex']==3):
        OppValue_Pred3= predictdf.at[i,'OppositionValue']
        
    elif(predictdf.at[i,'OppositionIndex']==4):
        OppValue_Pred4= predictdf.at[i,'OppositionValue']
        
    elif(predictdf.at[i,'OppositionIndex']==5):
        OppValue_Pred5= predictdf.at[i,'OppositionValue']
        
    elif(predictdf.at[i,'OppositionIndex']==6):
        OppValue_Pred6= predictdf.at[i,'OppositionValue']
        
    elif(predictdf.at[i,'OppositionIndex']==7):
        OppValue_Pred7= predictdf.at[i,'OppositionValue']
        
    elif(predictdf.at[i,'OppositionIndex']==8):
        OppValue_Pred8= predictdf.at[i,'OppositionValue']
        
    elif(predictdf.at[i,'OppositionIndex']==9):
        OppValue_Pred9= predictdf.at[i,'OppositionValue']
        
    elif(predictdf.at[i,'OppositionIndex']==10):
        OppValue_Pred10= predictdf.at[i,'OppositionValue']
        
    elif(predictdf.at[i,'OppositionIndex']==11):
        OppValue_Pred11= predictdf.at[i,'OppositionValue']
        
    elif(predictdf.at[i,'OppositionIndex']==12):
        OppValue_Pred12= predictdf.at[i,'OppositionValue']
        



PredictDataDf= pd.DataFrame({'Ven/Opp':[1,2,3,4,5,6,7,8,9,10
                                     ,11,12,13,14,15,16,17,18,19,20,
                                     21,22,23,24,25,26,27],
                             
                            'VenVal':[VenValue1_Pred,
                                      VenValue2_Pred,
                                      VenValue3_Pred,
                                      VenValue4_Pred,
                                      VenValue5_Pred,
                                      VenValue6_Pred,
                                      VenValue7_Pred,
                                      VenValue8_Pred,
                                      VenValue9_Pred,
                                      VenValue10_Pred,
                                      VenValue11_Pred,
                                      VenValue12_Pred,
                                      VenValue13_Pred,
                                      VenValue14_Pred,
                                      VenValue15_Pred,
                                      VenValue16_Pred,
                                      VenValue17_Pred,
                                      VenValue18_Pred,
                                      VenValue19_Pred,
                                      VenValue20_Pred,
                                      VenValue21_Pred,
                                      VenValue22_Pred,
                                      VenValue23_Pred,
                                      VenValue24_Pred,
                                      VenValue25_Pred,
                                      VenValue26_Pred,
                                      VenValue27_Pred],
                            'OppVal':[OppValue_Pred1,
                                      OppValue_Pred2,
                                      OppValue_Pred3,
                                      OppValue_Pred4,
                                      OppValue_Pred5,
                                      OppValue_Pred6,
                                      OppValue_Pred7,
                                      OppValue_Pred8,
                                      OppValue_Pred9,
                                      OppValue_Pred10,
                                      OppValue_Pred11,
                                      
                                      OppValue_Pred12,
                                     0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]})


ConValue_Pred=df.at[columnNum-1,'Consistency']
FormValue_Pred=df.at[columnNum-1,'Form']



Match_wise_Run=[]





Ven_Pred=[2,1,9,4,1,1,3,6,5,1,1,8,1,1]



Opp_Pred=[3,8,9,4,2,1,6,8,2,3,6,1,4,9]

travel_init=0

row_col=PredictDataDf.shape

rownumpred=row_col[0]

for i in range(14):
    for j in range(rownumpred):
        
        if(Opp_Pred[i]==PredictDataDf.at[j,'Ven/Opp']):
            
            OppPredValue=PredictDataDf.at[j,'OppVal']
            
        if(Ven_Pred[i]==PredictDataDf.at[j,'Ven/Opp']):
            
            VenPredValue=PredictDataDf.at[j,'VenVal']
    
    

    print(classifier.predict([[Ven_Pred[i],
                           Opp_Pred[i],
                           travel_init,
                           ConValue_Pred,
                           FormValue_Pred,
                           OppPredValue,
                           VenPredValue]]))
    Match_wise_Run.append(classifier.predict([[Ven_Pred[i],
                           Opp_Pred[i],
                           travel_init,
                           ConValue_Pred,
                           FormValue_Pred,
                           OppPredValue,
                           VenPredValue]]))
    
    for k in range(0,TravelRows):
        if((Ven_Pred[i]==Travel.at[k,'venue1'] or Ven_Pred[i]==Travel.at[k,'venue2']) and 
           (Ven_Pred[i-1]==Travel.at[k,'venue1'] or Ven_Pred[i-1]==Travel.at[k,'venue2'])):
            travel_init=(Travel.at[j,'Distance(km)'])



#####################################
#######################################
####### Performance Output ###############
            
Total_Wicket=0
            
for values in Match_wise_Run:
    
    if(values==1):
        
        Total_Wicket+=1
        
    elif(values==2):
        
        Total_Wicket+=2
    
    elif(values==3):
        
        Total_Wicket+=3
        
    elif(values==4):
        
        Total_Wicket+=4
        
    elif(values==5):
        Total_Wicket+=5
        
print(Total_Wicket)
        

Performance_df = pd.DataFrame({'Player_Name':['Yuzvendra Chahal'],'Total Wicket':[Total_Wicket],'Cost':[17]})
#Performance_df = pd.DataFrame(Total_Run, columns= ['Total Run'])

Performance_df.to_csv (r'Yuzvendra Chahal_Performance.csv', index = False, header=True)    
            
            
            
           