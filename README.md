# satellite-streak-detecting

This repository contains a step of project, where I test an approach of applying CNN, learning transfer and GAN augmentation for detecting if an image has a streak.
Detecting if FIT format image has a streak (probably made by a satelite), calculating its coords, checking TLE2 if matches, and detecting which satelite was that.

currently its preprocess part where i try to optimize checking TLE2 by reducing number of suspicious photos. I am using, among others, CNN, learning transfer and GAN augmentation due to we have small database, needed to analyse and  label manually. 
dataset is divided for a few groups. most important one is ds0 (50% with streaks), about which i am typing in code most freq.  but it is also the smallest one (40 files)
