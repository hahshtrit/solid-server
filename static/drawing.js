const canvas = document.getElementById("drawing-board");
const context = canvas.getContext("2d");

const canvasOffsetX = canvas.offsetLeft;
const canvasOffsetY = canvas.offsetTop;

canvas.width = window.innerWidth - canvasOffsetX;
canvas.height = window.innerHeight - canvasOffsetY;

let isDrawing = false;
let lineWidth = 5;
let startX;
let startY;

const draw = (e) => {
    if (!isDrawing) {
        return;
    }
    context.lineWidth = lineWidth;
    context.lineCap = 'round';

    context.lineTo(e.clientX - canvasOffsetX, e.clientY - canvasOffsetY)
    context.stroke();
    data = {
        'x': e.clientX - canvasOffsetX,
        'y': e.clientY - canvasOffsetY
    };
    socket.emit('draw', data)
}

canvas.addEventListener('mousedown', (e) => {
    isDrawing = true;
    startX = e.clientX;
    startY = e.clientY;
});

canvas.addEventListener('mouseup', (e) => {
    isDrawing = false;
    context.stroke();
    context.beginPath();
    socket.emit('stop_drawing', {'isDrawing': false});  //{'startX': startX, 'startY': startY, 'e': e});
});

canvas.addEventListener('mousemove', draw);

var s = io();
var socket = io('/draw');
socket.on('connect', function() {
    s.emit('my event_draw', {data: 'I\'m connected!'});
});

socket.on('drawing', function(data) {
    context.lineWidth = lineWidth;
    context.lineCap = 'round';

    context.lineTo(data['x'], data['y'])
    context.stroke();
});

socket.on('stopping_drawing', function(data) {
    // isDrawing = data['isDrawing'];
    // console.log(data['isDrawing']) 
    isDrawing = false;
    context.stroke();
    context.beginPath();
});