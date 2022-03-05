[Video](https://youtu.be/cWYMQqEHXVc)

## Script

Intro: In this LibreTime tutorial intended for Program Managers I will introduce both the concept of Podcasts and the Auto-loading Playlist to automatically schedule tracks in shows an hour before they are set to broadcast.

First I want to introduce the concept of podcasts and how they can be integrated with LibreTime, Podcasts allow you to have your LibreTime instance automatically download the latest show content from a show with a podcast feed also known as a RSS feed.

For the purposes of this tutorial we will add the Democracy Now podcast. So we need to get the URL (web address) from their site and copy it into our clipboard. All podcasts have an RSS feed but some shows don’t advertise it as openly as their iTunes link. You should be able to contact the publishers of any show you have permission to air and get their RSS feed. Now we will go to our libretime instance.

Click on Podcasts and then click the blue Add button and then past the feed URL and click Subscribe.

Now will generate a smartblock and playlist for this podcast so that we can add it to be automatically scheduled.

Click the show and then click edit, you can also double click it.
Now on the right a window should be open for your podcast.
If you want to change the name of the podcast you can do this here.
Now click Generate Smartblock and Playlist.
This will create a playlist containing a smartblock that will contain the newest episode of this show.

We also want to make sure that we download the latest episode right now. New episodes will be downloaded automatically if the “Download latest episodes” box is checked but this happens periodically and so we want to make sure we have the latest one right now. So we click the checkbox and then click import.

This will happen in the background and so we can navigate away. Podcasts are hosted externally so it can sometimes take a few minutes or more for the download to happen and for the track to be ingested.

Now we are going to add this show to an autoloading playlist so that it can air automatically every day with the latest episode.

So we can click on Calendar and we will have this Democracy Now air every week day at 11am. Type in the name, and then click In The Future for the start time and click repeats and select Monday through Friday by checking the box next to them.

Now the magic part comes in. Click the drop-down next to Autoloading playlist and then check the box next to Add Autoloading Playlist. Now we select the playlist we want to schedule automatically from this list. We are going to leave “Repeat Playlist Until Show is Full” for now as we only want our show to air once rather than start again and be interrupted part way through.

Now click Add This Show and it should be added to your Calendar. One hour before your show is set to air the latest podcast will be added. Now lets go and peek behind the scenes and see how the smartblock works to make this happen.

Click on SmartBlocks and then click on the Smartblock named Democracy Now! Audio
then click Edit. You will see the search criteria matches on the Album. This is because the Album is automatically changed to the podcast name for each track downloaded from the podcast. And it is limited to one item.

You can click preview and it should show the latest episode we just set to download.
Now lets peak under advanced options.

Under sort Tracks it says newest, by default smart blocks are set to random but for the purposes of podcasts we usually want to air the latest one. If new episodes aren’t being generated but you still want to air this show on a regular basis and you have already downloaded a number of tracks you can change this to Random and it will select different shows. Click on preview a few times and it should show a randomly selected track.

In doing so I noticed that one of the shows was substantially shorter than the rest. It might be the case that your podcast contains extra content that shouldn’t be treated as a full show. This could cause issues with your listeners and so in this case we will add an new criteria to the smartblock so it only pulls tracks longer than 55 minutes long since full episodes are always this long while the shorts added to the podcast are not.

So we will click New Criteria → Select Length and then is greater than for the modifier.
Time lengths are typed in as hour colon minutes : seconds – so we will type in 00:50:00 and click preview. It substantially shortened the number of tracks that were set to air and helping us to avoid a scenario where only a short segment aired instead of a full show. You probably won't need to do this for most podcasts but tricks like this can help you maintain your stations schedule without needing manual intervention. As you probably saw there are a lot of different Criteria that you can match on and so the possibilities are pretty boundless. We will explore this in more depth in a future tutorial but for the purposes of this one we can make sure we change sort tracks back to Newest and save it.

We are going to now go to playlists and see how it works with smartblocks.
Click on Playlists and then click on Democracy Now! And you should see the Democracy Now smartblock showing you can click Expand Dynamic Block to see what the search criteria is.

Lets say that you had a station specific introduction you wanted to always air for this show. You could add it to this playlist and it would also be scheduled along with the latest episode. This is a good way automate the scheduling of PSAs and also play station IDs. In the next tutorial we will introduce the concept of intro and outro playlists (a recently added feature) that allow you to automatically schedule tracks before and after autoloading playlists on a station wide basis. For right now though if you want to add any specific tracks before or after a podcast editing this specific playlist is the place to do it and you can click Save.

Now if you go back to the Calendar you should see the show you setup and instead of a red ! Mark it has a time clock to indicate that it is setup with an autoloading playlist. Currently the playlists are set to have their schedules built an hour before the show airs but we might add an option to customize this in future versions of LibreTime.

There are also additional settings that you might be interested in knowing about under Settings. You will also need to be the station Admin to access this and you won’t see it if you are just a program manager but I’ll briefly show these settings. In the future we might be moving these into their own section but click Settings and then General and if you scroll down you should see Overwrite Podcast Episode Metags which is enabled by default and Generate a smartblock and a playlist upon creation of a new podcast which is disabled by default. If you enable this whenever you add a podcast it will automatically create the smartblock and playlist based upon the playlists name and so you won't need to click on edit and “generate smartblock and playlist”. This might be useful if you plan on adding a lot of playlists at once but is up to an admin to introduce. Above you can see Intro Autoloading Playlist and Outro Autoloading Playlist – these sections will be the focus for our next tutorial.

So in this tutorial we showed how you can use Internet Podcasts to automatically download content from the web and then air the newest episode automatically in LibreTime. If you have any questions you can ask questions in the comments below or at discourse.libretime.org. Thanks for watching and tune in to the next tutorial soon.
