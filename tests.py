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
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

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

    @pytest.mark.parametrize('book_name, genre', [
        ('Приключения Шерлока Холмса', 'Детективы'),
        ('Маугли', 'Мультфильмы')
    ])
    def test_get_list_of_favorites_books_have_favorites_books(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.get_list_of_favorites_books()