[Video](https://youtu.be/TQ4mNfCw29I)

## Script

Intro: A guide to LibreTime settings for Admins

This LibreTime tutorial is focused towards site administrators who have installed LibreTime and want an introduction to the admin only settings. We will also focus on how to customize the streams that LibreTime provides and how to secure your Icecast instance. You will need to have admin permissions to a libretime instance to follow along.

First off login with your Admin login now click on Settings.
Click on General on this page you can customize various settings and add your station name and a logo that will show up on your radio page and on the top left of your installation.

See other tutorials for descriptions and information on the autoloading playlists and podcast settings.
In addition the TuneIn settings have not been tested and require getting special access from TuneIn for your station to test.

Most of these settings can be left alone. Under Dangerous Options you have the ability to wipe out your entire track library with a few clicks. This is a good reason to reserve admin access for people who really need it. So I would suggest that if your station is put together collaboratively you create logins for each user. To do this we will click Users

LibreTime has 4 different User Roles but mostly you will want to create DJs who are responsible for specific shows and can upload tracks and Program Managers who have the ability to edit the calendar and schedule all shows.

We will create an example program manager to give your imaginary friend larry the ability to help you get your station setup.
Click New User type in a User Name
and then the same password twice
and whatever information you want to add, the only other required field is Email and then under user type select Program Manager then click Save.

LibreTime doesnt send automatic notifications about new accounts created so you will need to relay this information to any users you create accounts for.

If you select DJ as the user type the user will only be able to upload their own tracks and can only schedule shows they are given permission to. See our tutorial on creating shows for more information.

Guest is basically a read-only view that can’t access the track library and can view past and upcoming scheduled content on the calendar.

Another important section is the Status Page.
If everything here has a green check mark here then it means that everything is working.

 Now we will explore the Streams section which is the most complex part of the admin and briefly talk about how to secure your Icecast setup which isn’t done by default if you installed from the install script.

Under Global you can enable Hardware Audio Output if you are using Libretime to feed an FM transmitter or otherwise want to create analog audio output. If you are doing this there are additional steps that might be necessary depending upon your OS.

You probably want to enable Auto Switch On if you plan on having you don’t want to require your DJs to take the additional step of toggling a the switch next to On Air after they connect to the stream.

Auto switch off will mean that your show will resume the playback of pre-scheduled shows after a DJ disconnects.

Otherwise you shouldn’t need to change any of the different settings unless your LibreTime instance is behind a firewall and you need to enable port forwarding.

Setting a login for master source username and password will provide anyone with this login the ability to broadcast over any existing show or even other live DJs who are using their show credentials. It should be used sparingly.

Now the important part. Default Streaming relies upon a hardcoded insecure password of hackme and so it should be changed before your station goes live.

In order to do this click Custom/3rd Party Streaming

Now you can type in the information here and change the bit rate. A higher bit rate will have better sound quality but will also require more bandwidth. LibreTime by default supports up to 3 streams.

Now you can play around with different settings here but by default icecast is installed on port 8000 and if you plan on using the Icecast server hosted by LibreTime then keep in mind the bandwidth that will be required to host listeners. If you were for instance hosting this off of a home or office internet connection rather than on a co-located or virtual private server if your station got popular enough it could negatively affect the internet connection for any other purposes. For a small hobby station with only a few listeners this could be fine but in general you might want to consider paying for a 3rd party icecast host or setting up your LibreTime instance in a datacenter or location with high amounts of bandwidth.

For the purposes of this tutorial we are going to assume that your libretime instance is using the built in libretime instance, the only thing that would change is you could put the hostname of a 3rd party server.

So this next step is important if you didn’t set up a new icecast2 password during the install process (this is next section will hopefully be outdated at some point). If you changed your icecast2 password you can skip forward and enter the new credentials otherwise I’m going to walk you through how to edit it from the command line) This is an important step because without it your libretime stream is insecure and anyone could in effect use your icecast stream and control the admin screen.

So we now we need to change the icecast2 config file. This requires actually modifying the underlying system config files if you are hosting your own libretime instance. So we are going to ssh into our server. This assumes that you have root or sudo credentials on the server you installed libretime. So go to a terminal on Linux or Mac OS X or use something like Putty.exe for windows and connect.
I will be connecting via ssh through vagrant for the purposes of this tutorial.

Once you have connected we are first going to back up and then edit your icecast config file
type
sudo cp /etc/icecast2/icecast.xml /etc/icecast2/icecast.bak
and then
sudo nano /etc/icecast2/icecast.xml
you might need to type in your password again. If it says permission denied you will need to check your credentials or otherwise type su and type in the root password. Once you have access to editing the file you scroll by using the arrow keys.

Be very careful when editing this file as deleting the wrong line or adding an extra unneeded character could cause your stream to not work.
We just want to change where it says “hackme” to a secure password – this can be a random string of characters or something that you will remember. You generally wont need to type this in again after you save the password in your stream settings.

If you are using nanoe and you want to try a shortcut you can hold the Ctrl button and then type W and then Ctrl and then R and it should pop up with Search (to replace): 
Type in hackme and then hit enter
now type in the password you want to use.
You can either click A for all or go through each change and confirm it. Basically you want to be sure you dont have hackme as a password anywhere.
Now you can save by holding Ctrl and then hitting the X
Type Y to save.

Now type 
sudo service icecast2 reload
and this will restart icecast with your new password.
This will also shut off your stream until you go back and type in the new password into the Output Streams setting of LibreTime
Make sure you click additional options and type the source password under password and then your admin username which is admin (unless you changed it) and the password you put in there.
You can also customize the Stream Name, description, genre and mount point.
Finally click Save click ok to the pop up and 
you will see a orange box that should turn green if you typed in the right credentials.

If something is wrong you will need to revisit the last steps via SSH and make sure the icecast.xml file wasn’t malformed.

To reset things back with the insecure password so you can try again you can type in
sudo cp /etc/icecast2/icecast.bak /etc/icecast2/icecast.xml
then
sudo service icecast2 reload

This will set your default password back to hackme and you should then proceed to try to change it to make it something secure.

One you have this changed you will also enable the ability to create different streams for instance a low bit rate mobile stream or connect to a 3rd party stream provider.

Once you are done with this if you have the proper Admin username and password you can go to Analytics and then click on Listener Stats and it should show a green OK under Stream Data Collection Status – this means that Libretime will be periodically querying your stream to see how many people are listening at a certain time and you can view these stats over time. 

And so that is all for this rather complex part of libretime setup. Keep in mind Libretime is alpha level software and so there are a lot of things that could be improved such as providing a better way to customize the icecast2 password. So if you are planning on running this as an admin prepare to be familiar with the discourse.libretime.org community and the github.com/libretime/libretime page and feel free to ask for help from the community if you run into any problems.

That concludes the LibreTime admin interface tutorial. We may do another tutorial that covers the actual install script and we might integrate the icecast change portions of this tutorial into that so feel free to gloss over that section if you have already done it. If you notice something other than hackme in your stream settings and the admin user and password filled in already then it is likely that we improved the install process. It is also possible that when you installed icecast2 you were asked to set a username and password. If that is the case then you can just type in what you changed it too.