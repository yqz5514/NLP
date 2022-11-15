import torch
from torch import nn
from torch.nn.utils.rnn import pad_sequence,pad_packed_sequence,pack_padded_sequence

docs = ['first second third',
        'first second',
        'first']

word_set=set()
for seq in docs:
  for word in seq.split(" "):
    word_set.add(word)

word_list=['<pad>']+list(word_set)
print(word_list)

word2idx={word: idx for idx,word in enumerate(word_list)}
vocab_size=len(word_list)
embedding_dim=10
# -------------------------------------------------------------------------------------
x = [torch.LongTensor([word2idx[word] for word in seq.split(" ")]) for seq in docs]
x_padded = pad_sequence(x, batch_first=True, padding_value=0)

print(x_padded)
seq_len=torch.LongTensor(list(map(len,x)))
print(seq_len)

embed=nn.Embedding(vocab_size,embedding_dim)
lstm=nn.LSTM(embedding_dim,hidden_size=5,batch_first=True)

embedding_seq_tensor=embed(x_padded)
print(embedding_seq_tensor)

packed_input = pack_padded_sequence(embedding_seq_tensor, seq_len.cpu().numpy(),
                                    batch_first=True,enforce_sorted=False)
print(packed_input.data.shape)
packed_output,(ht,ct)=lstm(packed_input)

print(packed_output.data.shape)
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