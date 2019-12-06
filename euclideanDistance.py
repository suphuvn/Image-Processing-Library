'''
Created on 2019 M11 7

@author: BrayamBoukhman
'''
import math
def euclideanDistance (q, s):
    d = 0                                
    i = 0                               
    temp = 0                            
    total = 0                       
    for i in range(len(q)):                
        temp = q[i] - s[i]               
        temp = math.pow(temp, 2)       
        total = total + temp            
        
    d = round(math.sqrt(total), 4)        
    
    return d