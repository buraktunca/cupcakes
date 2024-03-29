# Generated by Django 3.0.7 on 2020-10-09 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_altcategory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='altcategory',
            options={'ordering': ['-created_at'], 'verbose_name_plural': 'AltCategories'},
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('old_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=9)),
                ('image', models.ImageField(max_length=50, upload_to='products')),
                ('is_active', models.BooleanField(default=True)),
                ('is_bestseller', models.BooleanField(default=False)),
                ('quantity', models.IntegerField()),
                ('description', models.TextField()),
                ('meta_keywords', models.CharField(help_text='Comma-delimited set of SEO keywords for meta tag', max_length=255)),
                ('meta_description', models.CharField(help_text='Content for description meta tag', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.AltCategory')),
            ],
            options={
                'db_table': 'products',
                'ordering': ['-created_at'],
            },
        ),
    ]
