import opc, time
from PIL import Image

im = Image.open( "ledpov.png" )
im_width, im_height = im.size
im_pixels = im.load()

client = opc.Client('localhost:7890')

this_column = 0

update_hz = 1.0 / 25.0

while True:

    # pull pixels from image
    pixels = []
    for y in range(0,im_height):
        im_pixel = im_pixels[ this_column, y ]
        pixels.append( im_pixel )

    # put pixels to fadecandy
    client.put_pixels( pixels )
    client.put_pixels( pixels )

    # step along the width of the image
    this_column += 1
    if this_column >= im_width:
        this_column = 0

    # wait for the next frame
    time.sleep( update_hz ) 


