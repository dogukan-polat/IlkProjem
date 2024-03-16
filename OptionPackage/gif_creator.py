import imageio.v3 as iio

def create_gif():
    filenames = ['image1.png', 'image2.png']
    images = []
    for filename in filenames:
        images.append(iio.imread(filename))
        iio.imwrite('squirrel.gif', images, duration=500, loop=0)