from flask import Flask, request, render_template
import PyPDF2
from markupsafe import Markup
import markdown
import chatbot

app = Flask(__name__)

def load_pdf(path):
    with open(path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text


@app.route("/", methods=["GET", "POST"])
def home():
    response = ""
    clean_name = ""
    selected_pdf = "dbms_notes.pdf"

    if request.method == "POST":
        user_input = request.form.get("message")
        selected_pdf = request.form.get("subject")

        # 🚨 Empty input check
        if not user_input or user_input.strip() == "":
            response = "⚠️ No input received"
            return render_template("index.html", response=response, selected_pdf=selected_pdf)

        # 🔥 OTHER SUBJECT (no PDF)
        if selected_pdf == "other":
            text_data = ""
            clean_name = "GENERAL AI"
        else:
            clean_name = selected_pdf.replace("_notes.pdf", "").upper()
            path = "notes/" + selected_pdf
            text_data = load_pdf(path)

        # 🤖 AI response
        response_text = chatbot.chatbot_response(text_data, user_input)

        # ✅ Markdown → HTML
        response = Markup(markdown.markdown(response_text))

    return render_template("index.html", response=response, selected_pdf=selected_pdf)


if __name__ == "__main__":
    app.run(debug=True)