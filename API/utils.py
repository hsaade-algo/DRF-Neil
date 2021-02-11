from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    """Handles API Exceptions"""
    # exc: exception to be handled
    # context: dict of additional info
    response = exception_handler(exc, context)

    # Handling Authentication Errors
    if response is not None and response.status_code == 401:
        response.data['status_code'] = response.status_code
        response.data['detail'] = 'Authentication Error - Please log in first!'

    # Handling Permission Errors
    elif response is not None and response.status_code == 403:
        response.data['status_code'] = response.status_code
        response.data['detail'] = 'Permission Error - Access Denied for this endpoint!'

    # Handling Login Errors
    elif response is not None and response.status_code == 400:
        if response.data["non_field_errors"]:
            if response.data["non_field_errors"][0] == 'Unable to log in with provided credentials.':
                response.data = {}
                response.data['status_code'] = response.status_code
                response.data['detail'] = 'Wrong Username or Password - Please try again!'

    return response