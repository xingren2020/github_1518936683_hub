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



def geturl(u,tid):
   u=u[0:u.find('&tid=')+5]+tid+u[u.find('&type'):len(u)]
   return u

def geturl2(u,taskid,Pkg):
   u=u[0:u.find('1/task/')+7]+taskid+u[u.find('/complete'):u.find('Pkg=')+4]+Pkg+u[u.find('&sys'):len(u)]
   return u
def geturl3(u,cmd):
   u=u[0:u.find('cmd=')+4]+cmd+u[u.find('&imgtype'):len(u)]
   return u


def VD():
   Z()
   S()
   T()
   B()
   for index in range(len(taskidlist)):
     P(taskidlist[index],0)
     time.sleep(1)
  
def T():
   url=urllist[0]
   response =requests.get(url,headers=hd,timeout=10).text
   
   userRes=json.loads(response)
   for im in userRes['data']['comps']:
      print('ID='+im['id'])
     
     
   for im in userRes['data']['comps']:
     if im['id']=='6':
       print('\n钻石')

       msg=str(im['data']['cur_coin'])
       loger(msg)
     if im['id']=='966':
       print('\n头游戏按钮'+im['id'])
       time.sleep(1)
       
       for l in im['data']['jingang_list_ios']:
         top=l['jingangName']
         print(top)
       print('\n游戏内容')
       #time.sleep(1)
       print('倒计时,次数')
       x=im['data']['countDown']
       top='585:'+str(x['585']['countDown'])+'-'+str(x['585']['finishTimes'])+'\n'+'589:'+str(x['589']['countDown'])+'-'+str(x['589']['finishTimes'])
       print(top)
       if x['585']['countDown']==0:
          P('585',0)
       elif x['589']['countDown']==0:
          P('589',0)

     if im['id']=='18':
       print('\n签到'+im['id'])
       #time.sleep(1)
       
       for l in im['data']['checkin_list']:
         top=str(l['is_checkin'])+'-'+l['date']
         if l['date']==im['data']['current_date']:
            if l['is_checkin']==0:
              print('签到开始')
              S()
         print(top)
       top='共签到'+str(im['data']['checkin_count'])+'天,'+im['data']['current_date']
       print(top)
       
     if im['id']=='1066':
       print('\n限时专享'+im['id'])
       #time.sleep(1)
       print('taskid',im['data']['taskid'])
       for l in im['data']['tasklist']:
          top=l['id']+'-'+l['title']+'-'+'taskStatus:'+str(l['taskStatus'])+'---'+str(l['current_count'])+'/'+str(l['total_count'])+','
          if 'daoliu_pf_task_id' in l.keys():
             top+='daoliu_pf_task_id:'+l['daoliu_pf_task_id']
          print(top+'\n')
          
     if im['id']=='286':
       print('\n专享福利'+im['id'])
       #time.sleep(1)
       print('taskid',im['data']['taskid'])  
       for l in im['data']['tasklist']:
        if l['id']=='348' or l['id']=='396' or l['id']=='396':
          top=l['id']+'-'+l['title']+'---'+str(l['current_count'])+'/'+str(l['total_count'])+','+'taskStatus:'+str(l['taskStatus'])+'|'
          if 'daoliu_pf_task_id' in l.keys():
             top+='daoliu_pf_task_id:'+l['daoliu_pf_task_id']
          print(top+'\n')
     if im['id']=='1':
       print('\n日常任务'+im['id'])
       #time.sleep(1)
       print('taskid',im['data']['taskid'])

       for l in im['data']['tasklist']:
        if l['id']=='611' or l['id']=='232' or l['id']=='775' or l['id']=='144' or l['id']=='145':
          top=l['id']+'-'+l['title']+'---'+str(l['current_count'])+'/'+str(l['total_count'])+','+'taskStatus:'+str(l['taskStatus'])+'|'
          if 'daoliu_pf_task_id' in l.keys():
             top+='daoliu_pf_task_id:'+l['daoliu_pf_task_id']
          print(top+'\n')
          
     if im['id']=='288':
       print('\n现金大放送'+im['id'])
      # time.sleep(1)
       print('taskid',im['data']['taskid'])
       for l in im['data']['tasklist']:
        if l['id']=='613':
          top=l['id']+'-'+l['title']+'---'+str(l['current_count'])+'/'+str(l['total_count'])+','+'taskStatus:'+str(l['taskStatus'])+'|'
          if 'daoliu_pf_task_id' in l.keys():
             top+='daoliu_pf_task_id:'+l['daoliu_pf_task_id']
          print(top+'\n')
     if im['id']=='299':
       print('\n现金大放送'+im['id'])
       #time.sleep(1)
       top='user_name:'+im['data']['user_name']+'|'+'invite_code:'+im['data']['invite_code']+'|'+im['data']['kouling_open_url']
       print(top)
def Z():
   url=urllist[len(urllist)-1]
   userRes = requests.get(url,headers=hd,timeout=10).text
   data=json.loads(userRes)
   msg=data['mine']['data']['user']['userName']+'|'+data['mine']['data']['charm']['charmpoints']+'|'+data['mine']['data']['charm']['availablePoints']+'|'
   loger(msg)
def S():
   url=urllist[1]
   body=bdlist[0]
   userRes = requests.post(url,headers=hd,data=body,timeout=10).json()
   if userRes['errno']==0:
      print(userRes['data']['tips'])
   else:
      print(userRes['msg'])
def B():
   url=urllist[2]
   body=bdlist[1]
   userRes = requests.post(url,headers=hd,data=body,timeout=10).json()
   print(userRes)
   print(userRes['msg'])
   if userRes['errno']==0:
      P('675',0)
      P('675',1)
      P('675',2)
def D(taskid,Pkg):
   url=geturl2(urllist[3],taskid,Pkg)
   hd['Referer']=urllist[4]
   userRes = requests.get(url,headers=hd,timeout=10).json()
   if userRes['errno']==0 and 'awardCoin' in userRes['data']:
      print(userRes['data']['awardCoin'])
   else:
      print(userRes['errmsg'])
      

def R(taskid,Pkg):
   url=geturl2(urllist[5],taskid,Pkg)
   hd['Referer']=urllist[4]
   userRes= requests.get(url,headers=hd,timeout=10).json()
   if userRes['errno']==0:
      print(userRes['msg'])
   else:
      print(userRes['errmsg'])
   
   

def P(tid,flag):
   print('\n获取=======')
   url=geturl(urllist[7],tid)
   hd['Referer']=urllist[8]+tid
   userRes = requests.get(url,headers=hd,timeout=10).json()
   print(userRes['msg'])
   if (userRes['errno'] == 0 and userRes['data']['isDone'] ==0):
         	
      Pkg = userRes['data']['adInfo'][0]['material']['pkg']
      taskid = userRes['data']['taskPf']['taskId']
      print(Pkg,taskid)
      if flag==0:
         A(tid)
         time.sleep(20)
         C(taskid,Pkg)
         W()
      elif flag==1:
         A(tid)
         time.sleep(20)
         D(taskid,Pkg)
         W()
      elif flag==2:
         A(tid)
         time.sleep(20)
         R(taskid,Pkg)
         W()
   elif (userRes['errno'] == 0 and userRes['data']['isDone'] ==1):
      print("已完成")
def A(tid):
   print(urllist[9])
   url=urllist[9]+tid
   hd['Referer']=urllist[8]+tid
   userRes = requests.get(url,headers=hd,timeout=10).json()
   print(userRes['msg'])
def C(taskid,Pkg):
   url=geturl2(urllist[10],taskid,Pkg)
   hd['Referer']=urllist[8]
   userRes = requests.get(url,headers=hd,timeout=10).json()
   if userRes['errno']==0 and 'awardCoin' in userRes['data']:
      print(userRes['data']['awardCoin'])
   else:
      print(userRes['errmsg'])

   
   
   
   
   
def W():
   url=urllist[len(urllist)-2]
   userRes = requests.get(url,headers=hd,timeout=10).json()
   if userRes['errno']==0:
      print(userRes['data']['coin'])
   else:
      print(userRes['data']['errmsg'])
   

    




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
   watch('bd_vd_hd',hdlist)
   hd=eval(hdlist[0])
   watch('bd_vd_url',urllist)
   watch('bd_vd_ck',btlist)
   watch('bd_vd_bd',bdlist)
   watch('bd_vd_task',taskidlist)
   print(taskidlist)
   taskidlist=s(taskidlist)
   for j in range(1):
       print(f'''===={str(j+1)}''')
       hd['Cookie']=btlist[j]
       VD()
   print('🏆🏆🏆🏆运行完毕')
   print(result)
   pushmsg('白菜帮子',result)
    
    
   
     
if __name__ == '__main__':
       start()
    
