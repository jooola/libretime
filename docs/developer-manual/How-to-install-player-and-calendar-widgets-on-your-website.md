[Video](https://youtu.be/woTokbFVFo0)

Tutorial Script:
Intro: This LibreTime tutorial is intended for people who are setting up the radio station website and want an introduction to how you can use the LibreTime player widget to add a libretime player and calendar to your website.

When you first go to your libretime instance you will see the radio page. Essential the widgets all you to embed the schedule and player from this page on to different web pages using something called an iframe.

So login. 
And now click on Widgets
The Player will be selected by default.
You can change the Title but you will need to click select a stream for the changes to be applied to the embeddable code. 

Now copy the embeddable code to your clipboard.

The next part will require you to have access to your stations website to add the code.
For the purposes of this tutorial we will just create a HTML text file.
Open up a text editor on your operating system and type in <html>
then paste the code and finally type </html>

Now save it somewhere on your computer as radio.html
Now you can open this file with your web browser and it should play your station.
The web player currently relies upon Flash in some cases and could use some improvements. It also might run into issues if your web site uses https:// and your libretime instance does not.

Most likely you will be adding this code to your existing station website or relying upon the libretime radio page as your home page.

Now we will do the same with the schedule.
Go back to your Libretime page and click Weekly Schedule and then copy and paste the embeddable code.
Now we will open up the radio.html page and paste this code below the other code.
And save it.
Now you will see your schedule.
These widgets rely upon your station libretime instance being publicly accessible to the web through a common URL.

The Facebook widget doesn’t currently work and would require you to setup an App Id and possibly debug the code. We might remove it from future versions if nobody spends the time to test and make it working.

Another section of LibreTime that could use some more work is the Station Podcast module under My Podcast. It currently doesn’t work as of the time of this tutorial and we suggest that if you are looking to host a podcast for your station you look into a 3rd party situation or spend some time contributing to test the podcast code.

	