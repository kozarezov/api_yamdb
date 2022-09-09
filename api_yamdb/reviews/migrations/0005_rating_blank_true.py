from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('reviews', '0004_add_verbose_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='rating',
            field=models.IntegerField(blank=True, null=True,
                                      verbose_name='Рейтинг'),
        ),
    ]
