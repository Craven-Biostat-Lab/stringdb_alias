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


class HGNCMapper:
    """Mapper for HGNC IDs.
    This mapper is optimized for correctly mapping human HGNC Gene Symbols to STRING protein IDs
    """

    def __init__(self, info_file, aliases_file) -> None:
        """Initialize the mapper object
        
        Parameters
        ----------
        info_file
            The info file to use from string-db.org
        aliases_file
            The aliases file to use from string-db.org
        """

        # Thanks to Damian Szklarczyk from string-db for sharing the priority list for human
        hgnc_source_priority = [
            'BioMart_HUGO',
            'Ensembl_HGNC',
            'Ensembl_HGNC_curated_gene',
            'Ensembl_UniProt_GN',
            'BLAST_UniProt_GN',
            'BLAST_KEGG_NAME'
        ]

        aliases_df = pd.read_table(
            aliases_file,
            names=['protein', 'alias', 'source'],
            header=0
        )

        # Highest priority match is the gene name
        preferred_names = pd.read_table(
            info_file,
            header=0,
            names=['protein', 'alias'],
            usecols=[0,1]
        )

        preferred_names['source'] = 'preferred_name'
        preferred_names['priority'] = -1

        # Priority list as pandas table
        priority_df = pd.DataFrame({
            'source': hgnc_source_priority,
            'priority': range(len(hgnc_source_priority))})
        
        # Assign priorities to aliases frame, concatenate with preferred names, and sort
        self.lookups = pd.concat(
            [
                preferred_names,
                aliases_df.merge(priority_df, how='left', on='source')
            ],
            ignore_index=True
        ).sort_values(
            'priority',
            ascending=True,
            na_position='last',
            ignore_index=True
        )


    def get_string_ids(self, aliases):
        """Get STRING IDs for a list of aliases"""
        
        if not isinstance(aliases, pd.Series):
            aliases = pd.Series(aliases)
        
        alias_set = aliases.drop_duplicates()

        best_matches = self.lookups[self.lookups.alias.isin(alias_set)].groupby(
            ['alias']
        ).protein.first()

        return aliases.map(best_matches)


    def get_hgnc_ids(self, string_ids):

        if not isinstance(string_ids, pd.Series):
            string_ids = pd.Series(string_ids)
        
        id_set = string_ids.drop_duplicates()

        best_matches = self.lookups[self.lookups.protein.isin(id_set)].groupby(['protein']).protein.first()

        return string_ids.map(best_matches)