import bz2
path1='wd_pr_en.tsv.bz2'
with bz2.open(path1, 'rt') as f:
    data1=f.readlines()
    print(type(data1))
print(len(data1))
print(data1[0:10])
print(data1[-10:])


path2='wd_pr_en.ttl.bz2'
with bz2.open(path2, 'rt') as f:
    data2=f.readlines()
    print(type(data2))
print(len(data2))
print(data2[0:10])
print(data2[-10:])