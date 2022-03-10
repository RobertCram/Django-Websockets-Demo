/*

EXAMPLE GALLERY ITEM

<div class="gallery">
  <img src="" alt="" width="600" height="400">
  <div class="desc">Add a description of the image here</div>
</div> 

*/ 


function addImage(){
    imgTag = createImgTag(picsumUrl(), 'alt text')
    descTag = createDescTag('description')
    div = createGalleryDivTag(imgTag, descTag);
    document.body.appendChild(div)
}

function createGalleryDivTag(imgTag, descTag){
    const div = document.createElement("div");
    div.className = "gallery";        
    div.appendChild(imgTag)
    div.appendChild(descTag)
    return div;
}

function createImgTag(src, alt){
    const img = document.createElement("img");
    img.src = src;
    img.alt = alt;
    img.width = "600";
    img.height = "400";
    return img;
}

function createDescTag(text){
    const div = document.createElement("div");
    div.className = "desc";
    div.innerText = text;
    return div;
}

function picsumUrl(){
    return 'https://picsum.photos/400/600?id=' + Math.floor(Math.random()*1000)
}
