import pandas as pd

pd.options.mode.chained_assignment = None

jdihn_df = pd.read_csv('data/jdihn_raw.csv')
jdihn_df['judul_dokumen'] = jdihn_df['judul_dokumen'].apply(lambda x: x.strip().rstrip('.'))

temp_df = jdihn_df[['id', 'judul_dokumen', 'status_id', 'tanggal_penetapan']]
temp_df['judul_dokumen'] = temp_df['judul_dokumen'].str.lower()
temp_df.sort_values(['judul_dokumen', 'tanggal_penetapan', 'status_id'], ascending=[True, True, False], inplace=True)
duplicated_df = temp_df[temp_df.duplicated(['judul_dokumen'])]
drop_indexes = duplicated_df.index

new_jdihn_df = jdihn_df.drop(drop_indexes).reset_index(drop=True)
new_jdihn_df['id'] = new_jdihn_df.index + 1
new_jdihn_df.to_csv('data/jdihn_clean.csv')