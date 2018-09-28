import re
import matplotlib.pyplot as plt
import numpy as np
import sys
#import pandas as pd

'''
chatText = open('_chat.txt', encoding='utf-8').readlines()
'''
chatText = open('_chat.txt',"r")
'''

df=pd.read_fwf('_chat.txt',header=None,usecols=[0])
df1=pd.DataFrame(df[0].str.split('-',expand=True))
df2=pd.DataFrame(df1[1].str.split(':',expand=True))
data=df2[0]
'''

#non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), '')

dictionary = {}

for line in chatText:
	if line.find("[")!=-1 :
		line.strip("\n")
		
		lineSplit=line.split("]")
		
		#one line all shitty data fasak !
		#fasak fasak fasak
		name=lineSplit[1][1:lineSplit[1].find(":")]
	
		#dictionary update fasak !
		if dictionary.get(name, 0):
			dictionary[name] += 1
		else:
			dictionary[name] = 1
		#print(dictionary[name]) 
	

indices = np.arange(1, 51 , 5)

number_list = []
name_list = []

ind = 0

#one line sorting fasak!
sorted_dict = sorted( ((value, key) for (key,value) in dictionary.items()) , reverse = True)

for key, value in sorted_dict: 
	number_list.append(key)
	name_list.append(value)
	ind = ind+1
	if (ind >= 10):
		break

#print(number_list)

#fig, ax = plt.subplots()

plt.bar(indices, number_list)
plt.xticks(indices, name_list , rotation='vertical')
plt.subplots_adjust(bottom=0.30)
#plt.rc('xticks', labelsize=5)
#plt.rcParams.update({'font.size': 22}
plt.show()
