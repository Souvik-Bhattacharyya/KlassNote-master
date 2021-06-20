from django.db import models
from django.contrib.auth.models import User


class ProductCategory(models.Model):
    name = models.CharField(max_length=50, default="", null=False)

    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categories'

    def __str__(self):
        return self.name

    @property
    def get_products(self):
        return Product.objects.filter(category=self)

    @property
    def number_of_products(self):
        return len(self.get_products)


class Product(models.Model):
    category = models.ForeignKey(
        ProductCategory, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, default='', null=False)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(default=0.0, null=True, blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name

    @property
    def thumbnail(self):
        return self.get_images[0]

    @property
    def get_images(self):
        return ProductImage.objects.filter(product=self)

    @property
    def get_specifications(self):
        return ProductSpecification.objects.filter(product=self)

    @property
    def get_related_products(self):
        return RelatedProduct.objects.filter(product=self)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product_image/", null=True)


class ProductSpecification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    subject = models.CharField(max_length=500, default='', null=False)
    specification = models.TextField()


class RelatedProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    related = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='rel_prod', related_query_name='rel_prod')


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, null=False)
