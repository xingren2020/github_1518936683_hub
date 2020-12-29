import requests
import os
import re
import json
import time
import random
import timeit
import urllib
from datetime import datetime
from dateutil import tz

result=''
osenviron={}
msg=''
hd={}
urllist=[]
hdlist=[]
btlist=[]
redtm=0
bdlist=[]







def Av(i,hd,k,key='',flag=0):
   print(str(k)+'=🔔='*k)
   try:
      if flag==0:
         response = requests.get(f'''{i}{key}''',headers=hd,timeout=10)
      else:
         response = requests.post(f'''{i}''',headers=hd,data=key,timeout=10)
        
         
      userRes=json.loads(response.text)
      print(userRes)
      hand(userRes,k)
   except Exception as e:
      print(str(e))

def watch(flag,list):
   vip=''
   global djj_bark_cookie
   global djj_sever_jiang
   global djj_tele_cookie
   if "DJJ_BARK_COOKIE" in os.environ:
      djj_bark_cookie = os.environ["DJJ_BARK_COOKIE"]
   if "DJJ_TELE_COOKIE" in os.environ:
      djj_tele_cookie = os.environ["DJJ_TELE_COOKIE"]
   if "DJJ_SEVER_JIANG" in os.environ:
      djj_sever_jiang = os.environ["DJJ_SEVER_JIANG"]
   if flag in os.environ:
      vip = os.environ[flag]
   if flag in osenviron:
      vip = osenviron[flag]
   if vip:
       for line in vip.split('\n'):
         if not line:
            continue 
         list.append(line.strip())
       return list
   else:
       print(f'''【{flag}】 is empty,DTask is over.''')
       exit()
def hand(userRes,k):
   msg=''
   try:
       if k==1:
          msg+=f'''{userRes['result']['new_info']['repeat_count']}|{userRes['result']['new_info']['progress']}-{userRes['result']['new_info']['target']}|'''
          print('111',msg)
          loopt=userRes['result']['new_info']['target']-userRes['result']['new_info']['progress']
          if loopt>0 and loopt<300:
            time.sleep(loopt)
            Av(urllist[1],hd,(2))
          elif loopt<0:
             Av(urllist[1],hd,(2))
          else:
            time.sleep(6)
            Av(urllist[0],hd,(1))
       elif(k==2):
       	  if userRes['result']['ret_code']==0:
              msg+=f'''{userRes['result']['new_info']['repeat_count']}|{userRes['result']['new_info']['progress']}-{userRes['result']['new_info']['target']}|'''
              print('2222',msg)
              loopt=userRes['result']['new_info']['target']-userRes['result']['new_info']['progress']
              time.sleep(3)
              Av(urllist[0],hd,(1))
          else:
              time.sleep(20)
              Av(urllist[0],hd,(1))
  
   except Exception as e:
      print(str(e))
      
      
 



def pushmsg(title,txt,bflag=1,wflag=1,tflag=1):
   txt=urllib.parse.quote(txt)
   title=urllib.parse.quote(title)
   if bflag==1 and djj_bark_cookie.strip():
      print("\n【通知汇总】")
      purl = f'''https://api.day.app/{djj_bark_cookie}/{title}/{txt}'''
      response = requests.post(purl)
      #print(response.text)
   if tflag==1 and djj_tele_cookie.strip():
      print("\n【Telegram消息】")
      id=djj_tele_cookie[djj_tele_cookie.find('@')+1:len(djj_tele_cookie)]
      botid=djj_tele_cookie[0:djj_tele_cookie.find('@')]

      turl=f'''https://api.telegram.org/bot{botid}/sendMessage?chat_id={id}&text={title}\n{txt}'''

      response = requests.get(turl)
      #print(response.text)
   if wflag==1 and djj_sever_jiang.strip():
      print("\n【微信消息】")
      purl = f'''http://sc.ftqq.com/{djj_sever_jiang}.send'''
      headers={
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'
    }
      body=f'''text={txt})&desp={title}'''
      response = requests.post(purl,headers=headers,data=body)
def loger(m):
   print(m)
   global result
   result +=m     

    

def clock(func):
    def clocked(*args, **kwargs):
        t0 = timeit.default_timer()
        result = func(*args, **kwargs)
        elapsed = timeit.default_timer() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[🔔运行完毕用时%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked
    
    
    
    
@clock
def start():
   global result,hd,btlist,urllist,urlxlist,hdlist
   print('Localtime',datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))
   watch('wowo_naitang_hd',hdlist)
   hd=eval(hdlist[0])
   for j in range(1):
       print(f'''===={str(j+1)}''')
       urllist=[]
       btlist=[]
       watch('wowo_naitang_urlm'+str(j),urllist)
       watch('wowo_naitang_ckm'+str(j),btlist)
       hd['Cookie']=btlist[0]

       
       for k in range(len(urllist)):
          if k==1:
             continue
          Av(urllist[k],hd,(k+1))
   print('🏆🏆🏆🏆运行完毕')
    
    
   
     
if __name__ == '__main__':
       start()
    
