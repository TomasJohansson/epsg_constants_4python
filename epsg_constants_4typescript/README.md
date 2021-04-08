# epsg_constants_4typescript

## Purpose

The constants can be used for getting intellisense help, for example when using Visual Studio Code, and using some TypeScript/JavaScript coordinate transformation library using EPSG codes.  
For example if you want to use the CRS SWEREF99TM but do not remember its EPSG number 3006, then you can find it as in the screenshot below.

![EPSG_SQL](docs/images/sweden_1.png)


## Usage

Install the module into your TypeScript (or JavaScript) module:

```shell-script
pnpm install @programmerare/epsg_constants
```
or
```shell-script
npm install @programmerare/epsg_constants
```

Then you can use this kind of code from a TypeScript module:
```typescript
import {EpsgNumber} from '@programmerare/epsg_constants';
console.log("EpsgNumber WGS84 : " + EpsgNumber.WORLD__WGS_84__4326);
console.log("EpsgNumber SWEREF99TM : " + EpsgNumber.SWEDEN__SWEREF99_TM__3006);
```
You can use the same code as above from a JavaScript [Node.js](https://nodejs.org) module, if you are using *"type": "module"* in your file 'package.json', assuming that you are also using a recent version of '*Node.js*'.  
("type":"module" should work with [Node.js versions 13.2.0 and later](https://nodejs.medium.com/announcing-core-node-js-support-for-ecmascript-modules-c5d6dc29b663))  
An alternative for JavaScript, if you are not using *"type": "module"*  is to use the *require* syntax instead as below:
```javascript
const {EpsgNumber} = require("@programmerare/epsg_constants");
console.log("EpsgNumber WGS84 : " + EpsgNumber.WORLD__WGS_84__4326);
console.log("EpsgNumber SWEREF99TM : " + EpsgNumber.SWEDEN__SWEREF99_TM__3006);
```

If you for some unknown reason would like to use a big file with constants from a webpage, it is possible by including the file ['node_modules/@programmerare/epsg_constants/dist/epsg_constants_bundle.js'](https://github.com/TomasJohansson/epsg_constants_4typescript/blob/main/epsg_constants/dist/epsg_constants_bundle.js) in a webpage as in the [example webpage](https://github.com/TomasJohansson/epsg_constants_4typescript/blob/main/example_javascript_browser_bundle/index.htm)

## License

The constants in this library was [generated](https://github.com/TomasJohansson/crsTransformations/tree/master/crs-transformation-code-generation) based on data from [EPSG](http://www.epsg.org) Dataset.
It is released with license MIT.

Regarding the data itself: Ownership of the EPSG Dataset by IOGP is acknowledged as in the 
[Terms of Use](https://epsg.org/terms-of-use.html)

Some quotes from the above linked webpage 'Terms of use':
> "... The EPSG Facilities are published by IOGP at no charge.  
>  Distribution for profit is forbidden ...  
>  Ownership of the EPSG Dataset by IOGP must be acknowledged ... "  