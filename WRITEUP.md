# Project Overview

This project has the goal of detecting objects in an urban environment, which is a very important tool when it comes to Self Driving Cars. The human hability of driving requires acknowledge the differente between pedestrians, other cars and traffic signals, for example. Detecting objects gives us the tool to take different responses to every single case, which is essential to driving safety. 

# Set up

To get the details on running the code, follow the instructions in the file [README.md](https://github.com/brucefie/sdc-p1-objectdetection/blob/main/README.md). 
While working on the project, it was not necessary to download the data or use a particular GPU, since the Udacity Workspace was used.

# Dataset

The data analysed was from Waymo, containing pictures with streets, pedestrians and cars, like in example above. 

![Image from EDA](files/01.png)

After the Exploratory Data Analysis, there is the result that the data contained mostly cars, comparing to the other objects.
![Results from Exploratory EDA](files/02.png)

These images were initially on the paste "training_and_validation" and it was splitted to the validation and training paste, using 80% of the 100 images to training and 20% to validation, also 3 images went to test paste.  

# Training

The first try on training did not include any change in the model used and the results can be seen above, which include training loss, precision, recall, total loss, steps per second and learning rate graphics. 

![First training results](files/03.png) ![First training results](files/04.png) ![First training results](files/05.png) ![First training results](files/06.png) ![First training results](files/07.png) ![First training results](files/08.png) ![First training results](files/09.png) ![First training results](files/10.png) ![First training results](files/11.png) ![First training results](files/12.png) ![First training results](files/13.png) 

In order to test this model with different images, another experiment was made. The changes were applied on the [pipeline_new.config](https://github.com/brucefie/sdc-p1-objectdetection/blob/main/experiments/experiment2/pipeline_new.config), where random constrast and black and white were applied to some images. The results after training are above.

![Second training results](files/14.png) ![Second training results](files/15.png) ![Second training results](files/16.png) ![Second training results](files/17.png) ![Second training results](files/18.png) ![Second training results](files/19.png) ![Second training results](files/20.png) ![Second training results](files/21.png) ![Second training results](files/22.png)

In order to improve this model and its results, it is necessary to get different types of data, containing more balanced numbers of cyclists, cars and pedestrians.


