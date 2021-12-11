import os

# 모델 준비
FILENAME = 'model.pkl'
MODEL_PATH = os.path.abspath(os.path.join(os.getcwd(), FILENAME))

print(MODEL_PATH)