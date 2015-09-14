from PIL import Image
import pytesseract
import glob, os

def dealwith(name):
	im = Image.open(name + ".jpg")

	pix = im.load()

	width, height = im.size

	for x in range(width):
		for y in range(height):
			p = pix[x,y]
			v = ()
			if len(p) == 4 :
				(r,g,b,a) = p
			else :
				(r,g,b) = p

			if r > 100 and g < 49 and b < 49:
				v = (0,0,0)
			else :
				v = (255,255,255)

			if len(p) == 4:
				v = v + (255,)
			pix[x,y] = v

	print(pytesseract.image_to_string(im))
	#im.save(file + ".out.jpg","JPEG")


for infile in glob.glob("*.jpg"):
    file, ext = os.path.splitext(infile)
    print file, ext
    dealwith(file)

