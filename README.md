# EPSG constants

This Python package simply provides one Python class 'EpsgNumber' with lots of EPSG constants (which are used for defining coordinate reference systems).  
Those constants can be used for getting intellisense help, for example when using Visual Studio Code or PyCharm.

Visual Studio Code:  
![VScode](https://raw.githubusercontent.com/TomasJohansson/epsg_constants_4python/main/docs/images/epsg_constants_4python_vscode.gif)


PyCharm:  
![PyCharm](https://raw.githubusercontent.com/TomasJohansson/epsg_constants_4python/main/docs/images/epsg_constants_4python_pycharm.gif)

## Usage example

```python
# pip install epsg-constants
from epsg_constants.epsg_number import EpsgNumber

print("EpsgNumber WGS84 : " + str(EpsgNumber.WORLD__WGS_84__4326))
print("EpsgNumber SWEREF99TM : " + str(EpsgNumber.SWEDEN__SWEREF99_TM__3006))
```

## License information

The Python class with constants in this package was [generated](https://github.com/TomasJohansson/crsTransformations/tree/master/crs-transformation-code-generation) based on data from [EPSG](https://epsg.org/) Dataset.  
It is released with license MIT.

Regarding the EPSG **data**: Ownership of the EPSG Dataset by IOGP is acknowledged as in the [Terms of Use](https://epsg.org/terms-of-use.html)

Some quotes from the above linked webpage 'Terms of use':
> "... The EPSG Facilities are published by IOGP at no charge.
>  Distribution for profit is forbidden ...
>  Ownership of the EPSG Dataset by IOGP must be acknowledged ... "

## Version information

When the Python class was generated, the EPSG dataset version 10.011 was used.  
The EPSG version number is also used for the major/minor (10.11) numbers of this pypi package.
