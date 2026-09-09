from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def get_response(message):
    message = message.lower()

    if "hello" in message or "hi" in message:
        return "Hello! 👋 How can I help you today?"

    elif "course" in message:
        return "I can help you choose courses based on your interests and career goals."

    elif "exam" in message:
        return "For exams, create a study timetable, revise important topics, and practice previous questions. 📚"

    elif "study" in message:
        return "Try studying for 45 minutes and taking a 10-minute break. Keep your phone away while studying."

    elif "attendance" in message:
        return "Please maintain your attendance regularly. You can check with your college department for the exact percentage."

    elif "career" in message:
        return "You can explore careers in Software Development, Data Science, AI, Cybersecurity, Web Development and more."

    elif "python" in message:
        return "Python is a beginner-friendly programming language widely used in AI, Data Science and Web Development. 🐍"

    elif "javascript" in message:
        return "JavaScript is mainly used to make websites interactive and dynamic."

    elif "thank" in message:
        return "You're welcome! 😊 I'm happy to help."

    else:
        return "I'm your AI Student Support Assistant 🤖. You can ask me about studies, exams, courses, attendance, career, Python or JavaScript."


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/study")
def study():
    return render_template("study.html")


@app.route("/career")
def career():
    return render_template("career.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/chat")
def chat_page():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat_api():
    data = request.get_json()
    message = data.get("message", "")

    response = get_response(message)

    return jsonify({
        "response": response
    })

if __name__ == "__main__":
    app.run(debug=True)