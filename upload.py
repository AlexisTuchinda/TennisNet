import PySimpleGUI as sg
from PIL import Image
from video_process import split_frames


def upload():
    sg.theme("GreenTan") #can change later with predefined themes in the simple gui

    layout=[[[sg.Text("Upload a JPG Image: "), sg.FileBrowse(key="user_pose_img", file_types=(("JPG Images", "*.jpg"),))]], [sg.Button("Send Image")], [sg.Text("")], [sg.Text("OR:")], [sg.Text("")], [[sg.Text("Upload an AVI Video: "), sg.FileBrowse(key="user_pose_vid", file_types=(("AVI Video", "*.avi"),))]], [sg.Button("Send Video")]]

    window = sg.Window(title="TennisNet - Pose Analysis", layout=layout, margins=(200, 200))

    while True: 
        event, values = window.read()
        if event == "Send Image" and values["user_pose_img"] is not None:
            Image.open(values["user_pose_img"]).save("input/user_pose.jpg")
            break
        elif event == "Send Video" and values["user_pose_vid"] is not None:
            split_frames(values["user_pose_vid"])
            break
        elif event == sg.WIN_CLOSED:
            break

    window.close()

