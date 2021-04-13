#!/bin/bash

#replace this with the path of your project on the VPS
cd ~/cd

#pull from the branch
git pull

# followed by instructions specific to your project that you used to do manually
systemctl restart nginx