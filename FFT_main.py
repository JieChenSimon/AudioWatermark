import librosa
import matplotlib.pyplot as plt
import soundfile
import cv2

def embed_watermark(watermark_path, audio_path, key):
    print('key = ', key)
    y, sr = librosa.load(audio_path)
    waterImg = cv2.imread(watermark_path, 0)
    print('Starting to embed the image into the audio...')
    # stft 短时傅立叶变换
    a = librosa.stft(y)
    w = a.shape[0]
    h = a.shape[1]


    waterImg = cv2.resize(waterImg, (h, w))
    print(type(a[0][2]))
    r_a = key * waterImg + a
    b = librosa.istft(r_a)
    audio =  soundfile.write("test/masked_lijian_seu_key={}.wav".format(key), b, sr)
    print('Embedding finished!'.format(key))
    return audio

if __name__ == '__main__':
    keys = [0.001, 0.01, 0.03, 0.05, 0.07, 0.1, 0.5, 0.8]
    for key in keys:
        embed_watermark('figs/seu.png', 'audio/lijian.wav', key)



