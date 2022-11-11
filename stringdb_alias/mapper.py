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

        # TODO: Sort so that best match is first always, filter out entries if necessary.

    def get_string_ids(self, aliases):
        """Get STRING IDs for a list of aliases"""
        
        if not isinstance(aliases, pd.Series):
            aliases = pd.Series(aliases)
        
        alias_set = aliases.drop_duplicates()

        best_matches = self.aliases[self.aliases.alias.isin(alias_set)].groupby(
            ['alias']
        ).protein.first()

        return aliases.map(best_matches)
