import cv2
import os

it = 0

def video_to_frames(video, path_output_dir):
    # extract frames from a video and save to directory as 'x.png' where 
    # x is the frame index
    global it
    vidcap = cv2.VideoCapture(video)
    count = 0
    while vidcap.isOpened():

        success, image = vidcap.read()
	image = cv2.resize(image, (256,256))
        if success:
            it = it + 1
            if it % 10 == 0:
                cv2.imwrite(os.path.join(path_output_dir, '%d.png') % count, image)
                count += 1
        else:
            break
    cv2.destroyAllWindows()
    vidcap.release()

video_to_frames('/home/roy/end-to-end-car/video2picture/2018_0403_122644_001.MOV', '/home/roy/end-to-end-car/video2picture/captured_picture')
