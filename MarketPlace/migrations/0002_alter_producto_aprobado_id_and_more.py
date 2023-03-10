# Generated by Django 4.1.4 on 2022-12-26 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MarketPlace', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='aprobado_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='MarketPlace.aprobado'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='categoria_id',
            field=models.ForeignKey(on_delete=models.SET(4), to='MarketPlace.categoria'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='envio_id',
            field=models.ForeignKey(on_delete=models.SET(2), to='MarketPlace.envio'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='estado_id',
            field=models.ForeignKey(on_delete=models.SET(4), to='MarketPlace.estado_producto'),
        ),
        migrations.CreateModel(
            name='imagenCarrusel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(null=True, upload_to='carrusel')),
                ('carrusel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='MarketPlace.carrusel')),
            ],
        ),
    ]
