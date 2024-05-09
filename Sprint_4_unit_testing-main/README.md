Список тестовых методов класса TestBooksCollector:
- test_add_new_book_add_three_books_added: Проверка добавления трех книг
- test_add_new_book_have_no_genre: Проверка наличия жанра по умолчанию (нет жанра)
- test_add_new_book_book_with_large_or_empty_name_not_added: Негативная проверка добавления книг с названием 0\40+ символов
- test_add_new_book_double_add_not_added: Негативная проверка повторного добавления книги
- test_set_book_genre_genre_added: Проверка добавления жанра книге
- test_change_genre_genre_changed: Проверка изменения жанра книги на новый
- test_set_book_genre_with_excluded_genre: Негативная проверка добавления несуществующего жанра
- test_get_book_with_specific_genre_genre_specified: Проверка вывода книги определенного жанра
- test_get_book_with_wrong_genre_no_such_book: Негативная проверка фильтра по несуществующему жанру
- test_get_books_for_children_no_age_restricted_books: Проверка вывода списка книг без возрастного ограничения
- test_add_book_in_favorites_added_one_book: Проверка добавления книги в избранное
- test_add_book_in_favorites_twice_not_added: Негативная проверка повторного добавления книги в избранное
- test_add_book_in_favorites_add_non_dict_book_not_added: Негативная проверка добавления книги не из books_genre
- test_delete_book_from_favorites_book_is_deleted: Проверка удаления книги из избранного