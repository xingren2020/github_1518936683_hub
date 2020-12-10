def Date_Write(msg,id,ct):
   with open(str(id)+ct+'.txt','a',encoding='utf-8') as f:
        f.write(msg)
        
        
        
        
        
Date_Write('5556','222','zoom')
