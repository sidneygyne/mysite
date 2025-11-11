import json

import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_post_view_exercise(client):
    url = reverse("exercise")
    response = client.get(url)
    assert response.status_code == 200

    assert response.content == b'Olá, seja bem vindo!'