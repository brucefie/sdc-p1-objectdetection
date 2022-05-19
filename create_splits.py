import argparse
import glob
import os
import random
import shutil
import numpy as np
from utils import get_module_logger


def split(data_dir):
    """
    Create three splits from the processed records. The files should be moved to new folders in the 
    same directory. This folder should be named train, val and test.

    args:
        - data_dir [str]: data directory, /home/workspace/data/waymo
    """
    dataset = os.listdir(data_dir + 'training_and_validation')
    np.random.shuffle(dataset)
    train_sets, val_sets = np.split(dataset, [int(0.8 * len(dataset))])
    
    for i, data in enumerate(dataset):
        if i < int(0.75 * len(dataset)):
            shutil.move(data_dir+'/training_and_validation/'+ data, data_dir + '/train')
    # TODO: Split the data present in `/home/workspace/data/waymo/training_and_validation` into train and val sets.
    # You should move the files rather than copy because of space limitations in the workspace.
    
    val_sets = os.path.join(data_dir,'val')
    if os.path.exists(val_sets) == False:
        os.makedirs(val_sets)
    
    train_sets = os.path.join(data_dir,'train')
    if os.path.exists(train_sets) == False:
        os.makedirs(train_sets)
        
    test_sets = os.path.join(data_dir,'test')
    if os.path.exists(test_sets) == False:
        os.makedirs(train_sets)
                          
    
    files = [filename for filename in glob.glob(f'{data_dir}/*.tfrecord')]
    np.random.shuffle(files)
    train,val,test = np.split(files, [int(.8*len(files)), int(.2*len(files))])
 
    
    for t in train:
        shutil.move(t,train_sets)
        
    for v in val:
        shutil.move(v,val_sets)
        
    for t in test:
        shutil.move(t,test_sets)
                 
if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='Split data into training / validation / testing')
    parser.add_argument('--data_dir', required=True,
                        help='data directory')
    args = parser.parse_args()

    logger = get_module_logger(__name__)
    logger.info('Creating splits...')
    split(args.data_dir)