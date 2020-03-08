from PIL import Image, ImageDraw
import math

'''
A very hacky way to get circle coordinates for different population densities without having to do much math. Draws 3 circles all with different sizes and 
colors. Size depends on the density you want to store within the circle, so it's size * density + ~.5 to give it more space. It then iterates over every
pixel and checks the color and then appends it to it's assigned list
'''

def get_pixels(size):
	c_r = int(math.ceil(math.sqrt((size*1.7))))
	img = Image.new("RGB", (c_r, c_r))
	draw = ImageDraw.Draw(img)

	co_r = int(math.ceil((math.sqrt((size * 1.1)/3.14))))
	draw.ellipse((int(math.ceil(c_r/2)-co_r), int(math.ceil(c_r/2)-co_r), int(math.ceil(c_r/2)+co_r), int(math.ceil(c_r/2)+co_r)), fill = (255, 0, 0))

	b_r = int(math.ceil((math.sqrt((size * .90)/3.14))))
	draw.ellipse((int(math.ceil(c_r/2)-b_r), int(math.ceil(c_r/2)-b_r), int(math.ceil(c_r/2)+b_r), int(math.ceil(c_r/2)+b_r)), fill = (0, 255, 0))

	a_r = int(math.ceil((math.sqrt((size * .6)/3.14))))
	draw.ellipse((int(math.ceil(c_r/2)-a_r), int(math.ceil(c_r/2)-a_r), int(math.ceil(c_r/2)+a_r), int(math.ceil(c_r/2)+a_r)), fill = (0, 0, 255))	
	
	#img.save("test.png") if you wanna see the process

	sixtyp_pixel_list = []
	twentyf_pixel_list = []
	fifteen_pixel_list = []

	for x in range(c_r):
		for y in range(c_r):
			if img.getpixel((x, y)) == (0, 0, 255):
				sixtyp_pixel_list.append((x, y))
			if img.getpixel((x, y)) == (0, 255, 0):
				twentyf_pixel_list.append((x, y))
			if img.getpixel((x, y)) == (255, 0, 0):
				fifteen_pixel_list.append((x, y))	

	return fifteen_pixel_list, twentyf_pixel_list, sixtyp_pixel_list

