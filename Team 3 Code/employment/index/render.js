const fs = require("fs");
const path = require("path");

const getIndex = (fname = "") => {
    const folder = path.resolve("../html") + "/" + fname;
    const files = fs.readdirSync(folder);
    
    const baseURL = "../html/" + (fname === "" ? "" : fname + "/");
    let html = "", md = "";

    files.forEach(file => {
        if (path.extname(file) == ".html") {
            const name = path.basename(file, path.extname(file));
            html += `<a href="${baseURL}${file}">${name}</a>\n`;
            md += `- [${name}](${baseURL}${file})\n`;
        }
    });

    return { html: html, md: md };
};

let contentHTML = `<html lang="en">\n<head>\n<style>\na { display: block; }\n</style>\n</head>\n<body>\n<h1>Employment</h1>\n\n`;
let contentMD = "# Employment\n\n";

// Line charts

contentHTML += `<h2>Line Charts</h2>\n\n`;
contentMD += `## Line Charts\n\n`;

let res = getIndex("");

contentHTML += res.html;
contentMD += res.md;

// Stacked area charts

contentHTML += `\n<h2>Stacked Area Charts</h2>\n\n`;
contentMD += `\n## Stacked Area Charts\n\n`;

res = getIndex("stacked");

contentHTML += res.html;
contentMD += res.md;

// Write
contentHTML += `\n\n</body>\n</html>`;

const fileHTML = path.resolve("./index.html");
const fileMD = path.resolve("./README.md");

fs.writeFileSync(fileHTML, contentHTML);
fs.writeFileSync(fileMD, contentMD);
