
#%%
import numpy as np
x = np.random.randn(3,4)
y = np.random.randn(3,4)
z = np.random.randn(3,4)
a = x * y
b = a + z
c = np.sum(b)
#%%
print(x)
print(y)
print(z)
print(a)
print(b)
print(c)
#%%
grad_c = 1.0
grad_b = grad_c * np.ones((3,4));print(grad_b)
#%%
grad_a = grad_b.copy()
grad_z = grad_b.copy()
grad_x = grad_a * y
grad_y = grad_a *x

# graph is fast, designed by dictionary 
# tabnet
#%%
import numpy as np
np.random.randn(3,4)
# %%
