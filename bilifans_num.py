import json,requests,sys,os
import time
#粉丝数api
api="http://api.bilibili.com/x/relation/stat?vmid="
uid=str(sys.argv[1])
api=api+uid

######################获取粉丝数
up2=requests.get(api)
up2=json.loads(up2.text)
nowfans=up2["data"]["follower"]
oldfans=nowfans
#######################获取用户名
up1=requests.get("https://api.bilibili.com/x/space/acc/info?mid="+str(uid)+"&jsonp=jsonp")
up1=json.loads(up1.text)
name=up1["data"]["name"]
#######################

while (1):
    oldfans=nowfans
    up2=requests.get(api)
    up2=json.loads(up2.text)
    nowfans=up2["data"]["follower"]
    p="当前"+str(name)+"的粉丝数量:"+str(nowfans)+'|'
    
    if(nowfans-oldfans>0):
        bl="增加了"+str(nowfans-oldfans)+"个粉丝"
    elif(nowfans==oldfans):
        bl="粉丝不变"
    elif(nowfans-oldfans<0):
        bl="减少了"+str(oldfans-nowfans)+"个粉丝"
    p=p+bl
    print(p)
    time.sleep(1)