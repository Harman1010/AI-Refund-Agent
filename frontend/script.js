async function sendMessage() {

    const input = document.getElementById("message")

    const message = input.value

    if (!message) {
        return
    }

    const chatBox = document.getElementById("chat-box")

    chatBox.innerHTML += `
        <div class="user">
            <b>Customer:</b> ${message}
        </div>
    `

    const response = await fetch(
        "http://127.0.0.1:8000/chat",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message
            })
        }
    )

    const data = await response.json()

    chatBox.innerHTML += `
        <div class="agent">
            <b>Agent:</b> ${data.reply}
        </div>
    `

    const logsBox = document.getElementById("logs-box")

    logsBox.innerHTML = ""

    data.logs.forEach(log => {

        logsBox.innerHTML += `
            <div class="log">
                ${log}
            </div>
        `
    })

    input.value = ""

    chatBox.scrollTop = chatBox.scrollHeight
}