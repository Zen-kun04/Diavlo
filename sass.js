const sass = require('node-sass');
const path = require('path');
const fs = require('fs');

// Ruta del archivo SCSS de entrada
const inputFile = path.join(__dirname, 'src/styles/login.scss');

// Ruta del archivo CSS de salida
const outputFile = path.join(__dirname, 'electron/css/login.css');

// Configuración de node-sass
sass.render({
  file: inputFile,
  outFile: outputFile
}, (error, result) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(outputFile, result.css, (error) => {
      if (error) {
        console.error(error);
      }
    });
  }
});
