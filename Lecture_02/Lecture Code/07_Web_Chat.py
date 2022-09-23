#%%
from nltk.corpus import webtext
from nltk.corpus import nps_chat

#%%
for fileid in webtext.fileids():
   print(fileid, webtext.raw(fileid)[:65])

#%%
text = webtext.raw('firefox.txt')
print(text)
#%%
print([i for i in range(len(text)) if text.startswith('a', i)])

#%%
chatroom = nps_chat.posts('10-19-20s_706posts.xml')
#chatroom = nps_chat.words('10-19-20s_706posts.xml')
print(chatroom)
#%%
print(chatroom[123])
#%%
print(chatroom[2])

#%%
text2 = nps_chat.raw('11-09-teens_706posts.xml')
# %%
