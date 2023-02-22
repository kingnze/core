from django.db import models
from datetime import datetime
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from realtors.models import Realtor

class Property(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    propertyid = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    RentOrBuy = models.CharField(max_length=10,null=True ,blank=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to='photos/%y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%y/%m/%d/', null=True ,blank=True)
    photo_2 = models.ImageField(upload_to='photos/%y/%m/%d/', null=True ,blank=True)
    photo_3 = models.ImageField(upload_to='photos/%y/%m/%d/', null=True ,blank=True)
    photo_4 = models.ImageField(upload_to='photos/%y/%m/%d/', null=True ,blank=True)
    photo_5 = models.ImageField(upload_to='photos/%y/%m/%d/', null=True ,blank=True)
    published = models.BooleanField(default=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):

        return self.title

class Topproperty(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    propertyid = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    RentOrBuy = models.CharField(max_length=10,null=True ,blank=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to='photos/%y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_7 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_8 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_9 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    published = models.BooleanField(default=True)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

class Properties(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    property_id = models.CharField(max_length=200)
    title = models.CharField(max_length=500)
    RentOrBuy = models.CharField(max_length=10)
    address = models.CharField(max_length=500)
    state = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.CharField(max_length=20, blank=True)
    bathrooms = models.CharField(max_length=20, blank=True)
    garage = models.CharField(max_length=20, blank=True)
    sqft = models.IntegerField(blank=True)
    plot_size = models.CharField(max_length=50, blank=True)
    photo_main = models.ImageField(upload_to='photos/%y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_7 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    published = models.BooleanField(default=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):

        return self.title

class Top_properties(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    property_id = models.CharField(max_length=200)
    title = models.CharField(max_length=500)
    RentOrBuy = models.CharField(max_length=10)
    address = models.CharField(max_length=500)
    state = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.CharField(max_length=20, blank=True)
    bathrooms = models.CharField(max_length=20, blank=True)
    garage = models.CharField(max_length=20, blank=True)
    sqft = models.CharField(max_length=20, blank=True)
    plot_size = models.CharField(max_length=50, blank=True)
    photo_main = models.ImageField(upload_to='photos/%y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_7 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    published = models.BooleanField(default=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):

        return self.title

class Whoweare(models.Model):
    subtitle = models.CharField(max_length=200)
    title = models.CharField(max_length=500)
    property = models.CharField(max_length=500)
    advice = models.CharField(max_length=500)
    services = models.CharField(max_length=500)
    responsibility = models.CharField(max_length=500)
    structure = models.CharField(max_length=500)
    strategy = models.CharField(max_length=500)
    leadimg = models.ImageField(default='myleadimg.jpg',null=True,blank=True)
    body = RichTextField()
    slug = models.SlugField(max_length=550,null=True,blank=True)
    published = models.BooleanField(default=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):

        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Whoweare, self).save(*args, **kwargs)

    class Meta:
        db_table = 'Whoweare'
        managed = True
        verbose_name = 'Whoweare'
        verbose_name_plural = 'Whoweare'       

class whyus(models.Model):
    subtitle = models.CharField(max_length=200)
    title = models.CharField(max_length=500)
    text_1 = models.CharField(max_length=500)
    text_2 = models.CharField(max_length=500)
    text_3 = models.CharField(max_length=500)
    text_4 = models.CharField(max_length=500)
    leadimg = models.ImageField(default='myleadimg.jpg',null=True,blank=True)
    body = RichTextField()
    slug = models.SlugField(max_length=550,null=True,blank=True)
    published = models.BooleanField(default=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):

        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(whyus, self).save(*args, **kwargs)

    class Meta:
        db_table = 'whyus'
        managed = True
        verbose_name = 'whyus'
        verbose_name_plural = 'whyus' 

class About(models.Model):
    subtitle = models.CharField(max_length=200)
    title = models.CharField(max_length=500)
    subtitle_1 = models.CharField(max_length=500)
    leadimg = models.ImageField(default='myleadimg.jpg',null=True,blank=True)
    body = RichTextField()
    slug = models.SlugField(max_length=550,null=True,blank=True)
    published = models.BooleanField(default=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):

        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(About, self).save(*args, **kwargs)

    class Meta:
        db_table = 'About'
        managed = True
        verbose_name = 'About'
        verbose_name_plural = 'About' 

class Start(models.Model):
    start_1 = models.CharField(max_length=200)
    number_1 = models.CharField(max_length=200)
    start_2 = models.CharField(max_length=200)
    number_2 = models.CharField(max_length=200)
    start_3 = models.CharField(max_length=200)
    number_3 = models.CharField(max_length=200)
    start_4 = models.CharField(max_length=200)
    number_4 = models.CharField(max_length=200)
    def __str__(self):

        return self.start_1

    class Meta:
        db_table = 'Start'
        managed = True
        verbose_name = 'Start'
        verbose_name_plural = 'Start'  

class Allinone(models.Model):
    subtitle = models.CharField(max_length=200)
    title = models.CharField(max_length=500)
    description = models.TextField(blank=True)
    published = models.BooleanField(default=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):

        return self.title

class Contact(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f'{self.fname} {self.lname}'

    class Meta:
        db_table = 'contact'
        managed = True
        verbose_name = 'Contacts'
        verbose_name_plural = 'Contacts' 

class Blog(models.Model):
    title = models.CharField(max_length=550)
    slug = models.SlugField(max_length=550,null=True,blank=True)
    published = models.BooleanField(default=True,null=True,blank=True)
    flag = models.BooleanField(default=False,null=True,blank=True)
    date_posted = models.DateTimeField(default=datetime.now())
    leadimg = models.ImageField(default='myleadimg.jpg')
    body = RichTextField()

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    class Meta:
        db_table = 'Blog'
        managed = True
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog'



