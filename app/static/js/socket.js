var socket = io.connect("http://" + document.domain + ":" + location.port);
socket.on("connect", function(msg) {
    console.log("got socket connect from server: ", msg);
    socket.emit("clientHello", {data: "I'm connected!"});
});
socket.on("serverHello", function(msg) {
    console.log("got socket status from server: ", msg, msg.data);
	$("#socketStatus").text(msg.data);
});
