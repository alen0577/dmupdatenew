# Generated by Django 4.1.7 on 2023-06-21 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("DMcoreapp", "0063_lead_assign"),
    ]

    operations = [
        migrations.RemoveField(model_name="all_leads", name="ex_duration",),
    ]
