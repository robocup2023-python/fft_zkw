import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img=cv.imread("./textjojo.jpg",0)
f=np.fft.fft2(img)
fshift=np.fft.fftshift(f)
real=np.real(fshift)
unreal=np.imag(fshift)
magnitude_spectrum=20*np.log(np.abs(fshift))
real_spectrum=20*np.log(np.abs(real))+10*np.log(2)
imag_spectrum=20*np.log(np.abs(unreal))+10*np.log(2)
print(magnitude_spectrum.T==magnitude_spectrum)
plt.subplot(221)
plt.imshow(img,cmap="gray")
plt.title("original")
plt.axis("off")

plt.subplot(222)
plt.imshow(magnitude_spectrum,cmap="gray")
plt.title("result")
plt.axis("off")

plt.subplot(223)
plt.imshow(real_spectrum,cmap="gray")
plt.title("real")
plt.axis("off")

plt.subplot(224)
plt.imshow(imag_spectrum,cmap="gray")
plt.title("imag")
plt.axis("off")
plt.show()

