# Generated by Django 2.2.3 on 2019-07-15 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_user_postal_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='zipCode',
        ),
        migrations.AlterField(
            model_name='user',
            name='postal_code',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
