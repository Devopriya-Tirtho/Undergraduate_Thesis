# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 12:21:56 2020

@author: SHAFIN
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 19:17:44 2020

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
dataset=pd.read_csv('DineshKarthik.csv')

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
    y=dataset.at[i,'Venue']
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
df=pd.DataFrame(dataset,columns=['Match','Date','Runs','TotalRuns','Balls','Out','VenueIndex','OppositionIndex'
                                 ,'VenueExp'])
df['Date']=pd.to_datetime(df['Date'].astype(str), format='%d/%m/%Y')

################################
################################

#Number of Rows
a=df.shape
print(a[0])
columnNum=a[0]
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

'''Seasonwise Run,Ball,Total Out,Cumulative fifty,hundred,zero'''
##############################
#################################


SRun=[]
SOut=[]
SBall=[]
SFifty=[]
SHundred=[]
SZero=[]
run=0
ball=0
out=0
fifty=0
hundred=0
zero=0
count=2

for i in range (b[0]):
    if(i!=b[0]-1):
        
        if  (df.at[i,'SMatch']- df.at[i+1,'SMatch'])<0 :
            run+=df.at[i,'Runs']
            SRun.append(run)
            
            ball+=df.at[i,'Balls']
            SBall.append(ball)
            
            out+=df.at[i,'Out']
            SOut.append(out)
            
            if df.at[i,'Runs']>=50 and df.at[i,'Runs']<100:
                fifty=fifty+1
                SFifty.append(fifty)
            else:
               SFifty.append(fifty) 
               
            if df.at[i,'Runs']>=100:
                hundred=hundred+1
                SHundred.append(hundred)
                
            else:
               SHundred.append(hundred)
               
            if df.at[i,'Runs']==0:
                zero=zero+1
                SZero.append(zero)
                
            else:
               SZero.append(zero)
                
                
    

        else:
            run+=df.at[i,'Runs']
            SRun.append(run)
            run=0
            ball+=df.at[i,'Balls']
            SBall.append(ball)
            ball=0
            out+=df.at[i,'Out']
            SOut.append(out)
            out=0 
            
            if df.at[i,'Runs']>=50 and df.at[i,'Runs']<100:
                fifty=fifty+1
                SFifty.append(fifty)
                fifty=0
            else:
               SFifty.append(fifty)
               fifty=0
            if df.at[i,'Runs']>=100:
                hundred=hundred+1
                SHundred.append(hundred)
                hundred=0
            else:
               SHundred.append(hundred)
               hundred=0
            if df.at[i,'Runs']==0:
                zero=zero+1
                SZero.append(zero)
                zero=0
            else:
               SZero.append(zero)
               zero=0
               
               
               
    else:

        SRun.append(SRun[i-1]+df.at[i,'Runs'])
           
       
        SBall.append(SBall[i-1]+df.at[i,'Balls'])
           
        
        SOut.append(SOut[i-1]+df.at[i,'Out'])
        
        
        if df.at[i,'Runs']>=50 and df.at[i,'Runs']<100:
                fifty=fifty+1
                SFifty.append(fifty)
                
        else:
             SFifty.append(fifty)
         
        if df.at[i,'Runs']>=100:
                hundred=hundred+1
                SHundred.append(hundred)
               
        else:
             SHundred.append(hundred)
           
        if df.at[i,'Runs']==0:
                zero=zero+1
                SZero.append(zero)
              
        else:
             SZero.append(zero)
                                               
df["SRun"] = SRun  
df["SBall"] = SBall  
df["SOut"] = SOut  
df["SFifty"] = SFifty  
df["SHundred"] = SHundred  
df["SZero"] = SZero  
 


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

################################
################################

""" Number of Cumulative Outs """
TotalOutNumber=0
TotalOut=[]
for i in range(0,columnNum):
    if (df.at[i,'Out']==1):
        TotalOutNumber=TotalOutNumber+1
        TotalOut.append(TotalOutNumber)
    elif(df.at[i,'Out']==0):
        TotalOut.append(TotalOutNumber)

df["TotalOut"]=TotalOut

################################
################################




#For NoOfInningsConsistency###############
############################

MatchCon=[]
for value in df["Match"]:
    if value>=0 and value<=41:
        MatchCon.append(1)
    elif value>=42 and value<=71:
        MatchCon.append(2)
    elif value>=72 and value<=101:
        MatchCon.append(3)
    elif value>=102 and value<=131:
        MatchCon.append(4)
    elif value>=132 :
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
## TotalRuns by particular venue
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
    if (df.at[i,'Out']==1):
        if(val==1):
            outven1=outven1+1
            VenueTotalOut.append(outven1)
        elif(val==2):
            outven2=outven2+1
            VenueTotalOut.append(outven2)
        elif(val==3):
            outven3=outven3+1
            VenueTotalOut.append(outven3)
        elif(val==4):
            outven4=outven4+1
            VenueTotalOut.append(outven4)
        elif(val==5):
            outven5=outven5+1
            VenueTotalOut.append(outven5)
        elif(val==6):
            outven6=outven6+1
            VenueTotalOut.append(outven6)
        elif(val==7):
            outven7=outven7+1
            VenueTotalOut.append(outven7)
        elif(val==8):
            outven8=outven8+1
            VenueTotalOut.append(outven8)
        elif(val==9):
            outven9=outven9+1
            VenueTotalOut.append(outven9)
        elif(val==10):
            outven10=outven10+1
            VenueTotalOut.append(outven10)
        elif(val==11):
            outven11=outven11+1
            VenueTotalOut.append(outven11)
        elif(val==12):
            outven12=outven12+1
            VenueTotalOut.append(outven12)
        elif(val==13):
            outven13=outven13+1
            VenueTotalOut.append(outven13)
        elif(val==14):
            outven14=outven14+1
            VenueTotalOut.append(outven14)
        elif(val==15):
            outven15=outven15+1
            VenueTotalOut.append(outven15)
        elif(val==16):
            outven16=outven16+1
            VenueTotalOut.append(outven16)
        elif(val==17):
            outven17=outven17+1
            VenueTotalOut.append(outven17)
        elif(val==18):
            outven18=outven18+1
            VenueTotalOut.append(outven18)
        elif(val==19):
            outven19=outven19+1
            VenueTotalOut.append(outven19)
        elif(val==20):
            outven20=outven20+1
            VenueTotalOut.append(outven20)
        elif(val==21):
            outven21=outven21+1
            VenueTotalOut.append(outven21)
        elif(val==22):
            outven22=outven22+1
            VenueTotalOut.append(outven22)
        elif(val==23):
            outven23=outven23+1
            VenueTotalOut.append(outven23)
        elif(val==24):
            outven24=outven24+1
            VenueTotalOut.append(outven24)
        elif(val==25):
            outven25=outven25+1
            VenueTotalOut.append(outven25)
        elif(val==26):
            outven26=outven26+1
            VenueTotalOut.append(outven26)
        elif(val==27):
            outven27=outven27+1
            VenueTotalOut.append(outven27)
        else:
            VenueTotalOut.append(0)
            
            
            
            
    elif(df.at[i,'Out']==0):
        if(val==1):
            VenueTotalOut.append(outven1)
        elif(val==2):          
            VenueTotalOut.append(outven2)
        elif(val==3):         
            VenueTotalOut.append(outven3)
        elif(val==4):            
            VenueTotalOut.append(outven4)
        elif(val==5):           
            VenueTotalOut.append(outven5)
        elif(val==6):           
            VenueTotalOut.append(outven6)
        elif(val==7):         
            VenueTotalOut.append(outven7)
        elif(val==8):       
            VenueTotalOut.append(outven8)
        elif(val==9):           
            VenueTotalOut.append(outven9)
        elif(val==10):           
            VenueTotalOut.append(outven10)
        elif(val==11):           
            VenueTotalOut.append(outven11)
        elif(val==12):        
            VenueTotalOut.append(outven12)
        elif(val==13):         
            VenueTotalOut.append(outven13)
        elif(val==14):            
            VenueTotalOut.append(outven14)
        elif(val==15):         
            VenueTotalOut.append(outven15)
        elif(val==16):           
            VenueTotalOut.append(outven16)
        elif(val==17):         
            VenueTotalOut.append(outven17)
        elif(val==18):         
            VenueTotalOut.append(outven18)
        elif(val==19):         
            VenueTotalOut.append(outven19)
        elif(val==20):         
            VenueTotalOut.append(outven20)
        elif(val==21):         
            VenueTotalOut.append(outven21)
        elif(val==22):         
            VenueTotalOut.append(outven22)
        elif(val==23):         
            VenueTotalOut.append(outven23)
        elif(val==24):         
            VenueTotalOut.append(outven24)
        elif(val==25):         
            VenueTotalOut.append(outven25)
        elif(val==26):         
            VenueTotalOut.append(outven26)
        elif(val==27):         
            VenueTotalOut.append(outven27)
        else:
            VenueTotalOut.append(0)            
    else:
        VenueTotalOut.append(0)
   
df["VenueTotalOut"]=VenueTotalOut


## TotalRuns against particular opposition
opprun1=0
opprun2=0
opprun3=0
opprun4=0
opprun5=0
opprun6=0
opprun7=0
opprun8=0
opprun9=0
opprun10=0
opprun11=0
opprun12=0



OppTotalRun=[]   
for i in range(0,columnNum):
    val=df.at[i,'OppositionIndex']
    if(val==1):
        opprun1=opprun1+df.at[i,'Runs']
        OppTotalRun.append(opprun1)
    elif(val==2):
        opprun2=opprun2+df.at[i,'Runs']
        OppTotalRun.append(opprun2)
    elif(val==3):
        opprun3=opprun3+df.at[i,'Runs']
        OppTotalRun.append(opprun3)
    elif(val==4):
        opprun4=opprun4+df.at[i,'Runs']
        OppTotalRun.append(opprun4)
    elif(val==5):
        opprun5=opprun5+df.at[i,'Runs']
        OppTotalRun.append(opprun5)
    elif(val==6):
        opprun6=opprun6+df.at[i,'Runs']
        OppTotalRun.append(opprun6)
    elif(val==7):
        opprun7=opprun7+df.at[i,'Runs']
        OppTotalRun.append(opprun7)
    elif(val==8):
        opprun8=opprun8+df.at[i,'Runs']
        OppTotalRun.append(opprun8)
    elif(val==9):
        opprun9=opprun9+df.at[i,'Runs']
        OppTotalRun.append(opprun9)
    elif(val==10):
        opprun10=opprun10+df.at[i,'Runs']
        OppTotalRun.append(opprun10)
    elif(val==11):
        opprun11=opprun11+df.at[i,'Runs']
        OppTotalRun.append(opprun11)
    elif(val==12):
        opprun12=opprun12+df.at[i,'Runs']
        OppTotalRun.append(opprun12)
    else:
        OppTotalRun.append(0)
   
df["OppTotalRun"]=OppTotalRun


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
    if (df.at[i,'Out']==1):
        if(val==1):
            outopp1=outopp1+1
            OppTotalOut.append(outopp1)
        elif(val==2):
            outopp2=outopp2+1
            OppTotalOut.append(outopp2)
        elif(val==3):
            outopp3=outopp3+1
            OppTotalOut.append(outopp3)
        elif(val==4):
            outopp4=outopp4+1
            OppTotalOut.append(outopp4)
        elif(val==5):
            outopp5=outopp5+1
            OppTotalOut.append(outopp5)
        elif(val==6):
            outopp6=outopp6+1
            OppTotalOut.append(outopp6)
        elif(val==7):
            outopp7=outopp7+1
            OppTotalOut.append(outopp7)
        elif(val==8):
            outopp8=outopp8+1
            OppTotalOut.append(outopp8)
        elif(val==9):
            outopp9=outopp9+1
            OppTotalOut.append(outopp9)
        elif(val==10):
            outopp10=outopp10+1
            OppTotalOut.append(outopp10)
        elif(val==11):
            outopp11=outopp11+1
            OppTotalOut.append(outopp11)
        elif(val==12):
            outopp12=outopp12+1
            OppTotalOut.append(outopp12)
       
        else:
            OppTotalOut.append(0)
            
            
    elif(df.at[i,'Out']==0):
        if(val==1):
            OppTotalOut.append(outopp1)
        elif(val==2):          
            OppTotalOut.append(outopp2)
        elif(val==3):         
            OppTotalOut.append(outopp3)
        elif(val==4):            
            OppTotalOut.append(outopp4)
        elif(val==5):           
            OppTotalOut.append(outopp5)
        elif(val==6):           
            OppTotalOut.append(outopp6)
        elif(val==7):         
            OppTotalOut.append(outopp7)
        elif(val==8):       
            OppTotalOut.append(outopp8)
        elif(val==9):           
            OppTotalOut.append(outopp9)
        elif(val==10):           
            OppTotalOut.append(outopp10)
        elif(val==11):           
            OppTotalOut.append(outopp11)
        elif(val==12):           
            OppTotalOut.append(outopp12)        
        else:
            OppTotalOut.append(0)            
    else:
        OppTotalOut.append(0)
   
df["OppTotalOut"]=OppTotalOut







#Calculation of Average for all match
CalAvg=[]
for i in range(0,columnNum):
    #CalAvg.append(math.floor((df.at[i,'TotalRuns']/df.at[i,'TotalOut'])))
    CalAvg.append(df.at[i,'TotalRuns']/df.at[i,'TotalOut'])
df["CalAvg"]=CalAvg

#Calculation of Average by venue
VenAvg=[]
for i in range(0,columnNum):
    #CalAvg.append(math.floor((df.at[i,'TotalRuns']/df.at[i,'TotalOut'])))
    if(df.at[i,'VenueTotalOut']==0):
        VenAvg.append(df.at[i,'CalAvg'])
        ####VenAvg.append("NBA")
        ## NBA = No Batting Average
    else:
        VenAvg.append(df.at[i,'VenueRun']/df.at[i,'VenueTotalOut'])
df["VenAvg"]=VenAvg

#Calculation of Average Against Particular Opposition
OppAvg=[]
for i in range(0,columnNum):
    #CalAvg.append(math.floor((df.at[i,'TotalRuns']/df.at[i,'TotalOut'])))
    if(df.at[i,'OppTotalOut']==0):
        OppAvg.append(df.at[i,'CalAvg'])
        ####VenAvg.append("NBA")
        ## NBA = No Batting Average
    else:
        OppAvg.append(df.at[i,'OppTotalRun']/df.at[i,'OppTotalOut'])
df["OppAvg"]=OppAvg


################################
################################
#################################

#Calculation of Average for a particular season's match
SeasonAvg=[]
for i in range(0,columnNum):
    #CalAvg.append(math.floor((df.at[i,'TotalRuns']/df.at[i,'TotalOut'])))
    if(df.at[i,'SOut']==0):
        SeasonAvg.append(df.at[i,'CalAvg'])
        ####VenAvg.append("NBA")
        ## NBA = No Batting Average
    else:
        SeasonAvg.append(df.at[i,'SRun']/df.at[i,'SOut'])
df["SeasonAvg"]=SeasonAvg

################################
################################
#################################




#Calculation of SR for all match
CalSR=[]
for i in range(0,columnNum):
    #CalAvg.append(math.floor((df.at[i,'TotalRuns']/df.at[i,'TotalOut'])))
    if((df.at[i,'Runs']>0) and (df.at[i,'Balls']>0)):
        CalSR.append((df.at[i,'Runs']/df.at[i,'Balls'])*100)
    else: 
        CalSR.append(0)
df["CalSR"]=CalSR


################################
################################




#Calculation of Fifty
CalFifty=[]
for i in range(0,columnNum):
    if ((df.at[i,'Runs']>=50) and (df.at[i,'Runs']<100)):
        CalFifty.append(1)
    else:
        CalFifty.append(0) 
df["CalFifty"]=CalFifty


#Number of Fifties
fiftycount=0
NumFifty=[]
for i in range(0,columnNum):
    if (df.at[i,'CalFifty']==1):
        fiftycount=fiftycount+1
        NumFifty.append(fiftycount)
    else:
        NumFifty.append(fiftycount)
df["NumFifty"]=NumFifty
#Rating For Fifty for Consistency #shafinP
FiftyCon=[]
for value in df["NumFifty"]: 
     if value==0:
        FiftyCon.append(0)
     if value>=1 and value<=3:
        FiftyCon.append(1)
     elif value>=4 and value<=6:
        FiftyCon.append(2)
     elif value>=7 and value<=14:
        FiftyCon.append(3)
     elif value>=15 and value<=22:
        FiftyCon.append(4)
     elif value>=22 :
        FiftyCon.append(5)
df["FiftyCon"] = FiftyCon    

#Rating For Fifty for Form #shafinP
FiftyForm=[]
for value in df["SFifty"]: 
     if value==0:
        FiftyForm.append(0)
     if value>=1 and value<=2:
        FiftyForm.append(1)
     elif value>=3 and value<=4:
        FiftyForm.append(2)
     elif value>=5 and value<=6:
        FiftyForm.append(3)
     elif value>=7 and value<=8:
        FiftyForm.append(4)
     elif value>8 :
        FiftyForm.append(5)
df["FiftyForm"] = FiftyForm  


#Fifties In Particular Venue
fven1=0
fven2=0
fven3=0
fven4=0
fven5=0
fven6=0
fven7=0
fven8=0
fven9=0
fven10=0
fven11=0
fven12=0
fven13=0
fven14=0
fven15=0
fven16=0
fven17=0
fven18=0
fven19=0
fven20=0
fven21=0
fven22=0
fven23=0
fven24=0
fven25=0
fven26=0
fven27=0

VenueFifty=[]   
for i in range(0,columnNum):
    val=df.at[i,'VenueIndex']
    if (df.at[i,'CalFifty']==1):
        if(val==1):
            fven1=fven1+1
            VenueFifty.append(fven1)
        elif(val==2):
            fven2=fven2+1
            VenueFifty.append(fven2)
        elif(val==3):
            fven3=fven3+1
            VenueFifty.append(fven3)
        elif(val==4):
            fven4=fven4+1
            VenueFifty.append(fven4)
        elif(val==5):
            fven5=fven5+1
            VenueFifty.append(fven5)
        elif(val==6):
            fven6=fven6+1
            VenueFifty.append(fven6)
        elif(val==7):
            fven7=fven7+1
            VenueFifty.append(fven7)
        elif(val==8):
            fven8=fven8+1
            VenueFifty.append(fven8)
        elif(val==9):
            fven9=fven9+1
            VenueFifty.append(fven9)
        elif(val==10):
            fven10=fven10+1
            VenueFifty.append(fven10)
        elif(val==11):
            fven11=fven11+1
            VenueFifty.append(fven11)
        elif(val==12):
            fven12=fven12+1
            VenueFifty.append(fven12)
        elif(val==13):
            fven13=fven13+1
            VenueFifty.append(fven13)
        elif(val==14):
            fven14=fven14+1
            VenueFifty.append(fven14)
        elif(val==15):
            fven15=fven15+1
            VenueFifty.append(fven15)
        elif(val==16):
            fven16=fven16+1
            VenueFifty.append(fven16)
        elif(val==17):
            fven17=fven17+1
            VenueFifty.append(fven17)
        elif(val==18):
            fven18=fven18+1
            VenueFifty.append(fven18)
        elif(val==19):
            fven19=fven19+1
            VenueFifty.append(fven19)
        elif(val==20):
            fven20=fven20+1
            VenueFifty.append(fven20)
        elif(val==21):
            fven21=fven21+1
            VenueFifty.append(fven21)
        elif(val==22):
            fven22=fven22+1
            VenueFifty.append(fven22)
        elif(val==23):
            fven23=fven23+1
            VenueFifty.append(fven23)
        elif(val==24):
            fven24=fven24+1
            VenueFifty.append(fven24)
        elif(val==25):
            fven25=fven25+1
            VenueFifty.append(fven25)
        elif(val==26):
            fven26=fven26+1
            VenueFifty.append(fven26)
        elif(val==27):
            fven27=fven27+1
            VenueFifty.append(fven27)
                        
                                                            
    elif(df.at[i,'CalFifty']==0):
        if(val==1):
            VenueFifty.append(fven1)
        elif(val==2):          
            VenueFifty.append(fven2)
        elif(val==3):         
            VenueFifty.append(fven3)
        elif(val==4):            
            VenueFifty.append(fven4)
        elif(val==5):           
            VenueFifty.append(fven5)
        elif(val==6):           
            VenueFifty.append(fven6)
        elif(val==7):         
            VenueFifty.append(fven7)
        elif(val==8):       
            VenueFifty.append(fven8)
        elif(val==9):           
            VenueFifty.append(fven9)
        elif(val==10):           
            VenueFifty.append(fven10)
        elif(val==11):           
            VenueFifty.append(fven11)
        elif(val==12):        
            VenueFifty.append(fven12)
        elif(val==13):         
            VenueFifty.append(fven13)
        elif(val==14):            
            VenueFifty.append(fven14)
        elif(val==15):         
            VenueFifty.append(fven15)
        elif(val==16):           
            VenueFifty.append(fven16)
        elif(val==17):         
            VenueFifty.append(fven17)
        elif(val==18):         
            VenueFifty.append(fven18)
        elif(val==19):         
            VenueFifty.append(fven19)
        elif(val==20):         
            VenueFifty.append(fven20)
        elif(val==21):         
            VenueFifty.append(fven21)
        elif(val==22):         
            VenueFifty.append(fven22)
        elif(val==23):         
            VenueFifty.append(fven23)
        elif(val==24):         
            VenueFifty.append(fven24)
        elif(val==25):         
            VenueFifty.append(fven25)
        elif(val==26):         
            VenueFifty.append(fven26)
        elif(val==27):         
            VenueFifty.append(fven27)
        else:
            VenueFifty.append(0)
   
df["VenueFifty"]=VenueFifty

#Rating For Fifty for Venue done
FiftyVenue=[]
for value in df["VenueFifty"]: 
     if value==0:
        FiftyVenue.append(0)
     elif value>=1 and value<=3 :
        FiftyVenue.append(1)
     elif value>=4 and value<=6:
        FiftyVenue.append(2)
     elif value>=6 and value<=7:
        FiftyVenue.append(3)
     elif value>7:
        FiftyVenue.append(4)
df["FiftyVenue"] = FiftyVenue  




##Fifties against a particular opposition
fopp1=0
fopp2=0
fopp3=0
fopp4=0
fopp5=0
fopp6=0
fopp7=0
fopp8=0
fopp9=0
fopp10=0
fopp11=0
fopp12=0
    
    
OppFifty=[]   
for i in range(0,columnNum):
    val=df.at[i,'OppositionIndex']
    if (df.at[i,'CalFifty']==1):
        if(val==1):
            fopp1=fopp1+1
            OppFifty.append(fopp1)
        elif(val==2):
            fopp2=fopp2+1
            OppFifty.append(fopp2)
        elif(val==3):
            fopp3=fopp3+1
            OppFifty.append(fopp3)
        elif(val==4):
            fopp4=fopp4+1
            OppFifty.append(fopp4)
        elif(val==5):
            fopp5=fopp5+1
            OppFifty.append(fopp5)
        elif(val==6):
            fopp6=fopp6+1
            OppFifty.append(fopp6)
        elif(val==7):
            fopp7=fopp7+1
            OppFifty.append(fopp7)
        elif(val==8):
            fopp8=fopp8+1
            OppFifty.append(fopp8)
        elif(val==9):
            fopp9=fopp9+1
            OppFifty.append(fopp9)
        elif(val==10):
            fopp10=fopp10+1
            OppFifty.append(fopp10)
        elif(val==11):
            fopp11=fopp11+1
            OppFifty.append(fopp11)
        elif(val==12):
            fopp12=fopp12+1
            OppFifty.append(fopp12)
       
    elif(df.at[i,'CalFifty']==0):
        if(val==1):
            OppFifty.append(fopp1)
        elif(val==2):          
            OppFifty.append(fopp2)
        elif(val==3):         
            OppFifty.append(fopp3)
        elif(val==4):            
            OppFifty.append(fopp4)
        elif(val==5):           
            OppFifty.append(fopp5)
        elif(val==6):           
            OppFifty.append(fopp6)
        elif(val==7):         
            OppFifty.append(fopp7)
        elif(val==8):       
            OppFifty.append(fopp8)
        elif(val==9):           
            OppFifty.append(fopp9)
        elif(val==10):           
            OppFifty.append(fopp10)
        elif(val==11):           
            OppFifty.append(fopp11)
        elif(val==12):           
            OppFifty.append(fopp12)
       
        else:
            OppFifty.append(0)
   
    
df["OppFifty"]=OppFifty


    
#Rating For Fifty for Opposition done
FiftyOppRating=[]
for value in df["OppFifty"]: 
     if value==0:
        FiftyOppRating.append(0)
     elif value>=1 and value<=2:
        FiftyOppRating.append(1)
     elif value>=3 and value<=4:
        FiftyOppRating.append(2)
     elif value>=4 and value<=5:
        FiftyOppRating.append(3)
     elif value>5:
        FiftyOppRating.append(4)
df["FiftyOppRating"] = FiftyOppRating      
    
    
    
    
    
    


################################
################################

#Calculation of Hundred
CalHundred=[]
for i in range(0,columnNum):
    if ((df.at[i,'Runs']>=100) and (df.at[i,'Runs']<200)):
        CalHundred.append(1)
    else:
        CalHundred.append(0) 
df["CalHundred"]=CalHundred

#Number of Hundred
Hundredcount=0
NumHundred=[]
for i in range(0,columnNum):
    if (df.at[i,'CalHundred']==1):
        Hundredcount=Hundredcount+1
        NumHundred.append(Hundredcount)
    else:
        NumHundred.append(Hundredcount)
df["NumHundred"]=NumHundred


#Rating For Hundred for Consistency 
HundredCon=[]
for value in df["NumHundred"]: 
     if value==0:
        HundredCon.append(0)
     elif value==1:
        HundredCon.append(1)
     if value>=2 and value<=3:
        HundredCon.append(2)
     elif value>=4 :
        HundredCon.append(3)
df["HundredCon"] = HundredCon    

#Rating For Hundred for Form
CenturyForm=[]
for value in df["SHundred"]: 
     if value==0:
       CenturyForm.append(0)
     if value==1:
        CenturyForm.append(1)
     elif value==2:
        CenturyForm.append(2)
     elif value>=3:
        CenturyForm.append(3)

df["CenturyForm"] = CenturyForm  






#Hundreds In Particular Venue
hven1=0
hven2=0
hven3=0
hven4=0
hven5=0
hven6=0
hven7=0
hven8=0
hven9=0
hven10=0
hven11=0
hven12=0
hven13=0
hven14=0
hven15=0
hven16=0
hven17=0
hven18=0
hven19=0
hven20=0
hven21=0
hven22=0
hven23=0
hven24=0
hven25=0
hven26=0
hven27=0

VenueHundred=[]   
for i in range(0,columnNum):
    val=df.at[i,'VenueIndex']
    if (df.at[i,'CalHundred']==1):
        if(val==1):
            hven1=hven1+1
            VenueHundred.append(hven1)
        elif(val==2):
            hven2=hven2+1
            VenueHundred.append(hven2)
        elif(val==3):
            hven3=hven3+1
            VenueHundred.append(hven3)
        elif(val==4):
            hven4=hven4+1
            VenueHundred.append(hven4)
        elif(val==5):
            hven5=hven5+1
            VenueHundred.append(hven5)
        elif(val==6):
            hven6=hven6+1
            VenueHundred.append(hven6)
        elif(val==7):
            hven7=hven7+1
            VenueHundred.append(hven7)
        elif(val==8):
            hven8=hven8+1
            VenueHundred.append(hven8)
        elif(val==9):
            hven9=hven9+1
            VenueHundred.append(hven9)
        elif(val==10):
            hven10=hven10+1
            VenueHundred.append(hven10)
        elif(val==11):
            hven11=hven11+1
            VenueHundred.append(hven11)
        elif(val==12):
            hven12=hven12+1
            VenueHundred.append(hven12)
        elif(val==13):
            hven13=hven13+1
            VenueHundred.append(hven13)
        elif(val==14):
            hven14=hven14+1
            VenueHundred.append(hven14)
        elif(val==15):
            hven15=hven15+1
            VenueHundred.append(hven15)
        elif(val==16):
            hven16=hven16+1
            VenueHundred.append(hven16)
        elif(val==17):
            hven17=hven17+1
            VenueHundred.append(hven17)
        elif(val==18):
            hven18=hven18+1
            VenueHundred.append(hven18)
        elif(val==19):
            hven19=hven19+1
            VenueHundred.append(hven19)
        elif(val==20):
            hven20=hven20+1
            VenueHundred.append(hven20)
        elif(val==21):
            hven21=hven21+1
            VenueHundred.append(hven21)
        elif(val==22):
            hven22=hven22+1
            VenueHundred.append(hven22)
        elif(val==23):
            hven23=hven23+1
            VenueHundred.append(hven23)
        elif(val==24):
            hven24=hven24+1
            VenueHundred.append(hven24)
        elif(val==25):
            hven25=hven25+1
            VenueHundred.append(hven25)
        elif(val==26):
            hven26=hven26+1
            VenueHundred.append(hven26)
        elif(val==27):
            hven27=hven27+1
            VenueHundred.append(hven27)
            
    elif(df.at[i,'CalHundred']==0):
        if(val==1):
            VenueHundred.append(hven1)
        elif(val==2):          
            VenueHundred.append(hven2)
        elif(val==3):         
            VenueHundred.append(hven3)
        elif(val==4):            
            VenueHundred.append(hven4)
        elif(val==5):           
            VenueHundred.append(hven5)
        elif(val==6):           
            VenueHundred.append(hven6)
        elif(val==7):         
            VenueHundred.append(hven7)
        elif(val==8):       
            VenueHundred.append(hven8)
        elif(val==9):           
            VenueHundred.append(hven9)
        elif(val==10):           
            VenueHundred.append(hven10)
        elif(val==11):           
            VenueHundred.append(hven11)
        elif(val==12):        
            VenueHundred.append(hven12)
        elif(val==13):         
            VenueHundred.append(hven13)
        elif(val==14):            
            VenueHundred.append(hven14)
        elif(val==15):         
            VenueHundred.append(hven15)
        elif(val==16):           
            VenueHundred.append(hven16)
        elif(val==17):         
            VenueHundred.append(hven17)
        elif(val==18):         
            VenueHundred.append(hven18)
        elif(val==19):         
            VenueHundred.append(hven19)
        elif(val==20):         
            VenueHundred.append(hven20)
        elif(val==21):         
            VenueHundred.append(hven21)
        elif(val==22):         
            VenueHundred.append(hven22)
        elif(val==23):         
            VenueHundred.append(hven23)
        elif(val==24):         
            VenueHundred.append(hven24)
        elif(val==25):         
            VenueHundred.append(hven25)
        elif(val==26):         
            VenueHundred.append(hven26)
        elif(val==27):         
            VenueHundred.append(hven27)
        else:
            VenueHundred.append(0)
   
df["VenueHundred"]=VenueHundred

#Rating For Hundred for Venue done
HundredVenueRating=[]
for value in df["VenueHundred"]: 
     if value==0:
      HundredVenueRating.append(0)
     if value==1 :
        HundredVenueRating.append(2)
     elif value>=1:
        HundredVenueRating.append(3)
df["HundredVenueRating"] = HundredVenueRating 


##Hundreds against a particular opposition
hopp1=0
hopp2=0
hopp3=0
hopp4=0
hopp5=0
hopp6=0
hopp7=0
hopp8=0
hopp9=0
hopp10=0
hopp11=0
hopp12=0

OppHundred=[]   
for i in range(0,columnNum):
    val=df.at[i,'OppositionIndex']
    if (df.at[i,'CalHundred']==1):
        if(val==1):
            hopp1=hopp1+1
            OppHundred.append(hopp1)
        elif(val==2):
            hopp2=hopp2+1
            OppHundred.append(hopp2)
        elif(val==3):
            hopp3=hopp3+1
            OppHundred.append(hopp3)
        elif(val==4):
            hopp4=hopp4+1
            OppHundred.append(hopp4)
        elif(val==5):
            hopp5=hopp5+1
            OppHundred.append(hopp5)
        elif(val==6):
            hopp6=hopp6+1
            OppHundred.append(hopp6)
        elif(val==7):
            hopp7=hopp7+1
            OppHundred.append(hopp7)
        elif(val==8):
            hopp8=hopp8+1
            OppHundred.append(hopp8)
        elif(val==9):
            hopp9=hopp9+1
            OppHundred.append(hopp9)
        elif(val==10):
            hopp10=hopp10+1
            OppHundred.append(hopp10)
        elif(val==11):
            hopp11=hopp11+1
            OppHundred.append(hopp11)
        elif(val==12):
            hopp12=hopp12+1
            OppHundred.append(hopp12)
       
    elif(df.at[i,'CalHundred']==0):
        if(val==1):
            OppHundred.append(hopp1)
        elif(val==2):          
            OppHundred.append(hopp2)
        elif(val==3):         
            OppHundred.append(hopp3)
        elif(val==4):            
            OppHundred.append(hopp4)
        elif(val==5):           
            OppHundred.append(hopp5)
        elif(val==6):           
            OppHundred.append(hopp6)
        elif(val==7):         
            OppHundred.append(hopp7)
        elif(val==8):       
            OppHundred.append(hopp8)
        elif(val==9):           
            OppHundred.append(hopp9)
        elif(val==10):           
            OppHundred.append(hopp10)
        elif(val==11):           
            OppHundred.append(hopp11)
        elif(val==12):           
            OppHundred.append(hopp12)       
        else:
            OppHundred.append(0)
   
df["OppHundred"]=OppHundred


#Rating For Hundred for Opposition done
HundredOppRating=[]
for value in df["OppHundred"]: 
     if value==0:
      HundredOppRating.append(0)
     if value==1 :
        HundredOppRating.append(1)
     elif value>=2:
        HundredOppRating.append(2)
df["HundredOppRating"] = HundredOppRating 



################################
################################





#Calculation of Zero
CalZero=[]
for i in range(0,columnNum):
    if (df.at[i,'Runs']==0):
        CalZero.append(1)
    else:
        CalZero.append(0) 
df["CalZero"]=CalZero

#Number of Zero
Zerocount=0
NumZero=[]
for i in range(0,columnNum):
    if (df.at[i,'CalZero']==1):
        Zerocount=Zerocount+1
        NumZero.append(Zerocount)
    else:
        NumZero.append(Zerocount)
df["NumZero"]=NumZero


#Rating For Zero for Consistency
ZeroCon=[]
for value in df["NumZero"]: 
     if value==0:
        ZeroCon.append(0)
     if value>=1 and value<=4:
        ZeroCon.append(1)
     elif value>=5 and value<=9:
        ZeroCon.append(2)
     elif value>=10 and value<=14:
        ZeroCon.append(3)
     elif value>=15 and value<=19:
        ZeroCon.append(4)
     elif value>=20 :
        ZeroCon.append(5)
df["ZeroCon"] = ZeroCon    

#Rating For Zero for Form 
ZeroForm=[]
for value in df["SZero"]: 
     if value==0:
        ZeroForm.append(0)
     if value==1:
        ZeroForm.append(1)
     elif value==2:
       ZeroForm.append(2)
     elif value==3:
        ZeroForm.append(3)
     elif value==4:
        ZeroForm.append(4)
     elif value>=5 :
        ZeroForm.append(5)
df["ZeroForm"] =ZeroForm


##Zero against a particular opposition
zopp1=0
zopp2=0
zopp3=0
zopp4=0
zopp5=0
zopp6=0
zopp7=0
zopp8=0
zopp9=0
zopp10=0
zopp11=0
zopp12=0

OppZero=[]   
for i in range(0,columnNum):
    val=df.at[i,'OppositionIndex']
    if (df.at[i,'CalZero']==1):
        if(val==1):
            zopp1=zopp1+1
            OppZero.append(zopp1)
        elif(val==2):
            zopp2=zopp2+1
            OppZero.append(zopp2)
        elif(val==3):
            zopp3=zopp3+1
            OppZero.append(zopp3)
        elif(val==4):
            zopp4=zopp4+1
            OppZero.append(zopp4)
        elif(val==5):
            zopp5=zopp5+1
            OppZero.append(zopp5)
        elif(val==6):
            zopp6=zopp6+1
            OppZero.append(zopp6)
        elif(val==7):
            zopp7=zopp7+1
            OppZero.append(zopp7)
        elif(val==8):
            zopp8=zopp8+1
            OppZero.append(zopp8)
        elif(val==9):
            zopp9=zopp9+1
            OppZero.append(zopp9)
        elif(val==10):
            zopp10=zopp10+1
            OppZero.append(zopp10)
        elif(val==11):
            zopp11=zopp11+1
            OppZero.append(zopp11)
        elif(val==12):
            zopp12=zopp12+1
            OppZero.append(zopp12)
       
    elif(df.at[i,'CalZero']==0):
        if(val==1):
            OppZero.append(zopp1)
        elif(val==2):          
            OppZero.append(zopp2)
        elif(val==3):         
            OppZero.append(zopp3)
        elif(val==4):            
            OppZero.append(zopp4)
        elif(val==5):           
            OppZero.append(zopp5)
        elif(val==6):           
            OppZero.append(zopp6)
        elif(val==7):         
            OppZero.append(zopp7)
        elif(val==8):       
            OppZero.append(zopp8)
        elif(val==9):           
            OppZero.append(zopp9)
        elif(val==10):           
            OppZero.append(zopp10)
        elif(val==11):           
            OppZero.append(zopp11)
        elif(val==12):           
            OppZero.append(zopp12)
       
        else:
            OppZero.append(0)
   
df["OppZero"]=OppZero


#Rating For Zero for Opposition
ZeroOppRating=[]
for value in df["OppZero"]: 
     if value==0:
      ZeroOppRating.append(0)
     if value==1 :
        ZeroOppRating.append(1)
     elif value==2 :
        ZeroOppRating.append(2)
     elif value==3 :
        ZeroOppRating.append(3)
     elif value==4 :
        ZeroOppRating.append(4)
     elif value>=5:
        ZeroOppRating.append(5)
df["ZeroOppRating"] = ZeroOppRating 

################################
################################




#BattingAverage rating For Consistency,form
AvgRating=[]
for value in df["CalAvg"]:
    if value>=0.0 and value<=9.99:
        AvgRating.append(1)
    elif value>=10.0 and value<=19.99:
       AvgRating.append(2)
    elif value>=20.0 and value<=27.99:
        AvgRating.append(3)
    elif value>=28.0:
        AvgRating.append(4)

df["AvgRating"] = AvgRating  

#BattingAverage rating For form
AvgRatingForm=[]
for value in df["SeasonAvg"]:
    if value>=0.0 and value<=23.99:
        AvgRatingForm.append(1)
    elif value>=24.0 and value<=30.99:
       AvgRatingForm.append(2)
    elif value>=31.0 and value<=37.99:
        AvgRatingForm.append(3)
    elif value>=38.0:
        AvgRatingForm.append(4)

df["AvgRatingForm"] = AvgRatingForm  



#BattingAverage rating For  Venue 
AvgRatingVenue=[]
for value in df["VenAvg"]:
    if value>=0.0 and value<=6.99:
        AvgRatingVenue.append(1)
    elif value>=7.0 and value<=13.99:
        AvgRatingVenue.append(2)
    elif value>=14.0 and value<=56.99:
        AvgRatingVenue.append(3)
    elif value>=57.0 and value<=99.99:
        AvgRatingVenue.append(4)
    elif value>=100.0:
        AvgRatingVenue.append(5)  
df["AvgRatingVenue"] = AvgRatingVenue




#BattingAverage rating For  Opposition
AvgRatingOpp=[]
for value in df["OppAvg"]:
    if value>=0.0 and value<=7.99:
        AvgRatingOpp.append(1)
    elif value>=8.00 and value<=15.99:
        AvgRatingOpp.append(2)
    elif value>=16.00 and value<=54.99:
        AvgRatingOpp.append(3)
    elif value>=55.00 and value<=93.99:
        AvgRatingOpp.append(4)
    elif value>=94.00:
        AvgRatingOpp.append(5)
   
df["AvgRatingOpp"] = AvgRatingOpp
################################
################################

#BattingStrikeRate rating For Consistency,form, opposition and venue
SrRating=[]
for value in df["CalSR"]:
    if value>=0.0 and value<=65.99:
        SrRating.append(1)
    elif value>=66.00 and value<=130.99:
       SrRating.append(2)
    elif value>=131.00 and value<=183.99:
        SrRating.append(3)
    elif value>=184.00 and value<=236.99:
        SrRating.append(4)
    elif value>=237.00 :
        SrRating.append(5)

df["SrRating"] = SrRating  

#BattingStrikeRate rating For opposition 
SrRatingOpp=[]
for value in df["CalSR"]:
    if value>=0.0 and value<=53.99:
        SrRatingOpp.append(1)
    elif value>=54.00 and value<=107.99:
       SrRatingOpp.append(2)
    elif value>=108 and value<=183.99:
        SrRatingOpp.append(3)
    elif value>=184.00 and value<=259.99:
        SrRatingOpp.append(4)
    elif value>=260.00 :
        SrRatingOpp.append(5)

df["SrRatingOpp"] = SrRatingOpp  


#########################################################################
############# Highest Score in a Particular Venue Till Match Day#######
############################################################################

hsven1=[]
hsven2=[]
hsven3=[]
hsven4=[]
hsven5=[]
hsven6=[]
hsven7=[]
hsven8=[]
hsven9=[]
hsven10=[]
hsven11=[]
hsven12=[]
hsven13=[]
hsven14=[]
hsven15=[]
hsven16=[]
hsven17=[]
hsven18=[]
hsven19=[]
hsven20=[]
hsven21=[]
hsven22=[]
hsven23=[]
hsven24=[]
hsven25=[]
hsven26=[]
hsven27=[]


HighestScoreVenue=[]   
for i in range(0,columnNum):
    val=df.at[i,'VenueIndex']
    if(val==1):
        hsven1.append(df.at[i,'Runs'])
        hsven1.sort(reverse=True)
        HighestScoreVenue.append(hsven1[0])
    elif(val==2):
        hsven2.append(df.at[i,'Runs'])
        hsven2.sort(reverse=True)
        HighestScoreVenue.append(hsven2[0])
    elif(val==3):
        hsven3.append(df.at[i,'Runs'])
        hsven3.sort(reverse=True)
        HighestScoreVenue.append(hsven3[0])
    elif(val==4):
        hsven4.append(df.at[i,'Runs'])
        hsven4.sort(reverse=True)
        HighestScoreVenue.append(hsven4[0])
    elif(val==5):
        hsven5.append(df.at[i,'Runs'])
        hsven5.sort(reverse=True)
        HighestScoreVenue.append(hsven5[0])
    elif(val==6):
        hsven6.append(df.at[i,'Runs'])
        hsven6.sort(reverse=True)
        HighestScoreVenue.append(hsven6[0])
    elif(val==7):
        hsven7.append(df.at[i,'Runs'])
        hsven7.sort(reverse=True)
        HighestScoreVenue.append(hsven7[0])
    elif(val==8):
        hsven8.append(df.at[i,'Runs'])
        hsven8.sort(reverse=True)
        HighestScoreVenue.append(hsven8[0])
    elif(val==9):
        hsven9.append(df.at[i,'Runs'])
        hsven9.sort(reverse=True)
        HighestScoreVenue.append(hsven9[0])
    elif(val==10):
        hsven10.append(df.at[i,'Runs'])
        hsven10.sort(reverse=True)
        HighestScoreVenue.append(hsven10[0])
    elif(val==11):
        hsven11.append(df.at[i,'Runs'])
        hsven11.sort(reverse=True)
        HighestScoreVenue.append(hsven11[0])
    elif(val==12):
        hsven12.append(df.at[i,'Runs'])
        hsven12.sort(reverse=True)
        HighestScoreVenue.append(hsven12[0])
    elif(val==13):
        hsven13.append(df.at[i,'Runs'])
        hsven13.sort(reverse=True)
        HighestScoreVenue.append(hsven13[0])
    elif(val==14):
        hsven14.append(df.at[i,'Runs'])
        hsven14.sort(reverse=True)
        HighestScoreVenue.append(hsven14[0])
    elif(val==15):
        hsven15.append(df.at[i,'Runs'])
        hsven15.sort(reverse=True)
        HighestScoreVenue.append(hsven15[0])
    elif(val==16):
        hsven16.append(df.at[i,'Runs'])
        hsven16.sort(reverse=True)
        HighestScoreVenue.append(hsven16[0])
    elif(val==17):
        hsven17.append(df.at[i,'Runs'])
        hsven17.sort(reverse=True)
        HighestScoreVenue.append(hsven17[0])
    elif(val==18):
        hsven18.append(df.at[i,'Runs'])
        hsven18.sort(reverse=True)
        HighestScoreVenue.append(hsven18[0])
    elif(val==19):
        hsven19.append(df.at[i,'Runs'])
        hsven19.sort(reverse=True)
        HighestScoreVenue.append(hsven19[0])
    elif(val==20):
        hsven20.append(df.at[i,'Runs'])
        hsven20.sort(reverse=True)
        HighestScoreVenue.append(hsven20[0])
    elif(val==21):
        hsven21.append(df.at[i,'Runs'])
        hsven21.sort(reverse=True)
        HighestScoreVenue.append(hsven21[0])
    elif(val==22):
        hsven22.append(df.at[i,'Runs'])
        hsven22.sort(reverse=True)
        HighestScoreVenue.append(hsven22[0])
    elif(val==23):
        hsven23.append(df.at[i,'Runs'])
        hsven23.sort(reverse=True)
        HighestScoreVenue.append(hsven23[0])
    elif(val==24):
        hsven24.append(df.at[i,'Runs'])
        hsven24.sort(reverse=True)
        HighestScoreVenue.append(hsven24[0])
    elif(val==25):
        hsven25.append(df.at[i,'Runs'])
        hsven25.sort(reverse=True)
        HighestScoreVenue.append(hsven25[0])
    elif(val==26):
        hsven26.append(df.at[i,'Runs'])
        hsven26.sort(reverse=True)
        HighestScoreVenue.append(hsven26[0])
    elif(val==27):
        hsven27.append(df.at[i,'Runs'])
        hsven27.sort(reverse=True)
        HighestScoreVenue.append(hsven27[0])
   
    
    else:
        HighestScoreVenue.append(0)
   
df["HighestScoreVenue"]=HighestScoreVenue  

############# Rating Of Highest Scores ##############
################################################

HighestScoreRating=[]
for value in df["HighestScoreVenue"]:
    if value==0:
        HighestScoreRating.append(0)
    if value>=1.0 and value<=24:
        HighestScoreRating.append(1)
    elif value>=25 and value<=49:
        HighestScoreRating.append(2)
    elif value>=50 and value<=67:
        HighestScoreRating.append(3)
    elif value>=68 and value<=118:
        HighestScoreRating.append(4)
    elif value>119:
        HighestScoreRating.append(5)
df["HighestScoreRating"] = HighestScoreRating



#Rating For Runs




RunRating=[]
for value in df["Runs"]: 
     if value>=0 and value<=24:
        RunRating.append(1)
     elif value>=25 and value<=49:
        RunRating.append(2)
     elif value>=50 and value<=74:
        RunRating.append(3)
     elif value>=75 and value<=99:
        RunRating.append(4)
     elif value>=100 :
        RunRating.append(5)
df["RunRating"] = RunRating  







########################################
########################################
########################################
################################################################################
########################################

#######################################
####              Calculation of Consistency      ############
####################################

ConValue=[]
ConValue.append(0)
df.at[0,'Consistency']=0

for i in range(1,columnNum):
      ConValue.append(4*(df.at[i-1,'AvgRating'])+3*(df.at[i-1,'MatchCon'])+2*(df.at[i-1,'SrRating'])+0.3*(df.at[i-1,'HundredCon'])+0.5*(df.at[i-1,'FiftyCon'])-0.2*(df.at[i-1,'ZeroCon']))  

df["Consistency"] = ConValue  





#######################################
####              Calculation of Form      ############
####################################

FormValue=[]
FormValue.append(0)
df.at[0,'Form']=0

for i in range(1,columnNum):
    if(df.at[i,'SMatch']!=1):
        FormValue.append(4*(df.at[i-1,'AvgRatingForm'])+3*(df.at[i-1,'MatchForm'])+2*(df.at[i-1,'SrRating'])+0.3*(df.at[i-1,'CenturyForm'])+0.5*(df.at[i-1,'FiftyForm'])-0.2*(df.at[i-1,'ZeroForm']))  
    else:
        FormValue.append(0)
df["Form"] = FormValue  



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
 
def my_function_opp(m):
    x=0
    x=(4*(df.at[m,'AvgRatingOpp'])+3*(df.at[m,'MatchOpp'])+2*(df.at[m,'SrRatingOpp'])+0.3*(df.at[m,'HundredOppRating'])+0.5*(df.at[m,'FiftyOppRating'])-0.2*df.at[m,'ZeroOppRating'])
    return x






   
if len(OppositionNumberList1)>0:
    df.at[OppositionNumberList1[0]-1,"OppositionValue"]=0
    for i in range(1,len(OppositionNumberList1)):
        df.at[OppositionNumberList1[i]-1,"OppositionValue"]=my_function_opp(OppositionNumberList1[i-1]-1)
        
if len(OppositionNumberList2)>0:
    df.at[OppositionNumberList2[0]-1,"OppositionValue"]=0
    for i in range(1,len(OppositionNumberList2)):
        df.at[OppositionNumberList2[i]-1,"OppositionValue"]=my_function_opp(OppositionNumberList2[i-1]-1)
        
        
if len(OppositionNumberList3)>0:
    df.at[OppositionNumberList3[0]-1,"OppositionValue"]=0
    for i in range(1,len(OppositionNumberList3)):
        df.at[OppositionNumberList3[i]-1,"OppositionValue"]=my_function_opp(OppositionNumberList3[i-1]-1)
        
        
if len(OppositionNumberList4)>0:
    df.at[OppositionNumberList4[0]-1,"OppositionValue"]=0
    for i in range(1,len(OppositionNumberList4)):
        df.at[OppositionNumberList4[i]-1,"OppositionValue"]=my_function_opp(OppositionNumberList4[i-1]-1)
        
        
if len(OppositionNumberList5)>0:
    df.at[OppositionNumberList5[0]-1,"OppositionValue"]=0
    for i in range(1,len(OppositionNumberList5)):
        df.at[OppositionNumberList5[i]-1,"OppositionValue"]=my_function_opp(OppositionNumberList5[i-1]-1)
        
        
if len(OppositionNumberList6)>0:
    df.at[OppositionNumberList6[0]-1,"OppositionValue"]=0
    for i in range(1,len(OppositionNumberList6)):
        df.at[OppositionNumberList6[i]-1,"OppositionValue"]=my_function_opp(OppositionNumberList6[i-1]-1)
        
if len(OppositionNumberList7)>0:
    df.at[OppositionNumberList7[0]-1,"OppositionValue"]=0
    for i in range(1,len(OppositionNumberList7)):
        df.at[OppositionNumberList7[i]-1,"OppositionValue"]=my_function_opp(OppositionNumberList7[i-1]-1)
        
if len(OppositionNumberList8)>0:
    df.at[OppositionNumberList8[0]-1,"OppositionValue"]=0
    for i in range(1,len(OppositionNumberList8)):
        df.at[OppositionNumberList8[i]-1,"OppositionValue"]=my_function_opp(OppositionNumberList8[i-1]-1)
        
        
if len(OppositionNumberList9)>0:
    df.at[OppositionNumberList9[0]-1,"OppositionValue"]=0
    for i in range(1,len(OppositionNumberList9)):
        df.at[OppositionNumberList9[i]-1,"OppositionValue"]=my_function_opp(OppositionNumberList9[i-1]-1)
        
if len(OppositionNumberList10)>0:
    df.at[OppositionNumberList10[0]-1,"OppositionValue"]=0
    for i in range(1,len(OppositionNumberList10)):
        df.at[OppositionNumberList10[i]-1,"OppositionValue"]=my_function_opp(OppositionNumberList10[i-1]-1)
        
if len(OppositionNumberList11)>0:
    df.at[OppositionNumberList11[0]-1,"OppositionValue"]=0
    for i in range(1,len(OppositionNumberList11)):
        df.at[OppositionNumberList11[i]-1,"OppositionValue"]=my_function_opp(OppositionNumberList11[i-1]-1)
        
if len(OppositionNumberList12)>0:
    df.at[OppositionNumberList12[0]-1,"OppositionValue"]=0
    for i in range(1,len(OppositionNumberList12)):
        df.at[OppositionNumberList12[i]-1,"OppositionValue"]=my_function_opp(OppositionNumberList12[i-1]-1)



       
    
"""
OppValue=[]
for j in range(0,len(OppositionNumberList1)):
    val=OppositionNumberList1[j]-1
    OppValue.append(df.at[val,'Runs'])

print(OppValue)
"""

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

def my_function_venue(m):
    x=0
    x=(4*(df.at[m,'AvgRatingVenue'])+3*(df.at[m,'MatchVen'])+2*(df.at[m,'SrRating'])+0.3*(df.at[m,'HundredVenueRating'])+0.5*(df.at[m,'FiftyVenue'])+0.2*(df.at[m,'HighestScoreRating']))
    return x




if len(VenueNumberList1)>0:
    df.at[VenueNumberList1[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList1)):
        df.at[VenueNumberList1[i]-1,"VenueValue"]=my_function_venue(VenueNumberList1[i-1]-1)
          
if len(VenueNumberList2)>0:
    df.at[VenueNumberList2[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList2)):
        df.at[VenueNumberList2[i]-1,"VenueValue"]=my_function_venue(VenueNumberList2[i-1]-1)
        
if len(VenueNumberList3)>0:
    df.at[VenueNumberList3[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList3)):
        df.at[VenueNumberList3[i]-1,"VenueValue"]=my_function_venue(VenueNumberList3[i-1]-1)
        
if len(VenueNumberList4)>0:
    df.at[VenueNumberList4[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList4)):
        df.at[VenueNumberList4[i]-1,"VenueValue"]=my_function_venue(VenueNumberList4[i-1]-1)
        
if len(VenueNumberList5)>0:
    df.at[VenueNumberList5[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList5)):
        df.at[VenueNumberList5[i]-1,"VenueValue"]=my_function_venue(VenueNumberList5[i-1]-1)
        
if len(VenueNumberList6)>0:
    df.at[VenueNumberList6[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList6)):
        df.at[VenueNumberList6[i]-1,"VenueValue"]=my_function_venue(VenueNumberList6[i-1]-1)
        
if len(VenueNumberList7)>0:
    df.at[VenueNumberList7[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList7)):
        df.at[VenueNumberList7[i]-1,"VenueValue"]=my_function_venue(VenueNumberList7[i-1]-1)
        
if len(VenueNumberList8)>0:
    df.at[VenueNumberList8[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList8)):
        df.at[VenueNumberList8[i]-1,"VenueValue"]=my_function_venue(VenueNumberList8[i-1]-1)
        
if len(VenueNumberList9)>0:
    df.at[VenueNumberList9[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList9)):
        df.at[VenueNumberList9[i]-1,"VenueValue"]=my_function_venue(VenueNumberList9[i-1]-1)
        
if len(VenueNumberList10)>0:
    df.at[VenueNumberList10[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList10)):
        df.at[VenueNumberList10[i]-1,"VenueValue"]=my_function_venue(VenueNumberList10[i-1]-1)
        
if len(VenueNumberList11)>0:
    df.at[VenueNumberList11[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList11)):
        df.at[VenueNumberList11[i]-1,"VenueValue"]=my_function_venue(VenueNumberList11[i-1]-1)
        
if len(VenueNumberList12)>0:
    df.at[VenueNumberList12[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList12)):
        df.at[VenueNumberList12[i]-1,"VenueValue"]=my_function_venue(VenueNumberList12[i-1]-1)
        
    
if len(VenueNumberList13)>0:
    df.at[VenueNumberList13[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList13)):
        df.at[VenueNumberList13[i]-1,"VenueValue"]=my_function_venue(VenueNumberList13[i-1]-1)
        
if len(VenueNumberList14)>0:
    df.at[VenueNumberList14[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList14)):
        df.at[VenueNumberList14[i]-1,"VenueValue"]=my_function_venue(VenueNumberList14[i-1]-1)
        
if len(VenueNumberList15)>0:
    df.at[VenueNumberList15[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList15)):
        df.at[VenueNumberList15[i]-1,"VenueValue"]=my_function_venue(VenueNumberList15[i-1]-1)
        
if len(VenueNumberList16)>0:
    df.at[VenueNumberList16[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList16)):
        df.at[VenueNumberList16[i]-1,"VenueValue"]=my_function_venue(VenueNumberList16[i-1]-1)
        
if len(VenueNumberList17)>0:
    df.at[VenueNumberList17[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList17)):
        df.at[VenueNumberList17[i]-1,"VenueValue"]=my_function_venue(VenueNumberList17[i-1]-1)
        

if len(VenueNumberList18)>0:
    df.at[VenueNumberList18[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList18)):
        df.at[VenueNumberList18[i]-1,"VenueValue"]=my_function_venue(VenueNumberList18[i-1]-1)
        

if len(VenueNumberList19)>0:
    df.at[VenueNumberList19[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList19)):
        df.at[VenueNumberList19[i]-1,"VenueValue"]=my_function_venue(VenueNumberList19[i-1]-1)
        
    
if len(VenueNumberList20)>0:
    df.at[VenueNumberList20[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList20)):
        df.at[VenueNumberList20[i]-1,"VenueValue"]=my_function_venue(VenueNumberList20[i-1]-1)
        
if len(VenueNumberList21)>0:
    df.at[VenueNumberList21[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList21)):
        df.at[VenueNumberList21[i]-1,"VenueValue"]=my_function_venue(VenueNumberList21[i-1]-1)
        
if len(VenueNumberList22)>0:
    df.at[VenueNumberList22[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList22)):
        df.at[VenueNumberList22[i]-1,"VenueValue"]=my_function_venue(VenueNumberList22[i-1]-1)
        
if len(VenueNumberList23)>0:
    df.at[VenueNumberList23[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList23)):
        df.at[VenueNumberList23[i]-1,"VenueValue"]=my_function_venue(VenueNumberList23[i-1]-1)
        
if len(VenueNumberList24)>0:
    df.at[VenueNumberList24[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList24)):
        df.at[VenueNumberList24[i]-1,"VenueValue"]=my_function_venue(VenueNumberList24[i-1]-1)
if len(VenueNumberList25)>0:
    df.at[VenueNumberList25[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList25)):
       df.at[VenueNumberList25[i]-1,"VenueValue"]=my_function_venue(VenueNumberList25[i-1]-1)
       
if len(VenueNumberList26)>0:
    df.at[VenueNumberList26[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList26)):
       df.at[VenueNumberList26[i]-1,"VenueValue"]=my_function_venue(VenueNumberList26[i-1]-1)
if len(VenueNumberList27)>0:
    df.at[VenueNumberList27[0]-1,"VenueValue"]=0
    for i in range(1,len(VenueNumberList27)):
        df.at[VenueNumberList27[i]-1,"VenueValue"]=my_function_venue(VenueNumberList27[i-1]-1)




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
finaldf=pd.DataFrame(df,columns=['VenueIndex','OppositionIndex','Venue_Distance','Consistency','Form','OppositionValue','VenueValue','RunRating'])






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



X = finaldf[['VenueIndex','OppositionIndex','Venue_Distance','Consistency','Form','OppositionValue','VenueValue']]
y = finaldf['RunRating']



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
print(confusion_matrix(y_test, y_pred,labels=[1,2,3,4,5]))





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

TestList = test_df['RunRating'].tolist()

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




#logistic regression
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

# Summary of the predictions made by the classifier
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
# Accuracy score
from sklearn.metrics import balanced_accuracy_score
print('Logistic Regression Balanced accuracy is',balanced_accuracy_score(y_pred,y_test))

from sklearn.metrics import accuracy_score
print('accuracy Score is',accuracy_score(y_pred,y_test))


##############################
####################################
############ Custom Accuracy of Logistic Regression with True Positive, True Negative, FP, FN ####################

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
###### Logistic Regression Custom Accuracy ##############
print(y_pred)

PredList = y_pred.tolist()

print(PredList)

print(type(y_test))

test_df = y_test.to_frame()

TestList = test_df['RunRating'].tolist()

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


##################################
################################################
   






# K-Nearest Neighbours

from sklearn.neighbors import KNeighborsClassifier
classifier2 = KNeighborsClassifier(n_neighbors=8)
classifier2.fit(X_train, y_train)

y_pred = classifier2.predict(X_test)

# Summary of the predictions made by the classifier
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
# Accuracy score
from sklearn.metrics import balanced_accuracy_score
print('K-nearest Balanced accuracy is',balanced_accuracy_score(y_pred,y_test))

from sklearn.metrics import accuracy_score
print('accuracy Score is',accuracy_score(y_pred,y_test))

##########################
################################


##############################
####################################
############ Custom Accuracy of K-Nearest with True Positive, True Negative, FP, FN ####################

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



###### K-nearest Custom Accuracy ##############
print(y_pred)

PredList = y_pred.tolist()

print(PredList)

print(type(y_test))

test_df = y_test.to_frame()

TestList = test_df['RunRating'].tolist()

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


##################################
################################################
















# Support Vector Machine's 
from sklearn.svm import SVC

classifier = SVC()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

# Summary of the predictions made by the classifier
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
# Accuracy score
from sklearn.metrics import balanced_accuracy_score
print('SVM Balanced accuracy is',balanced_accuracy_score(y_pred,y_test))

from sklearn.metrics import accuracy_score
print('accuracy Score is',accuracy_score(y_pred,y_test))





##############################
####################################
############ Custom Accuracy of SVM with True Positive, True Negative, FP, FN ####################

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
###### SVM Custom Accuracy ##############
print(y_pred)

PredList = y_pred.tolist()

print(PredList)

print(type(y_test))

test_df = y_test.to_frame()

TestList = test_df['RunRating'].tolist()

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


##################################
################################################
















# Gaussian Naive Bayes
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

# Summary of the predictions made by the classifier
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
# Accuracy score
from sklearn.metrics import balanced_accuracy_score
print('Naive bayes Balanced accuracy is',balanced_accuracy_score(y_pred,y_test))

from sklearn.metrics import accuracy_score
print('accuracy Score is',accuracy_score(y_pred,y_test))

##########################
##############################
####################################
############ Custom Accuracy of naive bayes with True Positive, True Negative, FP, FN ####################

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














################################
###### Naive Bayes Custom Accuracy ##############
print(y_pred)

PredList = y_pred.tolist()

print(PredList)

print(type(y_test))

test_df = y_test.to_frame()

TestList = test_df['RunRating'].tolist()

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


##################################
################################################


#random

print('random forest')
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

# Summary of the predictions made by the classifier
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
# Accuracy score
from sklearn.metrics import balanced_accuracy_score
from sklearn.metrics import balanced_accuracy_score
print('Random Forest Balanced accuracy is',balanced_accuracy_score(y_pred,y_test))

from sklearn.metrics import accuracy_score
print('accuracy Score is',accuracy_score(y_pred,y_test))




##############################
####################################
############ Custom Accuracy of Random Forest with True Positive, True Negative, FP, FN ####################

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
###### Random Forest Custom Accuracy ##############
print(y_pred)

PredList = y_pred.tolist()

print(PredList)

print(type(y_test))

test_df = y_test.to_frame()

TestList = test_df['RunRating'].tolist()

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


##################################
################################################



# shafin 2-3-2021##########################







print(classifier.predict([[9,6,1100,33.9,33.3,26.8,37.7]]))

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
                                 'RunRating'])

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

Ven_Pred= [2,3,4,5,1,6,11,8,1,9,4,3,1,1]

Opp_Pred= [3,8,9,4,2,1,6,8,2,3,6,4,9,1]

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
            
Total_Run=0
            
for values in Match_wise_Run:
    
    if(values==1):
        
        Total_Run+=24
        
    elif(values==2):
        
        Total_Run+=49
    
    elif(values==3):
        
        Total_Run+=74
        
    elif(values==4):
        
        Total_Run+=99
        
    elif(values==5):
        Total_Run+=100
        
print(Total_Run)
        

Performance_df = pd.DataFrame({'Player_Name':['Dinesh Karthik'],'Total Run':[Total_Run],'Cost':[17]})
#Performance_df = pd.DataFrame(Total_Run, columns= ['Total Run'])

Performance_df.to_csv (r'karthik_Performance.csv', index = False, header=True)    
            
            
            
            
            
     

            
            
            
            
            




