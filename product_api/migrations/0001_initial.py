# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(default=b'No description available', max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(serialize=False, primary_key=True)),
                ('date', models.DateTimeField()),
                ('quantity_ordered', models.PositiveIntegerField()),
                ('total_cost', models.PositiveIntegerField()),
                ('customer', models.ForeignKey(to='product_api.Customer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(default=b'No description available', max_length=150)),
                ('price_per_unit', models.PositiveIntegerField()),
                ('size', models.CharField(max_length=100, blank=True)),
                ('colour', models.CharField(max_length=30, blank=True)),
                ('category', models.ForeignKey(to='product_api.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=75, blank=True)),
                ('website', models.URLField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(to='product_api.Supplier', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(to='product_api.Product'),
            preserve_default=True,
        ),
    ]
