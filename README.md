# epsg_constants_4python

## Purpose

The constants can be used for getting intellisense help, for example when using PyCharm or Visual Studio Code, and using some Python coordinate transformation library using EPSG codes.
For example if you want to use the CRS SWEREF99TM but do not remember its EPSG number 3006, then you can find it as in the screenshot below.

![EPSG_SQL](docs/images/sweden_1.png)


## Usage

Install the Python package:

```shell-script
pip install -i epsg-constants-programmerare
```

Then you can use this kind of Python code:
```python
from epsg_constants.epsg_number import EpsgNumber

print("EpsgNumber WGS84 : " + str(EpsgNumber.WORLD__WGS_84__4326))
print("EpsgNumber SWEREF99TM : " + str(EpsgNumber.SWEDEN__SWEREF99_TM__3006))
```

## License

The constants in this library was [generated](https://github.com/TomasJohansson/crsTransformations/tree/master/crs-transformation-code-generation) based on data from [EPSG](http://www.epsg.org) Dataset.
It is released with license MIT.

Regarding the data itself: Ownership of the EPSG Dataset by IOGP is acknowledged as in the [Terms of Use](https://epsg.org/terms-of-use.html)

Some quotes from the above linked webpage 'Terms of use':
> "... The EPSG Facilities are published by IOGP at no charge.
>  Distribution for profit is forbidden ...
>  Ownership of the EPSG Dataset by IOGP must be acknowledged ... "
