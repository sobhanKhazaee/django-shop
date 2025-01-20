from slugify import slugify

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='products/image/', default='products/images/default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(default="", null=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)  # استفاده از slugify از python-slugify
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("productDetails", args=[self.slug])

    def __str__(self):
        return self.name
