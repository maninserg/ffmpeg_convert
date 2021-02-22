# ffmpeg_convert

**About:** Python scripts for the more comfortable work with ffmpeg

<hr>

**Description:** 

There are 2 scripts:
1. ffmpeg_convert.py - for the batch converting files in the current directory
2. ffmpeg_info.py - for get the information about files in the current directory

Now the script "ffmpeg_convert.py" can make the following convertings:
1. .divx -----> .avi
2. .avi -----> .mpeg
3. .ts or .mts -----> .mp4
4. .mp4 -----> .mp4 with resize video stream

The script "ffmpeg_convert" automatically  defines types of input files and chooses method of converting with parametres from the script. In the process of the converting script make a subfolder for output files. 

You can use linux command sequences for two or more consistent convertings.
For example:
          `ffmpeg_convert.py -y; cd avi/; ffmpeg_convert.py -y`

<hr>

<b>Installation for Linux*:</b>

1. Clone the repository (or download the zip file and extract it):

    `git clone git@github.com:maninserg/youtube_downloader.git`
    
2. Go to the directory of the program:

    `cd <your name of directory>`

3. Create of a virtual environment

    `python3 -m venv .venv`
    
4. Activate the virtual environment

    `source .venv/bin/activate`
    
5. Install necessary packages using pip according to the requirements.txt file from a directory with the program
    
    `pip install -r requirements.txt`

<i>*The installation for MacOS or Windows can differ</i>

<hr>

**Screenshots:**

<p align="center">
  <img src="screenshots/ffmpeg_info_result.png"/>
<p align="center">The result table of ffmpeg_info.py's work"<p align="center">
</p>
