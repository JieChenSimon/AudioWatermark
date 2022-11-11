import librosa
import numpy as np
from PIL import Image

def watermark_extract():
    print('loading the audios...')
    y1, sr1 = librosa.load("audio/lijian.wav")
    y2, sr2 = librosa.load("output/masked_lijian_seu.wav")
    print('loading finished!')

    print('Starting to extract the image from the audio...')
    a = librosa.stft(y1)
    r_a = librosa.stft(y2)
    key = 0.001
    waterImg = (r_a-a)/key
    waterImg = np.array(waterImg, dtype='uint8')


    waterImg = Image.fromarray(waterImg)
    waterImg = waterImg.resize((100, 100), Image.ANTIALIAS) 
    waterImg = waterImg.convert("L")
    waterImg.save('output/extracted_seu1.png')
    # waterImg.show()
    print('Extracting finished!')