from django.db import models

class Concerns(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45,verbose_name="Concern Name",unique=True)
    ratings = (
        ('0', 'Neutral'),
        ('1', 'Ethical'),
        ('2', 'Unethical'),
    )
    rating = models.CharField(max_length=2, choices=ratings,default=0,verbose_name="Concern Rating")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
            managed = True
            db_table = 'concerns'
            # this do the trick that django admin doesn't place a further s after
            # the table name. Source: https://stackoverflow.com/questions/2587707/django-fix-admin-plural
            verbose_name_plural = "concerns"
            ordering = ("name",)

class Companies(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45,unique=True,verbose_name="Company Name")
    logo = models.CharField(max_length=45,verbose_name="Company Logo")
    concern = models.ForeignKey(Concerns, models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'companies'
        unique_together = (('id', 'concern'),)
        verbose_name_plural = "companies"
        ordering = ("name",)


class Brands(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=45, verbose_name= "Brand Name")
    logo = models.CharField(max_length=200, verbose_name="Brand Logo")
    rating = models.CharField(max_length=1, verbose_name="Brand Rating")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    company = models.ForeignKey(Companies, models.CASCADE)
    concern = models.ForeignKey(Concerns, models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'brands'
        verbose_name_plural = "brands"

class Products(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=45,verbose_name="Product Name")
    ean = models.CharField(max_length=45,verbose_name="Product EAN")
    image = models.CharField(max_length=45,verbose_name="Product Image")
    group = models.CharField(max_length=200,verbose_name="Product Group")
    brand = models.ForeignKey(Brands, models.CASCADE)
    concern = models.ForeignKey(Concerns, models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'products'
        unique_together = (('id','brand'),)
        verbose_name_plural = "products"
