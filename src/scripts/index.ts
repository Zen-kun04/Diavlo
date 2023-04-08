const test: string = "hola";
const numero: number = 123;

let algo: (string | number) = 123
let a: (string | number)[] = ["s", 123, "A"]

interface Test {
    nombre: string,
    edad: number
}

const json: Test = {
    nombre: "Baguette",
    edad: 19
}

const json2: Test[] = [
    {
        nombre: "Baguette",
        edad: 19
    },
    {
        nombre: "Joker",
        edad: 20
    }
]

console.log("hola mundo");
