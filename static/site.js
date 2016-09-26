// region Image zoom
// todo Add check for display height
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
// endregion

// region Main page
function buy(id) {
    $.post("buy", {jewel: id}, function () {
        location.href = 'home';
    });
}

function metalChecked(id, item) {
    $.post("metal", {metal: id, state: item.checked}, function () {
        location.href = 'home';
    });
}

function finenessChanged(parameter, value) {
    $.post("fineness", {parameter: parameter, value: value}, function () {
        location.href = 'home';
    });
}
// endregion Main page