from stringdb_alias import HGNCMapper

mapper = HGNCMapper('string-data/9606.protein.info.v11.5.txt.gz', 'string-data/9606.protein.aliases.v11.5.txt.gz')

print(mapper.get_string_ids(['ADCK2', 'TOMM7', 'PRODH']))

print(mapper.get_hgnc_ids(['9606.ENSP00000072869', '9606.ENSP00000351214', '9606.ENSP00000481127']))