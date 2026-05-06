from pdf_reader import load_pdf
from chatbot import chatbot_response
from voice import speak
from quiz import start_quiz

subject = input("Enter subject name (pdf file): ")

text = load_pdf(subject)

if text == "PDF not found":
    print("❌ PDF not found")
else:
    print("✅ PDF Loaded Successfully")

while True:
    print("\n1. Ask Question")
    print("2. Voice Answer")
    print("3. Quiz")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        q = input("Ask: ")
        ans = chatbot_response(text, q)
        print(ans)

    elif choice == "2":
        q = input("Ask: ")
        ans = chatbot_response(text, q)
        speak(ans)

    elif choice == "3":
        start_quiz()

    elif choice == "4":
        break

    else:
        print("Invalid choice")