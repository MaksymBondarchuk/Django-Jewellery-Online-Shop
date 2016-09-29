// region Image zoom
// todo Add check for display height
function zoomImage(image) {
    var modal = document.getElementById("modal");
    var modalImg = document.getElementById("zoomedImage");
    var captionText = document.getElementById("caption");

    var div = document.getElementById("modal-image");

    modal.style.display = "block";
    div.style.display = "block";
    modalImg.src = image.src;
    captionText.innerHTML = image.alt;
}

function showOrderMessage() {
    var modal = document.getElementById("modal");
    var div = document.getElementById("modal-text");

    modal.style.display = "block";
    div.style.display = "block";
}

function closeModal() {
    var modal = document.getElementById("modal");
    var image = document.getElementById("modal-image");
    var text = document.getElementById("modal-text");
    modal.style.display = "none";
    image.style.display = "none";
    text.style.display = "none";
}

// window.onclick = function(event) {
//     var modal = document.getElementById("modal");
//     if (event.target == modal) {
//         modal.style.display = "none";
//     }
// };

// endregion

// region Main page
function buy(id) {
    $.post("buy", {jewel: id}, function () {
        location.href = 'home';
    });
}

function remove(id) {
    $.post("remove", {jewel: id}, function () {
        location.href = 'order';
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

function completeOrder() {
    // $.post("complete", {}, function () {
    //     location.href = 'home';
    // });
}
// endregion Main page