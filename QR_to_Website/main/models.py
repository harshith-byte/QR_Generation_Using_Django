from pydoc import doc
from unicodedata import name
from django.db import models

from django.db import models
import qrcode
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File

# Create your models here.
class doctor_name(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to='qrcode',blank=True)

    def save(self,*args,**kwargs):
      qrcode_img=qrcode.make('0.0.0.0:8000/'+self.name)
      canvas=Image.new("RGB", (300,300),"white")
      draw=ImageDraw.Draw(canvas)
      canvas.paste(qrcode_img)
      buffer=BytesIO()
      fname=f'{self.name}.png'
      canvas.save(buffer,"PNG")
      self.image.save(fname,File(buffer),save=False)
      canvas.close()
      super().save(*args,**kwargs)

    def __str__(self):
        return self.name


class doctor_details(models.Model):
    name=models.CharField(max_length=200)
    phone=models.BigIntegerField()

    def __str__(self):
        return self.name
