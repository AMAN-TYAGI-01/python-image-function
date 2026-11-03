import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image = mpimg.imread("exter1.jpg")
fig, ax = plt.subplots()
ax.imshow(image)
ax.set_title("Example Image")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
plt.show()
