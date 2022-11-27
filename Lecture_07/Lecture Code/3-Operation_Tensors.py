#%%
import torch

#%%
T1 = torch.ones(4,4)
print(T1)
#%%
print(T1[:,0])
#%%
print(T1[:,-1])
#%%
print(T1[...,1])

#%%
T2 = torch.rand(4,1)
T3 = T1 @ T2 ; print(T3)
#The connection between the two operations that comes to my mind is 
# the following: To calculate the ci,j entry of the matrix C:=AB, 
# one takes the dot product of the i'th row of the matrix A with the j'th column of the matrix B.
#%%
T4 = T1.matmul(T2); print(T4)# multiplication
#%%
T5 = torch.randn(4,4)
T6 = T1 * T5; print(T6)
#%%
T7 = T1.mul(T5); print(T7)#element multipulication



# %%
