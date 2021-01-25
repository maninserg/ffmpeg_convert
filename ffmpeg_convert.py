import os

list_in =[]

for item in os.listdir(path="."):
    list_in.append(item)
list_in.sort()

for item in list_in:
    str_in_1 = item.replace(" ", "\ ")
    str_in = str_in_1.replace("\'", "\\'")
    if str_in.endswith(".divx"):
        """ Convert .divx --> .avi and fix bag divx with B-frames
        More info: https://forum.kodi.tv/showthread.php?tid=332945&page=12"""
        if not "avi" in os.listdir(path="."):
            os.mkdir("avi")
        str_out = "./avi/{}.avi".format(str(str_in.split(".")[0]))
        str_name = "{} -------> {}".format(str_in, str_out)
        print("\n" * 3)
        print("*" * len(str_name))
        print(str_name)
        print("*" * len(str_name))
        print("\n" * 3)
        ffmpeg_comm = ("ffmpeg -i {} -codec copy -bsf:v mpeg4_unpack_bframes {} -y".format(str_in, str_out))
        os.system (ffmpeg_comm)
    elif str_in.endswith(".avi"):
        """ Convert .avi --> .mpeg
        More info: https://nomone.com/2016/10/12/converting-videos-to-run-on-old-divx-devices/
        """
        if not "mpeg" in os.listdir(path="."):
            os.mkdir("mpeg")
            str_out = "./mpeg/{}.mpeg".format(str(str_in.split(".")[0]))
        str_name = "{} -------> {}".format(str_in, str_out)
        print("\n" * 3)
        print("*" * len(str_name))
        print(str_name)
        print("*" * len(str_name))
        print("\n" * 3)
        ffmpeg_comm = ("ffmpeg -i {} -vf scale=720:480:decrease -c:v mpeg4 -vtag xvid -qscale:v 5 -c:a libmp3lame -qscale:a 5 {} -y".format(str_in, str_out))
        os.system (ffmpeg_comm)
    elif str_in.endswith(".ts") or str_in.endswith(".mts"):
        """ Convert .ts or .mts --> .mp4
        More info: https://stackoverflow.com/questions/42432898/live-tv-recording-ts-to-mp4-with-ffmpeg
        """
        if not "mp4" in os.listdir(path="."):
            os.mkdir("mp4")
        str_out = "./mp4/{}.mp4".format(str(str_in.split(".")[0]))
        ffmpeg_comm = ("ffmpeg -i {} -c:v copy -c:a aac {}".format(str_in, str_out))
        os.system (ffmpeg_comm)
    elif str_in.endswith(".mp4"):
        """ Resize strem video for mp4
        More info: https://trac.ffmpeg.org/wiki/Scaling
        """
        r_factor = input("input resize factor:")
        if not "resize_{}".format(str(r_factor)) in os.listdir(path="."):
            os.mkdir("resize_{}".format(str(r_factor)))
        str_out = "./resize_{}/{}".format(r_factor, str_in)
        ffmpeg_comm = ("ffmpeg -i {} -vf scale=iw*{}:ih*{} {}".format(str_in, r_factor, r_factor, str_out))
        os.system (ffmpeg_comm)



"""
For test the first 30 sec: -t 00:00:30

------------------------
Convert .avi -----> .mp4
------------------------
001 way

ffmpeg -i file.avi -c:v libx264 -strict experimental -c:a aac  -preset medium  -profile:v high -level 4.2 -r 24 -g 24  -ac 2 -movflags faststart -threads 0 file.mp4

ffmpeg -i file.avi -c:v libx264 -strict experimental -c:a aac  -preset fast  -profile:v high -level 4.2 -r 24 -g 24  -ac 2 -movflags faststart -threads 0 file.mp4

More info: https://qna.habr.com/q/271888

https://superuser.com/questions/603289/getting-error-unknown-encoder-libvo-aacenc

002 way

ffmpeg -i input.avi -acodec copy -vcodec copy output.mp4

More info: https://stackoverflow.com/questions/48487313/how-to-process-a-video-to-mp4-with-ffmpeg-for-quality-and-compatibility

"""

