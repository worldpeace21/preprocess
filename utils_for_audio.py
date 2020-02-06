import os
from pydub import AudioSegment
from pydub.playback import play
import librosa
import numpy as np
import wave

def volume_up(audio_dir, dB):
"""
목적: .wav 파일의 데시벨을 증폭시킵니다.
Args: 
    - .wav 파일 주소
    - 증가시킬 데시벨의 크기

"""
    audio = AudioSegment.from_wav(audio_dir)
    audio = audio + dB
    audio.export(audio_dir, format='wav')
    
    
def volume_down(audio_dir, dB):
"""
목적: .wav 파일의 데시벨을 감소시킵니다.
Args: 
    - .wav 파일 주소
    - 감소시킬 데시벨의 크기

"""    
    audio = AudioSegment.from_wav(audio_dir)
    audio = audio - dB
    audio.export(audio_dir, format='wav')
    

def plot_audio(audio_dir):
"""
목적: 오디오 파일의 wavform을 시각화합니다.
Args: 
    - .wav 파일 주소

"""  
    y, sr = librosa.load(audio_dir, sr=44100)
    time = np.linspace(0, len(y)/sr, len(y))
    plt.plot(time, y)
    plt.ylabel("amplitude")
    plt.xlabel("time (s)")
    plt.savefig("plot_{}.png".format(audio_dir))
    plt.close() # 안 닫으면 겹쳐서 그려지게 된다.

    
def convert_mp3_to_wav(mp3_dir):
"""
목적: .mp3 파일을 .wav 파일로 변환합니다.
Args: 
    - .mp3 파일 주소

"""
    mp3_file= AudioSegment.from_mp3(mp3_dir)
    wav_dir = mp3_dir.replace('.mp3', '.wav')
    mp3_file.export(wav_dir, format='wav')
            

def get_sampling_rate(wav_dir):
"""
목적: .wav 파일의 sampling rate를 알려줍니다.
Args: 
    - .wav 파일 디렉토리
Return: 
    - sampling rate
"""    
    wav_file = AudioSegment.from_file(wav_dir)
    sampling_rate = wav_file.frame_rate
    
    return sampling_rate


def measure_wav_time(wav_dir):
"""
목적: .wav 파일의 시간을 측정합니다.
Args: 
    - .wav 파일 디렉토리
Return: 
    - .wav 파일 길이
"""

    wav_file = wave.open(wav_dir)
    frames = wav_file.getnframes()
    rate = wav_file.getframerate()
    time = frames / float(rate)
    
    return time
       
