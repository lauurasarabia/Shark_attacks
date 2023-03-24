

def reading_csv():
    attacks = pd.read_csv(f"/Users/lauurasarabia/ironhack/projects/Shark_attacks/data/attacks.csv", encoding="latin1")
    return attacks

def dropping_nan():
    attacks.dropna(how='all', inplace=True)
    attacks.dropna(axis=0, thresh=20, inplace=True)
    return attacks

def nan_values(df):
    """
    It counts all the "NaN" values by column on your DataFrame
    """
    result = df.isna().sum()
    return result

def dropping_columns():
    attacks.drop(['href formula', 
              'pdf', 
              'Date',
              'href',
              'Case Number.1', 
              'Case Number.2', 
              'Year', 
              'Name',
              'Sex ',
              'Case Number', 
              'Area',
              'Location',
              'original order',
              'Investigator or Source',
              'Time',
              'Type',
              'Unnamed: 22', 
              'Unnamed: 23'], 
             axis=1, inplace=True)
    return attacks

def renaming_columns():
    attacks.rename(columns={"Species ": "Species"}, inplace=True)
    attacks.reset_index(drop=True, inplace=True)
    return attacks

def replacing_char():
    attacks["Age"].replace({"40s": "40", "20s": "20",
                       "18 months": "1", "9 months": "1",
                       "30s": "30", "9 or 10": "9",
                       "Teen": "14", "teen": "14",
                        "50s": "50", "18 or 20": "19",
                       "12 or 13": "13", "8 or 10": "9",
                        "30 or 36": "33", "6½": "7",
                        "mid-30s": "35", "33 or 37": "35",
                        "21 or 26": "24", "7 or 8": "8",
                        "adult": "40", "(adult)": "40",
                        "young": "24", '"young"': "24",
                        "25 or 28": "27", "13 or 14": "13",
                        "31 or 33": "32", "2½": "3",
                        "10 or 12": "11", "25 to 35": "30",
                        "7      &    31": "7 & 31", 
                        "21, 34,24 & 35":"21 & 34 & 24 & 35",
                        "Both 11": "11 & 11", 
                        "37, 67, 35, 27,  ? & 27" : "37 & 67 & 35 & 27 & ? & 27"
                        
                       }, inplace=True)
    # We drop "Age" NaN values as if we use .fillna could change our hypothesis later on
    attacks.dropna(subset=['Age'], inplace=True)
    attacks.reset_index(drop=True, inplace=True)
    return attacks


