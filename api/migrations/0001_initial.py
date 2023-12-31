# Generated by Django 4.2.6 on 2023-12-16 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EShopHub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Сыдр', max_length=100)),
                ('description', models.TextField(blank=True)),
                ('price', models.FloatField(default=10)),
                ('data_create', models.DateField(auto_now_add=True)),
                ('date_update', models.DateField(auto_now=True)),
                ('exist', models.BooleanField(default=True)),
                ('photo', models.ImageField(null=True, upload_to='image/%Y/%m/$d')),
            ],
        ),
    ]
