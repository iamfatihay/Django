from django.db import models


class Account(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.username


class Profile(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    about = models.TextField(null=True)
    phone = models.BigIntegerField(null=True)
    #! #################
    # image kullanacaksam yapilacaklar;
    # 1> Pillow kur
    #        python -m pip install Pillow
    # 2> settings.py a ekle
    #        MEDIA_URL = 'media/'
    #
    # 3> urls.py a ekle
    #       from django.conf import settings
    #       from django.conf.urls.static import static
    #       urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    #! #################
    avatar = models.ImageField("userpicture", blank=True, null=True, upload_to="media/")

    # CASCADE    primary silindiginde foreign de silinir
    # set_NULL   null olarak gunceller
    # DO_NOTHING    field oldugu gibi kalir
    # SET_DEFAULT   istenilen bir deger atanir
    # PROTECT       silmeye izin vermiyor
    account = models.OneToOneField(Account, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "profile about user"
        verbose_name_plural = "users profile"


class Adress(models.Model):
    name = models.CharField(max_length=50)
    adress = models.TextField(null=True)
    account = models.ForeignKey(Account, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Product(models.Model):
    productname=models.CharField(max_length=20)
    account=models.ManyToManyField(Account)
    def __str__(self):
        return self.productname
    
# class basket(models.Model):
#     productname=models.CharField(max_length=20)
#     account=models.ManyToManyField(Account)
    



    #! #################
    #  python manage.py shell
    # (shell de >>>) obj=Profile.objects.all()   tum objeleri getirir
    # x=Profile.objects.get(name='sinan')    ismi sinan olani getirir
    # x=Profile.objects.filter(name__startswith='y')  ismi y ile baslayan gelir
    # x=Profile.objects.filter(name__contains='n')   icinde n gecenler
    # exit()   cikis yapmak icin
    #! #################
