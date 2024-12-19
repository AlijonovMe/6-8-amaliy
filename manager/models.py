from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nomi")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kategoriya "
        verbose_name_plural = "Kategoriyalar"


class Products(models.Model):
    name = models.CharField(max_length=150, verbose_name="Nomi")
    price = models.IntegerField(default=0, verbose_name="Narxi")
    count = models.IntegerField(default=0, verbose_name="Soni")
    description = models.TextField(default="Ma'lumot qo'shilmadi", verbose_name="Tavsifi")
    image = models.ImageField(upload_to="images/", verbose_name="Surati", blank=True, null=True)
    published = models.BooleanField(default=False, verbose_name="Nashr etilgani")
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name="Kategoriyasi")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Mahsulot "
        verbose_name_plural = "Mahsulotlar"
