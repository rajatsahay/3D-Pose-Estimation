import os
import os.path
import binvox_rw
import numpy as np
import tensorflow as tf
import cv2
from PIL import Image

#clg
test="03001627"
main="03211117"
bs=2

label_dir=os.listdir("/content/"+test+"_labels")
data=os.listdir("/content/"+test+" ")
total_size=len(data)

def train_labels():
  if len(label_dir)<bs:
    return []
  
  y_train={}
  for _ in range(bs):
    label=label_dir.pop()
    if(label.startswith(".")):
      continue
    binv=open("/content/"+test+"_labels/"+label+"/model.binvox",'rb')
    binvox_data=binvox_rw.read_as_3d_array(binv).data
    y_train[label]=np.asarray(binvox_data)

  return y_train

def train_data():
  if len(data)<bs:
    return []
  
  x_train={}
  for _ in range(bs):
    item=data.pop()
    tmp_im_array=[]
    if(item.startswith(".")):
      continue
    for item in os.listdir("/content/"+test+"/"+item+"/rendering"):
      if ".png" in item:
        img=np.array(Image.open("/content/"+test+"/"+item+"/rendering/"+item))
        img=tf.random_crop(img,[127,127,3])
        tmp_im_array.append(img)

    x_train[item]=tmp_im_array
    tmp_im_array=[]

  return x_train
