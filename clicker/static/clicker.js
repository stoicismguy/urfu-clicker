img = document.getElementById("img");
img.onclick = function (e) {
    img.parentElement.style.backgroundColor = "#7f4bf8";
    call_click()
    setTimeout(function () {
        img.parentElement.style.backgroundColor = "";
    }, 100);
}

buttons = document.getElementsByClassName("buy");
Array.from(buttons).forEach((element) => {
    element.onclick = function (e) {
        btn = e.target;
        power = parseInt(btn.getAttribute("power"));
        price = parseInt(btn.getAttribute("price"));
        link = btn.getAttribute("link");
        get_booster(power, price, link);
    };
});

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


function get_booster(power, price, link) {
    token = document.getElementsByName("csrfmiddlewaretoken")[0].getAttribute('value');
    ajax_data = {}
    ajax_data["power"] = power;
    ajax_data["price"] = price;
    ajax_data["csrfmiddlewaretoken"] = token;
    $.ajax({
        type: "POST",
        url: link,
        data: ajax_data,
        success: function (request) {
            if (request.status == "bad") {
                alert("Not enough money!")
            }
            else {
                document.getElementById("coins").innerText = `Coins: ${request.core.coins}`
                document.getElementById("power").innerText = `Power: ${request.core.click_power}`
            }        
        },
        error: function (response) {
            alert("WRONG!")
        }
    });
}
