import requests
import os
import re
import json

def Av(i,hd,j,k):
    print('=🔔='*k)
    try:
       response = requests.post(i,headers=eval(hd),data=j)
       if(k==1):
       	     print(json.loads(response.text)['data']['score'])
       elif(k==2):
       	     print(json.loads(response.text)['data']['score'])
    except Exception as e:
      print(str(e))


def watch(flag,list):
   vip=''
   if flag in os.environ:
      vip = os.environ[flag]
   if vip:
       for line in vip.split('\n'):
         if not line:
            continue 
         list.append(line.strip())
       return list
   else:
       print(f'''【{flag}】 is empty,DTask is over.''')
       exit()
       




def start():
   urllist=[]
   hdlist=[]
   bdlist=[]
   watch('sam_url',urllist)
   watch('sam_headers',hdlist)
   watch('sam_body0',bdlist)
   watch('sam_body1',bdlist)
   for j in range(1):
       print('===='+str(j))
       for k in range(2):
           Av(urllist[k],hdlist[0],bdlist[k+j],(k+1))
   print('🔔'*15)
if __name__ == '__main__':
       start()
    
