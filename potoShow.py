
import matplotlib.pyplot as plt
from ToArray import make_Array_from_image
image_path = r"test.png"

imgTensor = make_Array_from_image("test")



plt.imshow(imgTensor)
plt.show()
print("Done!")