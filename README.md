# qa_python Спринт 4
Создание экземпляра для теста вынесено в файл с фикстурми conftest.py
Список реализованных тестов:

# 1. Проверка метода __init__ на корректную инициализацию books_genre 
    test_init_books_genre_no_data_empty()

# 2. Проверка метода __init__ на корректную favorites
    test_init_favorites_no_data_empty()

# 3. Проверка метода __init__ на корректную инициализацию genre    
    test_init_genre_list_no_data_generated_list()

# 4. Проверка метода __init__ на корректную инициализациюgenre_age_rating    
    test_init_genre_age_rating_list_no_data_generated_list()

# 5. Проверка метода add_new_book(), книга добавляется, при длине имени меньше 40 символов и отсутствии в коллекции  
    test_add_new_book_name_lenght_less_40_book_added()

# 6. Проверка метода add_new_book(), книга не добавляется при некорректном имени
    test_add_new_book_incorrect_name_add_book_not_add()

# 7. Проверка метода set_book_genre(). Жанр добавляется, если она есть в списке книг и жанр из списка жанров    
    test_set_book_genre_book_and_genre_in_collectin_genre_added()

# 8. Проверка метода set_book_genre(). С некорректными данными при добавлении жанра к книге. Жанр не добавляется
    test_set_book_genre_book_wrong_genre_request_genre_not_added()

# 9. Проверка метода get_book_genre(). Добавлена 1 книга, получаем её жанр. Жанр выводится
    test_get_book_genre_one_book_genre_getted()    

# 10. Проверка метода get_books_with_specific_genre(), выводится список книг одного жанра
    test_get_books_with_specific_genre_exist_genre_books_shows()

# 11. Проверка метода get_books_with_specific_genre() с некорректными параметрами genre, список книг не выводится  
    test_get_books_with_specific_genre_wrong_genre_empty_books_list()

# 12. Проверка метода get_books_genre(). Добавлены 2 книги, выводится словарь с книгами.
    test_get_books_with_specific_genre_wrong_genre_empty_books_list()

# 13. Проверка метода get_books_for_children() в коллекции есть книги, книги фильтруются и выводятся только детские
    test_get_books_for_children_books_exist_shows_only_children_books()

# 14. Проверка метода add_book_in_favorites(). Добавляем 2 книги в избранное. Книги доавляются. 
    test_add_book_in_favorites_two_books_add_book_added()

# 15. Проверка  delete_book_from_favorites(). Две книги добавлены, одна удаляется. Остаётся одна книга в избранном
    test_delete_book_from_favorites_two_books_added_one_deleted_one_book_left()

# 16. Проверка метода get_list_of_favorites_books() 2 книги добавлены, список избранного выводится
    test_get_list_of_favorites_books_two_books_added_favorites_books_returned()