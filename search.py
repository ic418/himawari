import requests
import json
from get_CookieToken import read_CookieToken


def png_search(day):
    tok=read_CookieToken()
    CAKEPHP_cookie=tok['CAKEPHP']
    X_Csrftoken=tok['FIXED_TOKEN']

    # 文件的URL
    url = 'https://sc-nc-web.nict.go.jp/wsdb_osndisk/fileSearch/search'

    s=requests.session()
    s.cookies.update({"CAKEPHP":f"{CAKEPHP_cookie}"})

    headers = {

        # "Cookie": f"CAKEPHP={CAKEPHP_cookie}",
        "HashToken": "bDw2maKV",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "X-CSRFToken": X_Csrftoken,

    }

    array=[]
    for i in range(0,24):
        h="{:02d}".format(i)
        data={'searchPath': f'png/Pifd/{day}/{h}',
    'searchStr': f'*.png',
    'action': 'dir_download_dl'}
        response = s.post(url,data= data,headers=headers)
        # 检查请求是否成功
        if response.status_code == 200:
            print(f'状态码({day}/{h})：', response.status_code)
            array.append(response.text)
            # print(response.text)
        else:
            print(f'下载失败，状态码({day}/{h})：', response.status_code)
            # print(response.text)

    json_string = json.dumps(array)

    return json_string

if __name__ == "__main__":
    png_search('2024/05-26')




