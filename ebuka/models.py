from django.db import models

# Create your models here.
class Home(models.Model):
    name = models.CharField(max_length=50)
    greetings_1 = models.CharField(max_length=30)
    greetings_2 = models.CharField(max_length=30)
    picture = models.ImageField(upload_to='pictures/')

    # always keep record of the date when updated 
    updated = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.name


# ABout Section 
class About(models.Model):
    heading = models.CharField(max_length=50)
    career = models.CharField(max_length=50)
    description = models.TextField(blank=False)
    profile_img = models.ImageField(upload_to='profile/')

    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.career
    
class Profiles(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    social_name = models.CharField(max_length=20)
    link = models.URLField(max_length=200)


    def __str__(self):
        return self.social_name


# Skills section 
class Category(models.Model):
    name = models.CharField(max_length=30)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name


class Skills(models.Model):
    catergory = models.ForeignKey(Category, related_name="skills_set", on_delete=models.CASCADE)

    skills_name = models.CharField(max_length=20)


# Portfolio Section 
class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio/')
    link = models.URLField(max_length=200)


    def __str__(self):
        return f"Portfolio {self.id}"
