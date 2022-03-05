This is a rough outline of LibreTime and documentation of how the application functions - anyone is welcome to edit it with details from a walkthrough of the code but it will be lacking breadth until this happens for most parts

# Playlists

How playlists are added to shows

- Via UI ->

1. an Ajax call is sent to the ShowBuilder controller w/ json containing $mediaItems listing what is to be added and $scheduleItems the existing file it should schedule after
2. scheduleAddAction is called defined via addActionContext ('schedule-add')
3. a new Schedule is instanced and scheduleAfter is called w/ the item parameters from above $adjustSched is set to true by default and is always true in all uses in the codebase (yet is still passed)
4. insertAfter runs in the schedule - the filesToInsert parameter is always null (unless being called by moveItem w/ uses it) and this is explicitly cleared unless the $moveAction parameter is also called ) this results in a forLoop retrieiving the mediaItems with retrieveMediaFiles
5. retrieveMediaFiles - branches based upon 4 types (audioclip, playlist, stream, and block)
6. for playlists A new playlist object is constructed based upon the id and getContents is ran
7. getContents is a gnarly SQL query that results in an array of Rows gets the entire playlist as a two dimensional array, sorted in order of play.
8. If it's type 2 item it's a block and then it looks through the content (if it's static otherwise it pulls dynamic files which pulls getListOfFilesUnderLimit
9. GetListOfFilesUnderLimit -> first gets a list of files that meet the criteria which creates a PropelOnDemandCollection based upon a SQL query determined by the Criteria set the list of files under limit is added to an InsertList until the algorithm criteria for the block being full is finished.

- Types - stored in the Type field in the database - type 0 is a playlist with only media files

Library

The library shows "all" of the files in the database.

1. It uses a javascript library called datatables and we are currently dependent upon a legacy version that has been customized by previous developers. Most of the custom library code is in the js/airtime/library/library.js file.
2. It does a ajax query to Library/contents-feed which is part of the LibraryController.
3. This calls the searchLibraryFiles function on the StoredFile object and does some query building it calls DataTables.findEntries
4. findEntries adds the WHERE clause to the query with the AdvSearch and cycles through the terms and returns an array of matching tracks.
