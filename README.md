A simple project to analyze AA vods for shulker usage. For now.

# HOW TO USE IT

## There are many instructions not because this is complicated, but because I do not trust you. :) And any mistake will cause immediate issues, so...

Step 1: **Download your video**.

Get your video as an mp4. No instructions for this. But, yt-dlp will be installed in the next step, so you can do that first then yt-dlp your video.

Step 2: **Set up the project**.

Download this repository with either `git clone` or by the download button, whichever works.

Open the folder in:
- Windows: Powershell or Command Prompt
- macOS/Linux: An actually good shell that you surely know about (usually Termianal or iTerm or Xterm or whatever)

(e.g. `cd ~/user/downloads/vodanalyze`)

Ensure that you have Python installed:

`python --version`

Ensure that the version output from the above is 3.6 or above. **If you do not have Python installed, please search Google: "Install python 3", and use a reputable source for doing so.**

Step 3: **Install the requirements**.

Ideally use a virtual environment. But if you do not care, just:

`pip install yt-dlp` **For downloading videos. Not necessary for running the script.**

`pip install opencv-python` **Necessary.**

Step 4: **Download / acquire the video**.

Not much to say here. Get the video. Use `yt-dlp https://videourl` unless you already have it locally.

Step 5: **Get your shulker image**.

Open your video in VLC (or another usable video editor) and navigate to a frame where a shulker box is open. Then right click -> *Video* -> **Take Snapshot** (at the bottom). This will save *the current frame* as an image at the correct resolution to C:/Users/You/Pictures/somelongname.png.

Open this image in Paint (or any tool that allows cropping). Crop the image to just the text "Shulker", preferably the top half. You MUST NOT include anything 'outside of' the shulker in this image. Explanation: The script will search your entire video for frames that contain the image you are currently creating. So, if the image contains weird things that are not ALWAYS there when the shulker is open, it will fail. See resources/ for MANY examples and possibly precreated images for runners you might want to analyze.

Note also that the source resolution, gui scale, etc must all match PERFECTLY between the shulker box title image and the video itself. This is why you cannot just screenshot the video on youtube or whatnot, as the screenshot will not have the right resolution/size.

Step 6: **Run the program**.

`python analyze.py path-to-video path-to-shulker-image name-for-this`

This script automatically (**!!**) normalizes to 30fps. So, the output frames at the end will be in 30fps. In other words, if you see: Open frames: 12000 / Closed frames: 598511, that means you had 12000 open frames, so the shulker was opened for 12000 / 30 = 400s.

If you don't see opened shulkers for a long time, that might indicate a problem. Please re-read the instructions and ensure you have followed the steps. Note that super low quality videos will not work for this. You can DM me on discord if problems continue, I don't mind, but please include the files you are using (the source video's YouTube link, the screenshot you took from it within VLC, and the cropped image you used during processing).