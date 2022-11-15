#%%
import torch
T = torch.randn(3,4)
print(T.dtype)
print(T.shape)
print(T.device)# whic device I am working on
print(T)
#%%
if torch.cuda.is_available():
        tensor_gpu = T.to('cuda')# change device to gpu
else:
    print('Tensors are not in the GPU.')

# %%


