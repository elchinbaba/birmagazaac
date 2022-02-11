from django.db import models
from django.db.models.base import Model
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Magaza(models.Model):
    name = models.CharField(max_length=50, verbose_name='Ad', unique=True)
    choices = [
        ('beauty', 'Gözəllik'),
        ('clothing', 'Geyim'),
        ('jewellery', 'Daş-qaş'),
        ('painting', 'Rəsm'),
        ('photography','Foto'),
        ('food', 'Yemək'),
        ('sport', 'İdman'),
        ('toy', 'Oyuncaq'),
        ('other', 'Digər'),
        ]
    category = models.CharField(choices=choices, max_length=50, verbose_name='Kateqoriya')
    slug = models.SlugField(unique=True, editable=False, max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("magaza:post:detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        # if not self.slug:
        self.slug = slugify(self.name.replace('ı','i').replace('ə','e'))
        return super(Magaza, self).save(*args, **kwargs)

class Post(models.Model):
    magaza = models.ForeignKey('magaza.Magaza', related_name='posts', on_delete=models.CASCADE)

    title = models.CharField(max_length=50, verbose_name='Yazı')
    price = models.FloatField(verbose_name='Qiyməti')
    file = models.FileField(null=True, blank=True)
    publishing_datetime = models.DateTimeField(verbose_name='Paylaşım tarixi', auto_now_add=True)
    info = models.TextField(verbose_name='Məlumat', null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("magaza:post:detail", kwargs={"slug": self.magaza.slug, "pk": self.id})