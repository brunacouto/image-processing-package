from skimage.io import imread, imsave

def read_image(path, isgray=False):
    image = imread(path, as_gray=isgray)
    return image

def save_image(image, path):
    imsave(path, image)