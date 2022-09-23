# qa_python

## Testing
### The project have the following unit tests:

1.  test_add_new_book_add_two_books - Tests that add_new_book adds 2 books to collection
2.  test_set_book_rating_set_rating_5_for_existing_book - Tests the set_book_ratings() actually sets rating between 1 and 10 for existing book
3.  test_set_book_rating_doesnt_set_rating_11_for_existing_book - Tests the set_book_ratings() does not set rating above 10 for existing book
4.  test_set_book_rating_doesnt_set_rating_0_for_existing_book - Tests the set_book_ratings() does not set rating below 1 for existing book
5.  test_get_book_with_specific_rating_get_book_with_existing_rating - Tests that get_book_with_specific_rating returns appropriate book for the existing rating
6.  test_get_book_with_specific_rating_get_book_with_non_existing_rating_returns_empty_list - Tests that get_book_with_specific_rating returns empty list if non-existing rating value is given
7.  test_get_book_rating_get_existing_books_rating - Tests that get_book_rating returns correct rating value for the given book
8.  test_get_books_rating_returns_all_rating_values - Tests that get_books_rating returns all elements
9.  test_add_book_in_favorites_doesnt_add_book_out_of_collection - Tests that add_book_in_favorites does not add the book which is not in the collection
10. test_delete_book_from_favorites_delete_existing_book - Tests that delete_book_from_favorites() actually deletes existing book
11. test_get_list_of_favorites_books_return_all_added_to_favorites - Tests that get_list_of_favorites_books returns full list of added books
