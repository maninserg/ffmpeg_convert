# ffmpeg_convert

**About:** Python scripts for the more comfortable work with ffmpeg

<hr>

**Description:** There are 2 scripts:
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

<p align="center">
  <img src="screenshots/ffmpeg_info_result.png"/>
<p align="center">The result table of ffmpeg_info.py's work"<p align="center">
</p>
