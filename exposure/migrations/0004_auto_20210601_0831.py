# Generated by Django 3.2.3 on 2021-06-01 11:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('midia', '0005_auto_20210601_0831'),
        ('exposure', '0003_auto_20210601_0759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exposure',
            name='album_audio',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='midia.albumaudio', verbose_name='Álbum de áudio'),
        ),
        migrations.AlterField(
            model_name='exposure',
            name='album_image',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='midia.albumimage', verbose_name='Álbum de imagem'),
        ),
        migrations.AlterField(
            model_name='exposure',
            name='album_video',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='midia.albumvideo', verbose_name='Álbum de video'),
        ),
        migrations.AlterField(
            model_name='exposure',
            name='content',
            field=models.CharField(max_length=200, verbose_name='Descrição exposição'),
        ),
        migrations.AlterField(
            model_name='exposure',
            name='is_public',
            field=models.CharField(choices=[('ARQUIVAR', 'Arquivar'), ('PUBLICAR', 'Publicar')], default='Arquivar', max_length=20, verbose_name='Status de publicação'),
        ),
        migrations.AlterField(
            model_name='exposure',
            name='legend',
            field=models.CharField(max_length=200, verbose_name='Legenda da exposição'),
        ),
        migrations.AlterField(
            model_name='exposure',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Título da exposição'),
        ),
        migrations.AlterField(
            model_name='exposure',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Usuários'),
        ),
    ]