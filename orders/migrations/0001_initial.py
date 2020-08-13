# Generated by Django 3.0.4 on 2020-08-12 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=10)),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=50)),
                ('active', models.BooleanField(default=True)),
                ('expiry', models.DateTimeField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('max_times', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('payment_status', models.CharField(blank=True, max_length=20, null=True)),
                ('ordered', models.BooleanField(default=False)),
                ('completed', models.BooleanField(default=False)),
                ('tax', models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True)),
                ('delivery_fee', models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True)),
                ('coupon', models.CharField(blank=True, max_length=20, null=True)),
                ('coupon_discount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50, null=True)),
                ('cart_price', models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True)),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True)),
                ('order_items', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razorpay_payment_id', models.CharField(max_length=255)),
                ('razorpay_order_id', models.CharField(max_length=255)),
                ('razorpay_signature', models.CharField(max_length=255)),
                ('payment_complete', models.BooleanField(blank=True, default=False, null=True)),
                ('payment_status', models.CharField(blank=True, max_length=255, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserAppliedCouponList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='UserCoupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('times', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('coupon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Coupon')),
            ],
        ),
    ]
