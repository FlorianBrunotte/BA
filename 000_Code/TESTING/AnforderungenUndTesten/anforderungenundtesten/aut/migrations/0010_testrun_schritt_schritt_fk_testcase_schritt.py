# Generated by Django 3.1.2 on 2021-01-18 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aut', '0009_auto_20210118_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='testrun_schritt',
            name='schritt_fk_testcase_schritt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aut.testcase_schritt'),
        ),
    ]
