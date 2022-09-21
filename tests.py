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

    # Test the set_book_ratings() actually sets rating between 1 and 10 for existing book
    def test_set_book_rating_set_rating_5_for_existing_book(self, collector):
        collector.add_new_book('The elegant universe')
        collector.set_book_rating('The elegant universe', 5)

        assert collector.books_rating['The elegant universe'] == 5

    # Test the set_book_ratings() does not set rating above 10 for existing book
    def test_set_book_rating_doesnt_set_rating_11_for_existing_book(self, collector):
        collector.add_new_book('The elegant universe')
        collector.set_book_rating('The elegant universe', 11)

        assert collector.books_rating['The elegant universe'] == 1

    # Test the set_book_ratings() does not set rating below 1 for existing book
    def test_set_book_rating_doesnt_set_rating_0_for_existing_book(self, collector):
        collector.add_new_book('The elegant universe')
        collector.set_book_rating('The elegant universe', 0)

        assert collector.books_rating['The elegant universe'] == 1

    # Test that get_book_with_specific_rating returns appropriate book for the existing rating
    def test_get_book_with_specific_rating_get_book_with_existing_rating(self, collector):

        collector.add_new_book('The elegant universe')
        collector.set_book_rating('The elegant universe', 10)

        collector.add_new_book('Motivation and personality')
        collector.set_book_rating('Motivation and personality', 9)

        collector.add_new_book('Maus: A Survivor’s Tale')
        collector.set_book_rating('Maus: A Survivor’s Tale', 8)

        assert collector.get_books_with_specific_rating(9)[0] == 'Motivation and personality' and len(collector.get_books_with_specific_rating(9)) == 1

    # Test that get_book_with_specific_rating returns empty list if non-existing rating value is given
    def test_get_book_with_specific_rating_get_book_with_non_existing_rating_returns_empty_list(self, collector):

        collector.add_new_book('The elegant universe')
        collector.set_book_rating('The elegant universe', 10)

        collector.add_new_book('Motivation and personality')
        collector.set_book_rating('Motivation and personality', 9)

        collector.add_new_book('Maus: A Survivor’s Tale')
        collector.set_book_rating('Maus: A Survivor’s Tale', 8)

        assert len(collector.get_books_with_specific_rating(7)) == 0

    # Test that get_book_rating returns correct rating value for the given book
    def test_get_book_rating_get_existing_books_rating(self, collector):

        collector.add_new_book('A Promised Land')
        collector.set_book_rating('A Promised Land', 5)

        collector.add_new_book('Promises to Keep')
        collector.set_book_rating('Promises to Keep', 4)

        assert collector.get_book_rating('Promises to Keep') == 4