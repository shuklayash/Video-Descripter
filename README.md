# Video-Descripter
A sequence to sequence Deep Learning Model that convert a video into a textual description of  of the content. 

Global Parameters: 
```python 
n_inputs        = 4096
n_hidden        = 600
val_batch_size  = 100 # validation batch size
n_frames        = 80 # .npy (80, 4096) 
max_caption_len = 50
forget_bias_red = 1.0
forget_bias_gre = 1.0
dropout_prob    = 0.5
```
Changeable Parameters: (argparse)
```python
learning_rate   = 1e-4
num_epochs      = 100
batch_size      = 250
load_saver      = False # you can use pretrained model if you want
with_attention  = True
data_dir        = '.'
test_dir   = './testing_data'
```
```python 
import tensorflow as tf # keras.preprocessing included
import numpy as np
import pandas as pd
import argparse
import pickle
from colors import *
from tqdm import *
```
With bahdanau attention, we achieved **0.7049** for BLEU Score. The block shown below indicates the end of training status and`BLEU_eval.py` output message. You can check the sample output in `output.txt`.
Details for training and testing are provided below-
TRAINING DETAILS:

BLEU Score 0.70494110366799195  
Validation 100/100  
Total Loss 3.6234  
Epochs 5  
Training Loss 2.6644  

TESTING DETAILS:  

BLEU Score 0.70494110366799195

Full ruannable resource can be found at https://drive.google.com/drive/folders/1lXyiXjzJzEyGNN4ikTZeSuOR1Q_vQY8w?usp=sharing any update to the model  is most welcome!
