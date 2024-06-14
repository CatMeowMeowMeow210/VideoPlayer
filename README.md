# VideoPlayer
你想吃Bad Apple吗？
# 怎么运行？
你可以试着打开```VideoPlayer.py```
# 什么？你想更改程序里的视频？
那么你可以使用ffmpeg：
```
ffmpeg -i <你的视频> <项目路径>\res\video\%4d.png
ffmpeg -i <你的视频> <项目路径>\res\audio.wav
```
然后更改```VideoPlayer.py```里的设置：
```python
# ...

# 设置（不推荐改，除非你要更改程序里的视频）
image_num_max = 6577  # 所有帧数
fps_limit = 30  # 帧数限制
whether_to_force_the_cpu_to_lock_the_fps = True  # 是否强迫CPU让视频的FPS定在帧数限制的数值
screen_width, screen_height = 512, 384  # 分辨率
program_title = "Bad Apple!!"  # PYGAME窗口标题

# ...
```
