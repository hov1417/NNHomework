from IPython.display import Audio, display
import numpy as np

def allDone():
    display(Audio(url='https://sound.peal.io/ps/audios/000/000/537/original/woo_vu_luvub_dub_dub.wav', 
                  autoplay=True))

def describe(x):
	x = np.asarray(x)
	print(x.shape, x.min(), x.mean(), x.max())