import numpy as np
import re
import itertools
from collections import Counter
from openpyxl import Workbook,load_workbook
from datetime import datetime

def clean_str(string):
    """
    Tokenization/string cleaning for all datasets except for SST.
    Original taken from https://github.com/yoonkim/CNN_sentence/blob/master/process_data.py
    """
    string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
    string = re.sub(r"'", " ' ", string)
    string = re.sub(r"\'s", " \'s", string)
    string = re.sub(r"\'ve", " \'ve", string)
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    string = re.sub(r",", " , ", string)
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", " ( ", string)
    string = re.sub(r"\)", " ) ", string)
    string = re.sub(r"\?", " ? ", string)
    string = re.sub(r"\s{2,}", " ", string)
    return string.strip().lower()


def load_data(data_file, output_file):
    wb_i,wb_o = load_workbook(data_file),load_workbook(output_file,data_only = True)
    ws_i,ws_o= wb_i['AAPL NEWS'],wb_o['Sheet1']
    x_text = {}
    for i in range(ws_i.max_row-2):
        date_i = datetime.strptime(str(ws_i['A'+str(i+2)+''].value) +' '+ str(ws_i['B'+str(i+2)+''].value), '%Y-%m-%d %H:%M:%S')
        headline = clean_str(re.sub(r'[^\x00-\x7F]+',' ', str(ws_i['D'+str(i+1)+''].value)))
        text = clean_str(re.sub(r'[^\x00-\x7F]+',' ', str(ws_i['E'+str(i+1)+''].value)))
        for j in range(ws_o.max_row-2):
            date_o = datetime.strptime(str(ws_o['A'+str(j+2)+''].value), '%Y-%m-%d %H:%M:%S')
            str(ws_i['E'+str(i+1)+''].value)

# def load_data(data_file, output_file):
#     wb_i,wb_o = load_workbook(data_file),load_workbook(output_file,data_only = True)
#     ws_i,ws_o= wb_i['Sheet1'],wb_o['Sheet1']
#     x_text = {}
#     for i in range(ws_o.max_row-2):
#         date_obj = datetime.strptime(str(ws_o['A'+str(i+2)+''].value), '%Y-%m-%d %H:%M:%S')
#         key_start = (str(date_obj.month)+str(date_obj.day))
#         date_obj = datetime.strptime(str(ws_o['A'+str(i+3)+''].value), '%Y-%m-%d %H:%M:%S')
#         key_end = (str(date_obj.month)+str(date_obj.day))
#         key_value = ws_o['C'+str(i+3)+''].value
#         start_range = False
#         for j in range(ws_i.max_row):
#             key_i = str(ws_i['B'+str(j+1)+''].value) + str(ws_i['C'+str(j+1)+''].value)
#             if key_i == key_start:
#                     start_range = True
#             if key_i == key_end:
#                 break
#             if start_range == True:
#                 try : 
#                     x_text[key_value].append(clean_str(re.sub(r'[^\x00-\x7F]+',' ', str(ws_i['D'+str(j+1)+''].value))))
#                 except :
#                     x_text[key_value] = [clean_str(re.sub(r'[^\x00-\x7F]+',' ', str(ws_i['D'+str(j+1)+''].value)))]
#     input_x,y = [],[]
#     for key,value in x_text.items():
#     	text =''
#     	for heads in value:
#     		text = text + ' ' + heads
#     	input_x.append(text)
#     	y.append([1,0] if key >0 else [0,1])
#     return (input_x,y)

def load_test(excel_file):
    '''
    Loads the test excel file with 100 headlines marked with positive and negative sentiment
    Process the excel file and returns the headline and sentiment
    '''
    wb = load_workbook('test.xlsx')
    worksheet = wb['Sheet1']
    x_text,y = [],[]
    #print (worksheet['C1'].value)
    for i in range(100):
        senti_val = str(worksheet['B'+str(i+1)+''].value)
        if (senti_val == 'n' or senti_val=='p'):
            headline = str(worksheet['A'+str(i+1)+''].value)
            line = re.sub(r'[^\x00-\x7F]+',' ', headline)
            y.append([0,1] if senti_val == 'p' else [1,0])
            x_text.append(line)
    x_text = [clean_str(sent) for sent in x_text]
    return [x_text,np.array(y)]

def process_vocab(dim,word_vec):
    '''
    Processes the word vectors from glove.
    Returns vocabulary and the corresponding word-vectors.
    '''
    vocab,word2vec = {},[[0.0]*dim]
    for idx,(word,vec) in enumerate(word_vec.items()):
            vocab[word] = idx+1
            word2vec.append(list(map(float, vec)))
    print("==> vocab processing is done")
    return vocab, word2vec

def load_glove(dim):
    '''
    Loads the GloVe word-vectors with mentioned dimension.
    Return the word vectors in  dictionary format.
    '''
    word_vec = {}
    print("==> loading glove")
    with open(("glove.6B." + str(dim) + "d.txt" ), encoding = 'utf8') as f:  # "vec"
        for line in f:
            l = line.split()
            for idx,word in enumerate(l):
                if idx !=0:
                    try :
                        float(word)
                        break
                    except :
                        pass
            key = ' '.join(l[:idx])
            # print (key.encode("utf8"))
            word_vec[key] = list(map(float, l[idx:]))
            
    print("==> glove is loaded")
    return word_vec

def create_vector(word,dim,word2vec):
    '''
    Creates a word vector if the word is not present in the vocab.
    Returns the updated word vectors.
    '''
    vector = np.random.uniform(0.0,1.0,(dim,))
    word2vec[word] = vector
    with open("glove.6B." + str(dim) + "d.txt" ,'a') as gw:
    	gw.write('\n'+str(word))
    	for vec in vector.tolist():
    		gw.write(' '+str(vec))
    return word2vec

def batch_iter(data, batch_size, num_epochs, shuffle=True):
    """
    Generates a batch iterator for a dataset.
    """
    data = np.array(data)
    data_size = len(data)
    num_batches_per_epoch = int((len(data)-1)/batch_size) + 1
    for epoch in range(num_epochs):
        # Shuffle the data at each epoch
        if shuffle:
            shuffle_indices = np.random.permutation(np.arange(data_size))
            shuffled_data = data[shuffle_indices]
        else:
            shuffled_data = data
        for batch_num in range(num_batches_per_epoch):
            start_index = batch_num * batch_size
            end_index = min((batch_num + 1) * batch_size, data_size)
            yield shuffled_data[start_index:end_index]