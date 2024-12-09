import datetime
import sounddevice as sd
from PIL import ImageGrab
import numpy as np
import cv2
import ctypes
def screenrec():
    try:
        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()
        width = user32.GetSystemMetrics(0)
        height = user32.GetSystemMetrics(1)
        time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        file_name = f'{time_stamp}.mp4'
        fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        captured_video = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height))

        # Initialize audio capturing
        sample_rate = 44100
        audio_frames = []

        def audio_callback(indata, frames, time, status):
            audio_frames.append(indata.copy())

        audio_stream = sd.InputStream(samplerate=sample_rate, channels=2, callback=audio_callback)

        with audio_stream:
            while True:
                img = ImageGrab.grab(bbox=(0, 0, width, height))
                img_np = np.array(img)
                img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

                cv2.imshow('screen capture', img_final)

                captured_video.write(img_final)
                if len(audio_frames) > 0:
                    audio_frame = audio_frames.pop(0)
                    # Process the audio frame here or save it for integration with the video

                if cv2.waitKey(10) == ord('q'):
                    break
    except:
        print("an error occured")            
