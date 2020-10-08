## Turning off static noise from my laptop

My laptop is old. Very old. Four years and four months old, to be precise. And it makes this static,
buzzing noise whenever a CPU-intensive application is being ran. Whenever I want to watch a Twitch, 
a YouTube video, or participate in a Microsoft Teams or Zoom meeting, the buzzing sound starts up 
after about a minute (25 seconds in hot weather, when the AC is turned off). 

Fortunately, I found a fix to this problem. Right-click on the speaker icon, go to "Spatial Sound (Off)"
and click on "Off". But having to do this manually every 30 seconds is annoying, so I automated this 
process using PyAutoGUI. Yes, I can just buy a new SSD but its cooler to do it this way.


## Checking for new pacifist video

I really enjoy watching T-West's pacifist campaign runs in Age of Empires 2, where he completes 
entire campaigns and campaign objectives without killing a SINGLE enemy unit. If you sort his videos 
by popularity, 7 of the top 10 most popular are the pacifist videos entitled "Aoe2: Is It Possible
to Win the `X Campaign` Without Killing Enemy Units?"

Naturally, I look forward to the new pacifist video and wish to watch it as soon as its uploaded.
So I made a Python script that periodically checks every 10 seconds, using Google's YouTube API,
if the title of the latest uploaded video from T-West matches (partly matches) the specific kind of
video that I want to watch. If so, the script will stop checking and automatically open the new
pacifist video in my browser.

Google limits API usage quota to 10,000 queries per day. Using a "Search" API uses up 100 queries
per request but using a "Read" API on the latest uploads playlist only takes up 1 query per request.
I run the script when I wake up and close it when I sleep, so that's around 16 hours runtime or 5760
queries, well within the API quotas limited by Google without having to pay. An alternative way would
be to run the script on Google Cloud or other free cloud service, so it will be running 24/7 without 
having it in my computer background.

