import logging
from pathlib import Path

import spacy
from spacy.tokens import DocBin
import typer


def convert(lang: str, input_path: Path, output_path: Path):
    nlp = spacy.blank(lang)
    in_db = DocBin().from_disk(input_path)
    out_db = DocBin()
    logging.info(f"Read {len(in_db)} documents from {input_path}.")
    for doc in in_db.get_docs(nlp.vocab):
        new_doc = nlp.make_doc(doc.text)
        new_doc.user_data = doc.user_data
        new_doc.ents = doc.ents
        out_db.add(new_doc)
    out_db.to_disk(output_path)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    typer.run(convert)