

官方提供了2015-07-08到2024-05-25的数据，一共3245天，除去提供的本身就损坏的文件(包括视频不完整(时长低于12秒)，无法解码)和未提供的文件，还剩下3010个视频

The official data is provided from 2015-07-08 to 2024-05-25, covering a total of 3245 days. Excluding the files that were already damaged (including those that were incomplete with a duration of less than 12 seconds and could not be decoded) and the files that were not provided, there are still 3010 videos left.

3010 Days EARTH Timelaps & Himawari-8 & 2015-07-08 to 2024-05-25 & GEO



import time

async def display_progress(progress_queue):
    # 用于存储每个文件的开始时间
    start_times = {}
    while True:
        file_name, downloaded_size, total_size = await progress_queue.get()
        if file_name not in start_times:
            # 如果这是我们第一次看到这个文件，记录开始时间
            start_times[file_name] = time.time()

        if downloaded_size == -1:
            print(f"Failed to download {file_name}")
        elif downloaded_size == total_size:
            print(f"Completed download of {file_name}")
        else:
            # 计算速度
            elapsed_time = time.time() - start_times[file_name]
            speed = downloaded_size / elapsed_time if elapsed_time > 0 else 0
            # 计算预计完成时间
            remaining_size = total_size - downloaded_size
            eta = remaining_size / speed if speed > 0 else 0
            # 打印进度信息
            print(f"Downloading {file_name}: {downloaded_size/total_size:.2%} complete, "
                  f"{speed/1024:.2f} KB/s, ETA: {int(eta)} seconds")

        progress_queue.task_done()
