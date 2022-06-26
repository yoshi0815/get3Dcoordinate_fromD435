# coding: utf-8
import pyrealsense2 as rs
import numpy as np
import cv2

def get_click_point(event,x,y,flags,param):
    global depth_frame

    if event == cv2.EVENT_LBUTTONDOWN:

        if x>=640:
            return

        depth = depth_frame.get_distance(x, y)
        point = np.array([x,y,depth])
        if depth==0 :
            print("ERROR: cannot get depth data ! ")
            return 

        x=point[0]
        y=point[1]
        z=point[2]

        x,y,z=rs.rs2_deproject_pixel_to_point(color_intrinsics, [x, y], z)

        print("point:",[x,y,z])

pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

print("Start streaming")
pipeline.start(config)

align_to = rs.stream.color
align = rs.align(align_to)

cv2.namedWindow('RealsenseImage', cv2.WINDOW_AUTOSIZE)
cv2.setMouseCallback('RealsenseImage',get_click_point)

while cv2.waitKey(1)<0:

    frames = pipeline.wait_for_frames()
    aligned_frames = align.process(frames)
    depth_frame = aligned_frames.get_depth_frame()
    color_frame = aligned_frames.get_color_frame()
    #depth_frame = frames.get_depth_frame()
    #color_frame = frames.get_color_frame()

    color_intrinsics = color_frame.profile.as_video_stream_profile().intrinsics

    depth_image = np.asanyarray(depth_frame.get_data())
    color_image = np.asanyarray(color_frame.get_data())

    depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)
    images = np.hstack((color_image, depth_colormap))

    cv2.imshow("RealsenseImage",images)
