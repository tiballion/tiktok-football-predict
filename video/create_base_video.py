from moviepy.editor import ColorClip

def get_base_video():
    """Return a base video"""
    return ColorClip((1080,1920), color=(255,0,0), duration=5)

def save_base_video(name):
    """Save a base video"""
    clip = get_base_video()
    clip.write_videofile(f"{name}.mp4", fps=24)
