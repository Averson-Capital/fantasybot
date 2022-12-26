import pandas as pd 
import numpy as np

def process_gamelogs(df, fname = None, lname = None): 
    df = df.rename({'Unnamed: 7': 'gmresult'}, axis = 1)
    df = df.drop(['Unnamed: 0', 'Unnamed: 5', 'Rk', 'G'],axis=1)
    df['Age'] = df['Age'].apply(lambda x: x.split('-')[0])
        
    df['GmResult'] = df['gmresult'].str[0]
    df['PtsDiff'] = df['gmresult'].str[3:5]
    df.drop('gmresult', axis = 1, inplace = True)
    
    
    
    df.Date = pd.to_datetime(df.Date).dt.strftime('%Y%m%d')    
    
    df['MP'] = df['MP'].apply(lambda x: [int(x) for x in x.split(':') if len(x) <= 5])
    df['MP'] = df['MP'].apply(lambda x: (x[0]*60 + x[1])/60 if len(x) != 0 else 0)

    #df['diff'] = df.gmresult.apply(lambda x: x[1])
    
    df[['+/-', 'PtsDiff']] = df[['+/-', 'PtsDiff']].applymap(lambda x: x.replace('+',''))
    
    if fname != None and lname != None: 
        df['FirstName'] = fname
        df['LastName'] = lname
    
    return df.fillna(0)




def process_gamelogs(df, fname = None, lname = None): 
    df = df.rename({'Unnamed: 7': 'gmresult'}, axis = 1)
    df = df.drop(['Unnamed: 0', 'Unnamed: 5', 'Rk', 'G'],axis=1)
    df['Age'] = df['Age'].apply(lambda x: x.split('-')[0])
        
    df['GmResult'] = df['gmresult'].str[0]
    df['PtsDiff'] = df['gmresult'].str[3:5]
    df.drop('gmresult', axis = 1, inplace = True)
    
    
    
    df.Date = pd.to_datetime(df.Date).dt.strftime('%Y%m%d')    
    
    df['MP'] = df['MP'].apply(lambda x: [int(x) for x in x.split(':') if len(x) <= 5])
    df['MP'] = df['MP'].apply(lambda x: (x[0]*60 + x[1])/60 if len(x) != 0 else 0)

    #df['diff'] = df.gmresult.apply(lambda x: x[1])
    
    df[['+/-', 'PtsDiff']] = df[['+/-', 'PtsDiff']].applymap(lambda x: x.replace('+',''))
    
    if fname != None and lname != None: 
        df['FirstName'] = fname
        df['LastName'] = lname
    
    return df.fillna(0)


def concatenate_game_log(path): 
        log_dir = 'data/player_gamelogs'
        dfs = []
        for df in tqdm(os.listdir(log_dir)): 
            try: 

                if df[0] == '.': 
                    continue
                #print(df)

                filename = df.split('_')

                #print(filename)
                firstnm = filename[1]
                lastnm = filename[0]

                #print (firstnm, lastnm)


                cur_df = pd.read_csv(f'{log_dir}/{df}')
                dfs.append(process_gamelogs(cur_df, firstnm, lastnm))

            except Exception as e: 
                print(f'error processing {firstnm} {lastnm}') 
                continue
                
                
        return pd.concat(dfs)