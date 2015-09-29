import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django_bitbucket_hook.models import Hook


@csrf_exempt
@require_http_methods(["POST"])
def only_hook(request):
    info, user, repo = get_payload(request)

    if not user and not repo:
        return JsonResponse({'success': False, 'message': 'No JSON data or URL argument : cannot identify hook'})

    try:
        hook = Hook.objects.get(user=user, repo=repo)
        hook.execute()
    except Hook.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Not exist Hook'})
        # If there is not a script defined, then send a HookSignal
        # TODO
    return JsonResponse({})


@csrf_exempt
@require_http_methods(["POST"])
def hook_name(request, name):
    info, user, repo = get_payload(request)

    if not user and not repo and not name:
        return JsonResponse({'success': False, 'message': 'No JSON data or URL argument : cannot identify hook'})

    try:
        hook = Hook.objects.get(user=user, repo=repo, name=name)
        hook.execute()
    except Hook.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Not exist Hook'})
        # If there is not a script defined, then send a HookSignal
        # TODO
    return JsonResponse({})


@csrf_exempt
@require_http_methods(["POST"])
def hook_name_branch(request, name, branch):
    info, user, repo = get_payload(request)
    repo_branch = info.get('ref', False)
    _, repo_branch = repo_branch.rsplit('/', 1)

    if not user and not repo and not name and not branch and not repo_branch:
        return JsonResponse({'success': False, 'message': 'No JSON data or URL argument : cannot identify hook'})

    try:
        if repo_branch != branch:
            return JsonResponse({'success': False, 'message': 'This is not the right branch'})

        hook = Hook.objects.get(user=user, repo=repo, name=name, branch=branch)
        hook.execute()
    except Hook.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Not exist Hook'})
        # If there is not a script defined, then send a HookSignal
        # TODO
    return JsonResponse({})


def get_payload(request):
    # Git repo information from post-receive payload
    if request.META.get('CONTENT_TYPE') == "application/json":
        payload = json.loads(request.body.decode('utf8'))
    else:
        # Probably application/x-www-form-urlencoded
        payload = json.loads(request.POST.get("payload", "{}"))

    info = payload.get('repository', {})

    user = info.get('owner', {})
    repo = info.get('name', None)

    if isinstance(user, dict):
        user = user.get('name', None)

    return info, user, repo
