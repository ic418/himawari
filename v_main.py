from search import mp4_search
from config import start,finish
from load_JSON import load_JSON
import os
from img_downloader import img_downloader,video_downloader
from date_str import date_iterator
from multiprocessing import Pool, cpu_count
import fnmatch




def download(date):
    json_file=(mp4_search(date))
    # print(json_file)
    folder=f'vs/'
    if not os.path.exists(folder):
        os.makedirs(folder)
    for item in load_JSON(json_file):
        while True:
            try:
                video_downloader(folder, item)
                break  # 如果下载成功，跳出while循环
            except Exception as e:
                print(f"Download failed for item {item}. Retrying...")
                continue  # 如果下载失败，重新尝试

def strainght_download(folder,date):
    y=date.split('/')[0]
    m=date.split('/')[1].split('-')[0]
    d=date.split('-')[1]
    item={'name': f'{y}{m}{d}_pifd.mp4', 
          'hashUrl': 'bDw2maKV', 
          'd_url': f'/osn-disk/webuser/wsdb/share_directory/bDw2maKV/mp4/Pifd/{y}/{m}-{d}/{y}{m}{d}_pifd.mp4'}
    # print(item)
    
    
    
    while True:
        try:
            video_downloader(folder, item)
            break  # 如果下载成功，跳出while循环
        except Exception as e:
            print(f"Download failed for item {item}. Retrying...")
            continue  # 如果下载失败，重新尝试




if __name__ == "__main__":
    dates=[]
    folder='videos/'
    for date in date_iterator('2024-05-27',365*15):
        dates.append(date)
    # 获取CPU核心数
    num_cores = cpu_count()

    # 创建一个进程池
    with Pool(num_cores) as pool:
        file_args = [(folder,date) for date in dates]
        # 使用进程池并行处理文件
        pool.starmap(strainght_download, file_args)



