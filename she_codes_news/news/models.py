from django.db import models
from django.contrib.auth import get_user_model


USER = get_user_model()

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    # author = models.CharField(max_length=200)
    author = models.ForeignKey(
        USER, on_delete = models.CASCADE
    )
    pub_date = models.DateTimeField()
    content = models.TextField()
    image = models.TextField(max_length = 3000, blank = True)
    fave_by = models.ManyToManyField(
        USER, related_name="favourites", blank =True
    )
    # null is purely database-related, whereas blank is validation-related. If a field has blank=True , form validation will allow entry of an empty value. If a field has blank=False , the field will be required.
    
    # THE BELOW IS ANOTHER METHOD FOR ORDERING BY DESCENDING PUB DATE
    # class Meta:
    #    ordering = ["-pub_date"]

