import { resolve } from "path";
const fs = require('fs');

import * as TJS from "typescript-json-schema";

type IconNameSchema = {
  enum: string[]
}

// optionally pass argument to schema generator
const settings: TJS.PartialArgs = {
  //required: true,
};

// optionally pass ts compiler options
const compilerOptions: TJS.CompilerOptions = {
  //strictNullChecks: true,
};

// optionally pass a base path
const basePath = "./";

const program = TJS.getProgramFromFiles(
  [resolve("./node_modules/@fortawesome/fontawesome-common-types/index.d.ts")],
  compilerOptions,
  basePath
);

// We can either get the schema for one file and one type...
function clearAndUpper(text: string) {
  return text.replace(/-/, "").toUpperCase();
}
const schema = TJS.generateSchema(program, "IconDefinition", settings);
let longest = ""
const iconNameTuples = (schema?.definitions?.IconName as IconNameSchema).enum.map(val => {
  // to camel case
  const iconName = "fa" + val.replace(/(^\w|-\w)/g, clearAndUpper);
  if (iconName.length > longest.length) {
    longest = iconName
  }
  return `("${iconName}","${iconName}")`;
})

console.log("Icon names generated in names.py.")
console.log("Longest Icon Name:", longest.length)

const iconNamesPy = `FA_ICON_NAMES = [${iconNameTuples.join(",")}]`

fs.writeFileSync('names.py', iconNamesPy);
