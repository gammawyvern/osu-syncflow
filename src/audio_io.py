import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

def load_audio(audio_path: str):
    audio, sample_rate = librosa.load(audio_path, sr=None)
    mel_spec = librosa.feature.melspectrogram(y=audio, sr=sample_rate, n_mels=128, fmax=8000)
    mel_spec_db = librosa.power_to_db(mel_spec, ref=np.max)

    # plt.figure(figsize=(10, 4))
    # librosa.display.specshow(mel_spec_db, sr=sample_rate, x_axis='time', y_axis='mel')
    # plt.colorbar(format="%+2.0f dB")
    # plt.title("Mel-Spectrogram")
    # plt.tight_layout()
    # plt.show()

    return mel_spec_db

