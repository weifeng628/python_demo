# todo 上传文件demo
import requests
files = {
    'file':('test',open('./images/1cf0b8d7-2287-4b25-a31a-71b51fc173f8.jpg','rb'),'image/png',{'Expires':'0'})
}

def uplooad_data(url):
    html = requests.post(url,files=files)
    if html.status_code == 200:
        print(html.text)
    else:
        print('提交失败'+html.url)
    

if __name__ == '__main__':
    url = 'http://httpbin.org/post'
    uplooad_data(url)