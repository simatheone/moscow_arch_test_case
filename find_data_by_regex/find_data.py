import re
from typing import Generator, List


def read_file_generator(filename: str) -> Generator:
    """Читает файл и построчно отдает текст из указанного файла."""
    with open(filename, 'r') as file:
        for line in file:
            yield line


def find_regex_matches_in_text(text) -> List[str]:
    """
    Находит совпадения в тексте с регулярным выражением и
    отдает результат в виде листа со строками.
    """
    pattern = (
        r'((?:\d+[\s])+(?:кв\.(?:м|км)))|'
        r'((?:\d+[\s,])+(?:га|тыс\.кв\.м/га))|'
        r'((?:\d+[\s]м(?![а-яА-Я])))|'
        r'([0-9]+:[0-9]+:[0-9]+:[0-9]+)'
    )
    compiled_pattern = re.compile(pattern)
    found_mathces = compiled_pattern.findall(text)
    result_data = [''.join(match) for match in found_mathces]
    return result_data


if __name__ == '__main__':
    filename = 'text.txt'
    text_paragraph = read_file_generator(filename)

    result_data = []
    for text in text_paragraph:
        found_data = find_regex_matches_in_text(text)
        result_data.extend(found_data)
    print(result_data)
