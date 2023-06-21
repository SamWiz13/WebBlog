from django.db import models
from django.urls import reverse

class Category(models.Model):
    #  Category model for Pizza
    
    name =models.CharField(max_length=255, null=False, blank=False, unique=True, error_messages={"unique" : "This name already exist!"})
    slug =models.SlugField(null=False, blank=False, unique=True,  error_messages ={"unique" : "This slug already exist!"})


    def get_absolute_url(self):
        return reverse('myapp:pizza_list_by_category', args =[self.slug])

    class Meta:
        verbose_name =('Categorys')
        verbose_name_plural =('Categorys')

    def __str__(self):
        for_admin =f"{self.name} {self.slug}"
        return for_admin
    


class Pizza(models.Model):
    # Pizza model 
    category =models.ForeignKey(Category, on_delete =models.CASCADE)
    title =models.CharField(max_length =255)
    description =models.TextField()
    price =models.DecimalField(max_digits=10, decimal_places=2)
    slug =models.SlugField(null=False, blank=False, unique=True,  error_messages ={"unique" : "This slug already exist!"})
    image =models.ImageField(upload_to ="Pizza_image/")



    updated =models.DateTimeField(auto_now= True)
    created_at =models.DateTimeField(auto_now_add=True)

    
    
    def get_absolute_url(self):
        return reverse('myapp:pizza-detail', args =[self.id, self.slug])

    class Meta:
        verbose_name =('Pizza')
        verbose_name_plural =('Pizza')

    def __str__(self):
        for_admin =f"{self.title} {self.slug}"
        return for_admin


class  PizzaNumbers(models.Model):
    # Pizza numbers
    branches =models.PositiveIntegerField(default =1)
    awards =models.PositiveIntegerField(default =1)
    customer =models.PositiveIntegerField(default =1)
    staff =models.PositiveIntegerField(default =1)

    updated =models.DateTimeField(auto_now= True)
    created_at =models.DateTimeField(auto_now_add=True)



    class Meta:
        verbose_name =('Pizza Number')
        verbose_name_plural =('Pizza Number')

    def __str__(self):
        for_admin =f"{self.branches} {self.awards}"
        return for_admin



class Chef(models.Model):
    #  Chef model

    first_name =models.CharField(max_length=255)
    last_name =models.CharField(max_length=255)
    specialist =models.CharField(max_length=255)
    description =models.TextField()
    profile_image =models.ImageField(upload_to='chef/')
    updated =models.DateTimeField(auto_now= True)
    created_at =models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name =('Chef')
        verbose_name_plural =('Chef')


    def get_full_name(self):
        return f"{self.first_name}  {self.last_name}"


    def __str__(self):
        for_admin =f"{self.first_name} {self.specialist}"
        return for_admin
