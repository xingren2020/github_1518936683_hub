import requests
import os
import re
import json
import time
import random
import urllib
import timeit
result=''
djj_bark_cookie=''
djj_sever_jiang=''







def Av(i,hd,k,key=''):
   print(str(k)+'=🔔='*k)
   if(k==6):
       time.sleep(31)
   try:
     if(k==11):
         response = requests.post(f'''{i}{key}''',headers=hd,data={},timeout=10)
     else:
         response = requests.get(f'''{i}{key}''',headers=hd,timeout=10)
     print(response.text)
     userRes=json.loads(response.text)
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
   if(userRes['code']==0):
       if(k==1):
           msg+=f'''【{userRes['data']['user']['nickName']}】'''
       elif(k==2):
            msg+=f'''-{userRes['data']['user']['amount']}'''
       elif(k==3):
             msg+=f'''-{userRes['data']['readTime']}min-{userRes['data']['balance']['allBalance']}'''
       elif(k==10):
           if(userRes['msg']=='ok'):
              for item in userRes['data']['pageParams']['readTimeRewardTask']:
                  if userRes['enableFlag']==1 and userRes['doneFlag']==0:
                      Av(urllist[12],hd,(k),item['seconds'])
              for item in userRes['data']['pageParams']['readTimeTask']:
                    if item['enableFlag']==1 and item['doneFlag']==0:
                       Av(urllist[13],hd,(k),item['seconds'])
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
   urllist=[]
   hdlist=[]
   btlist=[]
   global result
   watch('ios_url',urllist)
   watch('ios_hd',hdlist)
   watch('ios_bt',btlist)
   time.sleep(random.randint(1,4))
   for j in range(len(btlist)):
       print(f'''===={str(j)}({len(urllist)})''')
       hd=eval(hdlist[0])
       hd['Cookie']=btlist[j]
       for k in range(len(urllist)-2):
           Av(urllist[k],hd,(k+1))
       print(str(j)+'💎'*15+'干就完了')
       result+='\n'
   if notice('4:00','5:00') or notice('22:00','23:00') or notice('13:00','14:00'):
       pushmsg('干就完事儿了',result)
if __name__ == '__main__':
       start()
    
