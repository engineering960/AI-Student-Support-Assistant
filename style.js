const input = document.getElementById("userInput");
const chatBox = document.getElementById("chatBox");


function addMessage(message, type) {

    const messageDiv = document.createElement("div");

    messageDiv.classList.add("message", type);

    const avatar = document.createElement("div");

    avatar.classList.add("avatar");

    avatar.textContent = type === "bot" ? "🤖" : "👨‍🎓";


    const text = document.createElement("div");

    text.classList.add("text");

    text.textContent = message;


    messageDiv.appendChild(avatar);
    messageDiv.appendChild(text);

    chatBox.appendChild(messageDiv);

    chatBox.scrollTop = chatBox.scrollHeight;
}


async function sendMessage() {

    const message = input.value.trim();

    if (message === "") {
        return;
    }

    addMessage(message, "user");

    input.value = "";

    try {

        const response = await fetch("/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })

        });


        const data = await response.json();

        addMessage(data.response, "bot");

    }

    catch (error) {

        addMessage(
            "Sorry! Something went wrong. Please try again.",
            "bot"
        );

        console.error(error);

    }
}


function quickMessage(message) {

    input.value = message;

    sendMessage();

}


input.addEventListener("keypress", function(event) {

    if (event.key === "Enter") {

        sendMessage();

    }

});