
# coding: utf-8

# In[2]:



import pandas as pd
import numpy as np
from tld import get_tld
edu_reserved_link = ['www','html','com','edu','htm','net','links','index']
reserved_link=['www','html','com','htm','net','links','index']

def plot_domain(data,name):
    ''' 
    plot domain analysis result data
    Params:data,result of domain analysis
    Type:list of tuples
    Params:name,name of domain
    Type:string 

    '''
    import matplotlib.pyplot as plt
    import numpy as np
    from scipy.interpolate import spline
    plt.rcdefaults()
    fig, ax = plt.subplots()
    
    index = np.arange(len(data))
    label = [i for i,j in data]
    y = [j for i,j in data]
    plt.bar(index,y,color = "#0099CC")
    ax.spines["top"].set_visible(False)  
    ax.spines["right"].set_visible(False) 
    plt.xlabel('Domain', fontsize=10)
    plt.ylabel('Occurence', fontsize=10)
    plt.xticks(index, label, fontsize=8, rotation=30)
    plt.title('TOP 15 '+name+' occurence when you type in \'California\'')
    index_new = np.linspace(index.min(),index.max(),300)
    y_smooth = spline(index,[i-20 for i in y],index_new)
    
    plt.plot(index_new,y_smooth,color = "#FF9933")
    foo_fig = plt.gcf()
    foo_fig.savefig('plot:'+name+'.jpg',dpi=500)
    plt.show()
    
def domainanalysis(fname1='note_list.csv',fname2 = 'link_list.csv'):
    ucsd_link = pd.DataFrame()
    notedata = pd.read_csv(fname1,sep = ',')
    linkdata = pd.read_csv(fname2,sep = ',')
    grp = linkdata.groupby('source_link')
    tld_dict={}
    domain_dict = {}
    edu_dict1={}
    ucsd_idx =[]
    notedata = notedata.values
    count = 0
    for idx, origin_link in notedata:
        try:
            res = get_tld(origin_link,as_object=True)
            domain_dict.setdefault(res.domain,0)
            domain_dict[res.domain]+=1
            tld_dict.setdefault(res.tld,0)
            tld_dict[res.tld]+=1
        except:
            pass
        try:
            link = origin_link.split('://')[1]
        except:
            continue
        link = link.split('.')
        link = [w.strip('/').split('/')[0] for w in link ]
        if 'ucsd' in link:
            try:
                ucsd_link = pd.concat([ucsd_link,grp.get_group(idx)],ignore_index = True)
            except:
                pass
            ucsd_idx.append(idx)
        if 'edu' in link:
            for keyword in link:
                if keyword in edu_reserved_link:
                    continue
                edu_dict1.setdefault(keyword,0)
                edu_dict1[keyword]+=1
    edu_result_list = sorted([(i,j) for i,j in edu_dict1.items()],key = lambda item: item[1])
    tld_result_list = sorted([(i,j) for i,j in tld_dict.items()],key = lambda item: item[1])
    domain_result_list = sorted([(i,j) for i,j in domain_dict.items()],key = lambda item: item[1])
    test_note={}
    s_link=[]
    t_link=[]
    for _,source,target in linkdata.values:
        if source in ucsd_idx and target in ucsd_idx:
            s_link.append(source)
            t_link.append(target)
    ucsd_link = pd.DataFrame({source:s_link,target:t_link})
    return edu_result_list[::-1][:15],domain_result_list[::-1][:15],tld_result_list[::-1][:15],ucsd_idx,ucsd_link

if __name__ == '__main__':
    note_fname = 'note_list.csv'
    link_fname = 'link_list.csv'
    print(len(pd.read_csv(note_fname)))
    edu_result,domain_result,tld_result,ucsd_idx, ucsd_link= domainanalysis()
    print(ucsd_idx)
    print(domain_result,tld_result)
    print(len(edu_result))
    plot_domain(domain_result,'Subdomain')
    plot_domain(tld_result,'Top level Domain')
    plot_domain(edu_result,'Domain related to .edu')




    

