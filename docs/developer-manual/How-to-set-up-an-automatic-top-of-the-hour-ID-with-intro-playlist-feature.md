[Video](https://youtu.be/XCXZyDBf4jc)

## Script

Intro: 
In this LibreTime tutorial I will explain how to use some advanced smartblock features to add random top of the hour station IDs to the beginning of shows with autoloading playlists.

First this tutorial assumes that you have watched the previous tutorial on how to setup autoloading playlists with podcasts, smartblocks and playlists. If you aren’t familiar with these concepts you might want to watch that one first.

So assuming you have shows with autoloading playlists in your schedule already you might want to add something like a top of the hour station ID to every show.

To do this we will start by defining a smartblock that will designate certain tracks as top of the hour station IDs. LibreTime is flexible in how you define this but for the purposes of tutorial we will use Genre to define this.

First click Smart Blocks then click the blue New button. A new Untitled Smart Block should show up in the right. If your screen is smaller resolution you will need to scroll down to see it.

Now for Name will type Top of the Hour Station ID. It is probably best to be explicit here so there is no confusion to other users of the system.

Now under Search Criteria we will select Genre for the modifier we will select is and then we will type TOTHID or short hand for top of the hour ID. You could type long form in here but it might be better to use a short hand in this case as any other users will need to match it explicitly and any typos would prevent their top of the hour IDs from airing. 

Now we will change the limit to items vs. hours and click preview.
I have already uploaded a few tracks with TOTHID as the genre and the smart block will select one at random.

Click save and you know have a top of the hour smartblock ID.

Now you might also not necessarily trust your DJs to create correct top of the hour IDs or you want to have some sort of vetting process so they need approval before they are added to the rotation. We can do this by adding an additional criteria. This step is optional but could be useful in certain situations. So we can Click New Criteria select Owner select is and type in Admin. You could also designate a special user or program manager login to handle these tracks.


This will mean that only tracks uploaded by the Admin will be selected. If we click save this will prevent top of the hour IDs uploaded by DJs from being selected unless an admin takes ownership over the track. I will show how you can do this to existing tracks in the next step.



If you want to record and add additional tracks you can upload tracks and edit their metadata so that the genre is TOTHID. 

We will upload a track now and go through these steps. Click upload find the file or drag one and then once it is done go to Tracks. It should be the latest item. When you are recording and exporting an mp3 you can usually set the metadata during the export process. If you do this it will automatically import with the right genre into LibreTime. If you didn’t do this ahead of time you can now click Edit – type in TOTHID for the Genre and click Save.


If you put Owner restrictions on your track so that only top of the hour IDs owned by a certain user would be selected from you can select that user as the new owner from the drop down list. Currently on Admins have the ability to change the Owner of tracks.

We have a shortened DJ specific guide that explains how to upload tracks and edit their metadata so that your DJs can learn how to do this without unneeded information. Check the description below for a link to it.

Now in order to add this to shows we can either add this Top of the Hour Station IDs Smartblock to an existing shows autoloading playlist or we can even set it to automatically be added to the top of every autoloading playlist through using a new feature called intro playlist.

To do this we need to create a playlist containing this smartblock.
Click Playlist then click New 
Type in the name of the playlist you want it to be.
Now click smartblocks on the left and it will list the smartblocks on your station.
If you don’t see the one you just added click Uploaded twice and it will sort them with the newest ones at top. Now drag the top of the hour station ID smartblock over to the right over to the right or click the checkbox and click “Add to current playlist” and it will be added. Now click Save and you will have a playlist that will always play a random top of the hour station ID.

Now to set a station wide autoloading playlist you currently need to also be an admin. So program managers will need to request this next step be performed by an admin for the time being. In the future we are considering creating a new settings section that program managers will be able to change the settings on. 

So if you can click settings. Click General and then go to Intro Autoloading Playlist and select the Top of the Hour station Id from the playlist list and click Save. 

Now everytime an autoloading playlist is scheduled the system will select a random top of the hour ID and insert it before any other content. 

You can also edit the show playlist itself and add this top of the hour smartblock before the content. So now for every show you automatically schedule you can be relatively sure that you will air the required station ID. 

Another cool thing about creating a special smartblock for this is that if you have DJs uploading individual tracks to their show they can easily add a station ID to their show just by adding the smartblock to the top of their show and it will automatically pull a random ID.

One big remaining challenge for automation that we haven’t addressed yet is that syndicated shows are of variable length and at this point we will potentially have silence after a show that doesn’t fill the full hour. We will cover some advanced smartblock features in our next tutorial that will explain how to use the outro playlist with smartblocks to find tracks to play in between shows without the risk of them being interrupted if they are too long to play in completion.