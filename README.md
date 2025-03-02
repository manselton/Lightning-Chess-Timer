# Lightning-Chess-Timer

*** Update: The Windows executable is extremely slow to load. As a hobbyist I have been unable to overcome this. I can only suggest that if you wish this little program to run well on Windows then you should do the same as any Linux/BSD user would. Install Python from https://www.python.org, install the python module installer pip and then the module pygame. The file lightning.py will then run smoothly with a double-click. ***

A simple gui to play a 3 second foghorn every 5-30 seconds.

Lightning Chess is nominally playing chess at 10 seconds per move. The present little program was made to facilitate this for my local club, Morriston Chess Club, and the West Wales Chess League. Previously we used a very old, hissy tape on an ancient full size tape player. I had a small shell script which ran from my laptop using a 3 second clip.

However, I was the only one happy to run with this as everyone else used Windows and needed a gui. So I decided to try to write one in Python. After a year, on and off, I finally got it working to my satisfaction. By chance I met Jack that week and he really put some polish on it and generated a Windows executable. The time setting is user-adjusted and includes the time of the foghorn. So the time displayed is the time between moves or the time between foghorns.

If you have Python 3 installed and the pygame module this gui will run from the source code. You need to have foghorn.mp3 in your path or the same directory as the executable. We hope you find it useful.
