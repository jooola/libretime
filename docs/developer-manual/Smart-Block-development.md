This is kind of a scratch page to explain how smartblocks currently work outside of the documentation and to share some ideas regarding possible modifications. 

The reason I'm creating a wiki for it is because I plan on doing things like explaining both the backend PHP coding way it is setup and also outlining the various feature requests we've had.

## Feature request notes
These came from a WCRS-LP & WGRN-LP meeting with 2 station producers who have been responsible in the past for scheduling everything via Airtime and are providing feedback as to how the functionality could be improved. As of now no "issues" have been opened for these this is a raw note dump. 

* Create a limited playback function that would play a track for X # of minutes and then cut off if it went over. Useful for insertion of spots onto the end of a show but not necessarily.
* If Else smartblock scheduling. Basically if a smartblock is empty then schedule another smartblock instead. This would be useful for the case of repeating shows where there isn't a episode uploaded in the last week. You could then instead opt to include a random show or select from a pool of evergreen shows.
* Regex based string matching for criteria
* Make a smartblock that is limited to the time remaining unscheduled in a show. This would be a truly smartblock that would expand to fill any dead air remaining in a show vs. requiring a preset x # of items or x # of minutes without repeating the whole playlist. - see [this PR](https://github.com/LibreTime/libretime/pull/605)
* Get rid of static smartblock because it isn't very useful and replace it with the ability to create a playlist based upon the smartblock. Smartblocks could then be used as playlist generators but would remain a set of criteria.
* Add an option for the smartblock to Offset the choice of tracks by X # of items. This would be useful in the case of smartblocks sorted by "newest" or "oldest". One producer schedules the newest show followed by the previous weeks show. There is no way of doing that currently with the sort options as they stand.
* Prevent the repetition of tracks within smartblocks that are all under the same show - this would allow for more flexible playlists that don't repeat themselves - but might be tricky to program

## Added to the issue queue from the above list
* Add a preview tracks button that will display tracks meeting current smartblock criteria to avoid the need to set a block to static and click generate to "preview" it. [issue #363](https://github.com/LibreTime/libretime/issues/363) 
* Re-enable the display of the number of items that meet the criteria. This code was for some reason disabled in the version of airtime our code is based off of but still exists in the codebase. [issue #366](https://github.com/LibreTime/libretime/issues/366)

## Additional feature requests pulled from the issue queue
* Prevent a smartblock from scheduling the same track one after another even when allowing duplicate smartblocks [issue #326](https://github.com/LibreTime/libretime/issues/326)
* Provide a mechanism to splice multiple smartblocks together by inserting a different smartblock every X # of items [issue #335](https://github.com/LibreTime/libretime/issues/335)
* Provide Import/Export functionality for Smartblocks -[Issue #94](https://github.com/LibreTime/libretime/issues/94)
* Make smartblock matching criteria break on specific words vs. matching phrases internal to words [Issue #63](https://github.com/LibreTime/libretime/issues/63)

# Collections vs. Smartblocks (ie the future of smartblocks)

The idea has been floated that it might make sense to rethink the way smartblocks are built to separate the # of items and order from the actual criteria. The central focus being the creation of a "collection" which would consist of a saved set of criteria that designate tracks. This would allow the filtering of the tracks table based upon whether it was in a Collection. For instance if you setup a collection called "Station IDs" there would be a drop down menu available from the tracks page called "filter by collection" and if you select Station IDs, it would only show all of the tracks that meet that criteria.

The advanced search criteria available via the drop-down triangle on the right of search bar was also unknown to the users of LibreTime and could help filter the tracks if it was known and included all of the potential fields you might want to filter by.

The idea was discussed as to whether the smartblock should be modified to select from a specific collection vs. including the criteria below the page. Or if the criteria could also be used to designate "in collection X" as another one of the fields. At this point in the discussion the idea was muddled enough that there was no consensus on the best way forward and it was agreed that the existing functionality should be improved as the low-lying fruit vs. overhauling the setup in a way that would add further confusion.

