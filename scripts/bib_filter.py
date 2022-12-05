from pathlib import Path
from argparse import ArgumentParser
import bibtexparser
from bibtexparser.bibdatabase import BibDatabase
from bibtexparser.bwriter import BibTexWriter


def main(in_bib_path: Path, out_bib_path: Path):
    input_db = bibtexparser.loads(in_bib_path.read_text(encoding='utf-8'))
    output_db = BibDatabase()
    arxiv_num = 0
    total_num = 0
    for entry in input_db.entries:
        total_num += 1
        if 'eprinttype' in entry:
            arxiv_num += 1
        else:
            output_db.entries.append(entry)

    print(f'{arxiv_num}/{total_num} are arxiv paper')

    bib_writer = BibTexWriter()
    bib_writer.indent = '  '
    with out_bib_path.open('w', encoding='utf-8') as f:
        f.write(bib_writer.write(output_db))


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('input', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    main(args.input, args.output)
