from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class S_Profile(models.Model):
    LEVEL_TERM=(
        ('LEVEL-4 TERM-1', 'LEVEL-4 TERM-1'),
        ('LEVEL-4 TERM-2', 'LEVEL-4 TERM-2'),
        


    )

    user=models.OneToOneField(User,on_delete=models.CASCADE)
    level_term=models.CharField(max_length=50, choices=LEVEL_TERM, null=True)
    identity=models.CharField(max_length=30)
    batch=models.CharField(max_length=20)
    phone=models.CharField(max_length=14)
    #image=models.ImageField(default='default.jpg', upload_to='')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()
    
