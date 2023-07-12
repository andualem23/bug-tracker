# Generated by Django 4.2.3 on 2023-07-06 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0007_alter_ticket_priority_alter_ticket_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='Attachments',
            field=models.ImageField(blank=True, null=True, upload_to='attachments/'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='priority',
            field=models.CharField(choices=[('None', 'None'), ('High', 'High'), ('Low', 'Low'), ('Medium', 'Medium')], max_length=40),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='type',
            field=models.CharField(choices=[('Other Comments', 'Other Comments'), ('Feature request', 'Feature Request'), ('Bugs/Errors', 'Bugs/Errors'), ('Traning/documents request', 'Traning/documents Request')], max_length=40),
        ),
    ]