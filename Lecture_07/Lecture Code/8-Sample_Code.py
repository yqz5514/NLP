import torch
from torch import nn
from torchtext.data.utils import get_tokenizer# for NN
from torchtext.vocab import build_vocab_from_iterator
from torch.utils.data import DataLoader
from torchtext.datasets import AG_NEWS
import time
# NLTK, spaCy can not work in gpu
# ------------------------------------------------------------------------------
train_iter = list(AG_NEWS(split='train'))
test_iter = list(AG_NEWS(split='test'))
print(train_iter[0])
# ------------------------------------------------------------------------------
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
tokenizer = get_tokenizer('basic_english')
def yield_tokens(data_iter): # create dataloader
    for _, text in data_iter: # iterate whoel sents..?
        yield tokenizer(text)

vocab = build_vocab_from_iterator(yield_tokens(train_iter), specials=["<unk>"])
vocab.set_default_index(vocab["<unk>"])
print(vocab(['here', 'is', 'an', 'example']))
# ------------------------------------------------------------------------------
text_pipeline = lambda x: vocab(tokenizer(x)) 
label_pipeline = lambda x: int(x) - 1
print(text_pipeline('here is the an example'))
print(label_pipeline('10'))
# ------------------------------------------------------------------------------
def collate_batch(batch):
    label_list, text_list, offsets = [], [], [0]
    for (_label, _text) in batch:
         label_list.append(label_pipeline(_label))
         processed_text = torch.tensor(text_pipeline(_text), dtype=torch.int64)
         text_list.append(processed_text)
         offsets.append(processed_text.size(0))
    label_list = torch.tensor(label_list, dtype=torch.int64)
    offsets = torch.tensor(offsets[:-1]).cumsum(dim=0)
    text_list = torch.cat(text_list)
    return label_list.to(device), text_list.to(device), offsets.to(device)
# ------------------------------------------------------------------------------
class TextClassificationModel(nn.Module):
    def __init__(self, vocab_size, embed_dim, num_class):
        super(TextClassificationModel, self).__init__()
        self.embedding = nn.EmbeddingBag(vocab_size, embed_dim)
        self.fc = nn.Linear(embed_dim, num_class) # one layer
        self.init_weights()
    def init_weights(self):
        initrange = 0.5
        self.embedding.weight.data.uniform_(-initrange, initrange)
        self.fc.weight.data.uniform_(-initrange, initrange)
        self.fc.bias.data.zero_()
    def forward(self, text, offsets):
        embedded = self.embedding(text, offsets)
        return self.fc(embedded)
# ------------------------------------------------------------------------------
num_class = len(set([label for (label, text) in train_iter]))
vocab_size = len(vocab)
emsize = 64
model = TextClassificationModel(vocab_size, emsize, num_class).to(device)
#MLP
# batch: number of observation, time: length of the sents, dimension(rich embedding)
#embedding(lok up table, hash table)
# nn.embedding is the first strp (the fly embedding training) 
# ------------------------------------------------------------------------------
def train(dataloader):
    model.train() #Put in train mode, can keep tracking each nuron shut down 
    #check model drop out
    total_acc, total_count = 0, 0
    log_interval = 500
    start_time = time.time()

    for idx, (label, text, offsets) in enumerate(dataloader):# GPU does not have garbage collade, 0 out
        optimizer.zero_grad()
        predicted_label = model(text, offsets)
        loss = criterion(predicted_label, label)
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 0.1)
        optimizer.step()
        total_acc += (predicted_label.argmax(1) == label).sum().item()
        total_count += label.size(0)
        if idx % log_interval == 0 and idx > 0:
            elapsed = time.time() - start_time
            print('| epoch {:3d} | {:5d}/{:5d} batches '
                  '| accuracy {:8.3f}'.format(epoch, idx, len(dataloader),
                                              total_acc/total_count))
            total_acc, total_count = 0, 0
            start_time = time.time()

def evaluate(dataloader):
    model.eval()# inference
    total_acc, total_count = 0, 0

    with torch.no_grad():
        for idx, (label, text, offsets) in enumerate(dataloader):
            predicted_label = model(text, offsets)
            loss = criterion(predicted_label, label)
            total_acc += (predicted_label.argmax(1) == label).sum().item()
            total_count += label.size(0)
    return total_acc/total_count
# ------------------------------------------------------------------------------
EPOCHS = 10
LR = 0.001
BATCH_SIZE = 64
criterion = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=LR)
# ------------------------------------------------------------------------------
train_dataloader = DataLoader(train_iter, batch_size=BATCH_SIZE,
                              shuffle=True, collate_fn=collate_batch)
#collate_fn can help deal with different length of each sents
test_dataloader = DataLoader(test_iter, batch_size=BATCH_SIZE,
                              shuffle=True, collate_fn=collate_batch)


for epoch in range(1, EPOCHS + 1):
    epoch_start_time = time.time()
    train(train_dataloader)
    accu_val = evaluate(test_dataloader)
    print('-' * 59)
    print('| end of epoch {:3d} | time: {:5.2f}s | '
          'valid accuracy {:8.3f} '.format(epoch,
                                           time.time() - epoch_start_time, accu_val))
    print('-' * 59)
# ------------------------------------------------------------------------------
torch.save(model.state_dict(), 'model_weights.pt')
# load the model first for inference
model.load_state_dict(torch.load('model_weights.pt'))
model.eval()


# try it on BOW
# why 