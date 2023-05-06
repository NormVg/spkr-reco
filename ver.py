#import torchaudio
#import speechbrain as sb
#from speechbrain.dataio.dataio import read_audio
#from IPython.display import Audio
print("loading module ")
from speechbrain.pretrained import SpeakerRecognition
#from speechbrain.pretrained import SepformerSeparation as separator
print("downloading modules and loding")
verification = SpeakerRecognition.from_hparams(
  source="speechbrain/spkrec-ecapa-voxceleb",
  savedir="pretrained_models/spkrec-ecapa-voxceleb")
print("ready predictor ")


def verify():
  print("starting predition ")
  score, prediction = verification.verify_files("1.wav", "t.wav")

  print(prediction[0].item(), score)
  print("predection done")
  return prediction[0].item()
  
