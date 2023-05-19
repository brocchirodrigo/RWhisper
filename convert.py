import subprocess


def convert(locale_file, new_name):
    subprocess.run("ffmpeg -i {} -map 0:a -b:a 20k -acodec libmp3lame {}".format(locale_file, new_name), shell=True, capture_output=True)
