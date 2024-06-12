import pytest
from Loan_app import app 

@pytest.fixture()
def client():
    return app.test_client()

def test_pinger(client):
    resp = client.get('/ping')
    assert resp.status_code == 200
    # assert resp == "<p>Hello i am under water!</p>"
    
def test_json(client):
    resp = client.get('/json')
    assert resp.status_code == 200
    assert resp.json == {"message": "Hi i am json!"}

def test_prediction(client):
    test_data = {'Gender': "Male",
                 'Married': "Unmarried",
                 'ApplicantIncome': 50000,
                 'Credit_History': "Cleared Debts",
                 'LoanAmount': 12000
                 }
    resp = client.post('/predict',json=test_data)
    assert resp.status_code == 200
    assert resp.json == {"loan_approval_status": "Rejected"}