import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('winequalityN.csv')

df.dropna(inplace=True)

# Feature Engineering
df_new = df.drop('free sulfur dioxide', axis = 1)

df_new['alcohol density'] = (df_new['alcohol']**5)/df_new['density']

df_ml = pd.get_dummies(df_new, drop_first=True)

df_ml = df_ml.drop(['density', 'alcohol'], axis = 1)

Y = df_ml['quality'].apply(lambda y: 1 if y>=6 else 0)

X = df_ml.drop('quality', axis = 1)

# Standardize feature values so that high valued feautures don't influence others

scaler = StandardScaler()
scaler.fit(X)
X_standard = scaler.transform(X)
X = X_standard #standardised numpy array of features

# train model
rfc = RandomForestClassifier()
rfc.fit(X, Y)

def prediction(i_fixed_acidity, i_volatile_acidity, i_citric_acid, i_residual_sugar, i_chlorides, i_total_sulfur_dioxide, i_density, i_ph, i_sulphates, i_type_white, i_alcohol):

    i_predict = np.array([i_fixed_acidity, i_volatile_acidity, i_citric_acid, i_residual_sugar, i_chlorides, i_total_sulfur_dioxide, i_ph, i_sulphates, ((i_alcohol**5)/i_density), i_type_white]).reshape(1,-1)
    scaler.fit(i_predict)

    i_predict_std = scaler.transform(i_predict)

    predict_output = rfc.predict(i_predict_std)
    predict_output_int = predict_output[0]

    return predict_output_int