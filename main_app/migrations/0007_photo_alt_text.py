# Generated by Django 3.2 on 2021-05-04 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_request_is_hidden'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='alt_text',
            field=models.TextField(default='user photograph', max_length=2000),
            preserve_default=False,
        ),
    ]
