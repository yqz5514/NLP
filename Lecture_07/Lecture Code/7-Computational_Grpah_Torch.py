#%%
import torch
from torch.autograd import Variable
# a pytorch variable is a node in a cimputational graph
#the autograd packages provides automatic differentiation for all operations on tensor
#%%
x = Variable(torch.randn(3,4), requires_grad = True);print(x)
#%%
y = Variable(torch.randn(3,4), requires_grad = True);print(y)
#%%
z = Variable(torch.randn(3,4), requires_grad = True);print(z)
a = x * y;print(a)
b = a + z
c = torch.sum(b)
#%%
print(c)
#%%
c.backward()#have all gradients computed automatically
#%%
print(x.grad.data)
#%%
print(y.grad.data)
print(z.grad.data)
#???????????????????????????????????????????
#%%
# ----------------------------------------
from torch import nn
class model(nn.Module):
    def __init__(self, hidden_dim):#initialize the neural network layers in __init__
        super(model, self).__init__()
        self.linear1 = nn.Linear(1, hidden_dim)# nn.Linear means (wp+b)
        self.act1 = torch.sigmoid
        self.linear2 = nn.Linear(hidden_dim, 1)
    def forward(self, x):
        return self.linear2(self.act1(self.linear1(x)))
# ----------------------------------------
# pass the models output logits to loss function
import torch
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr = 0.001)

# trainind loop
# ----------------------------------------
def train_loop (dataloader, model, loss, optimizer):
    size = len(dataloader.dataset)
    for batch, (X,y) in enumerate(dataloader):
        pred = model(X)
        loss = criterion(pred,y)
        optimizer.zero_grad()
        loss.backward()# claculate gradient of weigts
        optimizer.step()#if you have gradient, can do any optimazation
        
        #cross entrophy for classification
        #A gradient simply measures the change in all weights with 
        # regard to the change in error.
        
# how to do test loop?