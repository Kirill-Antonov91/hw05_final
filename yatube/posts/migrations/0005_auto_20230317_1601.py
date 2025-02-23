# Generated by Django 2.2.16 on 2023-03-17 13:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("posts", "0004_post_image"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="group",
            options={
                "verbose_name": "Группа",
                "verbose_name_plural": "Группы",
            },
        ),
        migrations.AlterModelOptions(
            name="post",
            options={
                "ordering": ["-pub_date"],
                "verbose_name": "Пост",
                "verbose_name_plural": "Посты",
            },
        ),
        migrations.AlterField(
            model_name="group",
            name="description",
            field=models.TextField(verbose_name="Описание"),
        ),
        migrations.AlterField(
            model_name="group",
            name="slug",
            field=models.SlugField(unique=True, verbose_name="Тег"),
        ),
        migrations.AlterField(
            model_name="group",
            name="title",
            field=models.CharField(max_length=200, verbose_name="Заголовок"),
        ),
        migrations.AlterField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="posts",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Автор",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="group",
            field=models.ForeignKey(
                blank=True,
                help_text="Выберите группу",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="posts",
                to="posts.Group",
                verbose_name="Группа",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="posts/",
                verbose_name="Картинка",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="pub_date",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="Дата публикации"
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="text",
            field=models.TextField(
                help_text="Введите текст поста", verbose_name="Текст поста"
            ),
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField(verbose_name="Текст комментария")),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор",
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="posts.Post",
                        verbose_name="Пост",
                    ),
                ),
            ],
            options={
                "verbose_name": "Комментарий",
                "verbose_name_plural": "Комментарии",
                "ordering": ["-created"],
            },
        ),
    ]
