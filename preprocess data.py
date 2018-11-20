
# coding: utf-8

# In[46]:


import numpy as np
import pandas as pd
fname = 'gr0.California'
with open(fname,'r') as f:
    data = f.readlines()
note_list = []
link_list = []
for line in data:
    line = line.strip().split(' ')
    if line[0] == 'n':
        note_list.append(line[1:])
    if line[0] == 'e':
        link_list.append(line[1:])
df_note = pd.DataFrame({'link': [ i[1] for i in note_list]},index = range(len(note_list)))
df_link = pd.DataFrame({'source_link': [ i[0] for i in link_list],'target_link ': [ i[1] for i in link_list]})
df_note.to_csv('note_list.csv', sep=',')
df_link.to_csv('link_list.csv', sep=',')



    
    


# In[12]:


# print(df.link)


# In[64]:



print(df_link.values)
grp=df_link.groupby('source_link')
print(len(df.link))
print(len(grp.get_group('0')))
print(df_link.values)

for source, target in grp.get_group('0').values:
    print(source,target)
    

