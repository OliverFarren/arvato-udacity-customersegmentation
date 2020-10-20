import pickle
import numpy as np
import pandas as pd
import math

analysis_dir = './analysis'
dataset_dir = './datasets'

class Pickler:
        
    @staticmethod
    def make_file_path(filename):
        return(dataset_dir+'/'+filename+'.pickle')
    
    @staticmethod
    def dump(obj,filename):
        if isinstance(filename,str):
            with open(Pickler.make_file_path(filename),'wb') as f:
                pickle.dump(obj,f)
        else:
            raise TypeError(f'Expected filename of type str but got type: {type(filename)}')
            
    @staticmethod
    def load(filename):
        with open(Pickler.make_file_path(filename),'rb') as f:
            obj = pickle.load(f)
            return obj
        

class VerbosityLevels():
    '''
    Define a set of levels for verbosity.
    '''
    DEBUG = 100
    HIGH = 75
    MED = 50    
    LOW = 25
    NONE = 0

class VerbosityPrinter:
    '''
    Define a set of calculated print functions that can be used to conditionally print messages
    '''
    
    _VL = VerbosityLevels()
    
    def __init__(self,verbosity_level):
        self.verbosity_level = verbosity_level
    
    @property
    def is_debug(self):
        return(self.verbosity_level >= self._VL.DEBUG)
        
    def debug(self,*args,**kwargs):
        if self.is_debug:
            print(*args,**kwargs)
          
    @property
    def is_high(self):
        return(self.verbosity_level >= self._VL.HIGH)
        
    def high(self,*args,**kwargs):
        if self.is_high:
            print(*args,**kwargs)
    
    @property
    def is_med(self):
        return(self.verbosity_level >= self._VL.MED)
        
    def med(self,*args,**kwargs):
        if self.is_med:
            print(*args,**kwargs)
    
    @property
    def is_low(self):
        return(self.verbosity_level >= self._VL.LOW)
        
    def low(self,*args,**kwargs):
        if self.is_low:
            print(*args,**kwargs)
    
    @property
    def is_none(self):
        return(self.verbosity_level >= self._VL.NONE)
    
    def none(self,*args,**kwargs):
        if self.is_none:
            print(*args,**kwargs)


class AzdiasUnknownValueManager:
        
    def __init__(
        self,
        *,
        replacer=np.NaN,
        ignore_features=[],
        azdias_analysis_path = analysis_dir + '/azdias_analysis.csv',
        verbosity=VerbosityLevels.NONE
    ):
        self.replacer=replacer
        self.ignore_features=ignore_features
        self.azdias_analysis_path = azdias_analysis_path
        self._azdias_analysis = None
        self.vp = VerbosityPrinter(verbosity)
        
        
    @property
    def azdias_analysis(self):
        if self._azdias_analysis is None:
            self._azdias_analysis = pd.read_csv(self.azdias_analysis_path,sep=',',header=0)
        
        return(self._azdias_analysis)
        
    
    def get_clean_df(self,df):
        
        vp = self.vp
        
        clean_df = df.copy()
        self.num_rows = len(clean_df.index)
        
        vp.med("% of Values Replaced:")
        features_to_change = self._get_features_to_change()
        for fe in features_to_change:
            
            unknowns = self._get_unknowns(fe)
            
            vp.debug(f'{fe} - Unknown values:{unknowns}')

            if vp.is_med: 
                self._print_stats(clean_df[fe],fe,unknowns)            
            
            clean_df[fe] = self._replace_unknowns(clean_df[fe],unknowns)     
  
        return(clean_df)
    
    
    def _get_features_to_change(self):
        
        aa = self.azdias_analysis
        aa_unknown_only = aa[aa.uknown_v0.notnull()]
    
        features_with_unknown = [fe for fe in aa_unknown_only.feature_name.values if fe not in self.ignore_features]
    
        return(features_with_unknown)
    
    
    def _get_unknowns(self,fe):
        
        aa = self.azdias_analysis
        
        unknown_0 = aa.uknown_v0[aa.feature_name == fe].values[0]
        unknown_1 = aa.uknown_v1[aa.feature_name == fe].values[0]
    
        assert not np.isnan(unknown_0)
        if np.isnan(unknown_1): unknown_1 = None
        
        return(unknown_0,unknown_1)
    
    
    def _replace_unknowns(self,series,unknowns):
        
        for unknown in unknowns:
            if unknown != None:
                series = series.replace([float(unknown),int(unknown)],self.replacer)
        return series
        
    def _print_stats(self,series,fe,unknowns):
        
        total_unknowns_replaced = self._get_total_unknowns(series,unknowns)
        
        if total_unknowns_replaced > 0:
            total_unknowns_replaced_percent = math.ceil(total_unknowns_replaced*100/self.num_rows)        
            print(f"{fe}: {total_unknowns_replaced_percent}%")
        
            
    def _get_total_unknowns(self,series,unknowns):
       
        total_unknowns = sum([series.value_counts()[unknown] for unknown in unknowns if unknown in series.value_counts()])
        return(total_unknowns)