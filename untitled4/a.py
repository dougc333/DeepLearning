import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
m = nn.ReLU()
input = torch.randn(2)
output = m(input)
print("output:",output)
m = nn.Threshold(0.1, 20)
array = np.arange(-5, 1,.1)
tensor = torch.from_numpy(array)
print(tensor.size())
out = F.rrelu(tensor)
out = nn.ReLU(m)
print("relu:",out)
print("out:",out(tensor))