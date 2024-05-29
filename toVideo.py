import cv2
import numpy as np
import os

# 读取图片序列
image_folder = r'C:\Users\ZY\Downloads\0524toNow-20240525T080714Z-001\bin2_no_opt'
images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
images.sort()  # 确保图片按照正确的顺序排列

# 获取第一张图片的尺寸，用于创建视频写入器
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

# 创建视频写入器
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 你可以选择其他的编解码器
video = cv2.VideoWriter('10video.mp4', fourcc, 10.0, (width, height))

# 将图片序列写入视频
print(len(images))
for i in range(len(images)):
    print(i)
    video.write(cv2.imread(os.path.join(image_folder, images[i])))

# 释放视频写入器
cv2.destroyAllWindows()
video.release()