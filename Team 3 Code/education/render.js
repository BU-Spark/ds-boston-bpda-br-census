const fs = require('fs');
const path = require('path');
const folder = path.resolve('./education');
// console.log(folder);

fs.readdir(folder, (err, files) => {
    files.forEach(file => {
        if (path.extname(file) == ".html") {
            console.log(`<a href="./${file}">${path.basename(file, path.extname(file))}</a>`);
        }
    });
});