
#%%
import torch
data = [[1,2,3,4],[4,5,6,7]]
data_tensor = torch.Tensor(data)# convert ddata to tensor #change object redcast??
print(data_tensor)

#%%
type(data_tensor)
#%%
type(data)
#%%
import numpy as np
data_numpy = np.array(data)
data_tensor = torch.Tensor(data_numpy)
print(data_tensor)

#%%
x = torch.ones_like(data_tensor)
print(x)
y = torch.randn_like(data_tensor)
print(y)

