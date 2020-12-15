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
cklist=[]
result=''

def Av(i,hd,k):
    print('=🔔='*k)
    try:
      
       response = requests.get(i,headers=hd)
       Res=response.json()
       #print(Res)
       if(k==1):
         print(Res['result'])
       if(k==2):
         R=Res['data']['userData']['nickname']+'-'+Res['data']['totalCoin']
         loger(R)
    except Exception as e:
      print(str(e))


def watch(flag,list):
   vip=''
   print('Localtime',datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))
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
       pushmsg('KS',result)
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
   print(m)
   global result
   result +=m+'\n'
    


def start():
   global cklist,urllist,hdlist
   time.sleep(random.randint(1,5))
   watch('KS_url',urllist)
   watch('KS_headers',hdlist)
   for j in range(10):
       print('====count===='+str(j+1))
       bdlist=[]
       watch('KS_cookies'+str(j),cklist)
       hd=eval(hdlist[0])
       hd['Cookie']=cklist[j]
       for k in range(len(urllist)):
          Av(urllist[k],hd,k+1)
       time.sleep(5)
   print('🔔'*15)
   
   

if __name__ == '__main__':
       start()
    
