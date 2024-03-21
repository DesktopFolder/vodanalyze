#!/usr/bin/env python3
import cv2
import numpy as np

START_COL = 0
END_COL = 0
START_ROW = 0
END_ROW = 0

def INIT_DIMENSIONS(width, height):
    global START_COL, START_ROW, END_COL, END_ROW
    START_COL = int((600 / 1920) * width)
    END_COL = int(width / 2)

    START_ROW = int((200 / 1080) * height)
    END_ROW = int((450 / 1000) * height)
    print(f'Initialized dimensions to: ({START_COL}, {START_ROW}), ({END_COL}, {END_ROW})')

def process_image(img_rgb, template):
    # [start_row:end_row, start_col:end_col]
    img_gray = cv2.cvtColor(img_rgb[START_ROW:END_ROW, START_COL:END_COL], cv2.COLOR_BGR2GRAY)
    
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        return True, img_gray
    return False, img_gray

    # cv2.imwrite('res{0}.png'.format(write), img_gray)
    # This will write different res.png for each frame. Change this as you require
    # cv2.imwrite('res{0}.png'.format(count),img_rgb)

def processImage(imgname, search, tag):
    mainimg = cv2.imread(imgname)
    height, width, h = mainimg.shape
    INIT_DIMENSIONS(width, height)
    template = cv2.imread(search, 0)
    opened, img = process_image(mainimg, template)
    print(f'Opened: {opened}')
    cv2.imwrite('testimage.png',img)

def processVideo(videoname, search, tag):
    vidcap = cv2.VideoCapture(videoname)
    template = cv2.imread(search,0)  # open template only once
    width  = vidcap.get(cv2.CAP_PROP_FRAME_WIDTH)   # float `width`
    height = vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # float `height`

    """
    1920x1080 monitor + gui 4:
        X = 608
        Y = 204

    1920x1080 monitor + gui 3:
        X = 696
        Y = 288
    """

    INIT_DIMENSIONS(width, height)
    
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    print('FPS:', fps)
    fo = 0
    fc = 0
    IN_OPENED=False
    foa = 0
    fca = 0
    f = open(f'output/{tag}.txt', 'w')
    while True:
        success, image = vidcap.read()
        if not success: break         # loop and a half construct is useful

        opened, img = process_image(image, template)
        if opened:
            # WE OPENED AN INVENTORY.
            fo += 1 # total fames opened
            foa += 1 # adjacent frames opened
            if not IN_OPENED:
                print(f'Opened after {fca} frames closed.')
                f.write(f'CLOSEDFOR {fca}\n')
                fca = 0
                IN_OPENED = True
                cv2.imwrite(f'output/{tag}{fo+fc}.png', img)
        else:
            fc += 1 # total frames closed
            fca += 1 # adjacent frames closed
            if IN_OPENED:
                print(f'Closed after {foa} frames opened.')
                f.write(f'OPENEDFOR {foa}\n')
                foa = 0
                IN_OPENED = False
                cv2.imwrite(f'output/{tag}{fo+fc}_closed.png', img)

        if (fo + fc) % 300 == 0:
            print(f'Processed {fo + fc} frames...')
    print(f'Open frames: {fo} / Closed frames: {fc}')

def processArgsVideo():
    import sys
    try:
        VIDEO_PATH = sys.argv[1]
        SHULKER_NAME_IMAGE_PATH = sys.argv[2]
        NAME = sys.argv[3]
    except:
        print('You must provide THREE arguments to this program, in order: PATH_TO_VIDEO, PATH_TO_SHULKER_NAME_IMAGE, NAME')
        print('NAME can be anything you want, e.g. mywr or feinrun.')
        print('Example: python analyze.py ./fein-wr.mp4 resources/fein-v0.png feinberg-wr')
        sys.exit(1)
    #if not VIDEO_PATH.endswith('.mp4'):
    #    raise RuntimeError(f'Video path {VIDEO_PATH} does not end with mp4?')
    processVideo(VIDEO_PATH, SHULKER_NAME_IMAGE_PATH, NAME)

if __name__ == "__main__":
    processArgsVideo()
    # processVideo('./fein-wr-2_24.mp4', 'resources/fein-wr1.png', 'fein-wr1')
    # processImage('resources/fein-snap.png', 'resources/fein-wr1.png', 'test')
