from django.db import models

# Create your models here.
class Admin(models.Model):
    username = models.CharField(max_length=20, default="")
    password = models.CharField(max_length=20, default="")
    confirmpassword = models.CharField(max_length=20, default="")


APP_CATEGORY = (
    ('entertainment', 'Entertainment'),
    ('education', 'Education'),
    ('social networking', 'Social Networking'),
    ('kids', 'Kids'),
    ('shopping', 'Shopping'),
    ('design', 'Design'),
    ('lifestyle', 'Lifestyle')
)

SUB_CATEGORY = (
    ('gaming', 'Gaming'),
    ('music Streaming', 'Music Streaming'),
    ('video Streaming', 'Video Streaming'),
    ('e-commerce', 'E-Commerce'),
    ('news', 'News'),
    ('messaging', 'Messaging'),
    ('social media', 'Social Media'),
    ('communication', 'Communication'),
    ('editing', 'Editing')
)

class Apps(models.Model):
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    appname = models.CharField(max_length=20, default="")
    applink = models.URLField(default="")
    appcategory = models.CharField(max_length=20, choices=APP_CATEGORY, default="")
    subcategory = models.CharField(max_length=20, choices=SUB_CATEGORY, default="")
    points = models.IntegerField(default="")
    photo = models.ImageField(upload_to='images/', blank=True, null=True)