import os
import sys
import string


BOOK_PATH = "book/book.txt"
PAGE_SIZE = 1050

book: dict[int, str] = {}

def _get_part_text(text: str, start: int, page_size: int) -> tuple[int, str]:
    punctuation = set(string.punctuation)
    max_page_size = page_size
    end_pos = start + page_size-1

    if end_pos < len(text) and text[end_pos] not in [*punctuation]:
        while end_pos < len(text) and text[end_pos] not in [*punctuation]:
            end_pos -= 1
    else:
        page_text = text[:start+page_size]

    if end_pos < len(text) and len(text[start:end_pos+1]) <= max_page_size:
        if text[end_pos+1] in [*punctuation]:
            while text[end_pos-2] not in [*punctuation]:
                end_pos -= 1
            page_text = text[start:end_pos-1]
        else:
            page_text = text[start:end_pos+1]
    else:
        page_text = text[start:]
    
    return page_text, len(page_text)


book: dict[int, str] = {}
PAGE_SIZE = 1050

def prepare_book(path: str) -> None:
    try:
        with open(path, 'r', encoding='utf-8') as file:
            file_content = file.read()
            start = 0
            page_counter = 1
            while start < len(file_content):
                page_text, size = _get_part_text(file_content, start, PAGE_SIZE)
                start += size
                book[page_counter] = page_text.strip()
                page_counter += 1
                        
    except FileNotFoundError:
        print(f"Файл '{path}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка при открытии/чтении файла: {e}")  

prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))