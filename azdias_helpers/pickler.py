
'''
Utility functions to assist pickling objects
'''
from . import config
import pickle

def make_file_path(filename):
    return(config.dataset_dir + '/'+filename+'.pickle')


def dump(obj,filename):
    if isinstance(filename,str):
        with open(make_file_path(filename),'wb') as f:
            pickle.dump(obj,f)
    else:
        raise TypeError(f'Expected filename of type str but got type: {type(filename)}')
        

def load(filename):
    with open(make_file_path(filename),'rb') as f:
        obj = pickle.load(f)
        return obj
    