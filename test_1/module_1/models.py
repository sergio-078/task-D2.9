from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

# создание модели автора новости/статьи
class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    ratingAuthor = models.SmallIntegerField(default=0)

    # метод подсчёта рейтинга пользователя
    def update_rating(self):
        resultPost = self.post_set.aggregate(postRating=Sum('rating'))
        ratingPost = 0
        ratingPost += resultPost.get('postRating')

        resultComment = self.post_set.aggregate(commentRating=Sum('rating'))
        ratingComment = 0
        ratingComment += resultComment.get('commentRating')

        self.ratingAuthor = ratingPost*3 + ratingComment
        self.save()


# создание модели категории новости/статьи (спорт, политика, образование и т. д.)
class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)


# создание модели новости/статьи, которые создают пользователи
class Post(models.Model):
    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_CHOICES = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья'),
    )
    categoryType = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=ARTICLE)
    dateCreation = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=128)
    text = models.TextField()
    rating = models.SmallIntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    postCategory = models.ManyToManyField(Category, through='PostCategory')

    # метод лайков
    def like(self):
        self.rating += 1
        self.save()

    # метод дизлайков
    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return f'{self.text[0:29]} ...'


# создание промежуточной модели для связи "многие ко многим"
class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)


# создание модели комментарии
class Comment(models.Model):
    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)

    # метод лайков
    def like(self):
        self.rating += 1
        self.save()

    # метод дизлайков
    def dislike(self):
        self.rating -= 1
        self.save()
