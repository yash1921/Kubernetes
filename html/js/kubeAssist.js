function kubeAjax(cmd) {
    document.getElementById("output").innerHTML = "Command is being Executed, Please wait..."
    var xhr = new XMLHttpRequest();


    xhr.open("GET", "http://192.168.239.126/cgi-bin/kubeAssist.py?command="+cmd, true);

    xhr.send();

    // Output from above url

    xhr.onload = function () {
        var output = xhr.responseText;
        document.getElementById("output").innerHTML = output;
    }
    


}


function printer(id) {
    var keyword = document.getElementById(id);
    return keyword.value;
}

