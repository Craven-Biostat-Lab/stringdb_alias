# stringdb_alias
A python package for working with string-db.org aliases (gene and protein ID mapping).

This package is specifically for working offline using downloaded files.
For accessing the STRINGdb API instead, see for example the [stringdb](https://pypi.org/project/stringdb/) package.

## Usage

### Mapping HGNC symbols

First, download the aliases and info files from string-db.org:

```
$ wget https://stringdb-static.org/download/protein.info.v11.5/9606.protein.info.v11.5.txt.gz
$ wget https://stringdb-static.org/download/protein.aliases.v11.5/9606.protein.aliases.v11.5.txt.gz
```

Then, initialize our mapper object with the downloaded files, and map lists of IDs

```
from stringdb_alias import HGNCMapper

mapper = HGNCMapper('9606.protein.info.v11.5.txt.gz', '9606.protein.aliases.v11.5.txt.gz')

print(mapper.get_string_ids(['ADCK2', 'TOMM7', 'PRODH']))
```

The mapper always returns a [pandas Series](https://pandas.pydata.org/pandas-docs/stable/reference/series.html).
This is convenient for directly mapping a column in a [DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/frame.html).
Moreover, if the input list is a pandas Series, the index is preserved in the output.