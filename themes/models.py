from django.db import models

# Model for site settings like site name,logo,contact details and about us information
class SiteSettings(models.Model):
    banner=models.ImageField(upload_to='media/site/',null=True,blank=True)# to add banner image in the model, upload_to is the folder inside media folder where images will be stored, null=True means its optional to add an image, blank=True means its optional in forms too
    caption=models.CharField(max_length=200,null=True,blank=True)# to add caption for the banner image, null=True means its optional to add a caption, blank=True means its optional in forms too