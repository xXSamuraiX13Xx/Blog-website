from django.db import models
from django.db.models.signals import pre_save
from XPYX.utils import unique_slug_generator

CAT = (
    ("Technology", "Technology"),
    ("General", "General"),
    ("Self-improvement", "Self-improvement"),
    ("Unsolved", "Unsolved"),
    ("Health&Fitness", "Health&Fitness"),
   
)

class Post (models.Model):
	cat = models.CharField(
        max_length = 20,
        choices = CAT,
        default = 'tech')
	author = models.ForeignKey("auth.user", on_delete = models.CASCADE) 
	keywordsSEO = models.CharField(max_length = 150, verbose_name='keywordsSEO', default="",  blank=True)
	DescSEO = models.CharField(max_length = 150, verbose_name='DescSEO', default="",  blank=True)
	PostURL = models.CharField(max_length = 150, verbose_name='PostURL', default="",  blank=True)
	title = models.CharField(max_length = 150, verbose_name='title')
	intro1 = models.TextField(default="",  verbose_name='intro1')
	sentence = models.TextField(default="", verbose_name='sentence')
	intro2 = models.TextField(default="",  verbose_name='intro2')
	title1 = models.CharField(max_length = 150, verbose_name='title1', default="",  blank=True)
	title2 = models.CharField(max_length = 150, verbose_name='title2', default="",  blank=True)
	title3 = models.CharField(max_length = 150, verbose_name='title3', default="",  blank=True)
	title4 = models.CharField(max_length = 150, verbose_name='title4', default="",  blank=True)
	title5 = models.CharField(max_length = 150, verbose_name='title5', default="",  blank=True)
	title6 = models.CharField(max_length = 150, verbose_name='title6', default="",  blank=True)
	title7 = models.CharField(max_length = 150, verbose_name='title7', default="",  blank=True)
	title8 = models.CharField(max_length = 150, verbose_name='title8', default="",  blank=True)
	title9 = models.CharField(max_length = 150, verbose_name='title9', default="",  blank=True)
	title10 = models.CharField(max_length = 150, verbose_name='title10', default="", blank=True)
	title11 = models.CharField(max_length = 150, verbose_name='title11', default="",  blank=True)
	title12 = models.CharField(max_length = 150, verbose_name='title12', default="",  blank=True) 
	content1 = models.TextField(default="", verbose_name='content1',  blank=True)
	content2 = models.TextField(default="", verbose_name='content2',  blank=True)
	content3 = models.TextField(default="", verbose_name='content3', blank=True)
	content4 = models.TextField(default="", verbose_name='content4',  blank=True)
	content5 = models.TextField(default="", verbose_name='content5',  blank=True)
	content6 = models.TextField(default="", verbose_name='content6',  blank=True)
	content7 = models.TextField(default="", verbose_name='content7',  blank=True)
	content8 = models.TextField(default="", verbose_name='content8',  blank=True)
	content9 = models.TextField(default="", verbose_name='content9',  blank=True)
	content10 = models.TextField(default="", verbose_name='content10', blank=True)
	content11 = models.TextField(default="", verbose_name='content11',  blank=True)
	content12 = models.TextField(default="", verbose_name='content12',  blank=True)
	link1 = models.URLField(max_length=200,default="", null=True, blank=True)
	link2 = models.URLField(max_length=200,default="", null=True, blank=True)
	link3 = models.URLField(max_length=200,default="", null=True, blank=True)
	link4 = models.URLField(max_length=200,default="", null=True, blank=True)
	link5 = models.URLField(max_length=200,default="", null=True, blank=True)
	link6 = models.URLField(max_length=200,default="", null=True, blank=True)
	link7 = models.URLField(max_length=200,default="", null=True, blank=True)
	link8 = models.URLField(max_length=200,default="", null=True, blank=True)
	link9 = models.URLField(max_length=200,default="", null=True, blank=True)
	link10 = models.URLField(max_length=200,default="", null=True, blank=True)
	link11 = models.URLField(max_length=200,default="", null=True, blank=True)
	link12 = models.URLField(max_length=200,default="", null=True, blank=True)
	coverorg = models.ImageField(upload_to="images/%y%m%d", null=True, blank=True, default="")
	cover1 = models.ImageField(upload_to="images/%y%m%d", null=True, blank=True, default="")
	cover2 = models.ImageField(upload_to="images/%y%m%d", null=True, blank=True, default="")
	cover3 = models.ImageField(upload_to="images/%y%m%d", null=True, blank=True, default="")
	cover4 = models.ImageField(upload_to="images/%y%m%d", null=True, blank=True, default="")
	cover5 = models.ImageField(upload_to="images/%y%m%d", null=True, blank=True, default="")
	cover6 = models.ImageField(upload_to="images/%y%m%d", null=True, blank=True, default="")
	cover7 = models.ImageField(upload_to="images/%y%m%d", null=True, blank=True, default="")
	cover8 = models.ImageField(upload_to="images/%y%m%d", null=True, blank=True, default="")
	cover9 = models.ImageField(upload_to="images/%y%m%d", null=True, blank=True, default="")
	cover10 = models.ImageField(upload_to="images/%y%m%d", null=True, blank=True, default="")
	cover11 = models.ImageField(upload_to="images/%y%m%d", null=True, blank=True, default="")
	cover12 = models.ImageField(upload_to="images/%y%m%d", null=True, blank=True, default="")
	outro = models.TextField(default="", verbose_name='outro')
	created_date = models.DateTimeField(verbose_name='published date')


	slug = models.SlugField(null=True, blank=True, unique=True)
	def  __str__(self):
		return self.title
def save(sender, instance, *args, **kwargs):
		if not instance.slug:
			instance.slug = unique_slug_generator(instance)
			
pre_save.connect(save, sender=Post)
