import cv2
import numpy as np

def img_downscaler(current_frame):
    current_frame_downscaled = cv2.imread(current_frame, (120, 60), interpolation=cv2.INTER_AREA)
    return current_frame_downscaled

def get_current_frame_array(n, video):
    video.set(cv2.CAP_PROP_POS_FRAMES, n)
    retval, frame_image = video.read()

    if retval == false:
        raise ValueError("Error in grabbing the current frame as a numpy array.")
    else:
        return frame_image

def get_brightness_ascii(b, g, r):
    ascii_characters = ".:-=+*#%@"
    brightness = (0.114*(b/255)) + (0.587*(g/255)) + (0.299*(r/255))
    if brightness <= 0.11:
        return f"{ascii_characters[0]}"
    elif brightness <= 0.22:
        return f"{ascii_characters[1]}"
    elif brightness <= 0.33:
        return f"{ascii_characters[2]}"
    elif brightness <= 0.44:
        return f"{ascii_characters[3]}"
    elif brightness <= 0.55:
        return f"{ascii_characters[4]}"
    elif brightness <= 0.66:
        return f"{ascii_characters[5]}"
    elif brightness <= 0.77:
        return f"{ascii_characters[6]}"
    elif brightness <= 0.88:
        return f"{ascii_characters[7]}"
    else:
        return f"{ascii_character[8]}"
    
def main():
    #INPUT
    video_file_path = input("Enter the path to your file>>> ")
    video = cv2.VideoCapture(f"{video_file_path}")
    #Might need to do some error handling here.


    #Here is the Creation of the final_video
    fps = video.get(cv2.CAP_PROP_FPS)
    width, height = 120, 60
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    writer = cv2.VideoWriter("output.mp4", fourcc, fps, (width, height))

    #Looping through all of the frames in the video
    for n in range(0, (video.get(cv.CAP_PROP_FRAME_COUNT))-1): #Where n is the number of frames the loop is at.
        frame_array = np.zeros((60, 120, 3), dtype=np.uint8)

        current_frame = get_current_frame_array(n, video)
        current_frame = img_downscaler(current_frame)

        #[y, x]
        for y in range(60):
            for x in range(120):
                pixels_channels = current_frame[y, x]


        writer.write(frame_array)
        writer.release()

if __init__ == "__main__":
    main()
