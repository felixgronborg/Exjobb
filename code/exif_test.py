import PIL.Image
import PIL.ExifTags
import glob


def get_field (exif,field) :
  for (k,v) in exif.iteritems():
     if TAGS.get(k) == field:
        return v


folder = glob.glob('C:/Users/Felix/Desktop/Skola/5/exjobb/samling_ex_jobb/original/*.jpg')
for filename in folder:
    img = PIL.Image.open(filename)
    # exif = img._getexif()
    
    exif = {
    PIL.ExifTags.TAGS[k]: v
    for k, v in img._getexif().items()
    if k in PIL.ExifTags.TAGS
    }
    print(exif.get('FocalLength'))