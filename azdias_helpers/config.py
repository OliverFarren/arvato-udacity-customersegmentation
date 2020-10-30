''' Declaration global variables
    Configure new directories
'''

import os
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

analysis_dir = './analysis'
dataset_dir = './datasets'

for new_dir in analysis_dir,dataset_dir:
    try:
        os.mkdir(new_dir)
        print(f"made new directory: {new_dir}")
    except FileExistsError:
        pass


imputer_name = 'SimpleImputer_model_mf'
imputer = SimpleImputer(strategy='most_frequent')

scaler_name = 'StandardScaler_model'
scaler = StandardScaler()

pca_name = 'PCA_model_basic'

cols_keep_notebook1_clustering = [
    'NATIONALITAET_KZ', 'ANZ_PERSONEN', 'CJT_TYP_5', 'D19_SOZIALES', 'CJT_TYP_6', 'CJT_TYP_3',
 'ONLINE_AFFINITAET', 'KOMBIALTER', 'LP_FAMILIE_FEIN', 'ALTERSKATEGORIE_GROB',
 'CJT_TYP_4', 'SEMIO_KRIT', 'FINANZ_VORSORGER', 'FINANZ_MINIMALIST', 'FINANZ_SPARER',
 'CJT_TYP_1', 'LP_STATUS_FEIN', 'SEMIO_LUST', 'OST_WEST_KZ', 'SEMIO_PFLICHT', 'FINANZ_ANLEGER',
 'ANZ_STATISTISCHE_HAUSHALTE', 'ANREDE_KZ', 'W_KEIT_KIND_HH', 'HH_EINKOMMEN_SCORE',
 'KBA13_BMW', 'LP_LEBENSPHASE_FEIN', 'D19_GESAMT_DATUM', 'SEMIO_TRADV', 'SEMIO_VERT',
 'D19_VERSAND_OFFLINE_DATUM', 'FINANZTYP', 'AGER_TYP', 'CJT_TYP_2', 'PRAEGENDE_JUGENDJAHRE',
 'EINGEZOGENAM_HH_JAHR', 'D19_VERSAND_DATUM', 'D19_BEKLEIDUNG_GEH', 'D19_BUCH_CD',
 'KBA13_HALTER_25', 'VERDICHTUNGSRAUM', 'RETOURTYP_BK_S']