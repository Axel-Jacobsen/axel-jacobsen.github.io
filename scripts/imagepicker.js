// List of files
var images = [
 'hbbpjec.jpg', 'AW16Y0i.jpg', 'XNjq5dC.jpg', 'Z7FLI6v.jpg', 'YWMo1IJ.jpg', 'q5u0Ngd.jpg', 'L6w1YUN.jpg', 'UZH8X4x.jpg', 'afBGhhB.jpg', 'X0sd0Ho.jpg', '7SqL0BC.jpg', 'ra6M5zu-2.jpg', '2dGXJp7.jpg', '3Dap2EL.jpg', 'sDsSu0m.jpg', 'hs6EUln.jpg', 'oSiYCN3.jpg', 'unbenannt3yywl.jpg', 'TNAG0Po.jpg', '2rQoBh8.jpg', 'GLi3zS6.jpg', 'VebP6Ol.jpg', '5bKd1fd.jpg', '1k3VaGh.jpg', 'uENexRC.jpg', 'eexbpm62e1601.jpg', 'QiUF7XB.jpg', 'GGYgJ0G.jpg', 'mQUd1tO.jpg', 'h8R5xMB.jpg', 'IW7I8dT.jpg', 'AdF1fVN.jpg', 'vQA6IsA.jpg', 'Spaceshuttle-Trough-Clouds.jpg', 'n0x244u8ajez.png', 'EeE9J.jpg', 'uasqmx0nfuhz.jpg'
];

function choosePic() {
    var randomNum = Math.floor(Math.random() * images.length);
    document.getElementById("background").src = "WallPapers/" + images[randomNum];
}

window.onload = choosePic;
