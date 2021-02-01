# Generated by Django 3.1.2 on 2021-01-13 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aut', '0002_auto_20210104_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testcase_schritt',
            name='schritt_ergebnis',
        ),
        migrations.RemoveField(
            model_name='testcase_schritt',
            name='schritt_tatsaechlichesergebnis',
        ),
        migrations.CreateModel(
            name='testrun_schritt',
            fields=[
                ('schritt_pk_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('schritt_tatsaechlichesergebnis', models.CharField(blank=True, max_length=128, null=True)),
                ('schritt_ergebnis', models.CharField(blank=True, choices=[('n', 'no run yet'), ('p', 'pass'), ('f', 'fail')], max_length=1)),
                ('schritt_fk_testrun', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aut.testrun')),
            ],
        ),
    ]
