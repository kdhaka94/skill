# Generated by Django 3.1.7 on 2021-06-25 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20210625_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='latestnotification',
            name='job_status',
            field=models.CharField(blank=True, default='Active', max_length=254, null=True),
        ),
    ]