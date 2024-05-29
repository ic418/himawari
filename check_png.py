from PIL import Image
import PIL
import os
from utils.pickle_storage import InstantFileStorage
PIL.Image.MAX_IMAGE_PIXELS = 121000000   
def is_png_image_valid(file_path):
    try:
        with Image.open(file_path) as img:
            img.verify()  # 验证图片的完整性
        return True
    except (IOError, SyntaxError) as e:
        print(f"图片文件{file_path}\n有问题: {e}")
        return False

def remove_invalid(directory,InstantFileFolder,InstantFileName):
    '''
    包含删除文件操作，谨慎使用！！！

    去除文件


    directory       要检查的文件夹
    InstantFileFolder       存储数组的文件夹
    InstantFileName   存储数组的文件名   如:'array_data.pkl'等
    
    
    '''
    files=[os.path.join(directory,filename) for filename in os.listdir(directory)]

    storage = InstantFileStorage(InstantFileFolder,'array_data.pkl')
    array_to_save=storage.load_array()

    files = [item for item in files if item not in array_to_save]
    for i in range(len(files)):
        if files[i][-3:]!='png':
            continue

        is_valid = is_png_image_valid(files[i])

        if  is_valid:
            array_to_save.append(files[i])
            storage.save_array(array_to_save)

            print(f'{i+1} in {len(files)} {files[i]} is valid')
            continue
        

        
        print(f'removing {i+1} in {len(files)}')
        os.remove(files[i])#3621


def PNGseqs_integrity_check(folder):
    files=[]
    for filename in os.listdir(folder):
        if filename[-3:]=='png':
            files.append(filename)
    # files=[os.path.join(folder,filename)]
    print(files[:])



if __name__ == "__main__": 
    # remove_invalid(r'D:\ZY\himawari\imgs',r'C:\ZY\Projects\himawari\utils','array_data.pkl')
