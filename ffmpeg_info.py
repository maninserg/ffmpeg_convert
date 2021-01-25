import os
from prettytable import PrettyTable

if 'info_tmp.txt' in os.listdir(path="."):
    os.remove(path='./info_tmp.txt')


list_items = []

for item in os.listdir(path="."):
    str_in_1 = item.replace(" ", "\ ")
    str_in = str_in_1.replace("\'", "\\'")
    list_items.append(str_in)
list_items.sort()

for item in list_items:
    os.system('ffprobe -i {} -show_format | grep "filename" >> info_tmp.txt'.format(item))
    os.system('ffprobe -i {} -show_streams | grep "codec_name" >> info_tmp.txt'.format(item))
    os.system('ffprobe -i {} -show_streams | grep "coded_width" >> info_tmp.txt'.format(item))
    os.system('ffprobe -i {} -show_streams | grep "coded_height" >> info_tmp.txt'.format(item))
    os.system('ffprobe -i {} -show_streams | grep "display_aspect_ratio" >> info_tmp.txt'.format(item))
    os.system('ffprobe -i {} -show_streams | grep "channels" >> info_tmp.txt'.format(item))
    os.system('ffprobe -i {} -show_streams | grep "channel_layout" >> info_tmp.txt'.format(item))
    os.system('ffprobe -i {} -show_format | grep "duration" >> info_tmp.txt'.format(item))
    os.system('ffprobe -i {} -show_format | grep "size" >> info_tmp.txt'.format(item))

list_files = []

f = open('info_tmp.txt', 'r')

for line in f:
    list_files.append(line)

list_files_clean = []
for item in list_files:
   it = item.strip('\n')
   list_files_clean.append(it)

list_files_del = []
for item in list_files_clean:
    it_list = item.split('=')
    it = it_list[1]
    list_files_del.append(it)
print(list_files_del)


list_files_table1 = []
i = 0
j = 10
for n in range(len(os.listdir(path="."))-1):
    list_files_table1.append(list_files_del[i:j])
    i += 10
    j += 10
    print(list_files_table1[n])

list_files_table = []
for item in list_files_table1:
    if len(item) != 0:
        list_files_table.append(item)

x = PrettyTable()
x.field_names = ["File", "Codec video stream", "Codec audio stream", "Weight",
                 "Height", "Ration", "Chanels", "Mono/Stereo",
                 "Duration", "Size"]

x.align["File"] = "l"

for i in range(len(list_files_table)):
    x.add_row(list_files_table[i])

print("\n" * 100)

print("Current folder: {}".format(os.getcwd()))
print("Count of files: {}".format(str(len(list_files_table))))
print(x)

os.remove(path="./info_tmp.txt")













