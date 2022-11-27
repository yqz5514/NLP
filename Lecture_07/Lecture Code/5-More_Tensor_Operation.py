#%%
import torch

#%%
t = torch.rand(2, 1, 2, 1); print(t)
r = torch.squeeze(t); print(r)
print(t.shape)
print(r.shape)
#%%
r = torch.squeeze(t, 3); print(r)# decrease dimension
# remove dimsion 1 from position 3 on tensor t
r.shape
#%%
x = torch.rand([1, 2, 3]); print(x) # 1:other-dim,2:rows, 3: cols
#%%
x.shape
#%%
r = torch.unsqueeze(x, 0); print(r)# add dimension 
r.shape
#%%
r = torch.unsqueeze(x, 2); print(r)
r.shape
# why you need create dimensions? espicially in nlp domain
# In nlp, the data timestamp is not always same(always unknown)--collader??

#%%
# why we do neuron network?
# BOWS(removed the order of sentence, only work with requency and not complex enough to fo task like genaralization, translation...)
v = torch.arange(9).reshape(3,3)
print(v)
#%%
# flatten a Tensor and return elements with given indexes
r = torch.take(v, torch.LongTensor([0, 4, 2]))
#Returns a new tensor with the elements of input at the given indices. The input tensor is treated as if it were viewed as a 1-D tensor. The result takes the same shape as the indices.
r.shape
print(r)
#%%
r = torch.transpose(v, 0, 1); print(r)
#torch.transpose(input, dim0, dim1)
#Returns a tensor that is a transposed version of input. The given dimensions dim0 and dim1 are swapped
#%%
mat1 = torch.randn(2, 3)
mat2 = torch.randn(3, 4)
r = torch.mm(mat1, mat2)
print(r)
#If input is a (n×m) tensor, mat2 is a (m×p) tensor, out will be a (n×p) tensor.
#mutiplication
#%%
v1 = torch.ones(3);print(v1)

r = torch.diag(v1);print(r) 
# np.diag, becasue the dervtive of .....is diagnose 

#(batch, time-lenght of data,dimension)

# linear algebria 
# %%
