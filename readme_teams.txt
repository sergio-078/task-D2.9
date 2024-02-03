Здесь описаны пошаговые команды в консоли shell для итогового задания D2.9.

1. Создать двух пользователей:
Se=User.objects.create_user(username='Sergei')
Ru=User.objects.create_user(username='Ruslan')

2. Создать два объекта модели Author, связанные с пользователями:
Author.objects.create(authorUser=Se)
Author.objects.create(authorUser=Ru)

3. Добавить 4 категории в модель Category:
Category.objects.create(name='sport')
Category.objects.create(name='weather')
Category.objects.create(name='celebrities')
Category.objects.create(name='volunteering')

4. Добавить 2 статьи и 1 новость:
author_1 = Author.objects.get(id=1)
Post.objects.create(author=author_1, categoryType='NW', title='chess competitions', text='news about chess competitions')
Post.objects.create(author=author_1, categoryType='AR', title='volunteering at school', text='an article about volunteering at school')
Post.objects.create(author=author_1, categoryType='AR', title='celebrities today', text='an article about celebrities')

5. Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий):
Post.objects.get(id=1).postCategory.add(Category.objects.get(id=1))
Post.objects.get(id=1).postCategory.add(Category.objects.get(id=4))
Post.objects.get(id=1).postCategory.add(Category.objects.get(id=3))
Post.objects.get(id=2).postCategory.add(Category.objects.get(id=4))
Post.objects.get(id=2).postCategory.add(Category.objects.get(id=3))
Post.objects.get(id=3).postCategory.add(Category.objects.get(id=3))
Post.objects.get(id=3).postCategory.add(Category.objects.get(id=4))

6. Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий):
Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=2).authorUser, text='Comment on sports news - Ruslan')
Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=2).authorUser, text='Comment on sports news - Sergei')
Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=1).authorUser, text='Comment on sports news - Sergei')
Comment.objects.create(commentPost=Post.objects.get(id=2), commentUser=Author.objects.get(id=2).authorUser, text='Comment on the article about volunteering - Ruslan')
Comment.objects.create(commentPost=Post.objects.get(id=3), commentUser=Author.objects.get(id=2).authorUser, text='Сomment on an article about celebrities - Ruslan')
Comment.objects.create(commentPost=Post.objects.get(id=3), commentUser=Author.objects.get(id=1).authorUser, text='Сomment on an article about celebrities - Sergei')
Comment.objects.create(commentPost=Post.objects.get(id=3), commentUser=Author.objects.get(id=2).authorUser, text='Сomment on an article about celebrities - Ruslan (two)')

7. Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов:
Comment.objects.get(id=1).like()	# лайк для 1-го комментария
Comment.objects.get(id=2).like()	# лайк для 2-го комментария
Comment.objects.get(id=3).like()	# лайк для 3-го комментария
Comment.objects.get(id=4).like()	# лайк для 4-го комментария
Comment.objects.get(id=5).like()	# лайк для 5-го комментария
Comment.objects.get(id=6).like()	# лайк для 6-го комментария
Comment.objects.get(id=7).like()	# лайк для 7-го комментария

Comment.objects.get(id=1).like()	# лайк для 1-го комментария
Comment.objects.get(id=1).like()	# лайк для 1-го комментария
Comment.objects.get(id=1).like()	# лайк для 1-го комментария

Comment.objects.get(id=1).rating	# результат равен 4

Comment.objects.get(id=1).dislike()	# дизлайк для 1-го комментария

Comment.objects.get(id=1).rating	# результат равен 3

Post.objects.get(id=1).like()		# лайк для 1-ой новости
Post.objects.get(id=2).like()		# лайк для 1-ой статьи
Post.objects.get(id=2).like()		# лайк для 1-ой статьи
Post.objects.get(id=2).like()		# лайк для 1-ой статьи
Post.objects.get(id=3).like()		# лайк для 2-ой статьи

8. Обновить рейтинги пользователей:
Author.objects.get(id=1).update_rating()
Author.objects.get(id=1).ratingAuthor
# второй автор не писал ни статей, ни новостей

9. Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта):
for i in Author.objects.order_by('-ratingAuthor')[:1]:
    f'Рейтинг пользователя {i.authorUser.username} составляет {i.ratingAuthor} лайков!'		# 'Рейтинг пользователя Sergei составляет 12 лайков!'

10. Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье:
for i in Post.objects.order_by('-rating')[:1]:
    print ('Лучшая статья была опубликована - ' + i.dateCreation.strftime('%d.%m.%Y %H:%M'))
    print ('Автор лучшей статьи/новости - ' + i.author.authorUser.username)
    print ('Рейтинг лучшей статьи/новости - ' + str(i.rating))
    print ('Заголовок лучшей статьи/новости - ' + i.title)
    print('Превью лучшей статьи/новости - {}.'.format(i.preview()))

11. Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье:
Post.objects.order_by('-rating')[0].comment_set.all().values('dateCreation', 'commentUser__username', 'rating', 'text')




