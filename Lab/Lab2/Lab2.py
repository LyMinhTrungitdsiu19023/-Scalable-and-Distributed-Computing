#2
import numpy as np
import matplotlib.pyplot as plt
# plt.plot(np.random.rand(10))
# plt.show()

#Problem 1.3
# import matplotlib.pyplot as plt
# import numpy as np
# CountryX = [400.2, 643.3, 1175.9, 3062.5, 6079.6, 11289.7, 16058.3]
# CountryY = [336.0, 472.0, 1028.0, 2092.0, 5131.0, 7689.0, 14147.0]
# CountryZ= [1307.0, 1158.0, 1191.0, 3140.0, 9023.0, 15502.0, 22218.0]

# years = list(range(1960, 2021, 10)) 
#ex1
# plt.plot(years, CountryX, color='pink', marker='*', linestyle='solid', label= "CountryX")
# plt.plot(years, CountryY, color='yellow', marker='*', linestyle='solid', label= "CountryY")
# plt.plot(years, CountryZ, color='green', marker='*', linestyle='solid', label= "CountryZ")
# plt.legend(loc='best')
# plt.title("GDP")
# plt.ylabel("Billions of $")
# plt.xlabel("Year")
# plt.show()
#ex2
# ind = np.arange(7) 


# barX = plt.bar(ind, CountryX, 0.25, color = 'pink')

# barY = plt.bar(ind+0.25, CountryY, 0.25, color='yellow')

# barZ = plt.bar(ind+0.5, CountryZ, 0.25, color = 'green')

# plt.xlabel("Years")
# plt.ylabel('Billions of $')
# plt.title("GDP")

# plt.xticks(ind+0.25,years)
# plt.legend( (barX, barY, barZ), ('CountryX', 'CountryY', 'CountryZ') )
# plt.show()
#ex3

# countries = ['X','Y','Z','W']
# export_rate = [50, 24, 18, 8]
# myexplode = [0, 0.2, 0, 0] #tach tung mang ra
# plt.pie(export_rate,labels= countries,autopct='%1.0f%%', explode = myexplode, shadow = True)
# plt.legend()
# plt.show() 

# #ex4
from scipy import misc


# img = misc.face()
img = plt.imread('Blackpink-Lisa.jpg')
img.shape
#color tone
# fig, h = plt.subplots(nrows=1, ncols=3, figsize=(15,5))

# for c, ax in zip(range(3), h):
#     tmp_im = np.zeros(img.shape, dtype="uint8")
#     tmp_im[:,:,c] = img[:,:,c]
#     ax.imshow(tmp_im)
#     ax.set_axis_off()

#Segmentation
def to_grayscale(im, weights = np.c_[0.3989, 0.5870, 0.1140]):

    tile = np.tile(weights, reps=(im.shape[0],im.shape[1],1))
    return np.sum(tile * im, axis=2)
def simple_threshold(im, threshold=128):
    return ((im > threshold) * 255).astype("uint8")

thresholds = [90,120,128,138,150]

fig, axs = plt.subplots(nrows=1, ncols=len(thresholds), figsize=(20,5));
gray_im = to_grayscale(img)
                        
for t, ax in zip(thresholds, axs):
    ax.imshow(simple_threshold(gray_im, t), cmap='Greys');
    ax.set_title("Threshold: {}".format(t), fontsize=20);
    ax.set_axis_off();


plt.imshow(img)
plt.show()

