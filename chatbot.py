from groq import Groq
import markdown

client = Groq(api_key="YOUR_API-KEY")

def chatbot_response(text_data, user_input):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": """
You are a professional AI Study Assistant.

Rules:
- Give well-structured answers
- Use headings (Definition, Types, Example)
- Use bullet points
- Add proper spacing
- Use simple student-friendly language
- Do NOT join words together
"""
                },
                {
                    "role": "user",
                    "content": f"""
Study Material:
{text_data[:1500]}

Question:
{user_input}
"""
                }
            ]
        )

        ai_text = response.choices[0].message.content

        # 🔥 Clean formatting
        ai_text = ai_text.replace(":", ":\n")
        ai_text = ai_text.replace("•", "\n•")
        ai_text = ai_text.replace(". ", ".\n\n")

        return ai_text.strip()

    except Exception as e:
        return f"Error: {str(e)}"