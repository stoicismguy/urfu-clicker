img = document.getElementById("img");
global_core_data = null;
global_click_counter = 0


img.onclick = function (e) {
    img.parentElement.style.backgroundColor = "#7f4bf8";
    call_click()
    setTimeout(function () {
        img.parentElement.style.backgroundColor = "";
    }, 100);
}

$.ajax({
    type: 'GET',
    url: core_data_link,
    success: function (request) {
        global_core_data = request.core;
        console.log(global_core_data)
    }
})


boost_buttons = document.getElementsByClassName("boost");
Array.from(boost_buttons).forEach((element) => {
    element.onclick = function (e) {
        var div = e.target;
        div.style.backgroundColor = "#7f4bf8";
        var number = parseInt(div.getAttribute("number"));
        var link = div.getAttribute("link");
        get_booster(number, link, div);
        setTimeout(function () {
            div.style.backgroundColor = "";
        }, 100);
    };
});


function call_click() {
    let coins_p = document.getElementById("coins")
    global_core_data.coins += global_core_data.click_power
    coins_p.innerText = parseInt(coins_p.innerText) + global_core_data.click_power
}

setInterval(function () {
    global_core_data.coins += (global_core_data.autoclick_power / 60);
    let coins_p = document.getElementById("coins");
    coins_p.innerText = parseInt(global_core_data.coins)
}, 1000)


setInterval(function () {
    set_coins();
}, 5000)

function set_coins() {
    let ajax_data = {}
    ajax_data["csrfmiddlewaretoken"] = document.getElementsByName("csrfmiddlewaretoken")[0].getAttribute('value');
    ajax_data['money'] = parseInt(global_core_data.coins);
    $.ajax({
        type: 'POST',
        url: set_coins_url,
        data: ajax_data,
        success: function (request) {
            render_core(request["core"]);
        }
    })
}


function render_core(core) {
    global_core_data = core;
    document.getElementById("coins").innerText = parseInt(core.coins);
    document.getElementById("power").innerText = parseInt(core.click_power);
    document.getElementById("auto").innerText = parseInt(core.autoclick_power);
}


function get_booster(number, link, div) {
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
                let coins = document.getElementById("coins");
                coins.style.color = "rgb(255, 0, 0)";
                setInterval(function () {
                    coins.style.color = "black";
                }, 150)
            }
            else {
                div.querySelector('[name="power"]').innerText = request['boost'].power;
                div.querySelector('[name="price"]').innerText = request['boost'].price;
                render_core(request["core"]);
            }        
        },
        error: function (response) {
            alert("WRONG!");
        }
    });
}

