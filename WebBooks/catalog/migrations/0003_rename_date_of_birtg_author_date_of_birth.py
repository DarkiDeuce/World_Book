# Generated by Django 4.2 on 2023-05-05 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_book_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='date_of_birtg',
            new_name='date_of_birth',
        ),
    ]
