import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score, classification_report

def run_logistic_regression(df):
    features = ['size_km', 'rel_vel_kps', 'miss_km']
    X = df[features]
    y = df['pha_flag']
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y)
    clf = LogisticRegression(class_weight='balanced', max_iter=1000)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    y_proba = clf.predict_proba(X_test)[:,1]
    acc = accuracy_score(y_test, y_pred)
    auroc = roc_auc_score(y_test, y_proba)
    report = classification_report(y_test, y_pred)
    return {
        'accuracy': acc,
        'auroc': auroc,
        'report': report,
        'model': clf
    }
