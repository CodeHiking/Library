# Generated by Django 4.1.7 on 2023-04-16 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_auto_20200412_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('education', 'Education'), ('entertainment', 'Entertainment'), ('comics', 'Comics'), ('biographie', 'Biographie'), ('history', 'History')], default='education', max_length=30),
        ),
    ]
