[Video Link](https://youtu.be/q9-QXDvhKjI)

## Script

Intro: This LibreTime tutorial is for program managers and admins and highlights how to create smart blocks that will select tracks to fill the remaining time in a show to prevent dead air without scheduling tracks that will be cut off by the end of a show. To do this we will first focus on how to schedule show and station promos and PSAs at the end of every autoloading playlist using the outro playlist.

This tutorial builds upon previous tutorials highlighting how smart blocks can be used with autoloading playlists and podcasts to create automatically schedule shows. So you might find it helpful to view that one first.

We will assume that you already have autoloading playlists setup for various shows in your schedule and we will now focus on creating a playlist containing smartblocks that will fill the remaining time in your show. This means for instance that if you schedule a show with tracks that have a length of 54 minutes the system with automatically schedule only 6 minutes of tracks. In previous versions of Libretime and Airtime this wasn’t possible.

So we are going to assume that you have upload a number of tracks that have the Genre set to station promo for the purposes of this tutorial and now we will create a smartblock that will fill the remaining time of any show it is added to with station promos.

Click smartblock
Click the blue New button
and then type in the name of the smartblock – we will call it Fill Show with Promos
Now we select Genre and the modifier of is and then type in promo

Now under Limit to: we select time remaining in show

This will now automatically select a number of tracks that will schedule matching tracks until either there aren’t any new tracks to add or adding another track would cause the track to be cut off. This will help prevent situations where you have an announcement that is cut off by a new show beginning.

If you click preview it should show up to an hours worth of tracks that match the criteria.

Now lets say we also have a type of track called Public Service Announcements with the genre set to PSA that we want to also be considered for this mix of tracks.

Since this is also using Genre we click New Modifier and select is and type PSA

You can preview to see if additional tracks match your criteria below.

This will now fill the end of your show with promos and PSAs and you can start to sound like a real radio station but there are still issues we need to resolve.

One is that your promos and PSAs as selected randomly by the software might not match the time remaining exactly. For instance if you have only 25 second long promos and you have only 15 seconds of time remaining it won’t schedule any tracks because they would be cut off.

There are two ways around this. You can add a large number of short variable length tracks in a genre called bumper promos and this will greatly increase the chances that the algorithm will be able to fill as close to the time as possible but you may end up with the same short files playing frequently at the end of every show.

Another option which we will explore here is to have another separate smartblock for sound bridges that will be ambient type of sounds that won't jar the listener when they are cut off. This could be any sort of ambient music, sound effect or even nature sounds. The important thing from a listeners perspective is probably that there isn’t any spoken word parts or singing that could be cut off.

Make sure you save this smart block and we will create a new smart block called sound bridges.
We will select Genre is Sound Bridge
and then set Limit to time remaining in show.
And now click Advanced options and check the box next to “Allow last track to excceed time limit”.
You can preview and it should show you the tracks in your database that have the genre set to sound bridge. If you want to be careful to avoid dead air and have a limited number of tracks you can click allow repeated tracks as well. This might end up in the same tracks being played a few times but it will help prevent a scenario where you have dead air.

So now we have these two types of smart blocks we still need to have them automatically scheduled and we should have a reliable way of avoiding dead air in between externally sourced shows of variable length.

This can be done two ways. One they could be added individually to the end of a shows autoloading playlist or we can create a new playlist and assign it to the Outro Playlist so that it is automatically scheduled at the end of every show with an autoloading playlist.

To do this lets create a new playlist, type in the name “Outro Playlist”
Then click on Smartblocks and First Drag the Promo smartblock
and then add below it the Sound Bridge smartblock

Now save this smartblock. The order is important here because they are both competing to fill the show and the second one will always fill the entire show whereas the first one might have some gaps if the tracks dont line up exactly.

Now you have to be an admin currently to access this section but click Settings then General and then under Outro Playlist select the newly created Outro Playlist from this section and click Save.

And now every autoloading playlist show will have tracks scheduled to fill any potential dead air.
This process can be modified and there are future changes planned allowing each autoloading playlist to have a specific intro and outro playlist selected for it as well as the possibility of adding the intro playlist and outro playlist to every show even with manually scheduled tracks. This hasn’t been done yet so keep an eye on the LibreTime release notes for upcoming details.

And as always feel free to ask us questions at discourse.libretime.org, below or on our website.
Thanks for learning about LibreTime. In our next tutorial we will focus on how you create use smart blocks to schedule a random mix of musical tracks for your station and explore some more advanced details of smartblocks.
