from django.db import models


class Hosting(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    logo = models.ImageField(upload_to='hosting/logo')
    avatar = models.ImageField(upload_to='hosting/avatar')

    affiliate_link = models.URLField()
    review = models.TextField()

    score = models.IntegerField(default=0)
    old_price = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    price = models.DecimalField(default=0, max_digits=5, decimal_places=2)

    features = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
