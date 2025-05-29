import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

#+    def __init__(self) - 1 позитивная
#+    def add_new_book(self, name) - 1 pos, 2 neg (уже есть в списке, больше 41 буквы)
#+   def set_book_genre(self, name, genre) - 1 pos,  2 neg (нет в списке книг, жанра нет в списке жанров)
#+   def get_book_genre(self, name) - 1 pos
#+  def get_books_with_specific_genre(self, genre) 1 pos, 1 нег (жанра нет в списке жанров)
#+  def get_books_genre(self) - 1 позитив
#+   def get_books_for_children(self) - 1 позитив
#   def add_book_in_favorites(self, name) - 1 позитив, 2 негатив (название не в списке книг, книга уже есть в избранном)
#   def delete_book_from_favorites(self, name) - 1 позитив, 1 негатив (книги нет в избранном)
#   def get_list_of_favorites_books(self) - 1 позитив

# Проверка метода __init__ на корректную инициализацию books_genre и favorites
    def test_empty_books_genre_and_favorites_true(self):
        collector = BooksCollector()

        assert collector.books_genre == {} and collector.favorites == []

# Проверка метода __init__ на корректную инициализацию genre и genre_age_rating    
    def test_genre_list_and_age_rating_list_true(self):
        collector = BooksCollector()
        expected_genre_list = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        expected_genre_age_rating = ['Ужасы', 'Детективы']

        assert collector.genre == expected_genre_list and collector.genre_age_rating == expected_genre_age_rating

# Проверка метода add_new_book(), книга добавляется, при длине имени меньше 40 символов и отсутствии в коллекции  
    def test_add_new_book_14_letters_name_book_added(self):
        collector = BooksCollector()
        collector.add_new_book('Синий Трактор')

        assert len(collector.get_books_genre()) == 1
 
# Проверка метода add_new_book(), книга не добавляется при некорректном имени
    @pytest.mark.parametrize("name, expected_count", [
            ('Котёнок Гав', 1),  # Проверка при добавлении книги, которая уже есть в коллекции
            ('', 1),        # Проверка при пустом названии книги
            ('Барабулька' * 10, 1) # Проверка при названии книги больше 40 символов длинной
        ])
    def test_add_new_book_incorrect_name_add_book_not_add(self, name, expected_count):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_new_book('Котёнок Гав')

        assert len(collector.get_books_genre()) == expected_count

# # Проверка метода set_book_genre(). Жанр добавляется, если она есть в списке книг и жанр из списка жанров    
#     def test_set_book_genre_book_and_genre_in_collectin_genre_added(self):
#         collector = BooksCollector()
#         collector.add_new_book('Преступление и наказание')
#         collector.set_book_genre('Преступление и наказание', 'Детективы')
#         assert collector.get_books_with_specific_genre('Детективы') == ['Преступление и наказание']

# Проверка метода set_book_genre(). Жанр не добавляется
    @pytest.mark.parametrize('name, genre', [
        ('Преступление и наказание', 'Скороговорки'), # Жанр не существует
        ('Котёнок Гав', 'Мультфильмы'),     # Книга не существует
        ('Преступление и наказание', ''),   # Жанр не указан
        ('', 'Детективы'),                  # Название книги не указано
    ])
    def test_set_book_genre_book_wrong_genre_request_genre_not_added(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book('Преступление и наказание')
        collector.set_book_genre(name, genre)

        assert not collector.get_books_with_specific_genre(genre) == [name]

# Проверка метода set_book_genre() и get_books_with_specific_genre(), выводится список книг одного жанра
    def test_get_books_with_specific_genre_exist_genre_books_shows(self):
        collector = BooksCollector()
        books = [
            ['Звёздные Войны', 'Фантастика'],
            ['Доктор Кто', 'Фантастика'],
            ['Фунтик', 'Мультфильмы']
        ]
        for i in books:
            collector.add_new_book(i[0])
            collector.set_book_genre(i[0], i[1])

        assert collector.get_books_with_specific_genre('Фантастика') == ['Звёздные Войны', 'Доктор Кто']

# Проверка метода set_book_genre() и get_books_with_specific_genre() с некорректными параметрами genre, список книг не выводится  
    @pytest.mark.parametrize('genre', [
        ('Скороговорки'), # Жанр не существует
        ('Комедии'),    # Книг жанра нет в коллекции
        ('')            # Жанр не указан
    ])
    def test_get_books_with_specific_genre_wrong_genre_books_not_shows(self, genre):
        collector = BooksCollector()
        books = [
            ['Звёздные Войны', 'Фантастика'],
            ['Доктор Кто', 'Фантастика'],
            ['Фунтик', 'Мультфильмы']
        ]
        for i in books:
            collector.add_new_book(i[0])
            collector.set_book_genre(i[0], i[1])

        assert collector.get_books_with_specific_genre(genre) == []

# Проверка метода         collector = BooksCollector()() в коллекции есть книги, книги фильтруются и выводятся только детские
    def test_get_books_for_children_books_exist_shows_only_children_books(self):
        collector = BooksCollector()
        books = [
            ['Звёздные Войны', 'Фантастика'],
            ['Доктор Кто', 'Фантастика'],
            ['Фунтик', 'Мультфильмы'],
            ['Кошмар на улице Вязов', 'Ужасы'],
            ['Мост', 'Детектив']
        ] 
        for i in books:
            collector.add_new_book(i[0])
            collector.set_book_genre(i[0], i[1])

        assert collector.get_books_for_children() == ['Звёздные Войны', 'Доктор Кто', 'Фунтик']

