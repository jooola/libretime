[Video](https://youtu.be/0oqsgnR4cco)

Tutorial Script:
Intro: In this tutorial I will show you how to add a random underwriting spot following every top of the hour ID to provide acknowledgment to supporters of your station. Underwriting is a term dervided from non-commercial licensed radio in the United States and typically needs to avoid calls to action as well as the mentioning of prices. But be sure to check with whatever regulatory authority if anyone dictates how you can record underwriting. For web streams there generally aren’t any regulations that I’m aware of.

So the idea here is that we already have a top of the hour station ID set up with an Intro Playlist. If you missed this tutorial it may be helpful to watch this other one first. Or you can follow along either way.

This underwriting setup is based upon the idea that you want to select a random underwriting announcement from a single underwriter at the top of every hour. Every time an underwriter is added to the pool they have an equal chance of getting aired. If you are making promises to your underwriters that they will have their spots aired a certain number of times or during certain times of the day you will need to do this more manually by editing the individual show autoloading playlists and adding the underwriting announcement or if you have DJs manually uploading tracks or streaming live they will need to add this announcement themselves or mention it on the air while they are doing their show.

For the purposes of this tutorial we are going to create a smart block called Underwriting and then the genre will be set to is underwriting.

And we will limit to 1 item and preview it a few times and then save it and exit out.

Now we will add to this to the intro playlist we setup earlier.
Goto playlists and find the intro playlist, if you don’t have one you can create one now.
Now drag the underwriting announcement smartblock in here. Your intro playlist should probably start with some kind of station ID be it a legal or otherwise followed by this underwriting announcement.

Now lets go to settings and general and make sure that the intro playlist is set to your intro playlist.
Now every show will begin with a station ID followed by a random underwriting spot and then the content. You can increase the # of spots that are aired.

We are planning to add additional features such as individualized intro playlists for specific shows and a log where you can look up all of the times that a specific track aired in the past. This could be useful for sharing with your underwriters. If you are a web radio or commercial radio station then you could use this to track ads. Additional functionality is planned in the future so keep checking the forum at https://discourse.libretime.org, our website or our github repository at https://github.com/libretime/libretime
