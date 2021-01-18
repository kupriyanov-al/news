from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField("Категория", max_length=50)

    class Meta:
        verbose_name = ("Категория")
        verbose_name_plural = ("Категории")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
        # return reverse("_detail", kwargs={"pk": self.pk})

class News(models.Model):
    header = models.CharField(("Заголовок"), max_length=50)
    text = models.TextField(("Текст"))
    date_create = models.DateTimeField(("Дата создания"), auto_now=False, auto_now_add=True)
    category = models.ForeignKey("Category", verbose_name=("Категория"), on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = ("Новость")
        verbose_name_plural = ("Новости")

    def __str__(self):
        return self.header

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})

