# Generated by Django 2.0.3 on 2018-03-20 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0005_auto_20180320_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='platform',
            field=models.ForeignKey(max_length=128, null=True, on_delete=django.db.models.deletion.SET_NULL, to='asset.platform', verbose_name='平台'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='region',
            field=models.ForeignKey(max_length=256, null=True, on_delete=django.db.models.deletion.SET_NULL, to='asset.region', verbose_name='区域'),
        ),
    ]