
# coding: utf-8

# In[181]:


def pr_matrix(fname = 'input.txt'):
    assert isinstance(fname, str)
    import csv
    with open(fname) as input_file:
        pr = list(csv.reader(input_file, delimiter=' '))
        import numpy as np
        counter = 0
        for i in range(len(pr)):
            if (pr[i][0] == 'n'):
                counter += 1
        pr_matrix = np.empty([counter,1])
        for i in range(len(pr_matrix)):
            pr_matrix[i][0] = 1/counter
    return pr_matrix


# In[182]:


if __name__ == '__main__':
    res = pr_matrix()
    print(res.shape)
    print(res)
