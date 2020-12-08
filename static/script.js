// Allow accessing the camera

var video = document.querySelector("#videoElement");

let img_string = "";
//mediaDevice and userMedia to navigate the access for camera

if(navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({
        video: true
        // after allowing the camera start the video stream
    }).then(function(stream) {
        video.srcObject = stream
        //play the video
        video.play();
    }).catch(function(error) {
        console.log(error);
    });
}

// capture Images
function capture(){
    // <canvas id="image" class="canvas"></canvas>
    let canvas = document.createElement("CANVAS");
    canvas.id = "image";
    canvas.height = 450;
    canvas.width = 500;
    let context = canvas.getContext('2d');
    let vid = document.querySelector('.videoObject');


    // var image = document.getElementById('image'),
    // context = image.getContext('2d');  //setting for resolution of image

        // draw a image when the button clicked on the canvas

    context.drawImage(video , 0 , 0 , 500 , 400);
    console.log(video.height, video.width, canvas.height , canvas.width);
    vid.innerHTML = '';
    vid.appendChild(canvas);
    let img = canvas.toDataURL("image/png").replace("image/png", "image/octet-stream");  // here is the most important part because if you dont replace you will get a DOM 18 exception.
    console.log(img);
    img_string = img;
    let change = document.querySelector('#change');
    // change.innerHTML = `<button onclick="fetchResult()">Process</button>`;
    change.innerHTML = `<a onclick="loading()" href="/process/${img}"><button>Process</button></a>`;
    // window.location.href=img; // it will save locally


}

function loading() {
    let canvas = document.querySelector('#image');
    canvas.outerHTML = `<div id="loading">
                    <div id="ring" class="ring">LOADING<div class='ringer'></div></div>
                </div>`;

}