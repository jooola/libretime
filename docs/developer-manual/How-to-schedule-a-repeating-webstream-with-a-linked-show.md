[Video](https://youtu.be/35mBGo9vYNo)

Tutorial Script:
Welcome to the tutorial on how to broadcast live with LibreTime and Butt

Intro: LibreTime is a radio station automation system designed to empower stations to collaboratively schedule their broadcast day. To do this the broadcast day is divided into different shows and specific DJ users can be given permission to schedule or broadcast during a specific timeframe by being given permissions to a specific show. In most cases LibreTime will be playing out pre-recorded tracks but it also has the ability to allow DJs to stream live remotely from the studio or anywhere with sufficiently fast internet access. The purpose of this tutorial is to show the basics of how to do this from the DJ point of view. If you are looking for how to upload and schedule tracks for your show you can see the previous tutorial in our DJ series. 

Streaming live requires that you have either a studio setup that allows you to mix music with your voice or that you use DJ software such as Mixxx that is configured to support both track playback and microphone input. For the purposes of this tutorial we are going to be concentrating on how to stream using the streaming software called Butt(Broadcast using this tool)with your audio setup preconfigured to route the sound you want to play through your soundcard.

The following description is based upon the default streaming configuration for libretime. If your administrator has changed them then you will need to get the information from them, but in general this should work.

First make sure you have butt installed, you will need version 0.1.17 or newer (previous versions had a bug that prevented them from working with LibreTime). You can see a link to the butt webpage below that contains download links below.

Once you have butt installed you will need to have a dedicated soundcard setup and connected to your mixer. Now we will go in and get butt configured to broadcast directly to LibreTime.

Open up butt – and click settings
now you will need to add your server – if you are using a shared studio computer but have different logins for each DJ then you might already have your server listed here in this case you can click edit.
You can also add a specific one for your sure but the settings will save your password and anyone with access to this computer will be able to stream during your show by selecting this.

Otherwise click add to add a new show.
On this screen we type LibreTime in the name 
Next we click IceCast 
Then under Address the weburl of your libretime install. Next we will put port 8002 as this is the default port for show users
Next for password type in the same password you use to login to libretime
under IceCast mountpoint type in /show
and under IceCast user type in your libretime user name.

Next we will click Audio and be sure that the soundcard your mixer is plugged into is selected under the Audio Device drop down. If you are using a USB mic and don’t see it or need to plug it in – try unplugging it and then closing and starting butt up again and see if it shows up.

If you are using a USB microphone you might need to select Mono for the channel in order to use it.
Now hopefully you are all setup.
To get started with your broadcast click the play button under the main butt window. Note: you will only be able to connect during the time your show is scheduled. The easiest way to time this is to login into Libretime and wait for it to show that your show is airing and then click play.

You can also record a copy of your show by clicking the record button, The butt settings has a menu where you can setup the record. By default is is a mp3 based upon your the date and the time in your default home or user directory.

Since LibreTime doesn’t currently record shows that are streamed this is your best bet if you want to later archive your live show so listeners who didn’t tune in can catch up later with it.

You can confirm that you are broadcasting from the dashboard under source streams it should show a orange light and the on air button should be lit up. There is a orange tab that you can slide to turn off the stream and resume the broadcast of what is previously scheduled to air. Depending upon the buffer setup by your admin there may be a delay from when you click connect and your audio starts to play on the stream.

If you have a problem connecting check with your system administrator to make sure that the settings are properly configured and that you have been given the right DJ access to your show.

There is also a master source login that is capable of overriding every show. This can be used if you want to setup a computer capable of overriding any show broadcast in your main studio. In general this login shouldn’t be given out as it provides the user with the ability to override another DJs show.