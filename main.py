from PIL import Image
import numpy as np
import wave
import matplotlib.pyplot as plt
import audioread
# # # transfer the image into gray
# # img = Image.open('figs/seu.png').convert('L')
# # img.save('figs/seu_gray.png')

# # # transfer the image into binary
# # img1 = Image.open('figs/seu_gray.png').convert('1')
# # img1.save('figs/seu_binary.png')
# # print('Original image size: ', img.size)

# # # resize the image
# # img2 = Image.open('figs/seu_binary.png').resize((1000, 1000))
# # print('The resized image size:',img2.size)
# # img2.save('figs/seu_binary_resize.png')


# # # 打开待嵌入水印的音频文件
# # f = wave.open('audio/lijian.wav', 'rb')
# # # 读取音频文件的参数
# # params = f.getparams()
# # nchannels, sampwidth, framerate, nframes = params[:4]
# # print('nchannels:', nchannels)
# # print('sampwidth:', sampwidth)
# # print('framerate:', framerate)
# # print('nframes:', nframes)
# # # 读取音频文件的声音数据
# # str_data = f.readframes(nframes)
# # f.close()

# # embed the image into the audio

# # def img2wav(fft_size = 1024):
# #     img = Image.open('figs/seu.png').convert('L')
# #     img = img.resize((img.width * fft_size // 2 // img.height,fft_size // 2), Image.BICUBIC)
# #     print('img.size:', img.size)
# #     img.save('figs/seu_1.png')
# #     img = np.array(img, dtype=np.float32)
# #     #变换到-100~0分贝
# #     img = img / 255 * 100 - 100
# #     #单位从分贝改成1，此时取值为0~1
# #     img = np.exp(img * (np.log(10) / 20))
# #     #翻转
# #     img = img[::-1].T
# #     # print('img', img)

# #     #防溢出，每列振幅不能超过1
# #     max_sum = max(col.sum() for col in img)
# #     if max_sum > 1:
# #         img = img / max_sum
    
# #     #打开音频文件
# #     f = wave.open('audio/lijian.wav', 'wb')
# #     f.setparams((1, 2, 44100, len(img) * fft_size, 'NONE', ''))
# #     for col in img:
# #         #傅里叶反变换
# #         print('col:', col)
# #         data = np.fft.irfft(col * fft_size, fft_size).real * 32767

# #         #最后一次防溢出，限制再-32767~32767之间
# #         for index in np.where(data < -32767):
# #             data[index] = -32767
# #         for index in np.where(data > 32767):
# #             data[index] = 32767
# #         #写到wav文件
# #         data = data.astype('short')
# #         f.writeframesraw(data)
        

# def img2wav():
#     f = wave.open('audio/lijian.wav', 'rb')
#     params = f.getparams()
#     nchannels, sampwidth, framerate, nframes = params[:4]
#     print('nchannels:', nchannels) #nchannels: 1
#     print('sampwidth:', sampwidth) #sampwidth: 2
#     print('framerate:', framerate) #framerate: 44100
#     print('nframes:', nframes) #nframes: 528384
    



# def draw_specturm():
#     #画音频频谱图
#     f = wave.open('audio/lijian.wav', 'rb')
#     params = f.getparams()
#     nchannels, sampwidth, framerate, nframes = params[:4]
#     str_data = f.readframes(nframes)
#     # print('str_data:', str_data)

#     data  = np.fromstring(str_data, dtype=np.short)
#     #取第一个声道
#     data.shape = (nframes, nchannels)
#     data = data.T[0]

#     plt.specgram(data, NFFT=1024, Fs=framerate, noverlap=0, scale='dB')
#     plt.savefig('figs/spectrum.png')

# img2wav()
# draw_specturm()

img = Image.open('figs/seu.png')
img.show()