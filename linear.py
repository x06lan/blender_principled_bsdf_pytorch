import torch.nn as nn
import torch.nn.functional as F
nn_net = [200*200*3, 20*20*3, 20*20*3, 20*20*3, 22]


class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.nn1 = nn.Linear(nn_net[0], nn_net[1])  # 第一層 Linear NN
        self.nn2 = nn.Linear(nn_net[1], nn_net[2])  # 第二層 Linear NN
        self.nn3 = nn.Linear(nn_net[2], nn_net[3])  # 第二層 Linear NN
        self.nn4 = nn.Linear(nn_net[3], nn_net[4])  # 第二層 Linear NN
        self.sig = nn.Sigmoid()
        self.drop = nn.Dropout()

        # self.nn5 = nn.Linear(nn_net[2], 1) #第二層 Linear NN

        # self.nn3 = nn.Linear(100, 2) #第三層 Linear NN

    def forward(self, x):
        x = F.relu(self.nn1(x))  # 對第一層 NN 使用Relu激活
        # x = F.relu(self.nn2(x))  # 對第一層 NN 使用Relu激活
        x = self.nn2(x)  # 對第一層 NN 使用Relu激活
        # x = self.drop(x)
        x = F.relu(self.nn3(x))  # 對第一層 NN 使用Relu激活
        x = self.nn4(x)  #對第一層 NN 使用Relu激活
        # x = F.relu(self.nn4(x))  # 對第一層 NN 使用Relu激活
        x = self.sig(x)
        # x = self.nn3(x)          #第二層直接輸出
        return x
