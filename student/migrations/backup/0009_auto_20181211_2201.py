# Generated by Django 2.1.3 on 2018-12-11 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_auto_20181211_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplines',
            name='status',
            field=models.IntegerField(blank=True, choices=[(1, 'Active'), (0, 'Inactive'), (2, 'Done'), (3, 'Cancelled')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='disciplines',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='discipline_type', to='student.Discipline_type'),
        ),
    ]
