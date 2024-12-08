#!/usr/bin/env python3

from glob import glob


def main():
    books_dir = "books"
    book_list = glob(f"{books_dir}/*.txt")
    final_report = get_report(book_list)
    print_report(final_report)


def get_report(books):
    report = []
    for book in books:
        with open(book) as b:
            text = b.read()
            analysis = {
                "name": book,
                "word_count": get_word_count(text),
                "letter_count": get_letter_count(text.lower()),
            }
            report.append(analysis)
    return report


def get_word_count(content):
    return len(content.split())


def get_letter_count(content):
    letter_count = {}
    for letter in content:
        if letter.isalpha():
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 0
    return {letter: letter_count[letter] for letter in sorted(letter_count)}


def print_report(report):
    for book in report:
        print(f"--- START - {book["name"]} ---")
        print(f"A total of {book["word_count"]} words found in the document.\n")
        for letter in book["letter_count"]:
            print(f"- '{letter}' found {book["letter_count"][letter]} times.")
        print(f"--- END - {book["name"]} ---\n\n")


main()
