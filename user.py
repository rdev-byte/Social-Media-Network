from django.contrib.auth.models import User

def test_create_user():
    # Create a new user
    user = User.objects.create(username='testuser')

    # Check that the user was created successfully
    assert user is not None

    # Check that the user's username is correct
    assert user.username == 'testuser'

    # Check that the user has an ID (i.e. has been saved to the database)
    assert user.id is not None
