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

    # TODO: Split the data present in `/home/workspace/data/waymo/training_and_validation` into train and val sets.
    # You should move the files rather than copy because of space limitations in the workspace.
    print("Path written by the user: {} ".format(data_dir))
    
    from_path = data_dir + '/waymo/training_and_validation'
    print("From path: {}".format(from_path))
    to_path = data_dir + '/waymo/'
    print("To path: {}".format(to_path))
    
    val_dir = os.path.join(from_path , to_path + 'val')
    if os.path.exists(val_dir) == False:
        os.makedirs(val_dir)
    
    train_dir = os.path.join(from_path , to_path + 'train')
    if os.path.exists(train_dir) == False:
        os.makedirs(train_dir)
        
    test_dir = os.path.join(from_path , to_path + 'test')
    if os.path.exists(test_dir) == False:
        os.makedirs(test_dir)
   
    dataset = [filename for filename in glob.glob(f'{from_path}/*.tfrecord')]
    print("Number of files: {}".format(len(dataset)))
    np.random.shuffle(dataset) #organize the list
    
    train_sets, val_sets = np.split(dataset, [int(0.8 * len(dataset))]) #split into train and val
    
    
    for t in train_sets:
        print(t)
        shutil.move(t, train_dir)
        
    for v in val_sets:
        print(v)
        shutil.move(v, val_dir)
        
                 
if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='Split data into training / validation / testing')
    parser.add_argument('--data_dir', required=True,
                        help='data directory')
    args = parser.parse_args()

    logger = get_module_logger(__name__)
    logger.info('Creating splits...')
    split(args.data_dir)