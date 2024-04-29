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
        btn.parentElement.style.backgroundColor = "#7f4bf8";
        number = parseInt(btn.getAttribute("number"));
        link = btn.getAttribute("link");
        get_booster(power, number);
        setTimeout(function () {
            btn.parentElement.style.backgroundColor = "";
        }, 100);
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



//то же самое что через фетч, но я не смог дату отправить, так что через ajax сделал
function get_booster(power, number) {
    token = document.getElementsByName("csrfmiddlewaretoken")[0].getAttribute('value');
    ajax_data = {}
    ajax_data["number"] = number;
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
                // console.log(request);
                document.getElementById("coins").innerText = `Coins: ${request.core.coins}`
                document.getElementById("power").innerText = `Power: ${request.core.click_power}`
                document.getElementById(number).textContent = `${request.boost.price} coins`
            }        
        },
        error: function (response) {
            alert("WRONG!")
        }
    });
}
