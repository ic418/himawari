import subprocess
import os

# 目标工作目录
target_directory = r'D:\ZY\himawari\2024-05-29_BIN2'

# FFmpeg 命令和参数hima920240529000000fd.png
ffmpeg_command = [
    'ffmpeg',
    '-framerate', '5',
    # '-pattern_type', 'glob',
    '-i', 'hima920240529%03d000fd.png',
    '-c:v', 'libx264',
    '-pix_fmt', 'yuv420p',
    '../out.mp4'
]

# 运行 FFmpeg 命令
try:
    # 检查目标目录是否存在
    if not os.path.exists(target_directory):
        raise FileNotFoundError(f"The directory {target_directory} does not exist.")

    # 切换到目标目录并执行 FFmpeg 命令
    process = subprocess.Popen(ffmpeg_command, 
                               cwd=target_directory, 
                               stdout=subprocess.PIPE, 
                               stderr=subprocess.PIPE,
                               shell=True)
    stdout, stderr = process.communicate()
    
    # 检查命令是否成功执行
    if process.returncode != 0:
        print(f"Error occurred while executing FFmpeg: {stderr.decode('utf-8')}")
    else:
        print("FFmpeg executed successfully.")
        print(stdout.decode('utf-8'))
except FileNotFoundError as fnf_error:
    print(fnf_error)
except Exception as e:
    print(f"An error occurred: {e}")