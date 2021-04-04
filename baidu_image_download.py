import requests
from uuid import uuid4
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'Referer': 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1617534533196_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&sid=&word=Python',
    'Cookie': ''
}

# s = requests.session()
# s.headers = headers

def get_img(url):
    html = requests.get(url,headers=headers)
    if html.status_code == 200:
        html.encoding = 'utf8'
        content = html.json()['data']
        for c in  content[:-1]:
            # print(c['middleURL'])
            download(c['middleURL'])
    else:
        print('获取图片错误')

def download(imageurl):
    print('开始下载{}'.format(imageurl))
    img = requests.get(imageurl,headers=headers)
    # 创建文件j夹
    mkdir('./images')
    # 保存文件
    with open('./images/{}.jpg'.format(uuid4()),'wb') as f:
        for chunk in img.iter_content(225):
            f.write(chunk)

def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
    else :
        print ('{}文件夹已存在'.format(path))

# 百度图片下载
if __name__ == '__main__':
    url = ' https://image.baidu.com/search/acjson?tn=resultjson_com&logid=8231168325122603173&ipn=rj&ct=201326592&is=&fp=result&queryWord=Python&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&word=Python&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn=30&rn=30&gsm=1e&1617534537830='
    get_img(url)