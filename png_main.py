from search import png_search
from get_CookieToken import update_CookieToken
from load_JSON import load_JSON
import os
from img_downloader import png_downloader
from date_str import date_iterator
from multiprocessing import Pool, cpu_count
from time import sleep
from random import uniform
import sys
def myargs(argv):
    if len(argv) != 4:
        print("请分别输入folder(相对于D:\ZY\himawari\),startdate(2024-05-01),backnum")
        sys.exit(2)

    folder = str(argv[1])
    startnum = str(argv[2])
    backnum = int(argv[3])
    folder=os.path.join('D:\ZY\himawari',folder)
    return folder,startnum,backnum
    
def itemsGen(date):
    # 生成一个0.1到1之间的随机浮点数
    # random_float = uniform(0.1, 1.0)
    # sleep(random_float)
    json_string=png_search(date)
    items=(load_JSON(json_string))
    return items

def strainght_download(folder,item):
        while True:
            try:
                png_downloader(folder, item)
                break  # 如果下载成功，跳出while循环
            except Exception as e:
                print(f"Download failed for item {item}. Sleep(1)ing...")
                sleep(1)
                continue  # 如果下载失败，重新尝试




if __name__ == "__main__":


    folder,startnum,backnum=myargs(sys.argv)
    update_CookieToken()


    items=[]
    dates=[]
    for date in date_iterator(startnum,backnum):
        dates.append(date)
    num_cores = cpu_count()


    # 创建一个进程池
    with Pool(num_cores) as pool:
        results = pool.map(itemsGen, dates)

        # 将所有结果拼接成一个大的数组
        all_items = [item for sublist in results for item in sublist]
        print(all_items,'\n',len(all_items))
        print(f'url收集完毕，等待2秒')
        sleep(2)
        file_args = [(folder,item) for item in all_items]
        pool.starmap(strainght_download, file_args)




