from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_participant_removes_email():
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"

    post_response = client.post(f"/activities/{activity_name}/signup?email={email}")
    assert post_response.status_code == 200

    delete_response = client.delete(f"/activities/{activity_name}/signup?email={email}")
    assert delete_response.status_code == 200

    activities = client.get("/activities").json()
    assert email not in activities[activity_name]["participants"]
