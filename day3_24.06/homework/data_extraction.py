import zipfile
from PIL import Image
import numpy as np
import pandas as pd


images = []
with zipfile.ZipFile('day3_24.06/homework/letters.zip', 'r') as zf:
    infoList = zf.infolist()
    nameList = zf.namelist()
    with open('day3_24.06/homework/letters.csv', "w") as letters:
        for ind, file in enumerate(infoList):
            imageFile = zf.open(file)
            lst = np.array(Image.open(imageFile).convert("L")).ravel().tolist()
            if len(lst) != 1024:
                images.append(
                    lst +
                    [0]*32 + 
                    # В датасете косяк, 4 фотки отличаются на 1 пиксель
                    [int(nameList[ind][:2])]
                )
            else:
                images.append(
                    lst +
                    [int(nameList[ind][:2])]
                )
    print('Done')

np.array(images)

np.savetxt(
    'day3_24.06/homework/letters.csv', 
    np.array(images), fmt='%i', delimiter=','
)

# matrix = np.loadtxt(
#     'day3_24.06/homework/letters.csv', 
#     delimiter=',', dtype=int
# )
# matrix