
import pandas as pd
import numpy as np

def build_trans_mat(length = len(pd.read_csv('note_list.csv')),fname = 'link_list.csv'):
    '''
	build transition matrix 
    Params:length, length of total notes
    Type:int
    Params:fname,file of links
    Type:string
    Return:trans_mat, transition matrix of links
    Type: ndarray
    '''
    data = pd.read_csv(fname,sep = ',')
    grp = data.groupby('source_link')
    data = data.values
    trans_mat = np.zeros([length,length],dtype = np.float)
    for _,source,target in data:
        trans_mat[target][source] = 1/(len(grp.get_group(source)))
    return trans_mat
    
if __name__ == '__main__':
    note_fname = 'note_list.csv'
    link_fname = 'link_list.csv'
    print(len(pd.read_csv(note_fname)))
    print(build_trans_mat())
    


# In[14]:




