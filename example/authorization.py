from .extensions import login_manager

@login_manager.user_loader
def load_user(user_id):
    return {'id': user_id}


@login_manager.request_loader
def load_user_from_request(request):
    return None
