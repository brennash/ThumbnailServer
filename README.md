# ThumbnailServer
Thumbnail server is a quick script to take a number of large input images, generate a load of 
thumbnails and an index.html linking everything together. Allow for a quick way of creating 
online photo galleries. 

## Installation (from bare bones)
<pre>
sudo apt-get update
sudo apt-get install git openssh-server python-pip apache2
sudo apt-get install zlib1g-dev
sudo apt-get install libjpeg-dev
sudo apt-get install libjpeg8-dev
sudo apt-get install python-dev

sudo nano /etc/ssh/ssh_config
# Set the following - PasswordAuthentication yes
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
more .ssh/id_rsa.pub 
# Copy your ssh public key and put it into GitHub
git clone git@github.com:brennash/ThumbnailServer.git
</pre>
