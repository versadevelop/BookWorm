# Generated by Django 4.1.10 on 2023-07-11 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0002_alter_book_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
