# Diavlo

### Comandos de setup:
> `git clone git@github.com:Zen-kun04/Diavlo.git`

> `npm i`

> `pip install -r requirements.txt`

### Antes de empezar a programar:
> Crear tu rama personal => `git branch -M <nombre de tu rama>`

> Subir la rama al repositorio (finalizar la creacion) => `git push origin <nombre de tu rama>`

> Cambiarte a tu rama ya creada => `git checkout <nombre de tu rama>`

### Comandos de commit:
> `git add .` => Agregar todos los cambios

> `git commit -m "update"` => Confirmar la subida de los cambios con el mensaje "update"

> `git push origin <nombre de tu rama>` => Subir los cambios al repositorio (la version de tu rama)

### Comandos generales:
> `npm run build-electron` => Compilar todos los archivos de Electron (SASS del src/ incluido)

> `npm run start-electron` => Lanzar la aplicacion de Electron después de haber compilado los archivos con el comando anterior

> `npm run build-parcel` => Compilar todos los archivos para Parcel (TypeScript, HTML, SCSS, imagenes, etc)

> `npm run start-parcel` => Lanzar la aplicacion de Parcel después de haber compilado los archivos con el comando anterior

> `npm run build-all` => Compilar Electron + Parcel (en orden) en caso de querer compilarlo todo y evitar ejecutar build-electron y build-parcel

> `npm run parcel` => Compilar y ejecutar la aplicacion Parcel (build-parcel + start-parcel)

> `npm run electron` => Compilar y ejecutar la aplicacion Electron (build-electron + start-electron)

### Orden de ejecucion para compatiblidad Pagina x Electron:
1. Build Electron
2. Build Parcel
3. Start app (Parcel o Electron)
#### Explicacion del orden:
> El punto de este orden es que al compilar los archivos de Electron también compila los archivos SCSS los cuales usa Parcel. Pero en este proyecto Parcel va a usar los SCSS **YA COMPILADOS** por lo tanto se compila primero Electron, al compilar con Parcel justo después no nos dara ningun error puesto que los HTML llaman a un CSS (anteriormente SCSS) el cual ya fue compilado por Electron y ya esta disponible.
De haberlo hecho al revés (primero Parcel y luego Electron) no nos habria dejado compilarlo ya que los HTML piden un CSS que no existe y eso a Parcel no le gusta.
