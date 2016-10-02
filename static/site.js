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
function metalChecked(id, item) {
    location.href = "metal/" + id + "/" + item.checked;
    // $.post("metal", {metal: id, state: item.checked});
}

function filterChanged(parameter, from_to, value) {
    if (!value || value == "")
        value = '-1';
    location.href = parameter + "/" + from_to + "/" + value;
    // $.post("fineness", {parameter: parameter, value: value});
}

function buy(id) {
    var div = document.getElementById(id + "-number");
    location.href = "buy/" + id + "/" + div.innerHTML;
}

function inc(id) {
    var div = document.getElementById(id + "-number");
    if (div.innerHTML * 1 < 99)
        div.innerHTML = div.innerHTML * 1 + 1;
}

function dec(id) {
    var div = document.getElementById(id + "-number");
    if (1 < div.innerHTML * 1)
        div.innerHTML = div.innerHTML * 1 - 1;
}
// endregion Main page