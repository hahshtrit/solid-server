$(document).ready(function() {

    var s = io();
    var socket = io('/dm');
    socket.on('connect', function() {
        console.log('wtf')
        socket.emit('connect_user', {data: 'I\'m connected!'});
        // socket.emit('establish', {data: 'I\'m connected!'});
    });

    $('#send_dm').on('click', function() {
        var reciever = $('#dm_target').val();
        var message = $('#dm_message').val();

        socket.emit('direct_message', {'username': reciever, 'message': message});
    });
    
    socket.on('new_dm', function(data) {
        // alert(data['sender'] + ': ' + data['message']);
        alert('New Direct Message from ' + data['sender']);
        // $('#last_dm').val() = data['sender'] + ': ' + data['message'];
        $('#last_dm').text(data['sender'] + ': ' + data['message']);
    });



});

// var s = io();
// var socket = io('/dm');
// socket.on('connect', function() {
//     console.log('wtf')
//     socket.emit('connect_user', {data: 'I\'m connected!'});
//     // socket.emit('establish', {data: 'I\'m connected!'});
// });