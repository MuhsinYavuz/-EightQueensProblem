from random import choice
matris = [['o','o','o','o','o','o','o','o'],
          ['o','o','o','o','o','o','o','o'],
          ['o','o','o','o','o','o','o','o'],
          ['o','o','o','o','o','o','o','o'],
          ['o','o','o','o','o','o','o','o'],
          ['o','o','o','o','o','o','o','o'],
          ['o','o','o','o','o','o','o','o'],
          ['o','o','o','o','o','o','o','o']]

def matrisYaz(): 
    
    for i in range(len(matris)):
        print()
        for j in range(len(matris)):
            
            print(matris[i][j],end = '  ')



        
      

kroY = []
kroX = []
b= 0
i = 0
j = 0
count = 0
hh = False 
dongude = False 
azalti = False
say = 0
cik = False
while i < 8 :
    say = say + 1
    if i == 0 : 
        matris = [['o','o','o','o','o','o','o','o'],
                  ['o','o','o','o','o','o','o','o'],
                  ['o','o','o','o','o','o','o','o'],
                  ['o','o','o','o','o','o','o','o'],
                  ['o','o','o','o','o','o','o','o'],
                  ['o','o','o','o','o','o','o','o'],
                  ['o','o','o','o','o','o','o','o'],
                  ['o','o','o','o','o','o','o','o']]
    a = choice([k for k in range(0,8) if k not in (kroX and kroY)])
    j = 0
    while j < 8 :
        
        if j ==a    :
            #print("En bas J : ", j )
            kroX.append(i)
            kroY.append(j)
            
            if i != 0 :
                
                
                
                while(j != 0 or i != 0):
                   # print("while bas1  i,j  ",i,j)
                    j = j -1 
                    i = i -1
                    b = b + 1
                   # print("while azal1 i,j  ",i,j)
                    if  matris[i][j] == 'X' :
                        #print('X olamaz1')
                        
                        cik =True
                        matris[i+b][j+b] = 'f'
                        kroX.remove(i+b)
                        kroY.remove(j+b)
                        j= j + b
                        i = i + b -1
                        dongude = True
                        azalti = True
                            
                        break
                    if j == 0 or i == 0 : 
                        #print('X olabilir1')
                        cik =False
                        matris[i+b][j+b] = 'X'
                        j= j + b
                        i = i +b 
                        #print("iiii :" , i)
                        dongude = False
                        azalti = False
                        break  
                    
                    
                     
                #print("1.while cıkısı i , j : ",i ,j )
                   
                b = 0                
                if cik == False :
                    
                    while(j != 7 ):
                        
                            
                           # print("while bas2  i,j  ",i,j)
                            if i != 0 :
                                
                                j = j +1 
                                i = i -1
                                b = b + 1
                           # print("while azal2 i,j  ",i,j)
                            
                            if  matris[i][j] == 'X' :
                                #print('X olamaz2')
                                
                                
                                matris[i+b][j-b] = 'f'
                                kroX.remove(i+b)
                                kroY.remove(j-b)
                                j= j - b
                                if azalti == False :
                                    
                                    i = i + b -1
                                else : 
                                    i =i +b 
                                dongude = True
                                    
                                break
                            if j == 7 or i == 0 : 
                               # print('X olabilir2')
                                
                                matris[i+b][j-b] = 'X'
                                j= j - b
                                i = i +b 
                               # print("iiii :" , i)
                               # print("jjjj :" , j)
                                dongude = False
                                break
                        
               # print("2.while cıkısı i , j : ",i ,j )          
                b = 0        
            else : 
                matris[i][j] = 'X'
               
         
            #print("\n",a,i,j)
             
           # s[i][j] = 'X'     
            #print('X ', end=' ')
           # print(s)
        else :
           pass
        j = j + 1
        
            
          
          
     
    for k in range(8) :
        if dongude == True  :
            
           # print("i : ", i+1)
           # print(matris[i+1][k])
           # print("co : ",matris[i+1].count('f'))
            if  'f' in matris[i+1][k] :
                count = matris[i+1].count('f') 
               # print("i2 : ", i+1)
                if count == (7-i) :
                   # print("asdffff")
                    
                    hh = True
                    break
               # print("i : ",  i+1)
               # print("count : ",  count)
                #print("Dongu : ",dongude )
        else :
           # print("i : ", i)
           # print(matris[i][k])
           # print("co : ",matris[i].count('f'))
            if  'f' in matris[i][k] :
                count = matris[i].count('f') 
               # print("i2 : ", i)
                if (7 - i) == count :
                   # print("asdffff")
                    
                    hh = True
                    break
               # print("i : ",  i)
               # print("count : ",  count)
               # print("Dongu : ",dongude )
    i = i + 1       
    if(hh == True) :
        i= 0
        j = 0
       # print("sıfırmı " , i , j)
        
        kroX.clear()
        kroY.clear()
        hh = False 
        dongude = False        
    print()
    #matrisYaz()
    print("\n")
print()
print("\n")
print(say," kez denendi.")
print("\n")
print("---------------------------------------")
for i in range(8):
    for j in range(8) :
        if 'f' in matris[i][j] :
            matris[i][j] = 'o'
matrisYaz()  
print("\n")        
print("---------------------------------------")
print("")


