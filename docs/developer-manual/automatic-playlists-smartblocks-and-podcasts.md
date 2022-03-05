This page will provide a complimentary overview and rough documentation for how automatic playlists option in shows can be combined with smartblocks and podcasts to automate the syndication of shows. In addition it will provide a way of sketching out some unstructured documentation and brainstorming of ideas culled from the issue queue as well as documenting how the code works exactly.

# Automating Syndicated programming with LibreTime

For those of us in the talk and non-commercial radio sector, ie we play more than tracks of music, a primary source of programming is externally produced syndicated shows hopefully available via RSS feed.

Prior to the introduction of the auto playlist functionality and podcasts, this required a human to download and upload and schedule every show you wanted to air on your station. This can be a huge amount of work, and the point of automation is to automate mundane tasks like this right ?

So how to accomplish this task without too much human effort- enter the automatic playlist.

If you are getting your programming from a RSS feed (aka Podcast) here are the steps.

1. Find the RSS feed URL from your podcast provider and copy it into the clipboard
2. Go to Podcasts on Libretime and click Add
3. Paste the RSS feed URL and click subscribe (only once).
4. If the RSS feed URL is valid you should now see it listed on your Podcasts - Dashboard
5. Click the podcast name and the click View Episodes (you should then see a list of episodes)
6. Click the checkbox next to the newest episode and click Import (this will start a gray swirly under the imported tab showing that this is happening in the background, it usually takes a few minutes for the download to complete and you can navigate away at this point and let the software do its thing.
7. Verify the smartblock and playlist for the podcast were created. LibreTime should of created a Smartblock and Playlist automatically for you sharing the same name as your podcast. You can click the Smartblock or Playlist dashboard to confirm. If this didn't happen go to Settings -> General table and ensure these options are both checked Podcast Album Override and Podcast Automatic Smartblock and Playlist. If they aren't check them save and then delete the podcast and follow options 1-6 again.

## Schedule your Show

8. Click the Calendar tab on the left
9. Find the day/time of the week you are wanting to schedule your show and click there on the calendar (must be in the future, so if it is Tuesday and you wanted to add a show on Monday you would need to go to Monday of next week and click the screen). Alternatively you can click New Show at the top of the screen and this will show the Add Show dialog on the left.
10. Type in the name of your show and any description etc.
11. Check the Auto Schedule Playlist option under the Automatic Playlist tab. This will now show a drop-down list of every playlist in LibreTime.
12. Select the playlist corresponding with the name of the Podcast added above (your show will now be scheduled automatically an hour before this show is set to air)
13. Fine tune when this show airs and set-up repeats. Under the When tab click Repeats? and select the appropriate days of the week or month that it will air. (If you have trouble seeing this on your screen the scroll bar is on the far right side of the browser)
14. Add any additional customizations including a custom Color or Logo and click Add this Show at the top or bottom of the tab.
15. Your show is now set to air on a repeating interval with fresh content updated from the RSS feed but you aren't quite done yet (if you want to add a custom station ID or filler to deal with programs that run short of the whole hour)
16. Click Playlists
17. Find the Playlist that corresponds with the Podcast you just added and click the checkbox next to it and Click "Edit" on the toolbar above the listing of playlists.
18. You should now see it on the right hand side with one Smartblock listed. You can now click Smartblocks or Tracks on the left to add additional smartblocks into your shows playlist. For instance you might want to Add a station ID smartblock to the front of the show and/or a filler or promo smartblock on the end. To add them either check the box next to them and click "Add to Current Playlist" above or simply drag the smartblock onto the playlist on the right.
19. When you are done click "Save" and you are all done.

Enjoy the stress free automatic scheduling that LibreTime provides.

### A few caveats

At this point on the Calendar your show will still show a Red ! meaning nothing has been scheduled for it. We (the developers) still need to modify the functionality to tell the Calendar page that there is an automatic playlist and thus it won't be empty when the show starts.
