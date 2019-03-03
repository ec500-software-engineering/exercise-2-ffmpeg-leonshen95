import subprocess
import threading
import os
import queue
import time


def input(filepath):
    # Access the target directory
    file_list = os.listdir(filepath)
    video_list = []
    # Search for videos ending with mp4 and add to array
    for file in file_list:
        if file.endswith('.mp4'):
            video_list.append(file)
    return video_list


def convert(video_name, resolve, Mbps, name):
    # covert the origin video
    video = video_name
    subprocess.check_output(['ffmpeg','-strict','-2','-i',video,'-b:v', Mbps + 'M', '-s', 'hd' + resolve, name])


def main():

    path = os.getcwd()
    all_video = input(path)
    q = queue.Queue()
    # create empty thread list for coming multi-thread job.
    threads_list = []

    for video in all_video:
        q.put(video)
    start = time.time()


    while q.qsize() != 0:
        # Start conversion jobs in the queue
        video = q.get()
        # Start conversion into two resolutions and Mbps simultaneously
        coroutine_1 = threading.Thread(target=convert,
                             name="thread_1",
                             kwargs={'video_name': video, 'resolve': '480', 'Mbps': '1',
                                                     'name': 'realshort_480.mp4'})
        coroutine_2 = threading.Thread(target=convert,
                                             name="thread_2",
                                             kwargs={'video_name': video, 'resolve': '720', 'Mbps': '2',
                                                     'name': 'realshort_720.mp4'})
        # Append coroutine jobs into thread list
        threads_list.append(coroutine_1)
        threads_list.append(coroutine_2)
        # Start threading
        coroutine_1.start()
        print('coroutine_1 has started')
        coroutine_2.start()
        print('coroutine_2 has started')

    end = time.time()
    # Record conversion time
    print('Time taken: {}'.format(end-start))


if __name__ == '__main__':
    main()