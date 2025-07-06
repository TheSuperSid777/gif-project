import imageio.v3 as iio
images = ['image1.png','image2.png']
gifs = []
for i in images:
    gifs.append(iio.imread(i))
iio.imwrite("my_gif.gif",gifs,duration = 500,loop = 0)