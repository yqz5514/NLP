#%%
from nltk.corpus import inaugural # preseident address?
#%%
print(inaugural.fileids())
#%%
#print([ x[:9] for x in inaugural.fileids()])
#%%
print([fileid[:4] for fileid in inaugural.fileids()])
# only print year
#%%
import nltk
cfd = nltk.ConditionalFreqDist(
    (target, fileid[:4])
    for fileid in inaugural.fileids()
    for w in inaugural.words(fileid)
    for target in ['america', 'citizen']
    if w.lower().startswith(target))
cfd.plot()