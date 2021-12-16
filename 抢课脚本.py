import time
import requests

def choose():
    url="http://jwglxt.zstu.edu.cn/jwglxt/xsxk/zzxkyzbjk_xkBcZyZzxkYzb.html?gnmkdm=N253512&su=20xx3399000xx"
    headers={
        "Host":"jwglxt.zstu.edu.cn",
        "Connection":"keep-alive",
        "Content-Length":"513",
        "Accept":"application/json, text/javascript, */*; q=0.01",
        "X-Requested-With":"XMLHttpRequest",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
        "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
        "Origin":"http://jwglxt.zstu.edu.cn",
        "Referer":"http://jwglxt.zstu.edu.cn/jwglxt/xsxk/zzxkyzb_cxZzxkYzbIndex.html?gnmkdm=N253512&layout=default&su=20xx3399000xx",
        "Accept-Encoding":"gzip, deflate",
        "Accept-Language":"zh-CN,zh;q=0.9",
        "Cookie":"JSESSIONID=499015252871D16739D5213855436943; UM_distinctid=17b5ecd979910-07ec16214c9fdf-c343365-151800-17b5ecd979aa2f; route=8db38f847ae08b0b44c89599a7db774a",
    }
    data='''jxb_ids=3271fae5261fbe38aa5c510c9548a46b226fa82e25c9881ccea2a72620f288ad9dadac9660bc9ce4142b96e183ee0efc0eab01217a86bc49d7634b909c6a473a2ac8fe5d55d4bf9f805e45a8646e6c2d6f55ce08d2eee92b65b914c5869d270fe2ec5fa1d020c977e1b16e3d7c469a864e6c12b3eda31c2be69faf1965efdab4&kch_id=67421&kcmc=(67421)%E7%8A%AF%E7%BD%AA%E5%BF%83%E7%90%86%E5%AD%A6+-+2.0+%E5%AD%A6%E5%88%86&rwlx=2&rlkz=0&rlzlkz=0&sxbj=0&xxkbj=0&qz=0&cxbj=0&xkkz_id=D1E3FC470273FF5EE0530100007FD7EC&njdm_id=2019&zyh_id=3900&kklxdm=10&xklc=1&xkxnm=2021&xkxqm=12'''
    req=requests.post(url=url,headers=headers,data=data)
    print(req.text)

if __name__=="__main__":
    space=5
    t=360
    k=int(t/space)
    for _ in range(k):
        time.sleep(space)
        choose()
