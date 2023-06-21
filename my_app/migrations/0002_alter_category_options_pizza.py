# Generated by Django 4.2.1 on 2023-05-10 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Categorys', 'verbose_name_plural': 'Categorys'},
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=3, max_digits=7)),
                ('slug', models.SlugField(error_messages={'unique': 'This slug already exist!'}, unique=True)),
                ('image', models.ImageField(upload_to='Pizza_image/')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.category')),
            ],
            options={
                'verbose_name': 'Pizza',
                'verbose_name_plural': 'Pizza',
            },
        ),
    ]