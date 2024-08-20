import pandas as pd
import joblib

def load_model(model_path):
    """Load a model from a file."""
    return joblib.load(model_path)

def predict_obesity(data):
    # 모델 로드
    model = load_model('obesity_model.pkl')  # 모델 파일이 현재 스크립트와 같은 디렉토리에 있다고 가정

    # 데이터 준비
    df = pd.DataFrame(data, index=[0])
    columns = ['waist', 'BMI', 'systolic blood pressure', 'diastolic blood pressure', 'ALT']
    df = df.reindex(columns=columns, fill_value=0)  # Fill missing columns with default values (0)

    # 예측
    prediction = model.predict(df)
    prob = model.predict_proba(df)

    return {
        'probability': {
            'obesity': prob[0][1] * 100
        }
    }
