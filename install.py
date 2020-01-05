import os
import tkinter as tk
import time
from threading import Thread


currentInstall = "Installing..."
finished = False
stopVal = False




class App():
    def __init__(self):
        global currentInstall
        global finished
        global stopVal

        self.root = tk.Tk()
        self.root.title("NeuroMath installer")
        self.root.geometry("312x324")
        # self.root.wm_iconbitmap('nm1.ico')
        self.root.protocol('WM_DELETE_WINDOW', self.stop)

        self.label = tk.Label(text=currentInstall, font=("Arial", 20, "bold"))
        self.button = tk.Button(text="Close", command=self.stop, state=tk.NORMAL)

        self.label.place(relx=0.21, rely=0.3)
        self.button.place(relx=0.4, rely=0.5)
        
        self.update_clock()
        self.root.mainloop()


    def update_clock(self):
        self.label.configure(text=currentInstall)
        if finished:
            self.button.configure(state=tk.NORMAL)
        if (stopVal == False):
            self.root.after(1000, self.update_clock)
        else:
            self.label.configure(text="Closing...")

    def stop(self):
        global stopVal
        global currentInstall
        currentInstall = "Closing..."
        stopVal = True

def startApp():
    App()

Thread(target=lambda x=None: App(), args=(), daemon=True).start()


currentInstall = "Upgrading pip"
os.system("python -m pip install --upgrade pip")

try:
	import kivy
	currentInstall = "Upgrading Kivy"
	os.system("python -m pip uninstall -y kivy.deps.glew kivy.deps.gstreamer kivy.deps.sdl2 kivy.deps.angle")
	os.system("python -m pip install docutils pygments pypiwin32 kivy_deps.sdl2==0.1.* kivy_deps.glew==0.1.*")
	os.system("python -m pip install kivy_deps.gstreamer==0.1.*")
	os.system("python -m pip install kivy_deps.angle==0.1.*")

	os.system("python -m pip install --upgrade docutils pygments pypiwin32 kivy_deps.sdl2==0.1.* kivy_deps.glew==0.1.*")
	os.system("python -m pip install --upgrade kivy_deps.gstreamer==0.1.*")
	os.system("python -m pip install --upgrade kivy_deps.angle==0.1.*")
	
	os.system("python -m pip install --upgrade kivy==1.11.1")

except Exception:
	currentInstall = "Installing kivy"
	os.system("python -m pip uninstall -y kivy.deps.glew kivy.deps.gstreamer kivy.deps.sdl2 kivy.deps.angle")
	os.system("python -m pip install docutils pygments pypiwin32 kivy_deps.sdl2==0.1.* kivy_deps.glew==0.1.*")
	os.system("python -m pip install kivy_deps.gstreamer==0.1.*")
	os.system("python -m pip install kivy_deps.angle==0.1.*")
	os.system("python -m pip install kivy==1.11.1")

try:
    import cv2
    currentInstall = "Upgrading OpenCV"
    os.system("python -m pip install --upgrade opencv-python")
except Exception:
    currentInstall = "Installing OpenCV"
    os.system("python -m pip install opencv-python")


if stopVal:
    exit()

try:
    import numpy
    currentInstall = "Upgrading NumPy"
    os.system("python -m pip install --upgrade numpy")
except Exception:
    currentInstall = "Installing NumPy"
    os.system("python -m pip install numpy")

if stopVal:
    exit()

try:
    import scipy
    currentInstall = "Upgrading Scipy"
    os.system("python -m pip install --upgrade scipy")
except Exception:
    currentInstall = "Installing Scipy"
    os.system("python -m pip install scipy")

if stopVal:
    exit()

try:
    import kivymd
    currentInstall = "Upgrading KivyMD"
    os.system("python -m pip install --upgrade kivymd==0.100.2")
except Exception:
    currentInstall = "Installing KivyMD"
    os.system("python -m pip install kivymd==0.100.2")

currentInstall = "Finished"
finished = True
