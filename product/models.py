from django.db import models


class ProductUnit(models.Model):
    class Meta:
        verbose_name = 'Product Unit'
        verbose_name_plural = 'Product Units'
        ordering = ('id', 'unit', 'package')

    def __str__(self):
        return self.unit

    unit = models.CharField(max_length=100, blank=False, verbose_name='Unit Name')
    package = models.CharField(max_length=100, blank=False, verbose_name='Package Name')


class PriceCurrency(models.Model):
    class Meta:
        verbose_name = 'Price Currency'
        verbose_name_plural = 'Price Currencies'
        ordering = ('id', 'name', 'decimal_number')

    def __str__(self):
        return self.name

    name = models.CharField(max_length=20, default='IRR', verbose_name='Currency Name')
    decimal_number = models.IntegerField(default=0, verbose_name='Number of Digits in Decimal')


class ProductCategory(models.Model):
    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categories'
        ordering = ('id', 'name', 'order')

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100, blank=False, verbose_name='Product Category Name')
    order = models.IntegerField(blank=False, verbose_name='Product Category Order')
    image = models.ImageField(blank=False, upload_to='product/category', default='product_holder.jpg',
                              verbose_name='Product Category Image')


class ProductSubcategory(models.Model):
    class Meta:
        verbose_name = 'Product Subcategory'
        verbose_name_plural = 'Product Subcategories'
        ordering = ('id', 'category', 'name', 'order')

    def __str__(self):
        return self.name

    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, blank=False)
    name = models.CharField(max_length=100, blank=False, verbose_name='Product Subcategory Name')
    order = models.IntegerField(blank=False, verbose_name='Product Subcategory Order')
    image = models.ImageField(blank=False, upload_to='product/subcategory', default='product_holder.jpg',
                              verbose_name='Product Subcategory Image')


class ProductType(models.Model):
    class Meta:
        verbose_name = 'Product Type'
        verbose_name_plural = 'Product Types'
        ordering = ('id', 'subcategory', 'name', 'specification', 'order')

    def __str__(self):
        return self.name

    subcategory = models.ForeignKey(ProductSubcategory, on_delete=models.CASCADE, blank=False)
    name = models.CharField(max_length=100, blank=False, verbose_name='Product Type Name')
    specification = models.CharField(max_length=100, verbose_name='Product Type Specification')
    technical_detail = models.TextField(verbose_name='Product Type Technical detail')
    site_link = models.URLField(verbose_name='Product URL to Site Page', default='http://www.bts-co.com')
    order = models.IntegerField(blank=False, verbose_name='Product Type Order')
    image = models.ImageField(blank=False, upload_to='product/products', default='product_holder.jpg',
                              verbose_name='Product Type Image')


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
    order = models.IntegerField(blank=False, verbose_name='Product Category Order')


class ProductPrice(models.Model):
    class Meta:
        verbose_name = 'Product Price'
        verbose_name_plural = 'Product Prices'
        ordering = ('id', 'tag', 'product', 'price', 'currency')

    def __str__(self):
        return [self.product, self.price, self.currency]

    tag = models.CharField(max_length=100, blank=False, verbose_name='Product Price List Name')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False)
    price = models.FloatField(default=1.0, verbose_name='Product Price')
    currency = models.ForeignKey(PriceCurrency, on_delete=models.CASCADE)
