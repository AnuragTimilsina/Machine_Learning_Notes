import subprocess
import sys
import os

base = os.path.dirname(os.path.realpath(__file__))

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


with open("requirements.txt") as requirements:
    requirements = requirements.readlines()[0]
    install(requirements)


import gdown

# Linear Algebra Notes
print("Downloading handwritten note files!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
url = 'https://drive.google.com/uc?id=1ctDc_OOH8AiBFS5yjgbqBZAPJVRdQFZU'
output = os.path.join(
    base, "./HandWrittenNotes/mathematics/Linear_Algebra_For_ML.pdf")
gdown.download(url, output, quiet=False)
print("File downloaded!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

# Regression
print("Downloading handwritten note files!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
url = 'https://drive.google.com/uc?id=1_noq65qpWN9Mxb5e_9OOM4pagKKOBRe5'
output = os.path.join(
    base, "./HandWrittenNotes/ML_Algorithms_notes/Regression.pdf")
gdown.download(url, output, quiet=False)
print("File downloaded!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


print(".............................")
print(".............................")
print(".............................")
print(".............................")
print("Installing packages from requirements.txt")



