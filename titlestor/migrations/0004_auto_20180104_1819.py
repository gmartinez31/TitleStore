# Generated by Django 2.0 on 2018-01-04 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titlestor', '0003_auto_20180104_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='firstName',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='client',
            name='lastName',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='client',
            name='middleName',
            field=models.CharField(max_length=256),
        ),
    ]