function kubeAjax(cmd) {
    // document.getElementById("output").innerHTML = "Command is being Executed, Please wait..."
    // var xhr = new XMLHttpRequest();


    // xhr.open("GET", "http://127.0.0.1:5500/backend/docker.py?command="+cmd, true);

    // xhr.send();

    // // Output from above url

    // xhr.onload = function () {
    //     var output = xhr.responseText;
    //     document.getElementById("output").innerHTML = output;
    // }
    alert(cmd)


}


function printer(id) {
    var keyword = document.getElementById(id);
    return keyword.value;
}

