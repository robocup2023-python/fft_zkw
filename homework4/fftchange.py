import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img=cv.imread("./textjojo.jpg",0)
f=np.fft.fft2(img)
fshift=np.fft.fftshift(f)
rows,cols=img.shape
crow,ccol=int(rows/2),int(cols/2)
a=100
fshift[crow-a:crow+a,ccol-a:ccol+a]=0
ishift=np.fft.ifftshift(fshift)
iimg=np.fft.ifft2(ishift)
iimg=np.abs(iimg)

cv.imwrite("./fftorg.jpg",img)
cv.imwrite("./fft.jpg",iimg)
plt.subplot(221),plt.imshow(img,cmap="gray")
plt.subplot(222),plt.imshow(iimg,cmap="gray")
plt.show()
