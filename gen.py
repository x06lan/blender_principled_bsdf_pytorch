import torch
import argparse
import cv2
import json
import numpy as np
# from vgg16 import Model
from PIL import Image
import torchvision.transforms.functional as TF
import random
from linear import Model
random.seed(4)

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate material')
    parser.add_argument('model',default="ml_data.bin", type=str, metavar='F',help='corpus-related data file')
    parser.add_argument('img',default="input.png", type=str, metavar='N',help='img')
    parser.add_argument('out',default="out.json", type=str, metavar='N',help='corpus-related data file')
    args = parser.parse_args()


    # print(args.model)
    model=Model().to(device)
    model.load_state_dict(torch.load(args.model))
    model.eval()
    # print(args.img)
    input_img = Image.open(args.img).convert('RGB')
    input_img= input_img.resize((200,200))
    input_img = TF.to_tensor(input_img)
    input_img=np.array(input_img)
    input_img=np.reshape(input_img,(120000))
    input_img=torch.Tensor(input_img).to(device)
    # input_img=input_img.unsqueeze(0)

    prediction=model(input_img)
    material=prediction.detach().numpy().tolist()
    bsdf_name=['Base Color','Base Color','Base Color','Base Color',
    'Subsurface',
    'Subsurface Radius',
    'Subsurface Color','Subsurface Color','Subsurface Color','Subsurface Color',
    'Metallic',
    'Specular',
    'Specular Tint',
    'Roughness',
    'Anisotropic',
    'Anisotropic Rotation',
    'Sheen',
    'Sheen Tint',
    'Clearcoat',
    'Clearcoat Roughness',
    'IOR',
    'Transmission',
    'Transmission Roughness',
    'Emission','Emission','Emission','Emission',
    'Alpha',
    'Normal',
    'Clearcoat Normal',
    'Tangent']
# Base Color
# r
# g
# ba
# Subsurface
# Subsurface Radius
# Subsurface Color
# r
# g
# ba
# Metallic
# Specular
# Specular Tint
# Roughness
# Anisotropic
# Anisotropic Rotation
# Sheen
# Sheen Tint
# Clearcoat
# Clearcoat Roughness
# IOR
# Transmission
# Transmission Roughness
# Emission
# r
# g
# ba
# Emission Strength
# Alpha
#     # material=material[0]
    print(material[0])
    with open(args.out,"w") as f:
        # print(material)
        f.write(json.dumps( material))
        f.close()

    # print(args.out)
    #  python gen.py model_save.bin data/1000/image/113.png out.json