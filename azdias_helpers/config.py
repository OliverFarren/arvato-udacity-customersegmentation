''' Declaration global variables
    Configure new directories
'''

import os

analysis_dir = './analysis'
dataset_dir = './datasets'

for new_dir in analysis_dir,dataset_dir:
    try:
        os.mkdir(new_dir)
        print(f"made new directory: {new_dir}")
    except FileExistsError:
        pass
