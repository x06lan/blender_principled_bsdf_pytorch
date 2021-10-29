from torch._C import Argument
import torch.nn as nn
import torch.nn.functional as F
nn_net = [100*100*3,100*100, 22]
def get_narray(in_arr,k_size):
    out_arr=[]
    width_x=len(in_arr)-k_size+1
    width_y=len(in_arr[0])-k_size+1
    for x in range(width_x):
        out_arr.append([])
        for y in range(width_y):
            # out_arr[x].append([])
            k_data=[]
            for k_x in range(k_size):
                for k_y in range(k_size):
                    k_data.append(in_arr[x+k_x][y+k_y])

            # print(k_data)
            out_arr[x].append(k_data)
            
        
    return out_arr
test=[]
tem=0
cum=3
for x in range(4):
    
    num_arr=[]
    for y in range(cum):
        num_arr.append(x*cum+y)
    # print(num_arr)
    test.append(num_arr)
        # tem+=1


print(test)

print(get_narray(test,2))


class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.nn_arr1=[]
        for x in range(100):
            self.nn_arr1[x].append([])
            for y in range(100):
                self.nn_arr1[x][y]=nn.Linear(3,1)

        self.nn_arr2=[]

        # self.nn1 = nn.Linear(nn_net[0], nn_net[1])  # 第一層 Linear NN
        # self.nn2 = nn.Linear(nn_net[1], nn_net[2])  # 第二層 Linear NN
        self.nn3 = nn.Linear(nn_net[2], nn_net[3])  # 第二層 Linear NN
        # self.nn4 = nn.Linear(nn_net[3], nn_net[4])  # 第二層 Linear NN
        self.sig = nn.Sigmoid()
        self.drop = nn.Dropout()
        self.tanh = nn.Tanh()

        # self.nn5 = nn.Linear(nn_net[2], 1) #第二層 Linear NN

        # self.nn3 = nn.Linear(100, 2) #第三層 Linear NN

    def forward(self, x):
        x = self.nn1(x)  # 對第一層 NN 使用Relu激活
        # x = F.relu(self.nn2(x))  # 對第一層 NN 使用Relu激活
        # x= self.tanh(x)
        x= F.relu(x)
        x = self.nn2(x)  # 對第一層 NN 使用Relu激活
        # x= self.tanh(x)
        # x = self.drop(x)
        # x = self.nn3(x)  # 對第一層 NN 使用Relu激活
        # x = self.nn4(x)  #對第一層 NN 使用Relu激活
        # x = F.relu(self.nn4(x))  # 對第一層 NN 使用Relu激活
        x = self.sig(x)
        # x = self.nn3(x)          #第二層直接輸出
        return x
