import pygame
import PIL
import cv2
import moviepy
import pydub
import tkinter as tk
import pkg_resources

def check_installation():
    print("✅ Pygame version:", pygame._version_)
    print("✅ Pillow version:", PIL._version_)
    print("✅ OpenCV version:", cv2._version_)
    print("✅ MoviePy version:", moviepy._version_)
    try:
        pydub_version = pkg_resources.get_distribution ("pydub").version
        print("✅ Pydub version:", pydub_version)
    except pkg_resources.DistributionNotFound:
        print("✅ Pydub version not found")
    print("✅ Tkinter is installed and working!")

if __name__ == "__main__":
    check_installation()