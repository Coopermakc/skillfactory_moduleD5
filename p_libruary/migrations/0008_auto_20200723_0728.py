# Generated by Django 2.2.6 on 2020-07-23 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_libruary', '0007_auto_20200723_0722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p_libruary.Publisher'),
        ),
    ]
