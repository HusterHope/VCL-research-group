import argparse
from pathlib import Path
import re

import bibtexparser
import xlsxwriter


def remove_brackets(content: str) -> str:
    for s in re.findall(r'''\\[~'"]\{(.*?)\}''', content):
        content = content.replace(f'''\\~{{{s}}}''', s)
        content = content.replace(f'''\\'{{{s}}}''', s)
        content = content.replace(f'''\\"{{{s}}}''', s)

    for s in re.findall(r'\{(.*?)\}', content):
        content = content.replace(f'{{{s}}}', s)

    return content


def gen_excel(bib_path: Path, xlsx_path: Path):
    if not bib_path.exists():
        print(bib_path, 'not existes')
        return
    # if xlsx_path.exists():
    #     print(xlsx_path, 'already existes')
    #     return

    print('parsing', bib_path)
    with bib_path.open(encoding='utf-8') as f:
        entries: list[dict[str, str]] = bibtexparser.load(f).entries
    print(len(entries), 'entries are parsed')

    workbook = xlsxwriter.Workbook(xlsx_path)
    worksheet = workbook.add_worksheet()

    headers = ['type', 'year', 'title', 'author', 'journal', 'volume', 'pages', 'url']
    for j, header in enumerate(headers):
        worksheet.write(0, j, header, )
    header_fmt = workbook.add_format({'bold': True})
    worksheet.set_row(0, cell_format=header_fmt)
    worksheet.set_column(first_col=2, last_col=4, width=40)

    cnt = 1
    for i, entry in enumerate(entries, start=1):
        entry_type = entry['ENTRYTYPE']

        title = entry['title'].replace('\n', '')
        title = remove_brackets(title)
        author = entry['author'].replace(' and\n', ', ')
        author = remove_brackets(author)

        # print(i, entry_type, title)

        if entry_type == 'article':
            journal = entry['journal']
            if 'eprinttype' in entry:
                print(f'eprint entry {i} are dropped, title={title}')
                continue
        elif entry_type == 'inproceedings':
            journal = entry['booktitle']
        elif entry_type == 'book':
            print(f'{entry_type} entry {i} are dropped, title={title}')
            continue
        elif entry_type == 'incollection':
            print(f'{entry_type} entry {i} are dropped, title={title}')
            continue
        else:
            raise ValueError(f'Unknown entry type {entry_type}')

        journal = journal.replace('\n', '')
        journal = remove_brackets(journal)

        items: list[str] = []
        items.append(entry['ENTRYTYPE'])
        items.append(entry['year'])
        items.append(title)
        items.append(author)
        items.append(journal)
        items.append(entry.get('volume', ''))
        items.append(entry.get('pages', ''))
        items.append(entry.get('url', ''))

        for j, item in enumerate(items):
            worksheet.write(cnt, j, item)
        cnt += 1
    
    workbook.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('bib_path', type=Path)
    parser.add_argument('xlsx_path', type=Path)

    args = parser.parse_args()
    gen_excel(**vars(args))
