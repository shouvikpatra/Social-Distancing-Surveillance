
import numpy as np
import argparse
import cv2
import sys
from scipy.spatial import distance
import datetime as dt
import time
from threading import Thread
# VideoCaptureAsync implements separate thread for reading stream from camera
from utils.videocaptureasync import VideoCaptureAsync
from utils.frameDisplay import FrameDisplay
from utils.distanceCalc import calculate_dist
from utils.DL_model import DetectorAPI,centre_calcualtion
# from hybrid_supplementary import VisionSurveillance , spawn_process
import multiprocessing

from multiprocessing import shared_memory , Queue
detection_confidence = 0.4
# N=4
shape = (800,800)
class VisionSurveillance:
    def __init__(self,queue,src=0):
        self.src = src;
        self.threshold_dist = 75
        self.queue=queue

    def start(self,index_count):
        # self.display_obj = FrameDisplay().start()
        # self.display_obj.index=index_count
        self.index=index_count
        self.cap = VideoCaptureAsync(src=self.src).start()
        # self.backUpdate_obj = background()
        return self

    # This function is for detection for each frame
    def detection(self,images,boxes,scores,classes,num,display,frame_data):
        index_count=self.index
        ret, current_frame = self.cap.read()
        if not ret or current_frame is None:
            # print("[INFO] Cam IP Stream unavailable...")
            # user_exit = self.display_obj.display_error()
            display[index_count]=None

        else:
            current_frame = cv2.resize(current_frame, (800,800))
            images[index_count] = current_frame.copy()
            self.queue.put(index_count)
            # print(images[index_count])
            # print(num[index_count])
            centres,current_frame =centre_calcualtion(boxes[index_count]
                                    ,scores[index_count],classes[index_count],num[index_count],
                                    current_frame,detection_confidence)

            pairs = calculate_dist(current_frame, centres, self.threshold_dist)
            # print(pairs)
            # user_exit = self.display_obj.update(current_frame)
            display[index_count]=current_frame
            if centres is None:
                frame_data[index_count][0]=0
            else:
                frame_data[index_count][0]=len(centres)

            if pairs is None:
                frame_data[index_count][1]=0
            else:
                frame_data[index_count][1]=len(pairs)



    def __exit__(self):
        self.cap.stop()
        self.display_obj.stop()


def spawn_process(sources,start_index,queue,N):
    existing_container = shared_memory.SharedMemory(name='image_container')
    images = np.ndarray((N,shape[0],shape[1],3), dtype=np.float32, buffer=existing_container.buf)

    display_shared = shared_memory.SharedMemory(name='display_container')
    display = np.ndarray((N,shape[0],shape[1],3), dtype=np.float32, buffer=display_shared.buf)

    boxes_shared = shared_memory.SharedMemory(name='boxes_container')
    boxes = np.ndarray((N,100,4),dtype=np.float32, buffer=boxes_shared.buf)

    scores_shared = shared_memory.SharedMemory(name='scores_container')
    scores = np.ndarray((N,100),dtype=np.float32, buffer=scores_shared.buf)

    classes_shared = shared_memory.SharedMemory(name='classes_container')
    classes = np.ndarray((N,100),dtype=np.float32, buffer=classes_shared.buf)

    num_shared = shared_memory.SharedMemory(name='num_container')
    num = np.ndarray((N),dtype=np.int, buffer=num_shared.buf)


    frame_data_memory = shared_memory.SharedMemory(name='frame_data_container')
    frame_data = np.ndarray((N,4), dtype=np.float32, buffer=frame_data_memory.buf)

    # The below objects are the instance of VisionSurveillance visionObjects
    # and each object det is for each different cameras
    stream_objects = []
    for i in sources:
        det = VisionSurveillance(queue,src=i)
        stream_objects.append(det)

    #Note: index is passed in start function as indexing is important
    #       at the time of frame display...as windows are named with index
    #       to avoid mixing and overriding of frames during display.
    for count,obj in enumerate(stream_objects):
        obj.start(start_index+count)

    user_exit=False
    breaker=False
    while True :
        for det in stream_objects:
            user_exit = det.detection(images,boxes,scores,classes,num,display,frame_data)
            if user_exit:
                breaker=True
        if breaker:
            print('Breaker Execution')
            break

    print('Process Exit started')
    #Exit operations
    for det in stream_objects:
        det.cap.stop()
        det.display_obj.stop()

    #Disconnect all Shared memory
    existing_container.unlink()
    boxes_shared.unlink()
    scores_shared.unlink()
    classes_shared.unlink()
    num_shared.unlink()
    sys.exit(0)
