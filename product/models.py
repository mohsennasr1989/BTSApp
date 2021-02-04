from django.db import models
from translate.models import Dictionary


class ProductUnit(models.Model):
    class Meta:
        verbose_name = 'Product Unit'
        verbose_name_plural = 'Product Units'
        ordering = ('id', 'name', 'unit', 'package')

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100, blank=False, default='Unit')
    translate = models.ForeignKey(Dictionary, on_delete=models.CASCADE, blank=False)
    unit = models.CharField(max_length=100, blank=False, verbose_name='Unit Name')
    package = models.CharField(max_length=100, blank=False, verbose_name='Package Name')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")


class PriceCurrency(models.Model):
    class Meta:
        verbose_name = 'Price Currency'
        verbose_name_plural = 'Price Currencies'
        ordering = ('id', 'name', 'decimal_number', 'translate')

    def __str__(self):
        return self.name

    name = models.CharField(max_length=20, default='IRR', verbose_name='Currency Name')
    translate = models.ForeignKey(Dictionary, on_delete=models.CASCADE, blank=False)
    decimal_number = models.IntegerField(default=0, verbose_name='Number of Digits in Decimal')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")


class ProductCategory(models.Model):
    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categories'
        ordering = ('id', 'name', 'order', 'translate')

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100, blank=False, verbose_name='Product Category Name')
    translate = models.ForeignKey(Dictionary, on_delete=models.CASCADE, blank=False)
    order = models.IntegerField(blank=False, verbose_name='Product Category Order')
    image = models.ImageField(blank=False, upload_to='product/category/', default='product/product_holder.jpg',
                              verbose_name='Product Category Image')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")


class ProductSubcategory(models.Model):
    class Meta:
        verbose_name = 'Product Subcategory'
        verbose_name_plural = 'Product Subcategories'
        ordering = ('id', 'category', 'name', 'order', 'translate')

    def __str__(self):
        return f'{self.category} - {self.name}'

    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, blank=False)
    name = models.CharField(max_length=100, blank=False, verbose_name='Product Subcategory Name')
    translate = models.ForeignKey(Dictionary, on_delete=models.CASCADE, blank=False)
    order = models.IntegerField(blank=False, verbose_name='Product Subcategory Order')
    image = models.ImageField(blank=False, upload_to='product/subcategory/', default='product/product_holder.jpg',
                              verbose_name='Product Subcategory Image')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")


class ProductType(models.Model):
    class Meta:
        verbose_name = 'Product Type'
        verbose_name_plural = 'Product Types'
        ordering = ('id', 'subcategory', 'name', 'specification', 'order', 'translate')

    def __str__(self):
        return f'{self.subcategory} - {self.name}'

    subcategory = models.ForeignKey(ProductSubcategory, on_delete=models.CASCADE, blank=False)
    name = models.CharField(max_length=100, blank=False, verbose_name='Product Type Name')
    translate = models.ForeignKey(Dictionary, on_delete=models.CASCADE, blank=False)
    specification = models.CharField(max_length=100, blank=True, verbose_name='Product Type Specification')
    technical_detail = models.TextField(blank=True, verbose_name='Product Type Technical detail')
    site_link = models.URLField(verbose_name='Product URL to Site Page', default='http://www.bts-co.com')
    order = models.IntegerField(blank=False, verbose_name='Product Type Order')
    image = models.ImageField(blank=False, upload_to='product/products/', default='product/product_holder.jpg',
                              verbose_name='Product Type Image')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")


class Product(models.Model):
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('id', 'product_type', 'code', 'new_code', 'size', 'unit', 'package_qty', 'order')

    def __str__(self):
        return self.code

    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, blank=False)
    code = models.CharField(max_length=10, blank=False, verbose_name='Product Code')
    new_code = models.CharField(max_length=10, blank=False, verbose_name='Product New Code')
    size = models.CharField(max_length=100, blank=False, verbose_name='Product Size')
    unit = models.ForeignKey(ProductUnit, on_delete=models.CASCADE)
    package_qty = models.IntegerField(default=1, verbose_name='Product Package Quantity')
    order = models.IntegerField(blank=False, verbose_name='Product Order')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")


class ProductPrice(models.Model):
    class Meta:
        verbose_name = 'Product Price'
        verbose_name_plural = 'Product Prices'
        ordering = ('id', 'tag', 'product', 'price', 'currency')

    def __str__(self):
        return [self.product.code, self.price, self.currency]

    tag = models.CharField(max_length=100, blank=False, verbose_name='Product Price List Name')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False)
    price = models.FloatField(default=1.0, verbose_name='Product Price')
    currency = models.ForeignKey(PriceCurrency, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
