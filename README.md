# FFmSlide
Podcasts are great, but they aren't all that conducive to cramming before a test.
Let's change that.

## Dependencies
Obviously, Python. Additionaly, FFmSlide requires ffmpeg be installed. You can find tutorials and binaries online. 
If you're a member of the OSX master race, you can install FFmpeg using Homebrew. 
```
brew install ffmpeg
```
If you don't have Homebrew, get on it son. If you're using Linux, well, you should know what to do. 
Check your package manager and kiss your FOSS ideals goodbye with these codecs. Windows... good luck. 
I know it works, but I can't tell you how.

## Installation
Download and unzip or clone the repo. Install the Python dependencies. 
```
sudo pip install -r requirements.txt
```

*DELETE THE DELETE_ME FILES IN SLIDES AND LECTURE_VIDEOS*

Seriously. I'm a lazy programmer, so it's all up to you.

Download the lecture podcasts from the UCSD ACMS podcast site, and place them in the appropriate folder. 
I'm not telling you which that is. It's up to you to figure it out.

I also suggest you rename them appropriately, such as "lect-1.mp4", "lect-2.mp4", and so on. The file names
determine the subdirectories in the slides folder later on.

## Usage
```
python FFmSlide.py
```

Slides magically appear in the slides folder under the appropriate subdirectory.

## Caveats
Prof. Garo Bournoutian was kind enough to allow me to distribute this program. UCSD lecture videos and the slides
contained therein are property of UCSD, so the sending of said files would most definitely fall under the category
of distribution of copyrighted material. Don't be an ass and make Garo regret allowing us to share this program.

TLDR; Don't share the slides or lecture videos anywhere.

This script is in no way affiliated with UCSD. If you any issues (which you will, some of this is a bit of a shoddy
rush job before the quiz) contact me via GitHub issues or email/Google Hangouts me at chriskweller@gmail.com 

I have no life. I'll respond.





