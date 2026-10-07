import pymupdf, sys
from PIL import Image
# view.py <pdf> <page> x0 y0 x1 y1
d=pymupdf.open('/home/user/classroom/tools/spotlight/pdf/'+sys.argv[1]); pm=d[int(sys.argv[2])].get_pixmap(dpi=200)
im=Image.frombytes('RGB',(pm.width,pm.height),pm.samples)
im.crop(tuple(map(int,sys.argv[3:7]))).save('/home/user/classroom/tools/spotlight/work/g23/z.png')
