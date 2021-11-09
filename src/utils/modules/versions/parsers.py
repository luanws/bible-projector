from __future__ import annotations

import re
from typing import Dict, List

from src.models.verse import Verse


def get_parsers_dict():
    return {
        'ont': ont_to_verses,
    }


def content_to_verses(extension: str, content: str, bible_shape: Dict[str, Dict[str, int]], version_id: int) -> List[Verse]:
    parsers_dict = get_parsers_dict()
    parser = parsers_dict[extension]
    verses = parser(content, bible_shape, version_id)
    return verses


def ont_to_verses(content: str, bible_shape: Dict[str, Dict[str, int]], version_id: int) -> List[Verse]:
    content = re.sub(r'<TS>.+<Ts>', '', content)
    content = re.sub(r'</?.+?>', '', content)
    verse_texts = content.split('\n')
    verses: List[Verse] = []
    for book_id in bible_shape.keys():
        for chapter_number in bible_shape[book_id].keys():
            number_of_verses = bible_shape[book_id][chapter_number]
            verses_texts_of_chapter = verse_texts[:number_of_verses]
            verse_texts = verse_texts[number_of_verses:]
            for i, text in enumerate(verses_texts_of_chapter):
                verse_number = i + 1
                verses.append(Verse(
                    book_id=int(book_id),
                    chapter_number=int(chapter_number),
                    verse_number=verse_number,
                    text=text,
                    version_id=version_id,
                ))
    return verses
