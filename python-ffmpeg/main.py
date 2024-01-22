from moviepy.editor import VideoFileClip


if __name__ == '__main__':
    clip = VideoFileClip('example.mp4')
    resized_clip = clip.resize(height=240)
    resized_clip.write_videofile('example_240p.mp4', codec="libx264", audio_codec="aac")
