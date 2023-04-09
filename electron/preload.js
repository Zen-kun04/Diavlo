window.addEventListener('DOMContentLoaded', function () {
    var create = function (type, version) {
        var elem = document.createElement('p');
        elem.textContent = "Version de ".concat(type, " es ").concat(version);
        document.getElementsByTagName('body')[0].appendChild(elem);
    };
    for (var _i = 0, _a = ['chrome', 'node', 'electron']; _i < _a.length; _i++) {
        var type = _a[_i];
        create(type, process.versions[type]);
    }
    var test = "hola";
    var numero = 123;
    var algo = 123;
    var a = ["s", 123, "A"];
    var json = {
        nombre: "Baguette",
        edad: 19
    };
    var json2 = [
        {
            nombre: "Baguette",
            edad: 19
        },
        {
            nombre: "Joker",
            edad: 20
        }
    ];
    console.log("hola mundo");
});
