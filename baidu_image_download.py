import requests
from uuid import uuid4
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'Referer': 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1617534533196_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&sid=&word=Python',
    'Cookie': 'BDqhfp=%E5%9B%BE%E7%89%87%26%26-10-1undefined%26%260%26%261; BIDUPSID=F6594064F3320243A7FF072DDC51A8C9; PSTM=1613901951; BAIDUID=F6594064F332024371A38C16EEF68D1E:FG=1; __yjs_duid=1_2f5d140b48b90e06312181870321981c1616510133861; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; BAIDUID_BFESS=F6594064F332024371A38C16EEF68D1E:FG=1; H_PS_PSSID=33802_33815_33258_33273_31253_33392_33713_26350_22160; PSINO=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDUSS=EJ6QTBib3F2WktZa3N5RzktNHI4NnhNTGFVaVM3ZW9UaU8tWklsOFlrMUM1WkJnRVFBQUFBJCQAAAAAAAAAAAEAAAATS6gccXEyd2UyAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEJYaWBCWGlge; BDUSS_BFESS=EJ6QTBib3F2WktZa3N5RzktNHI4NnhNTGFVaVM3ZW9UaU8tWklsOFlrMUM1WkJnRVFBQUFBJCQAAAAAAAAAAAEAAAATS6gccXEyd2UyAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEJYaWBCWGlge; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; BCLID=11294769601754854628; BDSFRCVID=mtkOJexroG382bReeqzQbSJh0eKKvV3TDYLEIXH30kmA-6kVgaSTEG0Pt8lgCZu-2ZlgogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=JJkO_D_atKvDqTrP-trf5DCShUFsQx7rB2Q-XPoO3K8WOpkCbt6SLUu7jMQr24biW5cpoMbgylRM8P3y0bb2DUA1y4vpK-ogQgTxoUJ2fnRJEUcGqj5Ah--ebPRiJPb9Qg-qahQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0hDvx-tI_-4_tbh_X5-RLf2TKLl7F54nKDp0Re5AbM4L8y4vB5qJZ2nRg2JoG5PoxsMTsQtcGyMkpMP5v0lRWQeQ-5KQN3KJmf-8lqtOp5DukyhOb2-biWbRM2MbdJqvP_IoG2Mn8M4bb3qOpBtQmJeTxoUJ25DnJhhCGe6Dbe55XjH-s5JtXKD600PK8Kb7VbnoVjMnkbJkXhPteqTDHBKT-Q4clKfOkjKJNyUR-36t7Qbrr-URfyNReQIO13hcdSR3p0pOpQT8r5a7QKMJzb4DHhJRjab3vOIJTXpO1jxPzBN5thURB2DkO-4bCWJ5TMl5jDh3Mb6ksD-FtqjKffnFH_C8QKbREHnkk-tvE2JLHqxby26nLbI39aJ5y-J7nhIP4-l5qbJ_h0f5gBtkj5m3iLfLbQpbZ8h5VWMA5D-PDLeFqah5MKG7nKl0MLP-WDb3JWR_VDlIjbUnMBMPj52OnaIQc3fAKftnOM46JehL3346-35543bRTLnLy5KJYMDcnK4-XjjbQjNrP; BCLID_BFESS=11294769601754854628; BDSFRCVID_BFESS=mtkOJexroG382bReeqzQbSJh0eKKvV3TDYLEIXH30kmA-6kVgaSTEG0Pt8lgCZu-2ZlgogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=JJkO_D_atKvDqTrP-trf5DCShUFsQx7rB2Q-XPoO3K8WOpkCbt6SLUu7jMQr24biW5cpoMbgylRM8P3y0bb2DUA1y4vpK-ogQgTxoUJ2fnRJEUcGqj5Ah--ebPRiJPb9Qg-qahQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0hDvx-tI_-4_tbh_X5-RLf2TKLl7F54nKDp0Re5AbM4L8y4vB5qJZ2nRg2JoG5PoxsMTsQtcGyMkpMP5v0lRWQeQ-5KQN3KJmf-8lqtOp5DukyhOb2-biWbRM2MbdJqvP_IoG2Mn8M4bb3qOpBtQmJeTxoUJ25DnJhhCGe6Dbe55XjH-s5JtXKD600PK8Kb7VbnoVjMnkbJkXhPteqTDHBKT-Q4clKfOkjKJNyUR-36t7Qbrr-URfyNReQIO13hcdSR3p0pOpQT8r5a7QKMJzb4DHhJRjab3vOIJTXpO1jxPzBN5thURB2DkO-4bCWJ5TMl5jDh3Mb6ksD-FtqjKffnFH_C8QKbREHnkk-tvE2JLHqxby26nLbI39aJ5y-J7nhIP4-l5qbJ_h0f5gBtkj5m3iLfLbQpbZ8h5VWMA5D-PDLeFqah5MKG7nKl0MLP-WDb3JWR_VDlIjbUnMBMPj52OnaIQc3fAKftnOM46JehL3346-35543bRTLnLy5KJYMDcnK4-XjjbQjNrP; __yjsv5_shitong=1.0_7_aa19820383dcec58602728c1c2e2f42933e8_300_1617533910474_120.208.120.44_074d16ec; userFrom=www.baidu.com; indexPageSugList=%5B%22%E5%9B%BE%E7%89%87%22%5D; cleanHistoryStatus=0; ab_sr=1.0.0_MGY3MGMyZTNlNTdkNGE4NzU5MzYzZGU0MzlhNDQyODE1ZTI4Yzg1NjhjNmVjZWIwMWNkMDA5MzUwMjMwZDZiNmYyMmEzNWFmMjBmZDZmZjZiMzc4YTI4Njg2MzUxYjJkYzY0ZTRmZGVlZDQxZjA0NDc2ODg4YmM3MTllMjdiNTI='
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