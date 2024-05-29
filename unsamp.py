import PIL
import numpy as np
import os
from PIL import Image
import fnmatch
from multiprocessing import Pool, cpu_count

PIL.Image.MAX_IMAGE_PIXELS = 121000000    

def underSamp(bin, folder, name, output=''):
    file_path = os.path.join(folder, name)
    print(f'undersampling {file_path}...')
    
    # 打开原始图像
    with Image.open(file_path) as img:
        # 调整图像大小
        size = int(11000 / bin)
        img = img.resize((size, size), resample=Image.NEAREST)
        
        # 将图像转换为8位深度
        # img = img.convert('P', palette=Image.ADAPTIVE, colors=256)
        
        # 保存转换后的图像
        if not output:
            img.save(file_path)
        else:
            img.save(output)
    print(f'undersampling over.')

def process_file(args):
    bin, folder, filename,folder_out  = args
    out = os.path.join(folder_out, filename)
    underSamp(bin, folder, filename, out)

if __name__ == "__main__":
    # 指定文件夹路径
    FoldertoBin2 = r'D:\ZY\himawari\2024-05-29'
    folder_out=r'D:\ZY\himawari\2024-05-29_BIN2'
    # 获取CPU核心数
    num_cores = cpu_count()

    # 创建一个进程池
    with Pool(num_cores) as pool:
        # 遍历文件夹中的所有文件
        for root, dirs, files in os.walk(FoldertoBin2):
            png_files = fnmatch.filter(files, '*.png')
            file_args = [(2, root, filename, folder_out) for filename in png_files]
            # 使用进程池并行处理文件
            pool.map(process_file, file_args)