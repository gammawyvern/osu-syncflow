import numpy as np
import torch

from cnn import AudioFeatureExtractorCNN
from audio_io import load_audio

def main():
    mel_spec_db = load_audio("../tmp/sample.mp3")

    mel_spec_db_normalized = (mel_spec_db - np.mean(mel_spec_db)) / np.std(mel_spec_db)
    input_tensor = torch.tensor(mel_spec_db_normalized).unsqueeze(0).unsqueeze(0)

    model = AudioFeatureExtractorCNN()
    features = model(input_tensor)

    print("Extracted Features:", features)

if __name__ == "__main__":
    main()
