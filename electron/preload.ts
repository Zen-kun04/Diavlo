window.addEventListener('DOMContentLoaded', () => {
    const create = (type: string, version: string | undefined) => {
        const elem: HTMLElement = document.createElement('p');
        elem.textContent = `Version de ${type} es ${version}`;
        document.getElementsByTagName('body')[0].appendChild(elem);
    }

    for(const type of ['chrome', 'node', 'electron']){
        create(type, process.versions[type]);
    }

    

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
    
    
})