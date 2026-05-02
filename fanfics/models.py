from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from ckeditor.fields import RichTextField


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    
    avatar = models.ImageField(
    upload_to="avatars/",
    default="avatars/default.png",
    blank=True
)
    country = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return self.user.username


class Tag(models.Model):

    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Fandom(models.Model):

    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Category(models.Model):

    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name




class Fanfic(models.Model):
    #Ongoing/Completed
    STATUS_CHOICES = [
    ('finished', 'Finished'),
    ('in_progress', 'In Progress'),
    ]

    title = models.CharField(max_length=255)
    synopsis = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
    )
    tags = models.ManyToManyField(Tag, blank=True)
    fandoms = models.ManyToManyField(Fandom, blank=True)
    categories = models.ManyToManyField(Category, blank=True)
    language = models.CharField(max_length=30, default="en")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="fanfics")
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    


class Chapter(models.Model):

    chapterName = models.CharField(max_length=255)
    story = models.TextField()
    fanfic = models.ForeignKey(Fanfic, on_delete=models.CASCADE, related_name= 'chapters')
    order = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.chapterName
    

    
class Like(models.Model):
    class Meta:
        unique_together = ('user', 'fanfic')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    fanfic = models.ForeignKey(Fanfic, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)



class Bookmark(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fanfic = models.ForeignKey(Fanfic, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)



class ReadingHistory(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    chapter = models.ForeignKey(
        Chapter,
        on_delete=models.CASCADE
    )

    read_at = models.DateTimeField(auto_now=True)



class Comment(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    chapter = models.ForeignKey(
        Chapter,
        on_delete=models.CASCADE,
        related_name="comments"
    )

    paragraph = models.IntegerField()
    content = models.TextField()
    

    created_at = models.DateTimeField(auto_now_add=True)


class Follow(models.Model):

    follower = models.ForeignKey(User,on_delete=models.CASCADE,related_name="following")
    following = models.ForeignKey(User,on_delete=models.CASCADE,related_name="followers")

    created_at = models.DateTimeField(auto_now_add=True)



class Notification(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

message = models.TextField()

link = models.CharField(max_length=255)

is_read = models.BooleanField(default=False)

created_at = models.DateTimeField(auto_now_add=True)



class Block(models.Model):
    blocker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blocking')
    blocked = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blocked_by')



class Report(models.Model):

     user = models.ForeignKey(User, on_delete=models.CASCADE)

fanfic = models.ForeignKey(Fanfic, on_delete=models.CASCADE)

reason = models.TextField()

created_at = models.DateTimeField(auto_now_add=True)