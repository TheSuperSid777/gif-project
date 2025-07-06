import imageio.v3 as iio
images = ["image1.jpeg","image2.jpeg"]
gifs = []
for i in images:
    gifs.append(iio.imread(images))
iio.imwrite("my_gif",gifs,duration = 500,loop = 0)