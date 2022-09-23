#%%
f = open('sample.txt', 'r', encoding='utf-8')
data = f.read()
# %%
lines = data.split(sep='.')
l_over15 = [x for x in lines if len(x)>15]
print(l_over15)
# %%
char_not_alp = [x for y in lines for x in y if not x.isalpha()]
#print(char_not_alp)
# %%
from collections import Counter
Cnt = Counter(char_not_alp)
#print(Cnt)
#%%
type(Cnt)
#%%
print(Cnt.most_common(5))


# %%
test11 = [x.count(Cnt.most_common(5)[1][0]) for x in l_over15 ]
print(test11)
# %%
