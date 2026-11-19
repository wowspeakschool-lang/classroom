from PIL import Image, ImageDraw
import math
face=Image.open('/home/user/classroom/media/sm0/new/face_boy1.webp').convert('RGBA')
W=H=800; fx,fy=(W-face.width)//2,(H-face.height)//2+20
P={'eyeL':(205,338),'eyeR':(355,338),'nose':(283,385),'mouth':(283,432),'earL':(78,392),'earR':(468,392)}
def arrow(d,start,end,col=(229,57,53)):
    ang=math.atan2(end[1]-start[1],end[0]-start[0]); L=48
    base=(end[0]-L*math.cos(ang),end[1]-L*math.sin(ang))
    left=(base[0]+26*math.sin(ang),base[1]-26*math.cos(ang)); right=(base[0]-26*math.sin(ang),base[1]+26*math.cos(ang))
    for w,c in [(26,'white'),(16,col)]:
        d.line([start,base],fill=c,width=w)
    d.polygon([end,left,right],fill=col,outline='white',width=5)
cards={'eyes':[((40,140),'eyeL'),((760,140),'eyeR')],
       'nose':[((760,560),'nose')],
       'mouth':[((40,700),'mouth')],
       'ears':[((25,640),'earL'),((775,640),'earR')]}
for name,arrs in cards.items():
    c=Image.new('RGBA',(W,H),'white'); c.alpha_composite(face,(fx,fy)); d=ImageDraw.Draw(c)
    for st,key in arrs:
        tx,ty=P[key]; tx+=fx; ty+=fy
        # stop arrow tip slightly before target
        ang=math.atan2(ty-st[1],tx-st[0]); end=(tx-14*math.cos(ang),ty-14*math.sin(ang))
        arrow(d,st,end)
    c.convert('RGB').save(f'arrow_{name}.png')
