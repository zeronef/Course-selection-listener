from math import trunc
import time
import requests
import random

def choose():
    url="http://jwglxt.zstu.edu.cn/jwglxt/xsxk/zzxkyzbjk_xkBcZyZzxkYzb.html?gnmkdm=N253512&su=2019339900029"
    headers={
        "Host":"jwglxt.zstu.edu.cn",
        "Connection":"keep-alive",
        "Content-Length":"486",
        "Accept":"application/json, text/javascript, */*; q=0.01",
        "X-Requested-With":"XMLHttpRequest",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
        "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
        "Origin":"http://jwglxt.zstu.edu.cn",
        "Referer":"http://jwglxt.zstu.edu.cn/jwglxt/xsxk/zzxkyzb_cxZzxkYzbIndex.html?gnmkdm=N253512&layout=default&su=2019339900029",
        "Accept-Encoding":"gzip, deflate",
        "Accept-Language":"zh-CN,zh;q=0.9",
        "Cookie":"JSESSIONID=1EC37FFB39C8AE02883A78D6BB4B5036; UM_distinctid=17b5ecd979910-07ec16214c9fdf-c343365-151800-17b5ecd979aa2f; route=8db38f847ae08b0b44c89599a7db774a",}
    data='''jxb_ids=572c24a044b65fe7c9dc2c1e92c278e194ee1c9b09b040ed7d848aa9f9fd02685d87cb65f6bdc0d4260a9891378648ffd08844323d9631051ef2a4ac5966300cee10cadc346bb550d0d00459997be922e0ed587fbe1bcb74c002f706459f0e6332523539e6c971d37caa44a4bb750ad9f46a7bd0abcbadf5b38a34cab6c75108&kch_id=03408&kcmc=(03408)%E6%A1%A5%E7%89%8C+-+2.0+%E5%AD%A6%E5%88%86&rwlx=2&rlkz=0&rlzlkz=1&sxbj=1&xxkbj=0&qz=0&cxbj=0&xkkz_id=D383A72E128C4508E0530100007F8E8F&njdm_id=2019&zyh_id=3900&kklxdm=10&xklc=2&xkxnm=2021&xkxqm=12'''
    req=requests.post(url=url,headers=headers,data=data)
    if req.text!='''{"msg":"0,CEE8E3299C8A9622E0530100007F91AC,100,","flag":"-1"}''':
        return True
    else:
        print(req.text)
        return False

if __name__=="__main__":
    while True:
        if choose()==True:
            break
        time.sleep(random.random()*1+0.5)
