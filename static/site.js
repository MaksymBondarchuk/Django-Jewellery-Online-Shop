function zoomImage(image) {
    var modal = document.getElementById("zoomImageDiv");
    var modalImg = document.getElementById("zoomedImage");
    var captionText = document.getElementById("caption");

    modal.style.display = "block";
    modalImg.src = image.src;
    captionText.innerHTML = image.alt;
}

function closeZoomedImage() {
    var modal = document.getElementById("zoomImageDiv");
    modal.style.display = "none";
}