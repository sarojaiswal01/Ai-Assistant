def start_quiz():
    questions = [
        ("What is Merge Sort?", "divide and conquer"),
        ("What is Stack?", "lifo"),
    ]

    score = 0

    for q, ans in questions:
        user = input(q + " : ").lower()
        if ans in user:
            print("✅ Correct")
            score += 1
        else:
            print("❌ Wrong")

    print("Score:", score)