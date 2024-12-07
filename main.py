#!/usr/bin/env python3


def main():
    books_dir = "books"
    book_name = "frankenstein"
    final_report = get_report(f"{books_dir}/{book_name}.txt")
    print_report(final_report)


def get_report(book):
    with open(book) as b:
        text = b.read()
        analysis = {
            "name": book,
            "word_count": get_word_count(text),
            "letter_count": get_letter_count(text.lower()),
        }
        return analysis


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
    print(f"--- START - {report["name"]} ---")
    print(f"A total of {report["word_count"]} words found in the document.\n")
    for letter in report["letter_count"]:
        print(f"- '{letter}' found {report["letter_count"][letter]} times.")
    print(f"--- END - {report["name"]} ---\n\n")


main()
