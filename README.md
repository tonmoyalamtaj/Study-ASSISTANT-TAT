# Study Assistant-TAT
#### Video Demo: https://www.youtube.com/watch?v=Ix6zPkfnOcc
#### Description:
Study Assistant-TAT is a youtube link manager for students. By this Project Anyone can store their Youtube link ,download that link and give title for their youtube link so that they can easily recognize the link. Users can access that youtube link by that's index. BUT REMEMBER THIS PROJECT ONLY WORK FOR YOUTUBE LINK.

## HOW TO SETUP

##### 1. Clone or Download the Project:

   Download the project files to your computer.

##### 2. Install Required Libraries:
   Open your terminal in the project folder and run:
   #### Terminal:
        pip install -r requirements.txt
##### 3. Now write this in the terminal:
###### But make sure you are in the project folder.
#### Terminal:
    python project.py

## HOW TO RUN
##### Step - 0
Atfirst you need to install some libraries to install it run this command in your terminal.
### Terminal:

##### Step - 1
By opening this project user's can find that's kind of interface.

#### Terminal:
    1.Inject any link
    2.open any link
       Please Enter your choice: 
### Now at first press 1.
##### step - 2
After that you can find like this
#### Terminal:
    1.Inject any link
    2.open any link
        Please Enter your choice: 1
    Enter your youtube vidio link: 
### Now give that valid link that you want to save
Now you can find this kinds of view:
#### Terminal:
    1.Inject any link
    2.open any link
        Please Enter your choice: 1
    Enter your youtube vidio link: https://www.youtube.com/watch?v=dWCk8wdvXPA
      ___  _    
     / _ \| | __
    | | | | |/ /
    | |_| |   < 
     \___/|_|\_\
            
    :) Your Program is running. :) 
    Enter your youtube vidio title:
##### step - 3
Now enter the title that you want. But remember this title is the representative of that link.
#### Terminal:
    Enter your youtube vidio title: CS50 Final Project
    OK
    Are you want to download this link[y/n|]:             

##### step - 4
Now if you want to download that vidio you can press y other wise you can press enter,n or what ever you want. If you press [y] the vidio will be download on that folder where you python file is. And After downloading you can take that vidio in another file location. 

And if you don't press y the vidio will not download but but that vidio link will be saved in (link_data_base.json). This is your dictionary where your data will be stored in json formate (javascript Object Notation) this file works like a python dictionary.
##### If you want to save that vidio which link you recently gave:-
#### Terminal:
    Are you want to download this link[y/n|]: y
<details>
    <summary><b>While downloading a vidio, you might see some text like this, this is normal, these ase messages from yt_dlp and ffmpef, these is no problem.</b></summary>

```bash
Are you want to download this link[y/n|]: y           
[youtube] Extracting URL: https://www.youtube.com/watch?v=dWCk8wdvXPA 
[youtube] dWCk8wdvXPA: Downloading webpage 
WARNING: [youtube] No supported JavaScript runtime could be found. Only deno is enabled by default; to use another runtime add  --js-runtimes RUNTIME[:PATH]  to your command/config. YouTube extraction without a JS runtime has been deprecated, and some formats may be missing. See  https://github.com/yt-dlp/yt-dlp/wiki/EJS  for details on installing one 
[youtube] dWCk8wdvXPA: Downloading android vr player API JSON 
[info] dWCk8wdvXPA: Downloading 1 format(s): 137 
[download] Destination: t.mp4 
[download]   0.0% of   31.01MiB at  Unknown B/s ETA Un
[download]   0.0% of   31.01MiB at  203.13KiB/s ETA 02
[download]   0.0% of   31.01MiB at  473.96KiB/s ETA 01
[download]   0.0% of   31.01MiB at 1015.64KiB/s ETA 00
[download]   0.1% of   31.01MiB at    2.05MiB/s ETA 00
[download]   0.2% of   31.01MiB at    2.15MiB/s ETA 00
[download]   0.4% of   31.01MiB at    2.52MiB/s ETA 00
[download]   0.8% of   31.01MiB at    1.95MiB/s ETA 00
[download]   1.6% of   31.01MiB at    2.31MiB/s ETA 00
[download]   3.2% of   31.01MiB at    1.99MiB/s ETA 00
[download]   6.4% of   31.01MiB at    1.85MiB/s ETA 00
[download]  12.0% of   31.01MiB at    2.01MiB/s ETA 00
[download]  19.2% of   31.01MiB at    2.22MiB/s ETA 00
[download]  28.0% of   31.01MiB at    2.81MiB/s ETA 00
[download]  31.9% of   31.01MiB at    2.49MiB/s ETA 00
[download]  31.9% of   31.01MiB at  Unknown B/s ETA Un
[download]  31.9% of   31.01MiB at  Unknown B/s ETA Un
[download]  32.0% of   31.01MiB at  Unknown B/s ETA Un
[download]  32.0% of   31.01MiB at  Unknown B/s ETA Un
[download]  32.0% of   31.01MiB at    1.60MiB/s ETA 00
[download]  32.1% of   31.01MiB at    1.77MiB/s ETA 00
[download]  32.3% of   31.01MiB at    2.99MiB/s ETA 00
[download]  32.7% of   31.01MiB at    4.39MiB/s ETA 00
[download]  33.5% of   31.01MiB at    5.49MiB/s ETA 00
[download]  35.1% of   31.01MiB at    3.29MiB/s ETA 00
[download]  38.4% of   31.01MiB at    2.61MiB/s ETA 00
[download]  44.8% of   31.01MiB at    3.56MiB/s ETA 00
[download]  57.7% of   31.01MiB at    4.56MiB/s ETA 00
[download]  63.6% of   31.01MiB at    4.81MiB/s ETA 00
[download]  63.6% of   31.01MiB at  Unknown B/s ETA Un
[download]  63.7% of   31.01MiB at  Unknown B/s ETA Un
[download]  63.7% of   31.01MiB at  Unknown B/s ETA Un
[download]  63.7% of   31.01MiB at    1.04MiB/s ETA 00
[download]  63.7% of   31.01MiB at    1.93MiB/s ETA 00
[download]  63.8% of   31.01MiB at    1.93MiB/s ETA 00
[download]  64.0% of   31.01MiB at    2.18MiB/s ETA 00
[download]  64.4% of   31.01MiB at    3.15MiB/s ETA 00
[download]  65.3% of   31.01MiB at    4.11MiB/s ETA 00
[download]  66.9% of   31.01MiB at    4.53MiB/s ETA 00
[download]  70.1% of   31.01MiB at    4.92MiB/s ETA 00
[download]  76.5% of   31.01MiB at    3.07MiB/s ETA 00
[download]  83.8% of   31.01MiB at    2.67MiB/s ETA 00
[download]  90.7% of   31.01MiB at    2.68MiB/s ETA 00
[download]  94.9% of   31.01MiB at    2.62MiB/s ETA 00
[download]  94.9% of   31.01MiB at  993.44KiB/s ETA 00
[download]  94.9% of   31.01MiB at    1.47MiB/s ETA 00
[download]  94.9% of   31.01MiB at    1.87MiB/s ETA 00
[download]  94.9% of   31.01MiB at    4.02MiB/s ETA 00
[download]  95.0% of   31.01MiB at    2.03MiB/s ETA 00
[download]  95.1% of   31.01MiB at    2.35MiB/s ETA 00
[download]  95.3% of   31.01MiB at    3.01MiB/s ETA 00
[download]  95.7% of   31.01MiB at    2.78MiB/s ETA 00
[download]  96.5% of   31.01MiB at    3.73MiB/s ETA 00
[download]  98.1% of   31.01MiB at    4.28MiB/s ETA 00
[download] 100.0% of   31.01MiB at    4.33MiB/s ETA 00
[download] 100% of   31.01MiB in 00:00:10 at 2.99MiB/s 
[youtube] Extracting URL: https://www.youtube.com/watch?v=dWCk8wdvXPA 
[youtube] dWCk8wdvXPA: Downloading webpage 
WARNING: [youtube] No supported JavaScript runtime could be found. Only deno is enabled by default; to use another runtime add  --js-runtimes RUNTIME[:PATH]  to your command/config. YouTube extraction without a JS runtime has been deprecated, and some formats may be missing. See  https://github.com/yt-dlp/yt-dlp/wiki/EJS  for details on installing one 
[youtube] dWCk8wdvXPA: Downloading android vr player API JSON 
[info] dWCk8wdvXPA: Downloading 1 format(s): 251 
[download] Destination: t.m4a 
[download]   0.1% of    1.83MiB at  Unknown B/s ETA Un
[download]   0.2% of    1.83MiB at  Unknown B/s ETA Un
[download]   0.4% of    1.83MiB at  Unknown B/s ETA Un
[download]   0.8% of    1.83MiB at  Unknown B/s ETA Un
[download]   1.7% of    1.83MiB at    2.02MiB/s ETA 00
[download]   3.4% of    1.83MiB at    1.70MiB/s ETA 00
[download]   6.8% of    1.83MiB at    1.89MiB/s ETA 00
[download]  13.6% of    1.83MiB at    1.96MiB/s ETA 00
[download]  27.3% of    1.83MiB at    2.23MiB/s ETA 00
[download]  54.6% of    1.83MiB at    2.46MiB/s ETA 00
[download] 100.0% of    1.83MiB at    2.41MiB/s ETA 00
[download] 100% of    1.83MiB in 00:00:00 at 2.23MiB/s 
ffmpeg version 8.1-full_build-www.gyan.dev Copyright (c) 2000-2026 the FFmpeg developers
  built with gcc 15.2.0 (Rev11, Built by MSYS2 project)
  configuration: --enable-gpl --enable-version3 --enable-static --disable-w32threads --disable-autodetect --enable-cairo --enable-fontconfig --enable-iconv --enable-gnutls --enable-lcms2 --enable-libxml2 --enable-gmp --enable-bzlib --enable-lzma --enable-libsnappy --enable-zlib --enable-librist --enable-libsrt --enable-libssh --enable-libzmq --enable-avisynth --enable-libbluray --enable-libcaca --enable-libdvdnav --enable-libdvdread --enable-sdl2 --enable-libaribb24 --enable-libaribcaption --enable-libdav1d --enable-libdavs2 --enable-libopenjpeg --enable-libquirc --enable-libuavs3d --enable-libxevd --enable-libzvbi --enable-liboapv --enable-libqrencode --enable-librav1e --enable-libsvtav1 --enable-libvvenc --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxavs2 --enable-libxeve --enable-libxvid --enable-libaom --enable-libjxl --enable-libsvtjpegxs --enable-libvpx --enable-mediafoundation --enable-libass --enable-frei0r --enable-libfreetype --enable-libfribidi --enable-libharfbuzz --enable-liblensfun --enable-libvidstab --enable-libvmaf --enable-libzimg --enable-amf --enable-cuda-llvm --enable-cuvid --enable-dxva2 --enable-d3d11va --enable-d3d12va --enable-ffnvcodec --enable-libvpl --enable-nvdec --enable-nvenc --enable-vaapi --enable-libshaderc --enable-vulkan --enable-libplacebo --enable-opencl --enable-libcdio --enable-openal --enable-libgme --enable-libmodplug --enable-libopenmpt --enable-libopencore-amrwb --enable-libmp3lame --enable-libshine --enable-libtheora --enable-libtwolame --enable-libvo-amrwbenc --enable-libcodec2 --enable-libilbc --enable-libgsm --enable-liblc3 --enable-libopencore-amrnb --enable-libopus --enable-libspeex --enable-libvorbis --enable-ladspa --enable-libbs2b --enable-libflite --enable-libmysofa --enable-librubberband --enable-libsoxr --enable-chromaprint --enable-whisper
  libavutil      60. 26.100 / 60. 26.100
  libavcodec     62. 28.100 / 62. 28.100
  libavformat    62. 12.100 / 62. 12.100
  libavdevice    62.  3.100 / 62.  3.100
  libavfilter    11. 14.100 / 11. 14.100
  libswscale      9.  5.100 /  9.  5.100
  libswresample   6.  3.100 /  6.  3.100
Input #0, mov,mp4,m4a,3gp,3g2,mj2, from 't.mp4':
  Metadata:
    major_brand     : dash
    minor_version   : 0
    compatible_brands: iso6avc1mp41
    creation_time   : 2025-08-10T11:49:30.000000Z
  Duration: 00:01:56.60, start: 0.000000, bitrate: 2231 kb/s
  Stream #0:0[0x1](und): Video: h264 (High) (avc1 / 0x31637661), yuv420p(tv, bt709, progressive), 1920x1080 [SAR 1:1 DAR 16:9], 2528 kb/s, 30 fps, 30 tbr, 15360 tbn (default)
    Metadata:
      creation_time   : 2025-08-10T11:49:30.000000Z
      handler_name    : ISO Media file produced by Google Inc.
Input #1, matroska,webm, from 't.m4a':
  Metadata:
    encoder         : google/video-file
  Duration: 00:01:56.62, start: 0.000000, bitrate: 131 kb/s
  Stream #1:0(eng): Audio: opus, 48000 Hz, stereo, fltp (default)
Stream mapping:
  Stream #0:0 -> #0:0 (copy)
  Stream #1:0 -> #0:1 (opus (native) -> aac (native))
Press [q] to stop, [?] for help
Output #0, mp4, to 'CS50_Final_Project.mp4':
  Metadata:
    major_brand     : dash
    minor_version   : 0
    compatible_brands: iso6avc1mp41
    encoder         : Lavf62.12.100
  Stream #0:0(und): Video: h264 (High) (avc1 / 0x31637661), yuv420p(tv, bt709, progressive), 1920x1080 [SAR 1:1 DAR 16:9], q=2-31, 2528 kb/s, 30 fps, 30 tbr, 15360 tbn (default)
    Metadata:
      creation_time   : 2025-08-10T11:49:30.000000Z
      handler_name    : ISO Media file produced by Google Inc.
  Stream #0:1(eng): Audio: aac (LC) (mp4a / 0x6134706D), 48000 Hz, stereo, fltp, 128 kb/s (default)
    Metadata:
      encoder         : Lavc62.28.100 aac
frame=   95 fps=0.0 q=-1.0 size=    1024KiB time=00:00:03.02 bitrate=2769.3kbits/s speed=5.86x elapsed=0:00:frame=  204 fps=196 q=-1.0 size=    2048KiB time=00:00:06.65 bitrate=2520.7kbits/s speed=6.38x elapsed=0:00:frame=  326 fps=210 q=-1.0 size=    3584KiB time=00:00:10.70 bitrate=2741.6kbits/s speed=6.91x elapsed=0:00:frame=  433 fps=209 q=-1.0 size=    5120KiB time=00:00:14.27 bitrate=2938.9kbits/s speed=6.88x elapsed=0:00:frame=  663 fps=257 q=-1.0 size=    8192KiB time=00:00:21.95 bitrate=3057.1kbits/s speed= 8.5x elapsed=0:00:frame=  925 fps=299 q=-1.0 size=   11776KiB time=00:00:30.65 bitrate=3146.8kbits/s speed=9.91x elapsed=0:00:frame= 1120 fps=310 q=-1.0 size=   14336KiB time=00:00:37.18 bitrate=3158.4kbits/s speed=10.3x elapsed=0:00:frame= 1244 fps=294 q=-1.0 size=   16128KiB time=00:00:41.23 bitrate=3203.9kbits/s speed=9.75x elapsed=0:00:frame= 1263 fps=258 q=-1.0 size=   16640KiB time=00:00:41.89 bitrate=3253.5kbits/s speed=8.57x elapsed=0:00:frame= 1277 fps=219 q=-1.0 size=   16896KiB time=00:00:42.28 bitrate=3273.5kbits/s speed=7.25x elapsed=0:00:frame= 1288 fps=199 q=-1.0 size=   17152KiB time=00:00:42.77 bitrate=3285.0kbits/s speed= 6.6x elapsed=0:00:frame= 1348 fps=190 q=-1.0 size=   17920KiB time=00:00:44.69 bitrate=3284.6kbits/s speed=6.29x elapsed=0:00:frame= 1416 fps=184 q=-1.0 size=   19200KiB time=00:00:47.04 bitrate=3343.7kbits/s speed= 6.1x elapsed=0:00:frame= 1487 fps=180 q=-1.0 size=   19712KiB time=00:00:49.25 bitrate=3278.2kbits/s speed=5.96x elapsed=0:00:frame= 1532 fps=172 q=-1.0 size=   20224KiB time=00:00:50.88 bitrate=3256.2kbits/s speed= 5.7x elapsed=0:00:frame= 1576 fps=165 q=-1.0 size=   20992KiB time=00:00:52.37 bitrate=3283.5kbits/s speed=5.49x elapsed=0:00:frame= 1633 fps=162 q=-1.0 size=   21504KiB time=00:00:54.27 bitrate=3245.9kbits/s speed= 5.4x elapsed=0:00:frame= 1651 fps=156 q=-1.0 size=   21760KiB time=00:00:54.86 bitrate=3248.8kbits/s speed=5.19x elapsed=0:00:frame= 1724 fps=155 q=-1.0 size=   23296KiB time=00:00:57.30 bitrate=3330.5kbits/s speed=5.17x elapsed=0:00:frame= 1774 fps=153 q=-1.0 size=   23296KiB time=00:00:58.98 bitrate=3235.3kbits/s speed=5.08x elapsed=0:00:frame= 1825 fps=151 q=-1.0 size=   23808KiB time=00:01:00.67 bitrate=3214.6kbits/s speed=5.01x elapsed=0:00:frame= 1866 fps=147 q=-1.0 size=   24320KiB time=00:01:02.01 bitrate=3212.6kbits/s speed= 4.9x elapsed=0:00:frame= 1894 fps=142 q=-1.0 size=   24576KiB time=00:01:02.84 bitrate=3203.4kbits/s speed= 4.7x elapsed=0:00:frame= 1924 fps=134 q=-1.0 size=   24576KiB time=00:01:03.72 bitrate=3159.4kbits/s speed=4.43x elapsed=0:00:frame= 1950 fps=126 q=-1.0 size=   24832KiB time=00:01:04.76 bitrate=3140.8kbits/s speed=4.18x elapsed=0:00:frame= 1979 fps=123 q=-1.0 size=   24832KiB time=00:01:05.81 bitrate=3090.9kbits/s speed= 4.1x elapsed=0:00:frame= 1999 fps=120 q=-1.0 size=   25344KiB time=00:01:06.49 bitrate=3122.3kbits/s speed=3.99x elapsed=0:00:frame= 2031 fps=118 q=-1.0 size=   25344KiB time=00:01:07.45 bitrate=3077.8kbits/s speed=3.91x elapsed=0:00:frame= 2068 fps=116 q=-1.0 size=   25600KiB time=00:01:08.77 bitrate=3049.1kbits/s speed=3.87x elapsed=0:00:frame= 2098 fps=115 q=-1.0 size=   25600KiB time=00:01:09.78 bitrate=3005.3kbits/s speed=3.81x elapsed=0:00:frame= 2126 fps=113 q=-1.0 size=   25856KiB time=00:01:10.72 bitrate=2995.1kbits/s speed=3.76x elapsed=0:00:frame= 2166 fps=112 q=-1.0 size=   26368KiB time=00:01:12.06 bitrate=2997.4kbits/s speed=3.72x elapsed=0:00:frame= 2220 fps=112 q=-1.0 size=   26624KiB time=00:01:13.83 bitrate=2954.0kbits/s speed=3.72x elapsed=0:00:frame= 2268 fps=111 q=-1.0 size=   27136KiB time=00:01:15.43 bitrate=2946.9kbits/s speed= 3.7x elapsed=0:00:frame= 2313 fps=111 q=-1.0 size=   27648KiB time=00:01:16.94 bitrate=2943.4kbits/s speed=3.68x elapsed=0:00:frame= 2372 fps=111 q=-1.0 size=   27648KiB time=00:01:18.91 bitrate=2870.2kbits/s speed=3.68x elapsed=0:00:frame= 2415 fps=110 q=-1.0 size=   27904KiB time=00:01:20.36 bitrate=2844.5kbits/s speed=3.66x elapsed=0:00:frame= 2474 fps=110 q=-1.0 size=   28160KiB time=00:01:22.32 bitrate=2802.1kbits/s speed=3.66x elapsed=0:00:frame= 2576 fps=112 q=-1.0 size=   28928KiB time=00:01:25.71 bitrate=2764.7kbits/s speed=3.73x elapsed=0:00:frame= 2666 fps=113 q=-1.0 size=   29696KiB time=00:01:28.72 bitrate=2741.8kbits/s speed=3.77x elapsed=0:00:frame= 2747 fps=114 q=-1.0 size=   29952KiB time=00:01:31.41 bitrate=2684.2kbits/s speed= 3.8x elapsed=0:00:frame= 2810 fps=114 q=-1.0 size=   30464KiB time=00:01:33.50 bitrate=2669.0kbits/s speed=3.81x elapsed=0:00:frame= 2886 fps=115 q=-1.0 size=   30720KiB time=00:01:36.04 bitrate=2620.3kbits/s speed=3.83x elapsed=0:00:frame= 2947 fps=115 q=-1.0 size=   30976KiB time=00:01:38.06 bitrate=2587.5kbits/s speed=3.84x elapsed=0:00:frame= 2988 fps=115 q=-1.0 size=   31232KiB time=00:01:39.45 bitrate=2572.5kbits/s speed=3.81x elapsed=0:00:frame= 3041 fps=114 q=-1.0 size=   31488KiB time=00:01:41.20 bitrate=2548.8kbits/s speed= 3.8x elapsed=0:00:frame= 3124 fps=115 q=-1.0 size=   31744KiB time=00:01:44.00 bitrate=2500.5kbits/s speed=3.83x elapsed=0:00:frame= 3198 fps=116 q=-1.0 size=   32000KiB time=00:01:46.24 bitrate=2467.5kbits/s speed=3.84x elapsed=0:00:frame= 3244 fps=114 q=-1.0 size=   32512KiB time=00:01:47.96 bitrate=2466.8kbits/s speed=3.81x elapsed=0:00:frame= 3300 fps=114 q=-1.0 size=   32512KiB time=00:01:49.86 bitrate=2424.2kbits/s speed= 3.8x elapsed=0:00:frame= 3338 fps=114 q=-1.0 size=   32768KiB time=00:01:51.12 bitrate=2415.6kbits/s speed=3.78x elapsed=0:00:frame= 3373 fps=113 q=-1.0 size=   33024KiB time=00:01:52.27 bitrate=2409.5kbits/s speed=3.75x elapsed=0:00:frame= 3457 fps=114 q=-1.0 size=   33280KiB time=00:01:55.09 bitrate=2368.8kbits/s speed=3.78x elapsed=0:00:[out#0/mp4 @ 000001b154b72280] video:31711KiB audio:1825KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: 0.357255%
frame= 3498 fps=113 q=-1.0 Lsize=   33655KiB time=00:01:56.56 bitrate=2365.2kbits/s speed=3.78x elapsed=0:00:30.87    
[aac @ 000001b1555db640] Qavg: 497.917
```
</details>

#### Step - 5
Now restart the project. And Now you should press 2 .
And then you will see the youtube vidio title what's you actually gave recently.

#### Terminal:
    1.Inject any link
    2.open any link
        Please Enter your choice: 2
    1.CS50 Final Project   
    Please Enter Your choice: 

##### step - 6
Now press the number which is infron of the title like in here you should press 1 to access recently stored youtube link.
#### Terminal:
    1.Inject any link
    2.open any link
        Please Enter your choice: 2
    1.CS50 Final Project
    Please Enter Your choice: 1

And then the program will be close and a youtube vidio will appear in your browser.

#### Terminal:
    1.Inject any link
    2.open any link
        Please Enter your choice: 2
    1.CS50 Final Project
    2.Computer Scientist Answers Computer Questions From Twitter
    Please Enter Your choice: 

In this case, if you want to access "2.Computer Scientist Answers Computer Questions From Twitter" this vidio you should press 2 if you want to access "1.CS50 Final Project" this vidio you should press 1. By this way you can use this project.

