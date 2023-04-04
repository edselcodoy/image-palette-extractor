function componentToHex(val) {
    let hex = val.toString(16);
    return hex.length == 1 ? "0" + hex : hex;
}

function clicked(index) {
    navigator.clipboard.writeText(computeHex(index));
    document.getElementById(`tooltip_${index}`).innerHTML = "Copied!";
}

function showHex(index) {
    let hex_text = computeHex(index);
    document.getElementById(`tooltip_${index}`).innerHTML = hex_text;
}

function computeHex(index) {
    let element = document.getElementById(`square_${index}`);
    let color = element.style.backgroundColor;
    let arr = color.match(/\d+/g);
    let rgb_values = arr.map(x => parseInt(x));
    return "#" + rgb_values.map(x => componentToHex(x)).join("");
}