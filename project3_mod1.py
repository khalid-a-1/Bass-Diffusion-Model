#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kobi Ocran and Amna Khalid
October 8, 2018
Bass Diffusion Models
project3.py
"""

import numpy as np
import matplotlib.pyplot as plt 

#==============================================================================
def productDiffusion(r,s,t,dt):
    '''
    The function implements the bass diffusion model
    
    Parameters:
        
        r - Constant  Adoption
        s - Social Contagion
        t - weeks
        dt(deltaT) - change in t
        
    Return values:
        
        A - The fraction of the population
        
    '''
    
    A=0
    AList=[A]
    time=0
    timeList =[time]
    rA=0
    rAs=[rA]
  
    for week in range(int(t//dt)+1):        
        A = A + r*(1-A)*dt+s*A*(1-A)*dt
        AList.append(A)
        time = time + dt
        timeList.append(time)
        rA = (AList[-1]-AList[-2])/dt
        rAs.append(rA)
        
       
        
    xList = []
    for step in range(int(t+1)):
        xList.append(step)
        
    return AList,timeList, rAs


#==============================================================================

def productDiffusion2(r,s,rIm,sIm,w,t,dt):
    '''
     The function implements the bass diffusion model
     including influentials and imitators
     
     Parameters:
         
         
         r  - Adoption rate of influential population
         s  - Social Contagion of influential population
         rIm - Adoption rate of imitator population 
         sIm - Social Contagion of imitator population 
         w - weight
         t - weeks
         dt - change in weeks
         
    Return: 
    
    B - The fraction of the imitator population 
    '''
    
    A=0
    AList=[A]
    rA=0
    rAs=[rA]
    B=0
    BList=[B]
    rB=0
    rBs=[rB]
    time=0
    timeList=[time]
    
    for week in range(int(t//dt)+1):
        A = A + r*(1-A)*dt+s*A*(1-A)*dt
        AList.append(A)
        B = B + rIm *(1-B)*dt+w*sIm*A*(1-B)*dt+(1-w)*sIm*B*(1-B)*dt
        BList.append(B)
        time = time + dt
        timeList.append(time)
        rA = (AList[-1]-AList[-2])/dt
        rAs.append(rA)
        rB = (BList[-1]-BList[-2])/dt
        rBs.append(rB)
        
        
    return AList,BList,timeList,rAs,rBs

#==============================================================================  

def main():
    
    
    r=0.002
    s=1.03
    rIm=0
    sIm=0.8
    w=0.6
    dt=0.01
    t=15
    Inf_popsize=600
    Im_popsize=400

    #Part A
    
    plt.figure(1)
    
    Adopters1,xList,rate_of_Adopters1 = productDiffusion(r,s,t,dt)
    print("The fraction of population is:",Adopters1[-1])
    plt.plot(xList,Adopters1,c="red")
    print("The rate of change of A(t):", rate_of_Adopters1[-1])
    plt.plot(xList,rate_of_Adopters1,c="blue")
    
    plt.title('The Bass Diffusion model')
    plt.xlabel('weeks')
    plt.ylabel('Proportion of Adopters')
    plt.legend(['Rate of change of adopters','Population that has adopted the model'])
    
    
    #Part B: 1st Plot

    plt.figure(2)
    Influencers1,Imitators1,xList,rAs,rBs= productDiffusion2(r,s,rIm,sIm,w,t,dt)
    
    
    for i in range(len(Influencers1)):
        Influencers1[i]=Influencers1[i] * Inf_popsize
    print("The final influencer population is:",Influencers1[-1])
    plt.plot(xList,Influencers1,c="green")
    Totalpop=[]
    for i in range(len(Imitators1)):
        Imitators1[i]=Imitators1[i] * Im_popsize
        Total=Imitators1[i]+Influencers1[i]
        Totalpop.append(Total)
    print("The final imitator population:",Imitators1[-1])
    plt.plot(xList,Imitators1,c="pink")
    plt.plot(xList,Totalpop,c="magenta")
    
    plt.title("The Bass Diffusion Model of imitators and influencers")
    plt.xlabel("Weeks")
    plt.ylabel("Population" )
    plt.legend(["Influencers","Imitators","Sum of Influencers & Imitators"])
    
    
    plt.figure(3)
    
    for i in range(len(rAs)):
        rAs[i]=rAs[i] * Inf_popsize
    print("The final influencer population is:",rAs[-1])
    plt.plot(xList,rAs,c="yellow")
    rTotalpop=[]
    for i in range(len(rBs)):
        rBs[i]=rBs[i] * Im_popsize
        rTotal=rAs[i]+rBs[i]
        rTotalpop.append(rTotal)
    print("The final rate imitator population:",rBs[-1])
    plt.plot(xList,rBs,c="navy")
    plt.plot(xList,rTotalpop,c="cyan")
    
    plt.title("The Bass Diffusion Model for rate of imitators and influencers")
    plt.xlabel("Weeks")
    plt.ylabel("Rate of Population" )
    plt.legend(["Rate of Influencers","Rate of Imitators","Sum of rate of Influencers & Imitators"])

    
    plt.show()
    
main()
