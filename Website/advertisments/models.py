from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user_name= models.OneToOneField(User, on_delete=models.CASCADE)
    Phone = models.CharField(max_length=10, default='')
    ad_profile_pic = models.ImageField(upload_to='profile_images/',default='' , blank=True)

    def __str__(self):
        return self.Phone


class Location(models.Model):
    user_name = models.OneToOneField(User , on_delete=models.CASCADE)
    location_id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=200, default='Not Mentioned')
    city = models.CharField(max_length=200, default='Not Mentioned')
    state = models.CharField(max_length=200, default='Not Mentioned')
    pin_code = models.CharField(max_length=6, default='000000')

    def __str__(self):
        return '{}, {}, {} | Pincode: {}'.format(self.location, self.city, self.state, self.pin_code)



class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=200, default='Other Category')
    cat_image = models.ImageField(upload_to='cat_images/', default='No Image', blank=True)
    cat_status = models.BooleanField(default=True)

    def __str__(self):
        return self.category_name


class sub_category(models.Model):
    sub_id = models.AutoField(primary_key=True)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category_name = models.CharField(max_length=200, default='Others')

    def __str__(self):
        return self.sub_category_name


class Ad(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='owner')
    ad_cat = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='ad_cat', default=0)
    ad_subcat = models.ForeignKey(sub_category, on_delete=models.CASCADE, max_length=20, related_name='ad_subcat',null=True, default=0)
    ad_title = models.CharField(max_length=200, default='None')
    condition = models.CharField(max_length=200, default='Not Mentioned')
    ad_brand = models.CharField(max_length=200, default='Not Mentioned')
    ad_model = models.CharField(max_length=200, default='Not Mentioned')
    ad_price = models.FloatField(null=False, default='Not on Sale')
    ad_description = models.CharField(max_length=900, default='Not Mentioned')
    ad_image1 = models.ImageField(upload_to='images/', default='No Images')
    ad_image2 = models.ImageField(upload_to='images/', default='No Images')
    ad_image3 = models.ImageField(upload_to='images/', default='No Images')
    ad_location = models.CharField(max_length=400, default='Not Mentioned')
    ad_city = models.CharField(max_length=200, default='Not Mentioned')
    ad_state = models.CharField(max_length=200, default='Not Mentioned')
    ad_pin_code = models.CharField(max_length=6, default='000000')
    post_date = models.DateField(default='')
    ad_status = models.BooleanField(default=True)

    def __str__(self):
        return "Product: {} | Brand: {} | Model: {}".format(self.ad_title, self.ad_brand, self.ad_model)


class Review(models.Model):
    review_of_ad = models.ForeignKey(Ad, on_delete=models.CASCADE , default=0)
    name_of_customer = models.ForeignKey(User , on_delete=models.CASCADE)
    subject = models.CharField(max_length=100 , default='None' , blank=True)
    message = models.CharField(max_length=500, default='None')
    review_parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    post_date_review = models.DateField(null=True,blank=True , auto_now_add=True)

    def __str__(self):
        return "{}  Posted by {} ".format(self.review_of_ad, self.name_of_customer)

class Contact(models.Model):
    user = models.ForeignKey(User , on_delete= models.CASCADE)
    name = models.CharField(max_length=30 , default='None')
    subject = models.CharField(max_length=40 , default= 'None')
    message = models.CharField(max_length= 200 , default='None')
    reply = models.CharField(max_length=200 , default='No Reply')
    post_date_contact = models.DateField(null=True, blank=True, auto_now_add=True)

    def __str__(self):
        return "{} asked {}".format(self.user , self.subject)
