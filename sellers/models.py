from django.db import models
from accounts.models import UserProfile

class Vendor(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    verified = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.shop_name