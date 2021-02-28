# Generated by Django 3.1.4 on 2021-02-18 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GuitarExamples',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guitar_model', models.CharField(max_length=250)),
                ('brand', models.CharField(max_length=250)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='total price')),
                ('guitar_img', models.ImageField(upload_to='', verbose_name='example of a guitar')),
            ],
            options={
                'verbose_name': 'GuitarExample',
                'verbose_name_plural': 'GuitarExamples',
            },
        ),
    ]