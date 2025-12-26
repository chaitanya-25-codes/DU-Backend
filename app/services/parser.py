import os
from typing import Optional

import pdfplumber
import docx


def parse_file(file_path: str) -> str:
    """Extract text content from a file.

    Supports .txt, .pdf and .docx. Raises ValueError for unsupported types.
    """
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".txt":
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()

    if ext == ".pdf":
        texts = []
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                texts.append(page.extract_text() or "")
        return "\n".join(texts)

    if ext == ".docx":
        doc = docx.Document(file_path)
        return "\n".join([p.text for p in doc.paragraphs])

    raise ValueError(f"Unsupported file type: {ext}")
