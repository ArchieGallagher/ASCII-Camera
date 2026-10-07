import cv2
import numpy as np

ascii_characters = ".:-=+*#%@"


def img_downscaler(current_frame):
    current_frame_downscaled = cv2.resize(
        current_frame, (120, 60), interpolation=cv2.INTER_AREA
    )
    return current_frame_downscaled


def get_current_frame_array(n, video):
    video.set(cv2.CAP_PROP_POS_FRAMES, n)
    retval, frame_image = video.read()

    if not retval:
        raise ValueError("Error in grabbing the current frame as a numpy array.")
    else:
        return frame_image


def get_brightness_ascii(b, g, r):
    brightness = (0.114 * (b / 255)) + (0.587 * (g / 255)) + (0.299 * (r / 255))
    index = int(brightness * len(ascii_characters))
    return ascii_characters[min(index, len(ascii_characters) - 1)]


def main():
    # INPUT
    video_file_path = input("Enter the path to your file>>> ")
    video = cv2.VideoCapture(f"{video_file_path}")
    if not video.isOpened():
        raise ValueError(f"Could not open video: {video_file_path}")

    # Here is the Creation of the final_video
    fps = video.get(cv2.CAP_PROP_FPS)
    width, height = 1280, 720
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    writer = cv2.VideoWriter("output.mp4", fourcc, fps, (width, height))

    # Writing the canvas which is like the frame_array from the other method
    canvas = np.zeros((720, 1280, 3), dtype=np.uint8)
    grid_columns, grid_rows = 120, 60
    canvas_w, canvas_h = 1280, 720

    # Pixels size of the individual ASCII cell
    cell_w = canvas_w / grid_columns  # 10.67 pixels
    cell_h = canvas_h / grid_rows  # 12.0 pixels

    # Looping through all of the frames in the video
    for n in range(
        int((video.get(cv2.CAP_PROP_FRAME_COUNT)) - 1)
    ):  # Where n is the number of frames the loop is at.
        current_frame = get_current_frame_array(n, video)
        current_frame = img_downscaler(current_frame)

        for i in range(120):
            for j in range(60):
                b, g, r = current_frame[j, i]  # numpy takes the coords as y, x not x, y
                current_ascii = get_brightness_ascii(b, g, r)
                # brightness, colour, append based on a grid thingy with the canvas
                x_pixel = int(i * cell_w)
                y_pixel = int((j + 1) * cell_h)
                cv2.putText(
                    canvas,
                    f"{current_ascii}",
                    (x_pixel, y_pixel),
                    cv2.FONT_HERSHEY_PLAIN,
                    0.8,
                    (int(b), int(g), int(r)),
                    1,
                )

        writer.write(canvas)
        canvas[:] = 0
    writer.release()


if __name__ == "__main__":
    main()
