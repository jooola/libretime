[Video](https://youtu.be/4TZT3UHeXcU)

## Script

Intro: Welcome to the Libretime Tutorial series. 

This tutorial will describe how to install LibreTime from the latest code on github.

Before we get started you will need a VPS(virtual private server) or physical server running Ubuntu 18.04. These instructions should also work with Ubuntu 16.04 as well. We are working on supporting the latest version of Debian but there are still some issues with certain packages so we recommend using Ubuntu 18.04 at this point.

It’s also important that if you are using 18.04 you either install from alpha.7 release or later or directly from git as the release includes important changes to php. Keep in mind LibreTime is still alpha level software but we have a community working on it constantly and striving to make it as easy to use as possible.

We also recommend that you install LibreTime on a dedicated server rather than sharing your server with another purpose. This is because the install script requires multiple services running and modifies apache. Also the install only supports a single instance of LibreTime on a server. 

With this in in mind you will also need sudo or root access to your server and you will need to connect via ssh.

If you are just trying to use LibreTime to test it out as a developer you can use vagrant. Check out our developer tutorial and the documents on libretime.org manual for more directions for how to get this setup. I will be using a vagrant box to record this screencast.

To run Libretime your server will need1GB or more of RAM and at least 10GB or more of storage for the OS and file storage.

You also will probably want to point a domain at your new server so that people can access it aside from the IP address. We are going to assume that you have this setup before you get started. 

So lets ssh into our newly created VPS.
Lets make sure that we have root permissions type sudo su
then type in your password. You should now be root. 
You can type exit and hit enter to go back to your regular exist
Next lets make sure we have git installed
type
sudo apt install git
after this either downloads or confirms that you have the latest version its never a bad idea to make sure your system packages are up to date before you start installing software
type sudo apt update (ENTER)
this will query the ubuntu server to get the latest packages
then
sudo apt upgrade (ENTER)

This will update your system software and may require an reboot or confirmation. Take care of this and then we will get started installing libretime

Now for the fun part 
type 
git clone https://github.com/LibreTime/libretime.git
this should download it from github and now
after this is done we will star thte install process
cd libretime (ENTER)
and 
sudo ./install -fiap (ENTER) this will start to install everything without asking you any questions
this should install and download all of the required packages to run libretime and should pop up at the end with the domain name that your server was configured with and a URL you can use to finish the install
its downloading the zf1s framework which is a fork of zend framework modified to support php 7.2 and above
now it is downloading the python packages which we use as some of the glue to tie the various parts of libretime together
now it is generating the locales and we are almost done

Go to the URL and you should see Database Settings – you shouldn’t need to change any of these settings.
Now you will probably want to change the rabbitmq settings on a production installation by default it is airtime airtime
So go back to your ssh terminal and type
sudo rabbitmqctl change_password airtime TYPEANEWPASSWORD
then replace the asterisks with the new password you typed and click next

For the URL here type in the URL you want people to be able to publically access your libretime system via. This will be automatically populated by the URL provided but if it is incorrect or you want to use something else here you can change it. The default part for web servers is port 80 so you shouldnt customize this unless you know what you are doing. Now click next.

The default setting of /srv/airtime/stor shouldn’t be changed unless you have a specific need here. There have been reports of alternate directories not working and you will need to make sure that the www-data user and group have permissions to any directory you change here. Click next and now you have the final steps to get your system up and running.

Copy and paste the various commands into your ssh window or type them manually ctrl shift V

sudo service airtime-playout start
sudo service airtime-liquidsoap start
sudo service airtime_analyzer start
sudo service airtime-celery start
Now you can go to your LibreTime install.

If everything is green and you see Login to Airtime! It was a success (note to self change that to LibreTime)
Click the button and you can login with the default user name password admin admin
You definitely will want to change the admin password immediately.

I also recommend immediately following the next tutorial linked below that introduces the Admin settings which includes how to change the default password for icecast2 and configure custom streams. Without doing so your LibreTime instance will be vulnerable.

Once you do that you should be able to get started running LibreTime by following the various tutorials listed below or just logging in and playing around until you figure it out.

Either way the LibreTime community is usually happy to answer questions at https://discourse.libretime.org and respond to feature request or bug reports at https://github.com/libretime/libretime

Let us know and thanks for trying LibreTime out.