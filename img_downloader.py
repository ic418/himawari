import requests
from tqdm import tqdm

from get_CookieToken import read_CookieToken
import os
from MyCustomError import MyCustomError


# 文件的URL


def download(folder,name,hashUrl,d_url):
    tok=read_CookieToken()
    CAKEPHP_cookie=tok['CAKEPHP']
    fixedToken=tok['FIXED_TOKEN']
    url = 'https://sc-nc-web.nict.go.jp/wsdb_osndisk/fileSearch/download'

    s=requests.session()

    headers = {
        "Cookie": f"CAKEPHP={CAKEPHP_cookie}",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    }


    data={
        "_method": "POST",
        "data[FileSearch][is_compress]": "false",
        'data[FileSearch][fixedToken]': fixedToken,
        'data[FileSearch][hashUrl]': hashUrl,
        "action": "dir_download_dl",
        "filelist[0]": d_url,
        "dl_path":d_url 
    }

    resp = s.post(url,data= data,headers=headers,stream=True)
    total = int(resp.headers.get('content-length', 0))
    if resp.status_code!=200:
            raise MyCustomError('error code: '+(str(resp.status_code)))
    if total == 0:
            raise MyCustomError("not exist:"+name)
    path=os.path.join(folder,name)
    with open(path, 'wb') as file, tqdm(
        desc=path,
        total=total,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in resp.iter_content(chunk_size=1024):
            size = file.write(data)
            bar.update(size)

def png_downloader(folder,item):
    if not os.path.exists(folder):
        os.makedirs(folder)
        print('folder')
    name=item['name']
    file=os.path.join(folder,name)
    if os.path.exists(file):
        print("文件已存在")
        return
    try:
        download(folder=folder,name=name,hashUrl=item['hashUrl'],d_url=item['d_url'])
    except MyCustomError as e:
         print(e)
    


def video_downloader(folder,item):
    if not os.path.exists(os.path.dirname(folder)):
        os.makedirs(os.path.dirname(folder))
    name=item['name']
    file=folder+name
    if os.path.exists(file):
        print("文件已存在")
        return
    try:
        download(folder=folder,name=name,hashUrl=item['hashUrl'],d_url=item['d_url'])
    except MyCustomError as e:
         print(e)
    
            

if __name__ == "__main__":
            item={'name': '20240522_pifd.mp4', 
                  'hashUrl': 'bDw2maKV', 
                  'd_url': '/osn-disk/webuser/wsdb/share_directory/bDw2maKV/mp4/Pifd/2024/05-22/20240522_pifd.mp4'}
            

            item={'name': 'hima920240520161000fd.png', 
                  'hashUrl': 'bDw2maKV', 
                  'd_url': '/osn-disk/webuser/wsdb/share_directory/bDw2maKV/png/Pifd/2024/05-20/16/hima920240520161000fd.png'}
            png_downloader(folder='imgs',item=item)





