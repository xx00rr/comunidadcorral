from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    address = models.CharField(max_length=300, blank=True)
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=30, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
