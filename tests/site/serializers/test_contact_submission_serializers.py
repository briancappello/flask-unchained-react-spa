from marshmallow.exceptions import ValidationError


def test_contact_submission_serializer():
    from backend.serializers import ContactSubmissionSerializer
    serializer = ContactSubmissionSerializer()

    # check it escapes html tags, and converts paragraphs to html
    data = {'message': '<h1>hello</h1>\nworld'}
    msg = serializer.message_to_html(data)['message']
    assert '<h1>' not in msg, 'it should escape html from user-submitted messages'
    assert msg.count('<p>') == 2, 'it should wrap paragraphs in <p> tags'
    assert msg.count('</p>') == 2, 'it should wrap paragraphs in <p> tags'

    # check required fields
    try:
        serializer.load({'name': None, 'email': None, 'message': None})
    except ValidationError as e:
        errors = e.normalized_messages()
        assert 'Name is required.' in errors['name']
        assert 'Email is required.' in errors['email']
        assert 'Message is required.' in errors['message']
        assert len(errors) == 3, errors.keys()
    else:
        assert False, 'Expected ValidationError to be raised'

    # check email must be valid
    try:
        serializer.load({'email': 'invalid'})
    except ValidationError as e:
        errors = e.normalized_messages()
        assert 'Not a valid email address.' in errors['email']
    else:
        assert False, 'Expected ValidationError to be raised'
