#%%
import torch

t = torch.rand(2, 1, 2, 1); print(t)
r = torch.squeeze(t); print(r)
print(t.shape)
print(r.shape)
#%%
r = torch.squeeze(t, 3); print(r)# decrease dimension
r.shape
#%%

x = torch.rand([1, 2, 3]); print(x)
#%%
x.shape()
#%%
r = torch.unsqueeze(x, 0); print(r)# add dimension 
r = torch.unsqueeze(x, 1); print(r)
# why you need create dimensions? espicially in nlp domain
# In nlp, the data timestamp is not always same(always unknown)--collader??

# why we do neuron network?
# BOWS(removed the order of sentence, only work with requency and not complex enough to fo task like genaralization, translation...)
v = torch.arange(9).reshape(3,3)
# flatten a Tensor and return elements with given indexes
r = torch.take(v, torch.LongTensor([0, 4, 2]))
r = torch.transpose(v, 0, 1); print(r)

mat1 = torch.randn(2, 3)
mat2 = torch.randn(3, 4)
r = torch.mm(mat1, mat2)# all of 

v1 = torch.ones(3)
r = torch.diag(v1) # np.diag, becasue the dervtive of .....is diagnose 

#(batch, time-lenght of data,dimension)

# linear algebria 