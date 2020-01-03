import os

os.system("python -m pip uninstall -y kivy.deps.glew kivy.deps.gstreamer kivy.deps.sdl2 kivy.deps.angle")
os.system("python -m pip install docutils pygments pypiwin32 kivy_deps.sdl2==0.1.* kivy_deps.glew==0.1.*")
os.system("python -m pip install kivy_deps.gstreamer==0.1.*")
os.system("python -m pip install kivy_deps.angle==0.1.*")
os.system("python -m pip install kivy==1.11.1")

os.system("python -m pip3 uninstall -y kivy.deps.glew kivy.deps.gstreamer kivy.deps.sdl2 kivy.deps.angle")
os.system("python -m pip3 install docutils pygments pypiwin32 kivy_deps.sdl2==0.1.* kivy_deps.glew==0.1.*")
os.system("python -m pip3 install kivy_deps.gstreamer==0.1.*")
os.system("python -m pip3 install kivy_deps.angle==0.1.*")
os.system("python -m pip3 install kivy==1.11.1")

try:
	import cv2
except Exception: 
	os.system("pip install opencv-python")
	os.system("pip3 install opencv-python")

try:
	import numpy
except: 
	os.system("pip install numpy")
	os.system("pip3 install numpy")

try:
	import scipy
except:
	os.system("pip install scipy")
	os.system("pip3 install scipy")

try:
	import threading
except:
	os.system("pip install threading")
	os.system("pip3 install threading")

try:
	import kivymd
except Exception:
	os.system("pip install kivymd==0.100.2")
	os.system("pip3 install kivymd==0.100.2")