import math
from numpy.core.fromnumeric import shape
import torch
import matplotlib.pyplot as plt
import json
import numpy as np
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms.functional as TF
import numpy as np
import cv2
from PIL import Image
import random
from vgg16 import Model
# from sq import SqueezeNet
# Model=SqueezeNet
# from linear import Model
random.seed(4)

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


def bsdf_arg(arr):
    out = []
    for i in arr:
        # print(type(i))
        try:
            for j in i:
                out.append(j)
        except:
            out.append(i)
    return out


f = open("data/1000_100_noe/save_value.txt", 'r', encoding='utf-8')
datas = f.read()
datas = json.loads(datas)
# print(len(datas[0]))
model = Model().to(device)
optimizer = torch.optim.RMSprop(model.parameters(), lr=0.0003)
# loss_function=nn.L1Loss(reduction='mean')
# loss_function = torch.nn.MSELoss()
loss_function = nn.SmoothL1Loss()


losss = []
all_pre = []
targe_pre = []
epochs = 100
run_sample = 1

for epoch in range(epochs):
    input_img_arr = []
    input_targe_arr = []
    for j in range(run_sample):
        i = int(random.random()*1000)
        # print(i)
        # input_img = cv2.imread('data/1000/image/{}.png'.format(i))
        input_img = Image.open(
            'data/1000_100_noe/image/{}.png'.format(i)).convert('RGB')
        # input_img = input_img.resize((200, 200))
        input_img = input_img.resize((224, 224))

        # input_img = np.reshape(input_img, (120000))
        input_img = TF.to_tensor(input_img)
        input_img=np.array(input_img)

        # print(input_img.shape)

        input_targe = bsdf_arg(datas[i])
        input_targe = np.array(input_targe)

        input_img_arr.append(input_img)
        input_targe_arr.append(input_targe)

    input_img_arr = torch.tensor(input_img_arr)
    input_img_arr = input_img_arr.float()
    input_img_arr = input_img_arr.to(device)

    input_targe_arr = torch.tensor(input_targe_arr)
    input_targe_arr = input_targe_arr.float()
    input_targe_arr = input_targe_arr.to(device)

    # print(input_img_arr.shape)
    # print(input_targe_arr.shape)
    # prediction = model(input_img_arr)
    prediction = model(input_img_arr)

    loss = loss_function(prediction, input_targe_arr)
    losss.append(loss.item())
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    every = 1
    if i % every == every-1:
        print("loss:", loss.item())
        print(epoch+1, "/", epochs, ";", j+1, "/", run_sample)
        torch.save(model.state_dict(), "model_save.bin")
        print("save")

# torch.save(model.state_dict(), "model_save.bin")
# print("save")
# print(run_sample,epochs)
# print(len(losss))
# plt.plot(range(run_sample*epochs), losss)
with open("loss.json", "w") as f:
    f.write(json.dumps(losss))
    f.close()
plt.plot(range(epochs), losss)
plt.show()
