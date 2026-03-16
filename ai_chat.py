def get_response(text):

    text = text.lower()

    if "hello" in text:
        return "Hello. How are you today?"

    elif "your name" in text:
        return "I am your AI English tutor."

    elif "how are you" in text:
        return "I am fine. How can I help you improve your English?"

    elif "bye" in text:
        return "Goodbye. Keep practicing English."

    elif "i love u" in text:
        return "i love u too."

    else:
        return "Please speak again. I am learning English with you."