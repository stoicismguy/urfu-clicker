img = document.getElementById("img");
img.onclick = function (e) {
    img.parentElement.style.backgroundColor = "#7f4bf8";
    call_click()
    setTimeout(function () {
        img.parentElement.style.backgroundColor = "";
    }, 100);
}

function call_click() {
    fetch('/call_click', {
        method: "GET"
    }).then(response => {
        if (response.ok) {
            return response.json()
        }
        return Promise.reject(response)
    }).then(data => {
        document.getElementById("coins").innerText = `Coins: ${data.core.coins}`
    }).catch(error => console.log(error))
}
