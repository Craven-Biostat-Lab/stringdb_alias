"""ID mapper, converts from one type of ID to another"""

import pandas as pd

class IDMapper:
    """ID mapper, converts from one type of ID to another"""

    def __init__(self, aliases_file) -> None:
        """Initialize the mapper object
        
        Parameters
        ----------
        aliases_file
            The aliases file to use from string-db.org
        """
        self.aliases = pd.read_table(
            aliases_file,
            delimiter=' ',
            names=['protein', 'alias', 'source'],
            header=0
        )

    def get_proteins(self, aliases):
        pass
