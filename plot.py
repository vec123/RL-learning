import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import csv
from io import StringIO

def read_data_to_list(csv_file):
    converted = StringIO()
    with open(csv_file) as file:
       converted.write(file.read().replace('[', '"[').replace(']', ']"'))
    read_data=[]
    converted.seek(0)
    reader = csv.reader(converted)
    for row in reader:
       read_data.append(row)
    read_data = list(map(list, zip(*read_data )))

    for episode, col in enumerate(read_data):
        for i, value in enumerate(col):
            col[i] = value.replace('[','').replace(']','')
            col[i] = col[i].split()
            col[i] = np.array(col[i]).astype(float)
        read_data[episode]= col
    return(np.array(read_data))

#states = read_data_to_list("states_all.csv")

def plot(data, dim,name):
        for episode in range(0,data.shape[0]):
            plt.figure()
            plt.plot(data[episode, :, dim])
            plt.title("Dimension: {}".format(dim))
            plt.xlabel('Time')
            plt.ylabel(name)
            plt.savefig("Plots/{}_{}_dim_{}".format(name,episode,dim))
            plt.close()

#plot(states, 0)
data =read_data_to_list("states_all.csv")
for i in range(0,data.shape[2]):
    plot(data,i,"states")

data =read_data_to_list("actions_all.csv")
for i in range(0,data.shape[2]):
        plot(data,i,"action")

data =read_data_to_list("rewards_all.csv")
for i in range(0,data.shape[2]):
        plot(data,i,"rewards")


data =read_data_to_list("sine_from_env.csv")
for i in range(0,data.shape[2]):
        plot(data,i,"sine_from_env")


#for i in range(0,len(data)):
#    plt.figure()
#    plt.plot(data[i][:])
#    plt.xlabel('Time')
#    plt.ylabel('Action')
#    plt.savefig("Plots/Action_{}".format(i))
#    plt.close()


#data = np.transpose(pd.read_csv("states_all.csv",  header=None,  dtype = np.float64).to_numpy())
#for i in range(0,len(data)):
#    plt.figure()
#    plt.plot(data[i][:])
#    plt.xlabel('Time')
#    plt.ylabel('State')
#    plt.savefig("Plots/State_{}".format(i))
#    plt.close()

#data = np.transpose(pd.read_csv("Rewards_all.csv",  header=None,  dtype = np.float64).to_numpy())

#for i in range(0,len(data)):
#    plt.figure()
#    plt.plot(data[i][:])
#    plt.xlabel('Time')
#    plt.ylabel('Rewards')
#    plt.savefig("Plots/Rewards_{}".format(i))
#    plt.close()



#try:
#    data = np.transpose(pd.read_csv("sine_from_env.csv",  header=None,  dtype = np.float64).to_numpy())
#    for i in range(0,len(data)):
#        plt.figure()
        #plt.xlabel('Time')
        ##        plt.plot(data[i][:])
        #plt.ylabel('Sine')
        #plt.savefig("Plots/Sine_{}".format(i))
        #plt.close()
#except:
    #pass
