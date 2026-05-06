import PyPDF2

def load_pdf(path):
    text = ""

    with open(path, "rb") as file:
        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            content = page.extract_text()
            if content:
                text += content + "\n\n"

    return text