import requests
import os
import json
import random
import urllib
import time
from datetime import datetime
from dateutil import tz
osenviron={}
djj_bark_cookie=''
djj_sever_jiang=''


urllist=[]
hdlist=[]
keylist=[]
result=''

def Av(i,key,hd,k):
    print('=🔔='*k)
    try:
      if(k==1 or k==2):
        i=i+key
      elif(k==3):
        i=i+key+'&type=boxTask&incrId=139'
      elif(k==4):
        i=i+key+'&type=boxVideoTask&videoId=168'
      elif(k==5):
        i=i+key+'&activeId=31&drawType=1&pca=Wheel.Index'
      elif(k==6):
        i=i+key+'&type=videoTask&videoId=158'
      elif(k==7):
        i=i+key+'&source=wantold'
      elif(k==8):
        i=i+key+'&taskId=53&ext%5Bid%5D=53&ext%5Bamount%5D=15&ext%5BisPop%5D=0'
      elif(k==9):
        i=i+key+'&vid=127&addNum=20'
      response = requests.get(i,headers=eval(hd))
      Res=response.text
      #print(Res)
      if(k==10):
         Res=response.json()
         msg=Res['body']['userInfo']['userNick']+'_'+str(Res['body']['gold']['goldAmount'])
         print(msg)
         loger(msg)
    except Exception as e:
      print(str(e))


def watch(flag,list):
   vip=''
   
   global djj_bark_cookie
   global djj_sever_jiang
   if "DJJ_BARK_COOKIE" in os.environ:
     djj_bark_cookie = os.environ["DJJ_BARK_COOKIE"]
   if "DJJ_SEVER_JIANG" in os.environ:
      djj_sever_jiang = os.environ["DJJ_SEVER_JIANG"]
   if flag in osenviron:
      vip = osenviron[flag]
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
       pushmsg('Dj_20201216update',result)
       exit()
       

def pushmsg(title,txt,bflag=1,wflag=1):
   txt=urllib.parse.quote(txt)
   title=urllib.parse.quote(title)
   if bflag==1 and djj_bark_cookie.strip():
      print("\n【通知汇总】")
      purl = f'''https://api.day.app/{djj_bark_cookie}/{title}/{txt}'''
      response = requests.post(purl)
      #print(response.text)
   if wflag==1 and djj_sever_jiang.strip():
      print("\n【微信消息】")
      purl = f'''http://sc.ftqq.com/{djj_sever_jiang}.send'''
      headers={
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'
    }
      body=f'''text={txt})&desp={title}'''
      response = requests.post(purl,headers=headers,data=body)
   global result
   #print(result)
   result =''
    
def loger(m):
   #print(m)
   global result
   result +=m+'\n'
    


def start():
   print('Localtime',datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))
   global urllist,hdlist,keylist
   time.sleep(random.randint(1,5))


   for j in range(10):
       print('====count===='+str(j+1))
       urllist=[]
       hdlist=[]
       keylist=[]

       watch('dj2020_url'+str(j),urllist)
       watch('dj2020_header',hdlist)
       watch('dj2020_key',keylist)
       
       if(len(urllist)==0 or len(hdlist)==0 or len(keylist)==0):
          print('ooooovvveeeerr::::::::')
          break
       for k in range(len(urllist)):
          Av(urllist[k],keylist[j],hdlist[j],(k+1))
          time.sleep(random.randint(1,4))
       time.sleep(random.randint(1,4))
   
   print('🔔'*15)
   
   

if __name__ == '__main__':
       start()
    
