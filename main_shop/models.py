from django.db import models


#***********#
# Guitar Examples

# Parts of Guitar

# Cart

# Cart Product

# Order

# Customer

# Scpecifications
#***********#

class GuitarExamples(models.Model):
    # можеш юзать models.TextField вмєсто models CharField,
    # в ньом не нада указувать длінну
    guitar_model = models.CharField(max_length=250)
    brand = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='total price')
    guitar_img = models.ImageField(verbose_name="example of a guitar")

    def __str__(self):
        return "Guitar model: {}. Price: {}. Brand {}.".format(self.guitar_model, self.price, self.brand)

    def get_jsonified(self):
        return {
            'guitar_model': self.guitar_model,
            'brand': self.brand,
            # 'price': self.price,
            # 'guitar_img': self.guitar_img,
        }

    class Meta:

        verbose_name = "GuitarExample"
        verbose_name_plural = "GuitarExamples"
