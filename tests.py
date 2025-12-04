import pytest

from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_book(self):
        collector = BooksCollector()
        collector.add_new_book('Маугли')
        assert collector.books_genre['Маугли'] == ''

    def test_add_new_book_length_more_40(self):
        collector = BooksCollector()
        name_length = 'x' * 41 
        collector.add_new_book(name_length)
        assert name_length not in collector.books_genre

    def test_add_new_book_length_is_0(self):
        collector = BooksCollector()
        name_length = ''
        collector.add_new_book(name_length)
        assert name_length not in collector.books_genre

    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Приключения Шерлока Холмса')
        collector.set_book_genre('Приключения Шерлока Холмса', 'Детективы')
        assert collector.get_book_genre('Приключения Шерлока Холмса') == 'Детективы'
    
    def test_set_book_unacceptable_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Приключения Шерлока Холмса')
        collector.set_book_genre('Приключения Шерлока Холмса', 'Поэзия')
        assert collector.get_book_genre('Приключения Шерлока Холмса') == ''

    def test_set_and_get_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Приключения Шерлока Холмса')
        collector.set_book_genre('Приключения Шерлока Холмса', 'Детективы')
        assert collector.get_book_genre('Приключения Шерлока Холмса') == 'Детективы'

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Приключения Шерлока Холмса')
        collector.set_book_genre('Приключения Шерлока Холмса', 'Детективы')
        assert collector.get_books_with_specific_genre('Детективы') == ['Приключения Шерлока Холмса']

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Приключения Шерлока Холмса')
        assert collector.get_books_genre() == {'Приключения Шерлока Холмса': ''}
    
    def test_get_books_for_children_list_is_not_empty(self):
        collector = BooksCollector()
        collector.add_new_book('Маугли')
        collector.set_book_genre('Маугли', 'Мультфильмы')
        assert 'Маугли' in collector.get_books_for_children()

    def test_get_books_for_children_list_is_empty(self):
        collector = BooksCollector()
        collector.add_new_book('Приключения Шерлока Холмса')
        collector.set_book_genre('Приключения Шерлока Холмса', 'Детективы')
        assert 'Приключения Шерлока Холмса' not in collector.get_books_for_children()
    
    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Приключения Шерлока Холмса')
        collector.add_book_in_favorites('Приключения Шерлока Холмса')
        assert 'Приключения Шерлока Холмса' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_twice(self):
        collector = BooksCollector()
        collector.add_new_book('Приключения Шерлока Холмса')
        collector.add_book_in_favorites('Приключения Шерлока Холмса')
        collector.add_book_in_favorites('Приключения Шерлока Холмса')
        assert collector.get_list_of_favorites_books().count('Приключения Шерлока Холмса') == 1

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Приключения Шерлока Холмса')
        collector.add_book_in_favorites('Приключения Шерлока Холмса')
        collector.delete_book_from_favorites('Приключения Шерлока Холмса')
        assert 'Приключения Шерлока Холмса' not in collector.get_list_of_favorites_books()

    @pytest.mark.parametrize('book_name', [
        'Приключения Шерлока Холмса',
        'Маугли'
    ])
    def test_get_list_of_favorites_books_have_favorites_books(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.get_list_of_favorites_books()