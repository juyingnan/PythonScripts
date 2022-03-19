from skimage import io
import skimage
import argparse

parser = argparse.ArgumentParser(description='Convert an input image to single channel tiff')
parser.add_argument('addresses', metavar='A', type=str, nargs='+',
                    help='input file location')
parser.add_argument('--rgb', dest='rgb', default=False,
                    help='if all rgb channels are saved (default: False - only gray channel)')

args = parser.parse_args()
print(args.addresses)

for address in args.addresses:

    img = io.imread(address, as_gray=not args.rgb)
    print(img.size)
    img16 = skimage.img_as_uint(img, force_copy=False)

    tiff_address = address.rpartition('.')[0] + '.tif'

    io.imsave(tiff_address, img16)


