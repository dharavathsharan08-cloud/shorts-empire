import numpy as np, moviepy.editor as mp, os, math
W,H,duration = 1080,1920,11.5  # 11.5 s to loop seamlessly

# 1) black canvas
bg = mp.ColorClip((W,H),color=(0,0,0)).set_duration(duration)

# 2) impossible Penrose triangle wire-frame (code drawn)
t = np.linspace(0,2*np.pi,200)
x = 400*np.cos(t) + W/2
y = 400*np.sin(t) + H/2 + 200*np.sin(3*t) # fake 3-D
wire = mp.VideoClip(lambda t: mp.make_frame(t,x,y,W,H), duration=duration)
wire = wire.set_mask(mp.VideoClip(lambda t: mp.make_mask(t,x,y,W,H), duration=duration, ismask=True))

# 3) rotate + zoom loop
wire = wire.rotate(lambda t: t*30).resize(lambda t: 1+0.05*np.sin(4*np.pi*t/duration))

# 4) white flash last frame
flash = mp.ColorClip((W,H),color=(255,255,255)).set_duration(0.08).set_start(duration-0.08)

# 5) sub-bass audio 18 Hz
sub = mp.AudioArrayClip([[0.1*np.sin(2*np.pi*18*t) for t in np.arange(0,duration,1/48000)]],fps=48000)
# 6) 120 Hz boom at start
boom = mp.AudioArrayClip([[0.6*np.sin(2*np.pi*120*t) for t in np.arange(0,0.15,1/48000)]],fps=48000)
audio = mp.CompositeAudioClip([sub,boom])

# 7) build final
final = mp.CompositeVideoClip([bg,wire,flash]).set_audio(audio)
final.write_videofile("short.mp4",fps=30,audio_codec="aac",bitrate="8000k")
