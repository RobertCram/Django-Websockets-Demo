const gallerySocket = new WebSocket('ws://' + window.location.host + '/ws/gallery/');

var batchnumber = 0;

gallerySocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    addImage(data.src, data.desc);
};

gallerySocket.onclose = function(e) {
    console.error('Gallery socket closed');
};
