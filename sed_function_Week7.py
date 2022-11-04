#!/usr/bin/env python
# coding: utf-8

# In[12]:


def sed(strfind, strreplace, file1, file2):
    #Open File1
    fileopn1 = open(file1)

    # Write to File2
    filewrt2 = open(file2, 'w+')
    
        # Check for strfind
    for l in fileopn1:
        if strfind in l:
            try:
                #Replace with strreplace
                replace_l = l.replace(strfind,strreplace)
                filewrt2.write(replace_l)
            except ValueError:
                Error=messagebox.showinfo("An error has occured")
            
        else:
            filewrt2.write(l)
            


# In[14]:


sed('love', 'adore', 'C:\GIS\Sed_file1.txt', 'C:\GIS\Sed_file2.txt')


# In[ ]:




