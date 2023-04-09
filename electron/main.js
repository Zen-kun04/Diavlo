// Modules
var _a = require('electron'), app = _a.app, BrowserWindow = _a.BrowserWindow;
var path = require('path');
// Keep a global reference of the window object, if you don't, the window will
// be closed automatically when the JavaScript object is garbage collected.
var mainWindow;
// Create a new BrowserWindow when `app` is ready
function createWindow() {
    mainWindow = new BrowserWindow({
        width: 1000, height: 800,
        webPreferences: {
            // --- !! IMPORTANT !! ---
            // Disable 'contextIsolation' to allow 'nodeIntegration'
            // 'contextIsolation' defaults to "true" as from Electron v12
            contextIsolation: false,
            nodeIntegration: true
        }
    });
    // Load index.html into the new BrowserWindow
    mainWindow.loadFile('../src/templates/login.html');
    // Open DevTools - Remove for PRODUCTION!
    mainWindow.webContents.openDevTools();
    // Listen for window being closed
    mainWindow.on('closed', function () {
        mainWindow = null;
    });
}
// Electron `app` is ready
app.on('ready', createWindow);
// Quit when all windows are closed - (Not macOS - Darwin)
app.on('window-all-closed', function () {
    if (process.platform !== 'darwin')
        app.quit();
});
// When app icon is clicked and app is running, (macOS) recreate the BrowserWindow
app.on('activate', function () {
    if (mainWindow === null)
        createWindow();
});
