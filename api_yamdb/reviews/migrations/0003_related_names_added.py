import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0002_add_model_review_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('text', models.TextField(max_length=200,
                                          verbose_name='Комментарий к отзыву')),
                ('pub_date', models.DateTimeField(auto_now_add=True,
                                                  verbose_name='Дата публикации')),
                ('author',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to=settings.AUTH_USER_MODEL,
                                   verbose_name='Автор комментария')),
            ],
        ),
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='reviews', to='reviews.title',
                verbose_name='Произведение'),
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.AddField(
            model_name='comment',
            name='review',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='comments', to='reviews.review'),
        ),
    ]
