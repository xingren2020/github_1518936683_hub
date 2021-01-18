import requests
import os
import re
import json
import time
import timeit
import random
import urllib
import io
import gzip
from datetime import datetime
result=''
app='readapp'
osenviron={}



urllist=[]
hdlist=[]
btlist=[]
CMlist=[]
SFlist=[]
hd=''
def Av(i,k,key=''):
   print(f'''{len(urllist)}-{k}'''+'🔔'*k)
   try:
     response = requests.post(i,headers=hd,data=json.dumps(key),timeout=10)
     userRes=json.loads(response.text)
     if k!=12:
       print('code:'+str(userRes['code']))
     if k!=10:
       print('msg:'+userRes['msg'])
     hand(userRes,k)
        
   except Exception as e:
      print(str(e))
def Va(i,k):
   print(f'''{len(urllist)}-{k}'''+'🔔'*k)
   try:
    req = urllib.request.Request(i,headers=hd)
    bs = urllib.request.urlopen(req).read()
    bi = io.BytesIO(bs)
    gf = gzip.GzipFile(fileobj=bi, mode="rb")
    userRes=gf.read().decode('utf-8',errors = 'ignore')
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
       exit()
def hand(userRes,k):
   msg=''
   if(k==1):
     msg=f'''{userRes['nick']}|'''
     
   if(k==3):
     msg=f'''openNum:{userRes['data']['openNum']}|'''
     
   elif(k==9):
     key=userRes['data']['addShelf']['finished']
     print('截胡:'+str(key))
     if(not key):
       Av(urllist[9],10)
     else:
       Av(urllist[12],13)
   elif(k==10):
      for id in userRes['bookList']:
        CMlist.append(id['bid'])
      Va(urllist[10],11)
   elif(k==11):
      userRes=json.loads(userRes)
      for id in userRes['books']:
        SFlist.append(id['bookid'])
      tem=list(set(CMlist)-set(CMlist)&set(SFlist))
      Lid=random.choice(CMlist)
      bd={"books":[{"bookid":Lid,"method":"add","resType":1,"offset":0,"updatetime":1606951410,"format":"未知格式","origin":"29342","chapterid":1}]}

      Av(urllist[11],12,bd)
   elif(k==13):
     msg=f'''{userRes['data']['userBalance']['coin']}|{userRes['data']['userBalance']['cash']}|{userRes['data']['watchVideo']['videoCount']}-20'''
   elif(k==14):
     Av(urllist[14]+userRes['data']['inspireVideoAd']['adPositionId'],15)
     Av(urllist[14]+'204096',15)
     Av(urllist[14]+'204139',15)
   loger(msg)

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
    #print(response.text)
def loger(m):
   print(m)
   global result
   result +=m                
def notice(b,e):
    ll=False
    start_time = datetime.strptime(str(datetime.now().date())+b, '%Y-%m-%d%H:%M')
    end_time =  datetime.strptime(str(datetime.now().date())+e, '%Y-%m-%d%H:%M')
    now_time = datetime.now()
    if now_time > start_time and now_time<end_time:
       ll=True
    else:
    	ll=False
    return ll
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
   global result
   global hd
   watch('readapp_url',urllist)
   watch('readapp_hd',hdlist)
   watch('readapp_bt',btlist)
   time.sleep(random.randint(1,3))
   for j in range(len(btlist)):
       print(f'''===={str(j)}({len(hdlist)})''')
       hd=eval(hdlist[0])
       hd['Cookie']=btlist[j]
       
       for k in range(len(urllist)):
           if (k>8 and k<13) or k==14:
              continue
           if(k==7):
             ll=btlist[j].split(';')
             hd.update({cookie.split('=')[0].strip():cookie.split('=')[-1].strip() for cookie in ll})
           Av(urllist[k],(k+1))
           
       print(str(j)+'💎'*15+'干就完了')
       result+='\n'
   pushmsg('QAPP阅读2021118',result)
 
if __name__ == '__main__':
       start()
    
