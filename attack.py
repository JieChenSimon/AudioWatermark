from FFT_main import embed_watermark
import numpy as np
import librosa
from PIL import Image
import soundfile
# keys = [0.001, 0.01, 0.03, 0.05, 0.07, 0.1, 0.5, 0.8]


#攻击方式是高斯白噪声

def watermark_extract(audio_attack_path):
    y1, sr1 = librosa.load("audio/lijian.wav")
    print("original audio:", y1.shape)
    print('the type of the audio:', type(y1))
    y2, sr2 = librosa.load(audio_attack_path)
    print('The audio after attacking:', y2.shape)
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
    waterImg.save('test/extracted_attack_seu.png')
    # waterImg.show()
    print('Extracting finished!')


def attack(audio_embeded, attack_mode,sr):
    if attack_mode == 'add_noise_gaussian':
        percent  = 0.1
        print('the length of the audio:', len(audio_embeded))
        noise = percent * np.random.normal(0, 1, len(audio_embeded))
        print('the type of the noise:', type(noise))
        audio_embeded_attack = audio_embeded + noise
        print('the type of the attacking audio:', type(audio_embeded_attack))
        # librosa.write('test/attack_audio_embeded', audio_embeded_attack, sr, norm=True)
        soundfile.write("test/attack_audio_embeded_normal_0.5.wav", audio_embeded_attack, sr)
        print('attack finished and attack file saved!')
    if attack_mode == 'add_noise_uniform':
        percent  = 0.001
        print('the length of the audio:', len(audio_embeded))
        noise = percent * np.random.uniform(-1, 1, len(audio_embeded))
        print('the type of the noise:', type(noise))
        audio_embeded_attack = audio_embeded + noise
        print('the type of the attacking audio:', type(audio_embeded_attack))
        # librosa.write('test/attack_audio_embeded', audio_embeded_attack, sr, norm=True)
        soundfile.write("test/attack_audio_embeded_uniform_0.001.wav", audio_embeded_attack, sr)
        print('attack finished and attack file saved!')
    

    return audio_embeded_attack



#select the attack mode

if __name__ == '__main__':
    y, sr = librosa.load("test/masked_lijian_seu_key=0.5.wav")
    print("embedding audio shape:",y.shape)
    # attack_mode you can choose from '高斯白噪声', '高斯滤波', '
    attack_mode = 'add_noise_gaussian'
    audio_embeded_attack = attack(y, attack_mode, sr)
    watermark_extract("test/attack_audio_embeded.wav")

