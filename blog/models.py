from django.db import models
from django.utils import timezone

#objects are properties whereas methods are actions
#class is use to define objects
#post is the name the entire model (thing we are trying to create).the 1st letter has to be upper case
#models.Model means that the Post is a Django Model, so Django knows that it should be saved in the database
class Post(models.Model): # defines de model  to be an object
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
#def means that is a method / function. this methods return something
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
# Create your models here.
