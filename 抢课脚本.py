from math import trunc
import time
import requests
import random

def choose():
    url="http://jwglxt.zstu.edu.cn/jwglxt/xsxk/zzxkyzbjk_xkBcZyZzxkYzb.html?gnmkdm=N253512&su=2019339900029"
    headers={
        "Host":"jwglxt.zstu.edu.cn",
        "Connection":"keep-alive",
        "Content-Length":"513",
        "Accept":"application/json, text/javascript, */*; q=0.01",
        "X-Requested-With":"XMLHttpRequest",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
        "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
        "Origin":"http://jwglxt.zstu.edu.cn",
        "Referer":"http://jwglxt.zstu.edu.cn/jwglxt/xsxk/zzxkyzb_cxZzxkYzbIndex.html?gnmkdm=N253512&layout=default&su=2019339900029",
        "Accept-Encoding":"gzip, deflate",
        "Accept-Language":"zh-CN,zh;q=0.9",
        "Cookie":"JSESSIONID=88D7E04166DD86A80B46C802A288E822; UM_distinctid=17b5ecd979910-07ec16214c9fdf-c343365-151800-17b5ecd979aa2f; route=5b4bcd4773eecbd92d9b8db6854c870c",}
    data='''jxb_ids=3cd63905bb0e2b716d3deb038dd8d6930fee04e7b66d292c102b48085589a1a18ef7148b147fa8a8f7c8758f1fa2f4176e741e9cf7fc712c04d54c3cbdac2cac9f1e2011047ebe44184a5d4c8ae740f43823303a4748d41c428d73e8b51afaaa87be6c5948cc55ed020f8a9e4d51a568cacc4d65ce4727457a7bb607efb82312&kch_id=67421&kcmc=(67421)%E7%8A%AF%E7%BD%AA%E5%BF%83%E7%90%86%E5%AD%A6+-+2.0+%E5%AD%A6%E5%88%86&rwlx=2&rlkz=0&rlzlkz=1&sxbj=1&xxkbj=0&qz=0&cxbj=0&xkkz_id=D383A72E128C4508E0530100007F8E8F&njdm_id=2019&zyh_id=3900&kklxdm=10&xklc=2&xkxnm=2021&xkxqm=12'''
    req=requests.post(url=url,headers=headers,data=data)
    if req.text!='''{"msg":"0,CF4BEC4F046A62AAE0530100007FD7AF,150,","flag":"-1"}''':
        return True
    else:
        print(req.text)
        return False

if __name__=="__main__":
    space=5
    t=360
    k=1000000000
    for _ in range(k):
        if choose()==True:
            break
        time.sleep(random.random()*1)
