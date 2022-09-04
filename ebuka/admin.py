from django.contrib import admin

from ebuka.models import About, Category, Home, Portfolio, Profiles, Skills

# Register your models here.


# registering the home section 
admin.site.register(Home)

# About 
class ProfileInline(admin.TabularInline):
    model = Profiles
    extra = 1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [
        ProfileInline,
    ]


# Skills 
class SkillsInline(admin.TabularInline):
    model = Skills
    extra = 2


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        SkillsInline,
    ]


# Portfolio
admin.site.register(Portfolio)