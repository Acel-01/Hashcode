# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 00:56:53 2021

@author: Emeka Aladimma
"""

inFile = 'a_example'
inFile = 'b_little_bit_of_everything.in'

with open(inFile,'r') as i:
    lines = i.readlines()

lines0 = lines[0].split()

numOfPizzas = lines0[0]
numTeamOfTwo = lines0[1]
numTeamOfThree = lines0[2]
numTeamOfFour = lines0[3]

#print(numOfPizzas)
#print(numTeamOfTwo)
#print(numTeamOfThree)
#print(numTeamOfFour)

deliveries = 0
d = []

numOfPizzasInt = int(numOfPizzas) 
numTeamOfTwoInt = int(numTeamOfTwo)
numTeamOfThreeInt = int(numTeamOfThree)
numTeamOfFourInt = int(numTeamOfFour)

for ingredients in range(1,numOfPizzasInt+1):
    c = lines[ingredients][1:].strip().split(" ")
    d.append(c)
#print(d)

ingredNumList = 0
stringOutput = ""
    
for i in range(1,numOfPizzasInt+1):
    if numOfPizzasInt >= 2 and numOfPizzasInt != 3 and numTeamOfTwoInt > 0:
        numOfPizzasInt -= 2
        deliveries += 1
        delivery2Teams = "2"
        delivery2Teams += f" {str(ingredNumList)}"
        ingredNumList += 1
        delivery2Teams += f" {str(ingredNumList)}"
        ingredNumList += 1
        numTeamOfTwoInt -= 1
        #print(delivery2Teams )
        stringOutput += f"\n{delivery2Teams}"
        
    elif numOfPizzasInt >= 3 and numOfPizzasInt != 4 and numTeamOfThreeInt > 0:
        numOfPizzasInt -= 3
        deliveries += 1
        delivery3Teams = "3"
        delivery3Teams += f" {str(ingredNumList)}"
        ingredNumList += 1
        delivery3Teams += f" {str(ingredNumList)}"
        ingredNumList += 1
        delivery3Teams += f" {str(ingredNumList)}"
        ingredNumList += 1
        numTeamOfThreeInt -= 1
        #print(delivery3Teams)
        stringOutput += f"\n{delivery3Teams}"
        
    elif numOfPizzasInt >= 4 and numTeamOfFourInt > 0:
        numOfPizzasInt -= 4
        deliveries += 1
        delivery4Teams = "4"
        delivery4Teams += f" {str(ingredNumList)}"
        ingredNumList += 1
        delivery4Teams += f" {str(ingredNumList)}"
        ingredNumList += 1
        delivery4Teams += f" {str(ingredNumList)}"
        ingredNumList += 1
        delivery4Teams += f" {str(ingredNumList)}"
        ingredNumList += 1
        numTeamOfFourInt -= 1
        #print(delivery4Teams)
        stringOutput += f"\n{delivery4Teams}"
        

#print(deliveries)
#print(stringOutput)
finalStringOutput = str(deliveries)+stringOutput
print(finalStringOutput)
        
outFile = 'output1Testing'
with open(outFile,'w') as o:
    for line in finalStringOutput:
        o.write(line)
        
