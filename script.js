/* Theme toggle */
function toggleTheme() {
    document.body.classList.toggle("light");

    let icon = document.querySelector(".toggle");
    icon.innerHTML = document.body.classList.contains("light") ? "Light Mode" : "Dark Mode";
}

function validateField(id) {
    let input = document.getElementById(id);
    let group = document.getElementById(id + "-group");
    let errorText = group.querySelector(".error-text");

    if (input.value === "" || isNaN(input.value)) {
        group.classList.add("error");
        input.classList.add("shake");
        errorText.style.display = "block";

        setTimeout(() => input.classList.remove("shake"), 300);
        return false;
    } else {
        group.classList.remove("error");
        errorText.style.display = "none";
        return true;
    }
}

function predict() {

    let validAmount = validateField("amount");
    let validTime = validateField("time");

    if (!validAmount || !validTime) return;

    let loader = document.getElementById("loader");
    let resultDiv = document.getElementById("result");

    loader.style.display = "block";
    resultDiv.style.display = "none";

    let features = [
        parseFloat(document.getElementById("time").value),
        parseFloat(document.getElementById("amount").value)
    ];

    fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({features: features})
    })
    .then(res => res.json())
    .then(data => {
        loader.style.display = "none";
        resultDiv.style.display = "block";

        if (data.result === 1) {
            resultDiv.className = "result fraud";
            resultDiv.innerHTML = "Fraud Detected!";
        } else {
            resultDiv.className = "result safe";
            resultDiv.innerHTML = "Safe Transaction";
        }
    })
    .catch(() => {
        loader.style.display = "none";
        resultDiv.style.display = "block";
        resultDiv.innerHTML = "Server Error";
    });
}