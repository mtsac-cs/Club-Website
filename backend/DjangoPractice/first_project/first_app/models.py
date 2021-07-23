from django.db import models

class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)

    # From our OOP overview, remember that we have special
    # methods, in this case we will use one called __str__
    # so that when someone decides to print an object of our
    # Topic class, it will return the top_name attribute as
    # a string. 
    def __str__(self):
        return self.top_name

class WebPage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(WebPage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date) # cast it as string because it is a date object

