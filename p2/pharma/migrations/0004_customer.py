# Generated by Django 3.2 on 2021-06-17 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharma', '0003_product_catagory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=500)),
            ],
        ),
    ]
