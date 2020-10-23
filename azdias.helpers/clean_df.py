import numpy as np
import pandas as pd
import math

import config
import verbosity as v
import pickler

def unknown_to_nan(df,verbosity=v.NONE):
    '''Takes azdias style dataframe as input and returns with unknowns converted to NaN'''
    
    def _get_features_to_change():

        aa_unknown_only = azdias_analysis[azdias_analysis.uknown_v0.notnull()]

        features_with_unknown = [fe for fe in aa_unknown_only.feature_name.values if fe in df_clean.columns]

        return(features_with_unknown)

    def _get_unknowns():

        unknown_0 = azdias_analysis.uknown_v0[azdias_analysis.feature_name == fe].values[0]
        unknown_1 = azdias_analysis.uknown_v1[azdias_analysis.feature_name == fe].values[0]

        assert not np.isnan(unknown_0)
        if np.isnan(unknown_1): unknown_1 = None

        return(unknown_0,unknown_1)

    def _print_stats():

        total_unknowns_replaced = _get_total_unknowns()

        if total_unknowns_replaced > 0:
            total_unknowns_replaced_percent = math.ceil(total_unknowns_replaced*100/num_rows)        
            print(f"{fe}: {total_unknowns_replaced_percent}%")


    def _get_total_unknowns():

        total_unknowns = sum([df[fe].value_counts()[unknown] for unknown in unknowns if unknown in df[fe].value_counts()])
        return(total_unknowns)        

    def _replace_unknowns():

        for unknown in unknowns:
            if unknown != None:
                df_clean[fe] = df_clean[fe].replace([float(unknown),int(unknown)],np.NaN)

        return(df_clean[fe])
    
    #############################################
    # Main function block
    
    vp = v.VerbosityPrinter(verbosity)
    azdias_analysis = pd.read_csv(config.analysis_dir + '/azdias_analysis.csv',sep=',',header=0)
    
    vp.low('Running unknown_to_nan...')
    
    df_clean = df.copy()
    num_rows = len(df_clean.index)
    
    vp.med("% of Values Replaced")
    features_to_change = _get_features_to_change()
    for fe in features_to_change:
        
        unknowns = _get_unknowns()
        
        vp.debug(f'{fe} - Unknown values:{unknowns}')
        
        if vp.is_med:
            _print_stats()
            
        df_clean[fe] = _replace_unknowns()
                
    vp.low("Finished unknown_to_nan...")
    return(df_clean)


def onehot_encode(series,*,min_value=0,max_value=1,verbosity=v.NONE):
    '''Take a pandas series and return a onehot encoded dataframe'''

    vp = v.VerbosityPrinter(verbosity)
    vp.low('Running onehot_encoder...')
    
    values = series.dropna().unique()
    
    vp.med(values)
    
    df = pd.DataFrame()
    for value in sorted(values):
        col_enc     = (f'{series.name}_{math.ceil(value)}')
        df[col_enc] = series.map(lambda x: max_value if x == value else min_value)
        
        vp.high(col_enc)
        
    vp.low('Finished onehot_encoder.')
    return(df)


def onehot_encode_df(df,verbosity=v.NONE):
    
    vp = v.VerbosityPrinter(verbosity)
    
    vp.low('Running onehot_encode_df...')
    
    fe_to_oh = ['ARBEIT','NATIONALITAET_KZ']
    
    for fe in fe_to_oh:
        if fe in df.columns:
            series_oh = onehot_encode(df[fe],verbosity=verbosity)
            df = pd.concat([df,series_oh],axis=1)
            df = df.drop(fe,axis=1)
    
    vp.low('Finished running onehot_encode_df...')
    
    return(df)

def split_cameo_deuintl_2015(df_clean,verbosity=v.NONE):
    '''
    Split the CAEMO_DEUINTL_2015 feature into two.
    
    10,20,30,40,50 corresponds to wealth (W)
    1,2,3,4,5 corresponds to life stage (LS)
    
    Returns a dataframe of the two new features
    '''
    
    vp = v.VerbosityPrinter(verbosity)

    vp.low('Running split_cameo_deuintl_2015...')
    
    wealth_col = 'CAMEO_INTL_2015_W'
    life_stage_col = 'CAMEO_INTL_2015_LS'
    
    series = df_clean['CAMEO_INTL_2015'].copy()
    series = series.replace(['XX'],0)
    series = series.replace([np.NaN],0)
    series = series.astype(float)
    
    cameo_intl_df = pd.DataFrame()
    
    cameo_intl_df[wealth_col] = series.apply(lambda x: math.floor(x/10))
    cameo_intl_df[life_stage_col] = series.apply(lambda x: x % 10)
    
    cameo_intl_df[wealth_col] = cameo_intl_df[wealth_col].replace([0],np.NaN)
    cameo_intl_df[life_stage_col] = cameo_intl_df[life_stage_col].replace([0],np.NaN)
    
    df_clean = pd.concat([df_clean,cameo_intl_df],axis=1)
    df_clean = df_clean.drop('CAMEO_INTL_2015',axis=1)
    
    vp.low('Finished split_cameo_deuintl_2015...')
    
    return(df_clean)


def etl_pipeline(df,*,cols_keep=None,verbosity=v.NONE):

    vp = v.VerbosityPrinter(verbosity)
    
    vp.low('Running etl_pipeline...')
    
    df_clean = df.copy()
    
    if cols_keep == None:
        cols_keep = pickler.load('cols_keep')
 
    df_clean = df_clean[cols_keep]    
    df_clean = unknown_to_nan(df_clean,verbosity=verbosity)
    df_clean = onehot_encode_df(df_clean,verbosity=verbosity)
    df_clean = split_cameo_deuintl_2015(df_clean,verbosity=verbosity)

    vp.low('Finished running etl_pipeline.')

    return(df_clean)
