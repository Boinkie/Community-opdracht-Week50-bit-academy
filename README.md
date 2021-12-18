# Community-opdracht-Week50-bit-academy
Mijn programmeeroplossing voor de vraagstukken uit de Community Challenge in week 50, georganiseerd door de Bit Academy.

We gaan in deze opdracht een rooster maken voor de coaches van de Bit Academy en vergelijken o.a. gewerkte uren met de uren die als voorkeur zijn opgegeven.

Note;
Bij het delen van kolommen en toevoegen van kolommen aan dataframes kreeg ik een warning:
"A value is trying to be set on a copy of a slice from a DataFrame".
Oplossing:
This error is usually a result of creating a slice of the original dataframe before declaring your new column. To avoid the error add your new column to the original dataframe and then create the slice: .loc[row_indexer,col_indexer] = value instead. 
Zie: https://re-thought.com/how-to-add-new-columns-in-a-dataframe-in-pandas/

