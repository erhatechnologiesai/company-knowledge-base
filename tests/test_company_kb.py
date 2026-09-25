import unittest
from fastapi.testclient import TestClient
from app.api import app

class TestCompanyKB(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_public_access(self):
        res = self.client.post("/ask", json={"user_role": "intern", "query": "What is our office policy?"})
        self.assertEqual(res.status_code, 200)
        self.assertTrue(res.json()["access_granted"])

    def test_rbac_denial(self):
        res = self.client.post("/ask", json={"user_role": "intern", "query": "What are our financial reserves?"})
        self.assertEqual(res.status_code, 200)
        self.assertFalse(res.json()["access_granted"])
        self.assertIn("RESTRICTED", res.json()["answer"])

    def test_rbac_executive_approval(self):
        res = self.client.post("/ask", json={"user_role": "executive", "query": "What are our financial reserves?"})
        self.assertEqual(res.status_code, 200)
        self.assertTrue(res.json()["access_granted"])

if __name__ == "__main__":
    unittest.main()
