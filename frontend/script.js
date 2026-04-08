async function analyze() {
    const input = document.getElementById("userInput").value;

    try {
        const response = await fetch("http://127.0.0.1:5000/analyze", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ input: input })
        });

        const data = await response.json();

        // HANDLE ERROR RESPONSE
        if (data.error) {
            document.getElementById("result").innerText =
                "Error: " + data.error;
            return;
        }

        document.getElementById("result").innerText =
            "is_attack: " + data.is_attack + ", type: " + data.type;

    } catch (err) {
        document.getElementById("result").innerText =
            "Request failed: " + err;
    }
}