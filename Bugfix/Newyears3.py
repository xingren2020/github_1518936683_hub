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
djj_bark_cookie=''
djj_sever_jiang=''
osenviron={}
msg=''
hd=''
urllist=[]
hdlist=[]
btlist=[]
newurllist=[]
redtm=0
bdlist=[]

def Av2(i,hd,bd,k):
   try:
      print(str(k)+'=🔔='*k)
      response = requests.post(i,headers=hd,data=bd,timeout=10).json()
      if(response['code']==0):
        print('成功....')
      else:
         print('失败....')
   except Exception as e:
      print(str(e))
def Va2(i,hd,k):
   try:
      print(str(k)+'=🔔='*k)
      response = requests.get(i,headers=hd,timeout=10)
      Rs=response.json()
      Tr=Rs['data']['transList']
      for q in range(5):
        Tm=time.localtime(float(Tr[q]['createTime']/1000))
        Tm=time.strftime("%Y-%m-%d %H:%M:%S",Tm)
        print(f'''【{Tm}】''',Tr[q]['amount'])
   except Exception as e:
      print(str(e))
def fistme():
   global result
   today=datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%H:%M", )
   print('today:',today)
   if(today[0:2]=='00' and int(today[3:5])<20):
      tm=19-int(today[3:5])
      for j in range(len(btlist)):
         print(f'''===={str(j)}({len(btlist)})''')
         hd=eval(hdlist[0])
         hd['Cookie']=btlist[j]
         Av2(newurllist[0],hd,bdlist[j],j+1)
         Va2(newurllist[1],hd,j+1)
         result+='【'+getid2(bdlist[j])[0:4]+'-'+getid1(btlist[j])[0:4]+'】\n'
         print('count'+str(j+1)+'💎运行完毕')
         print(result)
         result=''
      time.sleep(tm*60)
      print('Localtime',datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))
      	
def Av(i,hd,k,key=''):
   print(str(k)+'=🔔='*k)
   if(k==6):
      time.sleep(31)
   try:
     if(k==11):
         response = requests.post(f'''{i}{key}''',headers=hd,data={},timeout=10)
     else:
         response = requests.get(f'''{i}{key}''',headers=hd,timeout=10)

     userRes=json.loads(response.text)
     print(userRes['code'])
     hand(userRes,k)
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
   global redtm
   try:
     if(userRes['code']==0):
       if(k==1):
           msg=f'''{userRes['data']['user']['nickName'][0:2]}'''
           print(msg)
       elif(k==2):
            msg=f'''|{userRes['data']['treasureBox']['tipText']}|{userRes['data']['treasureBox']['count']}'''
            print(msg)
            for t in userRes['data']['taskList']:
               if t['type']==200:
                 if t['doneFlag']==0:
                   Av(urllist[2],hd,3)
                   time.sleep(5)
                   Av(urllist[3],hd,4)
               elif t['type']==210:
                 if t['doneFlag']==0:
                   Av(urllist[7],hd,8)
               elif t['type']==230:
                 if t['doneFlag']==0:
                   Av(urllist[4],hd,5)
            if userRes['data']['treasureBox']['timeInterval']==0:
               Av(urllist[5],hd,6)
               time.sleep(31)
               Av(urllist[6],hd,7)

       elif(k==10):
           if(userRes['msg']=='ok'):
              for item in userRes['data']['pageParams']['readTimeRewardTask']:
                  if item['enableFlag']==1 and item['doneFlag']==0:
                      Av(urllist[11],hd,12,item['seconds'])
              for item in userRes['data']['pageParams']['readTimeTask']:
                    if item['enableFlag']==1 and item['doneFlag']==0:
                       Av(urllist[12],hd,13,item['seconds'])
       elif(k==14):
           if(userRes['code']==0 and userRes['data'] ['hasPackage']):
             redtm=userRes['data']['readTime']
             print(redtm)
             
             
             Av(urllist[14],hd,15)
       elif(k==15):
         if userRes['code']==0:
           for item in userRes['data']:
                if(not item['isPick'] and item['readTime']<=redtm):
                   Av(urllist[15],hd,16,item['readTime'])
       elif(k==16):
          print(userRes)
   except Exception as e:
      print(str(e))
def getid1(id):
   lll=id.split(';')
   for l in lll:
     if l.find('ywguid=')>=0:
      return l[(l.find('ywguid=')+7):len(l)]
def getid2(id):
   id=json.dumps(id)
   lll=id.split(',')
   for l in lll:
     if l.find('guid')>=0:
      return l[(l.find('guid')+7):len(l)]     
      
    
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
   global result,hd
   print('Localtime',datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))
   newloop=6
   watch('ios_urlxx',urllist)
   watch('ios_newurl',newurllist)
   watch('ios_newhd',hdlist)
   watch('ios_newbd3',bdlist)
   watch('ios_newbt3',btlist)
   fistme()
   for mm in range(newloop):
     result=''
     print('第'+str(mm+1)+'🏆次运行开始')
     time.sleep(random.randint(1,4))
     fistme()
     for j in range(len(btlist)):
       print(f'''===={str(j+1)}({len(btlist)})''')
       result+='['+str(len(btlist))+'-'+str(j+1)+']'
       hd=eval(hdlist[0])
       hd['Cookie']=btlist[j]
       for k in range(len(urllist)):
         fistme()
         if(k>1 and k<8) or k==11 or k==12 or k==14 or k==15:
            continue
         Av(urllist[k],hd,(k+1))
       result+=getid1(btlist[j])+'\n'
     print('第'+str(mm+1)+'🏆🏆🏆🏆次运行完毕')
     if mm<2:
       time.sleep(60)
     print('Localtime',datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))
     
     
    
   
     
if __name__ == '__main__':
       start()
    
