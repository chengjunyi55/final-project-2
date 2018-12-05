#Converts gpas and gre scores to two lists of numbers of accepted and rejected \
#school ranking respectively, using keras linear regression and a functional \
#api with no hidden layer.
#Data downloaded from https://github.com/evansrjames/gradcafe-admissions-data.

import os
os.environ["TF_CPP_MIN_LOG_LEVEL"]="2"
import json
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from tensorflow.python.keras.models import Model, Sequential
from tensorflow.python.keras.layers import Input, Dense
from tensorflow.python.keras.callbacks import Callback, EarlyStopping

with open("ranking.json", "r") as rank:
    rank_dic=json.load(rank)
def key(no):
    if no in range(len(rank_dic.keys())):
        return list(rank_dic.keys())[no]
def rank(no):
    if no in range(len(rank_dic.keys())):
        return int(key(no).split("-")[0])

def train(data):
    with open("thegradcafe_accepted.json", "r") as nf:
        list1=json.load(nf)
    x1=np.array(list1[0])
    x2=np.array(list1[1])
    x3=np.array(list1[2])
    x4=np.array(list1[3])
    x5=np.array(list1[4])
    y1=np.array(list1[7])
    dat=np.array([x1,x2,x3,x4,x5]).transpose()
    idx_list=np.array(range(len(y1)))
    idx_test=np.random.choice(len(y1), size=int(len(y1)*0.25), replace=False)
    idx_train=np.delete(idx_list, idx_test).astype("int")
    dat_train=dat[idx_train,:]
    dat_test=dat[idx_test,:]
    y1_train=y1[idx_train]
    y1_test=y1[idx_test]
    inputs=Input(shape=(5,))
    y=Dense(1, activation="linear")
    output=y(inputs)
    model=Model(inputs, output)
    model.compile(optimizer='sgd', loss='mae', metrics=["mae"])
    history=model.fit(dat_train, y1_train, epochs=100, verbose=0)
    result1=round(float(model.predict(data, verbose=1)))

    with open("thegradcafe_rejected.json", "r") as nf:
        list1=json.load(nf)
    x1=np.array(list1[0])
    x2=np.array(list1[1])
    x3=np.array(list1[2])
    x4=np.array(list1[3])
    x5=np.array(list1[4])
    y1=np.array(list1[7])
    dat=np.array([x1,x2,x3,x4,x5]).transpose()
    idx_list=np.array(range(len(y1)))
    idx_test=np.random.choice(len(y1), size=int(len(y1)*0.25), replace=False)
    idx_train=np.delete(idx_list, idx_test).astype("int")
    dat_train=dat[idx_train,:]
    dat_test=dat[idx_test,:]
    y1_train=y1[idx_train]
    y1_test=y1[idx_test]
    inputs=Input(shape=(5,))
    y=Dense(1, activation="linear")
    output=y(inputs)
    model=Model(inputs, output)
    model.compile(optimizer='sgd', loss='mae', metrics=["mae"])
    history=model.fit(dat_train, y1_train, epochs=100, verbose=0)
    result2=round(float(model.predict(data, verbose=1)))

    schools1=[]
    schools2=[]
    schools3=[]

    max_rank=100-result2
    no=100-result2
    while rank(no)==max_rank:
        schools2.append(rank_dic.get(key(no))[0])
        no=no+1
    while len(schools2)<5:
        schools2.append(rank_dic.get(key(no))[0])
        no=no+1
    max_rank=100-result1
    no=100-result1
    while rank(no)==max_rank:
        schools1.append(rank_dic.get(key(no))[0])
        no=no+1
    while len(schools1)<5:
        schools1.append(rank_dic.get(key(no))[0])
        no=no+1
    while len(schools3)<5:
        schools3.append(rank_dic.get(key(no))[0])
        no=no+1
    """
    for key in rank_dic.keys():
        rank=int(key.split("-")[0])
        if result2+rank==100:
            schools2.append(rank_dic.get(key)[0])
        elif result2+rank>100 and len(schools2)<5:
            schools2.append(rank_dic.get(key)[0])
        if result1+rank==100 and rank_dic.get(key)[0] not in schools2:
            schools1.append(rank_dic.get(key)[0])
        elif result1+rank>100 and len(schools1)<5 and \
             rank_dic.get(key)[0] not in schools2:
            schools1.append(rank_dic.get(key)[0])
        if result1+rank>100 and rank_dic.get(key)[0] not in schools1 and \
           rank_dic.get(key)[0] not in schools2 and len(schools3)<5:
            schools3.append(rank_dic.get(key)[0])
    """
    return [schools1, schools2, schools3]
