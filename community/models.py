from django.db import models
from users import models as userModels
from django.contrib.auth.models import User

# Create your models here.
class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    post = models.ForeignKey(userModels.ProfilePosts, on_delete=models.CASCADE)
    user_comment = models.TextField(max_length=500, verbose_name="User Comment")
    like_count = models.IntegerField(verbose_name="Like Count", default=0)
    time_commented = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user_comment
