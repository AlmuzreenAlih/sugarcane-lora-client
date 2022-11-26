// const imgimg = document.querySelector( 'ccc' )

// imgimg.addEventListener( 'mousemove', event => {
    
//     const bb = canvas.getBoundingClientRect();
//     const x = Math.floor( (event.clientX - bb.left) / bb.width * canvas.width );
//     const y = Math.floor( (event.clientY - bb.top) / bb.height * canvas.height );
    
//     console.log({ x, y });
  
// });

$(document).ready(function() {
    $("img").on("click", function(event) {
        var x = (event.pageX - this.offsetLeft)*640;
        x = Math.floor((x/this.width));
        var y = (event.pageY - this.offsetTop)*480;
        y = Math.floor((y/this.height));
        alert("X Coordinate: " + x + " Y Coordinate: " + y);
    });
});

async function JS_Hello_Button_Function() {
    var a = await eel.Py_HelloFunction("Hello Python")();
    document.getElementById("Hello_Button").innerHTML = "Hi";
    alert("Python Says: " + a);
}

eel.expose(JS_Alert_Hello);
function JS_Alert_Hello(a) {
    loadImg(img1, "Video.jpg?x=" + new Date().getTime()).then((img) => {
        if (img.height == 480) {
            document.getElementById("pic1").src=img.src;
        }
    });
}

eel.expose(JS_Show_Progress);
function JS_Show_Progress(text) {
    progressLabel.innerHTML = text;
}

function inspect() {
    return `a is ${this.a} and b is ${this.b}`;
  }

eel.expose(JS_Delete_Elements);
function JS_Delete_Elements() {
    cntnt = document.getElementById("PicsContainer");
    console.log(cntnt.childNodes.length);
    xx = cntnt.childNodes.length;
    for (let x = 0; x < xx; x++) {
        if ((cntnt.lastChild.innerHTML != undefined) && (cntnt.lastChild.innerHTML != "Image List")) {
            console.log(cntnt.lastChild.innerHTML);
            cntnt.removeChild(cntnt.lastChild);
        }
        console.log(x);
    }
}

eel.expose(JS_Send_Paths);
function JS_Send_Paths(Paths) {
    Paths.forEach(element => {
        const para = document.createElement("a");
        // alert("Hi1")
        para.innerHTML = element.substring(7,element.length);
        // alert("Hi2")
        let arr_fname = (element.substring(7,element.length-4)).split(" ");
        // alert(arr_fname);
        if (arr_fname[1] == "not_mature") {ClassName = "Not Mature";}
        if (arr_fname[1] == "mature") {ClassName = "Mature";}
        para.onclick = function() {
            document.getElementById("ImagePrev").src = element;
            document.getElementById("Classification").innerHTML = "Classification: " + (ClassName);
            document.getElementById("Percentage").innerHTML = "Percentage: " + arr_fname[2];
        };
        document.getElementById("PicsContainer").appendChild(para);
    });
}

eel.expose(JS_Show_Timeout);
function JS_Show_Timeout() {
    document.getElementById("prompt").innerHTML = "Receive Timeout. Client side should try again."
    $( "#dialog" ).dialog("open");
}

eel.expose(JS_Show_Success);
function JS_Show_Success() {
    document.getElementById("prompt").innerHTML = "File successfully received."
    $( "#dialog" ).dialog("open");
}

const loadImg = function(img, url) {
    return new Promise((resolve, reject) => {
      img.src = url;
      img.onload = () => resolve(img);
      img.onerror = () => reject(img);
    });
  };
  
  const img1 = new Image();

