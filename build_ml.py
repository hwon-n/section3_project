# LightGBM 찾아보기

import os
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, RandomizedSearchCV
from lightgbm import LGBMRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from category_encoders.count import CountEncoder
from sklearn.preprocessing import LabelEncoder, StandardScaler
from category_encoders import OneHotEncoder
from category_encoders.cat_boost import CatBoostEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline, Pipeline
from sklearn.metrics import accuracy_score, r2_score, f1_score, mean_absolute_error, mean_squared_error, classification_report, roc_auc_score, plot_confusion_matrix
from category_encoders.target_encoder import TargetEncoder


CSV_FILENAME = 'Games.csv'
CSV_FILEPATH = os.path.join(os.getcwd(), CSV_FILENAME)


Games = pd.read_csv(CSV_FILEPATH)

# train, val, test셋 나누기
train, test = train_test_split(Games, test_size = 0.2, random_state = 42)
train, val = train_test_split(train, test_size = 0.2, random_state=42)


# Tag 열 전처리 위해서 55개 이상의 Tag 목록 만들기
over_50_Tag = train['Tag'].value_counts() >= 50
over_50 = over_50_Tag.to_frame()
true_over = over_50.loc[(over_50.Tag == True)]
true_over = true_over.reset_index()
condition = true_over['index'].values.tolist()

# Tag_list = ['Singleplayer', 'Full controller support', 'RPG', '2D', 'exclusive', 'Partial Controller Support', 'Co-op', 'Horror', 'Multiplayer']
Tag_list = condition[:9]

# 데이터 전처리 위한 list
platform_list = ['Commodore / Amiga', 'SEGA', 'Web', 'Neo Geo']
Genre_list = ['Racing', 'Arcade', 'Sports', 'Platformer', 'Massively Multiplayer', 'Family', 'Fighting', 'no genre', 'Board Games', 'Card', 'Educational']

def platform(p):
    if p == 'iOS' or p == 'Android':
        return 'Mobile'
    elif p in platform_list:
        return 'other'
    elif p in ['Nintendo', 'PlayStation', 'Xbox']:
        return 'Video/Console'
    elif p == 'Apple Macintosh':
        return p
    else:
        return 'PC'


def engineer(df):
    df.Tag = df.Tag.apply(lambda x: x if x in Tag_list else 'other')
    df.Platform = df.Platform.apply(platform)
    df.Genres = df.Genres.apply(lambda x: 'other' if x in Genre_list else x)
    df = df.reset_index(drop=True)

    return df

train = engineer(train)
val = engineer(val)
test = engineer(test)

target = 'Added'

# train, val, test셋 X, y로 분리
X_train = train.drop(target, axis=1)
y_train = train[target]
X_val = val.drop(target, axis=1)
y_val = val[target]
X_test = test.drop(target, axis=1)
y_test = test[target]

encoder_list = ['Platform', 'Genres', 'Tag', 'Esrb_rating']

# multiple linear regression
# linear_pipe = make_pipeline(
#     TargetEncoder(cols = encoder_list),
#     SimpleImputer(),
#     StandardScaler(),
#     LinearRegression()
# )

# linear_pipe.fit(X_train, y_train)
# y_pred = linear_pipe.predict(X_val)


# mse = mean_squared_error(y_val, y_pred)
# rmse = mse ** 0.5
# mae = mean_absolute_error(y_val, y_pred)
# r2 = r2_score(y_val, y_pred)

# print('Training score: ', linear_pipe.score(X_train, y_train)) # 0.15212
# print('Validation score: ', linear_pipe.score(X_val, y_val)) # 0.10359
# print(f'MSE: {mse:.1f}\nRMSE: {rmse:.1f}\nMAE: {mae:.1f}\nR2: {r2:.1f}') # 1786127.8, 1336.5, 839.5, 0.1


# randomforest model\


rf_pipe = make_pipeline(
    TargetEncoder(cols = encoder_list),
    SimpleImputer(),
    StandardScaler(),
    RandomForestRegressor(random_state=42)
)

rf_pipe.fit(X_train, y_train)
y_pred = rf_pipe.predict(X_val)


mse = mean_squared_error(y_val, y_pred)
rmse = mse ** 0.5
mae = mean_absolute_error(y_val, y_pred)
r2 = r2_score(y_val, y_pred)

print('Training score: ', rf_pipe.score(X_train, y_train))
print('Validation score: ', rf_pipe.score(X_val, y_val))
print(f'MSE: {mse:.4f}\nRMSE: {rmse:.4f}\nMAE: {mae:.4f}\nR2: {r2:.4f}')

# for i in list(range(2, 11)):
#     scores = cross_val_score(rf_pipe, X_train, y_train, cv = i, scoring = 'neg_root_mean_squared_error')
#     print(f'cv = {i}, scores = {scores}')
#     print(f'scores mean = {scores.mean()}')


# hyperparameter tuning
dists = {
    'randomforestregressor__n_estimators': [200, 300, 400, 500],
    'randomforestregressor__criterion': ['squared_error', 'absolute_error', 'poisson'],
    'randomforestregressor__max_depth': [2, 5, 8, 11, None],
    'randomforestregressor__min_samples_split': [2, 4, 6, 10, None],
    'randomforestregressor__min_samples_leaf': [2, 5, 8, 10, None],
    'randomforestregressor__max_features': ['auto', 'sqrt', 'log2']
}

clf = RandomizedSearchCV(
    rf_pipe,
    param_distributions = dists,
    n_iter = 5,
    cv = 10,
    verbose = 1,
    scoring = 'neg_root_mean_squared_error',
    n_jobs = -1
)

# clf.fit(X_train, y_train)

# print('best hyperparameter: ', clf.best_params_)
# print('best f1 score: ', clf.best_score_)

new_rf_pipe = make_pipeline(
    TargetEncoder(cols = encoder_list),
    SimpleImputer(),
    StandardScaler(),
    RandomForestRegressor(
        n_estimators = 300,
        min_samples_split = 6,
        min_samples_leaf = 8,
        max_features = 'sqrt',
        criterion ='squared_error',
        random_state = 42
    )
)

new_rf_pipe.fit(X_train, y_train)
y_pred = new_rf_pipe.predict(X_val)


mse = mean_squared_error(y_val, y_pred)
rmse = mse ** 0.5
mae = mean_absolute_error(y_val, y_pred)
r2 = r2_score(y_val, y_pred)

print('Training score: ', new_rf_pipe.score(X_train, y_train))
print('Validation score: ', new_rf_pipe.score(X_val, y_val))
print(f'MSE: {mse:.4f}\nRMSE: {rmse:.4f}\nMAE: {mae:.4f}\nR2: {r2:.4f}') # r2 score: 0.239로 좋아하는 내가 참 싫다