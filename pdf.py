from word_search_generator import WordSearch
puzzle = WordSearch("dog, cat, pig, horse, donkey, turtle, goat, sheep")
puzzle.save(path="./puzzle.pdf")