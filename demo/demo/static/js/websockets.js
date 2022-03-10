const gallerySocket = new WebSocket('ws://' + window.location.host + '/ws/gallery/');

gallerySocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    addImage(data.src, data.desc);
};

gallerySocket.onclose = function(e) {
    console.error('Gallery socket closed');
};

function generateImages(number){
    if(confirm(`About to add ${number} images`)){
        gallerySocket.send(JSON.stringify({'pics': number}));
    }    
}
