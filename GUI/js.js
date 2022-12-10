// const imgimg = document.querySelector( 'ccc' )

// imgimg.addEventListener( 'mousemove', event => {
    
//     const bb = canvas.getBoundingClientRect();
//     const x = Math.floor( (event.clientX - bb.left) / bb.width * canvas.width );
//     const y = Math.floor( (event.clientY - bb.top) / bb.height * canvas.height );
    
//     console.log({ x, y });
  
// }); 


function IdentifyVariety(numberstring) {
    var ns = numberstring*100;
    Varieties = ["Phil-1999","Phil-2000","PHIL-2004-1011","PHIL-2006-2289", "PHIL-2007-243"]
    return Varieties[ns%(Varieties.length)];
}

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
    Paths.forEach(element1 => {
        const para = document.createElement("a");
        // alert("Hi1")
        para.innerHTML = element1.substring(7,element1.length);
        // alert("Hi2")
        
        para.onclick = function() {
            let arr_fname = (element1.substring(7,element1.length-4)).split("-");
        console.log(arr_fname[1]);
        console.log(arr_fname[2]);
        let arr_fname_1 = arr_fname[1].split(" ")
        let arr_fname_2 = arr_fname[2].split(" ")
        ClassNames = [];
        ClassNames2 = "";
        // alert("Hi3")

        arr_fname_1.forEach(element2 => {
            if (element2 == "nm") {ClassNames.push("Not Matured")}
            if (element2 == "m") {ClassNames.push("Matured")}
        });
        let yy = 0;
        // alert("Hi4")

        arr_fname_2.forEach(element3 => {
            ClassNames[yy] = ClassNames[yy] + " " + element3 + " (" + IdentifyVariety(element3) + ")"
            ClassNames2 = ClassNames2 + ClassNames[yy] + "<br>"
            yy++;
        });
            console.log(element1)
            console.log(ClassNames2)
            document.getElementById("ImagePrev").src = element1;
            document.getElementById("Classification").innerHTML = ClassNames2;
            document.getElementById("Percentage").innerHTML = "";
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
function JS_Show_Success(n) {
    if (n == 1) {
        document.getElementById("prompt").innerHTML = "Results successfully received."
        $( "#dialog" ).dialog("open");
    }
    if (n == 2) {
        document.getElementById("prompt").innerHTML = "File successfully received."
        $( "#dialog" ).dialog("open");
    }
}

const loadImg = function(img, url) {
    return new Promise((resolve, reject) => {
      img.src = url;
      img.onload = () => resolve(img);
      img.onerror = () => reject(img);
    });
  };
  
  const img1 = new Image();


let element1="img123456-nm m nm m-0.8 0.77 0.5 0.44.jpg"
let arr_fname = (element1.substring(7,element1.length-4)).split("-");
console.log(arr_fname[1]);
console.log(arr_fname[2]);
let arr_fname_1 = arr_fname[1].split(" ")
let arr_fname_2 = arr_fname[2].split(" ")
ClassNames = [];
ClassNames2 = "";
arr_fname_1.forEach(element2 => {
    if (element2 == "nm") {ClassNames.push("Not Matured")}
    if (element2 == "m") {ClassNames.push("Matured")}
});
let yy = 0;
arr_fname_2.forEach(element3 => {
    ClassNames[yy] = ClassNames[yy] + " " + element3
    ClassNames2 = ClassNames2 + ClassNames[yy] + "\n"
    yy++;
});

console.log(ClassNames2);