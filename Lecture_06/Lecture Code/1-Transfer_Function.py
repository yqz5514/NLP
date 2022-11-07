#%%
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-darkgrid')

#  %%-----------------------------------------
p = np.linspace(start=-8, stop=8, num=1000)
#  %%-----------------------------------------
def poslin(n):
    return np.maximum(0, n)

def purelin(n):
    return n

def logsig(n):
    return  1/(1 + np.exp(-n))
#A transformer model is a neural network that learns context and thus meaning by tracking relationships in sequential data like the words in this sentence.

#  %%-----------------------------------------
t_poslin = poslin(p)

plt.plot(p, t_poslin, ls='-')
plt.xlabel('p')
plt.ylabel('t')
plt.title('Transfer Function')
plt.show()
#  %%-----------------------------------------
t_logsig = logsig(p)

plt.plot(p, t_logsig, ls='-')
plt.xlabel('p')
plt.ylabel('t')
plt.title('Transfer Function')
plt.show()



# %%
