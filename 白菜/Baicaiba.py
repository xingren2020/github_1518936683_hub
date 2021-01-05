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


djj_bark_cookie=''
djj_sever_jiang=''
djj_tele_cookie=''
   
   
result=''
osenviron={}
msg=''
hd={}
urllist=[]
hdlist=[]
btlist=[]
bdlist=[]
taskidlist=[]
tid=''
pKg=''
taskid=''




def geturl(u,tid):
   u=u[0:u.find('&tid=')+5]+tid+u[u.find('&type'):len(u)]
   return u

def geturl2(u,taskid,Pkg):
   u=u[0:u.find('1/task/')+7]+taskid+u[u.find('/complete'):u.find('Pkg=')+4]+Pkg+u[u.find('&sys'):len(u)]
   return u

def Av(i,hd,k,key=''):
   print(str(k)+'=🔔='*k)
   try:
     if(k==2 or k==5 or k==1):
         response = requests.post(i,headers=hd,data=key,timeout=10)
         userRes=json.loads(response.text)
         hand(userRes,k)
     else:
         response = requests.get(i,headers=hd,timeout=10)
         if k==13:
            userRes=response.text
         else:
            userRes=json.loads(response.text)
         hand(userRes,k)
   except Exception as e:
      print(str(e))


def hand(userRes,k):
   global tid,pKg,taskid
   msg=''
   try:
     if k==1:
       msg=''
       i=0
       print('7级以上的吧:')
       for it in userRes['forum_info']:
         if int(it['user_level'])>=7:
            i+=1
            msg+='【'+str(i)+'】-'+it['forum_id']+'-'+it['forum_name']+'-'+it['user_level']+'-'+it['user_exp']+'/'+it['need_exp']+'-'+it['is_sign_in']+'|'+it['cont_sign_num']+'\n'
       print(msg)
       msg=''
       i=0
       print('1-6级的吧:')
       for it in userRes['forum_info']:
          if int(it['user_level'])<7:
            i+=1
            msg+='【'+str(i)+'】-'+it['forum_id']+'-'+it['forum_name']+'-'+it['user_level']+'-'+it['user_exp']+'/'+it['need_exp']+'-'+it['is_sign_in']+'|'+it['cont_sign_num']+'\n'
       print(msg)
       if userRes['forum_info'][0]['is_sign_in']=='0':
          Av(urllist[k],hd,bdlist[k],(k+1))
     elif k==2:
          print(userRes)
     elif k==3:
         for im in userRes['data']['comps']:
           if im['id']=='964':
             time.sleep(1)
             x=im['data']['countDown']
             if x['656']['countDown']==0:
               hd['Referer']=urllist[6]+'656'
               Av((urllist[8]+'656'),hd,9)
               time.sleep(1)
               Av(geturl(urllist[7],'656'),hd,8)
             if x['657']['countDown']==0:
               hd['Referer']=urllist[6]+'657'
               Av((urllist[8]+'657'),hd,9)
               time.sleep(1)
               Av(geturl(urllist[7],'657'),hd,8)
             if x['658']['countDown']==0:
               hd['Referer']=urllist[6]+'658'
               Av((urllist[8]+'658'),hd,9)
               time.sleep(1)
               Av(geturl(urllist[7],'658'),hd,8)
           if im['id']=='214':
             time.sleep(1)
             for l in im['data']['checkin_list']:
               if l['date']==im['data']['current_date']:
                 if l['is_checkin']==0:
                     Av(urllist[1],hd,2)
               
             top='共签到'+str(im['data']['checkin_count'])+'天,'+im['data']['current_date']
             print(top)
     elif k==5:
         print(userRes['msg'])
         hd['Referer']=urllist[6]+'746'
         Av((urllist[8]+'746'),hd,9)
         time.sleep(1)
         Av(geturl(urllist[7],'746'),hd,8)
         
         hd['Referer']=urllist[6]+'752'
         Av((urllist[8]+'752'),hd,9)
         time.sleep(1)
         Av(geturl(urllist[7],'752'),hd,8)
     elif k==8:
       time.sleep(1)
       print(userRes['msg'])
       if (userRes['errno'] == 0 and userRes['data']['isDone'] ==0):
         Pkg = userRes['data']['adInfo'][0]['material']['pkg']
         taskid = userRes['data']['taskPf']['taskId']
         time.sleep(20)
         if tid=='752':
            hd['Referer']=urllist[6]
            Av(geturl2(urllist[5],taskid,Pkg),hd,6)
         elif tid=='746':
           hd['Referer']=urllist[6]
           Av(geturl2(urllist[10],taskid,Pkg),hd,11)
         else:
            Av(geturl2(urllist[9],taskid,Pkg),hd,10)
         Av(urllist[11],hd,12)
       elif (userRes['errno'] == 0 and userRes['data']['isDone'] ==1):
          print("已完成")
     elif k==9:
        print('ac')
     elif k==10:
        if userRes['errno']==0:
           print(userRes['data']['coin'])
        else:
            print(userRes['errmsg'])
     elif k==13:
       data=json.loads(prehtml(userRes))

       data=data['comps'][0]['data']
       msg=data['user_name']+'|'+str(data['user_info']['earned_coin'])+'|'+str(data['user_info']['check_coin'])+'|'+str(data['user_info']['enabled_coin'])+'|'+str(data['user_info']['available_money']/100)
       loger(msg)
   
   

   
        
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


def pushmsg(title,txt,bflag=1,wflag=1,tflag=1):
   try:
     txt=urllib.parse.quote(txt)
     title=urllib.parse.quote(title)
     if bflag==1 and djj_bark_cookie.strip():
         print("\n【Bark通知】")
         purl = f'''https://api.day.app/{djj_bark_cookie}/{title}/{txt}'''
         response = requests.post(purl)
   except Exception as e:
      print(str(e))
   try:
     if tflag==1 and djj_tele_cookie.strip():
         print("\n【Telegram消息】")
         id=djj_tele_cookie[djj_tele_cookie.find('@')+1:len(djj_tele_cookie)]
         botid=djj_tele_cookie[0:djj_tele_cookie.find('@')]

         turl=f'''https://api.telegram.org/bot{botid}/sendMessage?chat_id={id}&text={title}\n{txt}'''

         response = requests.get(turl,timeout=5)
   except Exception as e:
      print(str(e))
   try:
     if wflag==1 and djj_sever_jiang.strip():
        print("\n【微信消息】")
        purl = f'''http://sc.ftqq.com/{djj_sever_jiang}.send'''
        headers={'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
        body=f'''text={txt})&desp={title}'''
        response = requests.post(purl,headers=headers,data=body)
   except Exception as e:
      print(str(e))
def loger(m):
   print(m)
   global result
   result +=m     

def s(st):
   st=st[0][1:len(st[0])-1]
   l=[]
   for i in st.split(','):
      l.append(i[1:4])
   return l
def prehtml(Sg):
   tmd=Sg[Sg.find('window.PAGE_DATA =')+19:Sg.find('window.securityData =')-2]
   return tmd
   
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
   global result,hd,btlist,urllist,hdlist,bdlist,taskidlist
   print('Localtime',datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))
   watch('bd_tb_hd',hdlist)
   hd=eval(hdlist[0])
   watch('bd_tb_url',urllist)
   watch('bd_tb_ck',btlist)
   watch('bd_tb_bd',bdlist)
   watch('bd_tb_task',taskidlist)
   taskidlist=s(taskidlist)
   
     
   for j in range(1):
     print(f'''===={str(j+1)}''')
     hd['Cookie']=btlist[j]
     for index in range(len(taskidlist)):
       hd['Referer']=urllist[6]+taskidlist[index]
       Av((urllist[8]+taskidlist[index]),hd,9)
       time.sleep(1)
       Av(geturl(urllist[7],taskidlist[index]),hd,8)
     
     for k in range(len(urllist)):
       if k==0 :
         Av(urllist[k],hd,(k+1),bdlist[k])
       elif k==4:
        	Av(urllist[k],hd,(k+1),bdlist[3])
       elif k==1 or k==7 or k==8 or k==5 or k==9 or k==10 or k==11 or k==6:
         continue
       else:
         Av(urllist[k],hd,(k+1))
   print('🏆🏆🏆🏆运行完毕')
   pushmsg('一颗大白菜吧',result)
    
    
   
     
if __name__ == '__main__':
       start()
    
