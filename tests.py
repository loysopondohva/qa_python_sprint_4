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

#    def __init__(self) - 1 позитивная
#    def add_new_book(self, name) - 1 pos, 2 neg (уже есть в списке, больше 41 буквы)
#    def set_book_genre(self, name, genre) - 1 pos,  2 neg (нет в списке книг, жанра нет в списке жанров)
#   def get_book_genre(self, name) - 1 pos
#   def get_books_with_specific_genre(self, genre) 1 pos, 1 нег (жанра нет в списке жанров)
#   def get_books_genre(self) - 1 позитив
#   def get_books_for_children(self) - 1 позитив
#   def add_book_in_favorites(self, name) - 1 позитив, 2 негатив (название не в списке книг, книга уже есть в избранном)
#   def delete_book_from_favorites(self, name) - 1 позитив, 1 негатив (книги нет в избранном)
#   def get_list_of_favorites_books(self) - 1 позитив

