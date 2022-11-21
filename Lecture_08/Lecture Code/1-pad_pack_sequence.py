#%%
import torch
from torch import nn
from torch.nn.utils.rnn import pad_sequence,pad_packed_sequence,pack_padded_sequence
import numpy
#%%
docs = ['first second third',
        'first second',
        'first']

word_set=set()
for seq in docs:
  for word in seq.split(" "):
    word_set.add(word)

word_list=['<pad>']+list(word_set)
print(word_list)
#%%
word2idx={word: idx for idx,word in enumerate(word_list)}
vocab_size=len(word_list)
embedding_dim=10

#%%
print(word2idx)
print(vocab_size)
#%%
# -------------------------------------------------------------------------------------
x = [torch.LongTensor([word2idx[word] for word in seq.split(" ")]) for seq in docs]
#%%
x
#%%
x_padded = pad_sequence(x, batch_first=True, padding_value=0)

#%%
print(x_padded)

#%%
seq_len=torch.LongTensor(list(map(len,x)))
print(seq_len)

#%%
embed=nn.Embedding(vocab_size,embedding_dim)# save embedding
lstm=nn.LSTM(embedding_dim,hidden_size=5,batch_first=True)#batch_first can adjust the input order batch to the first
#input(seq_len, batch, input_size) this is the rgular input order
embedding_seq_tensor=embed(x_padded)
print(embedding_seq_tensor)
#%%
seq_len.cpu().numpy()
#%%

packed_input = pack_padded_sequence(embedding_seq_tensor, seq_len,
                                    batch_first=True,enforce_sorted=False)
print(packed_input.data.shape)
print(packed_input)
#%%
packed_output,(ht,ct)=lstm(packed_input)
#%%
print(packed_output)

print(packed_output.data.shape)
#%%
output, input_sizes = pad_packed_sequence(packed_output, batch_first=True)
print(ht[-1])

#%%
# what kind of data this network try to accept?
# sequenced data
# what output we expected for this network?
# sequenced data
# what is output of first layer of mlp? what does it mean?
# transformed input data in time....? and MLP does not preseverve order
# why the input and output are delay?
# what is the problem of infinite memory model?
# vanish gradient, suffer from train procedure. 
# the backprogagtion will not work for this because 
# translation: two face problem
# - understanding the meaning of it (encoder , encode english to some meaningful  )
#   and convert it to another language(decoder, decode )
# they are not happen semotineous, this called seq2seq
# what is problem for seq2seq: not all sequence are important, so we use attention to select those sequence ahs most impact 
# all of thme ar rnn
# dot product is important becasue use it find similarity 
# seq2seq attention
# self attention
#know to how to train RNN and add pack stack 

#squeeze的用法主要就是对数据的维度进行压缩或者解压。

#先看torch.squeeze() 这个函数主要对数据的维度进行压缩，去掉维数为1的的维度，比如是一行或者一列这种，一个一行三列（1,3）的数去掉第一个维数为一的维度之后就变成（3）行。squeeze(a)就是将a中所有为1的维度删掉。不为1的维度没有影响。a.squeeze(N) 就是去掉a中指定的维数为一的维度。还有一种形式就是b=torch.squeeze(a，N) a中去掉指定的定的维数为一的维度。

#再看torch.unsqueeze()这个函数主要是对数据维度进行扩充。给指定位置加上维数为一的维度，比如原本有个三行的数据（3），在0的位置加了一维就变成一行三列（1,3）。a.squeeze(N) 就是在a中指定位置N加上一个维数为1的维度。还有一种形式就是b=torch.squeeze(a，N) a就是在a中指定位置N加上一个维数为1的维度