from django.db import models
from django.urls import reverse


class Category(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='scategory', null=True, blank=True)
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='category/%y/%m/%d/', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self, page_number=1):
        return reverse('home:category', args=[self.slug, page_number])


class Feature(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ManyToManyField(Category, related_name='products')
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='products/%y/%m/%d/')
    description = models.TextField()
    features = models.ManyToManyField(Feature)
    related_products = models.ManyToManyField('self', blank=True)
    price = models.IntegerField()
    discount = models.IntegerField(default=0)
    Sales_number = models.IntegerField(default=0)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home:product_detail', args=[self.slug])

    def get_asking_price(self):
        discount = self.price * self.discount / 100
        return self.price - discount


class Order(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200, null=True)
    province = models.CharField(max_length=200, null=True)
    City = models.CharField(max_length=200, null=True)
    street = models.CharField(max_length=200, null=True)
    apartment = models.CharField(max_length=200, null=True)
    Postalcode = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=11, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    products = models.ManyToManyField('Product', through='OrderItem')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Order {self.pk} - {self.name}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} of {self.product.name}'

    # def get_total_item_price(self):
    #     return self.quantity * self.product.get_asking_price
    #
    # def get_final_price(self):
    #     return self.get_total_item_price()
