from pathlib import Path
from pypdf import PdfReader
from docx import Document

def extract_text(file_path):
    """
    Extracts text from a given file.

    Args:
        file_path (str): The path to the file from which to extract text.

    Returns:
        str: The 
        extracted text from the file.
    """
    if file_path is None:
        raise ValueError("File path cannot be None")
    
    path = Path(file_path)
    if not path.is_file():
        raise FileNotFoundError(f"File Not Found : {file_path}")
    
    
    suffix= path.suffix.lower()

    if suffix not in ['.txt', '.md', '.pdf', '.docx']:
        raise ValueError(f"Unsupported file type: {suffix}. Supported types are: .txt, .md, .pdf, .docx")

    if suffix in (".txt", ".md"):
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()

        except Exception as e:
            raise RuntimeError(
                f"Failed to extract text from {file_path}") from e
        
    elif suffix == '.pdf':
        try:
            reader = PdfReader(file_path)
            text = ""
            for page in reader.pages:
                text += (page.extract_text() or "") + "\n"
        except Exception as e:
            raise RuntimeError(
                f"Failed to extract text from {file_path}") from e
        
    elif suffix == '.docx':
        try:
            doc = Document(file_path)
            text = "\n".join(para.text for para in doc.paragraphs)
        except Exception as e:
            raise RuntimeError(
                f"Failed to extract text from {file_path}") from e

    source_file = path.name
        
    return text, source_file