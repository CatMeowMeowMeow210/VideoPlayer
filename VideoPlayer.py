import sys
import threading
import pygame

# 设置（不推荐改，除非你要更改程序里的视频）
image_num_max = 6577  # 所有帧数
fps_limit = 30  # 帧数限制
whether_to_force_the_cpu_to_lock_the_fps = True  # 是否强迫CPU让视频的FPS定在帧数限制的数值
screen_width, screen_height = 512, 384  # 分辨率
program_title = "Bad Apple!!"  # PYGAME窗口标题

# Program code

running = True  # Used to notify the video thread of termination

pygame.init()  # Initialize PYGAME
pygame.mixer.init()  # Initialize the audio player

screen = pygame.display.set_mode((screen_width, screen_height))  # Set resolution
pygame.display.set_caption(program_title)  # Set window title

clock = pygame.time.Clock()  # Set the clock


def play_video():  # Video thread
    global running
    for image_num in range(1, image_num_max + 1):  # Loop the video frame
        if not running:  # Accept video thread termination notifications
            break  # Exit the loop to terminate the video thread
        video = pygame.image.load(f"res/video/{image_num:04d}.png")  # Loads the specified video frame
        screen.blit(video, (0, 0))  # Draws the video frame on the window
        if whether_to_force_the_cpu_to_lock_the_fps:
            clock.tick_busy_loop(fps_limit)  # Limit the number of video frames
        else:
            clock.tick(fps_limit)  # Limit the number of video frames
        print(f"fps_limit={fps_limit} fps={clock.get_fps()} image_num={image_num:04d}")  # Print some debugging
        # information
    running = False


pygame.mixer.music.load("res/audio.wav")  # Loading audio file
pygame.mixer.music.play()  # Play audio file

video_thread = threading.Thread(target=play_video)  # Initialize the video thread
video_thread.start()  # Start video thread

while True:  # An endless loop
    pygame.display.flip()  # Refresh window
    for event in pygame.event.get():  # Accept window event
        if event.type == pygame.QUIT:  # Window close key press event
            running = False  # Notifies the video thread of termination
            video_thread.join()  # Wait for the video thread to end
            pygame.quit()  # Close PYGAME
            sys.exit()  # Exit main program
    if not running:
        video_thread.join()  # Wait for the video thread to end
        pygame.quit()  # Close PYGAME
        sys.exit()  # Exit main program
