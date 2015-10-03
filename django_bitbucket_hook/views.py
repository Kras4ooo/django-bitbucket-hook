import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django_bitbucket_hook.models import Hook


@csrf_exempt
@require_http_methods(["POST"])
def only_hook(request):
    payload, user, repo = get_payload(request)

    if not user and not repo:
        return JsonResponse({'success': False, 'message': 'No JSON data or URL argument : cannot identify hook'})

    try:
        hook = Hook.objects.get(user=user, repo=repo)
        hook.execute()
    except Hook.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Not exist Hook'})
    return JsonResponse({'success': True})


@csrf_exempt
@require_http_methods(["POST"])
def hook_name(request, name):
    payload, user, repo = get_payload(request)

    if not user and not repo and not name:
        return JsonResponse({'success': False, 'message': 'No JSON data or URL argument : cannot identify hook'})

    try:
        hook = Hook.objects.get(user=user, repo=repo, name=name)
        hook.execute()
    except Hook.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Not exist Hook'})
    return JsonResponse({'success': True})


@csrf_exempt
@require_http_methods(["POST"])
def hook_name_branch(request, name, branch):
    payload, user, repo = get_payload(request)
    repo_branch = payload.get('ref', False)

    if repo_branch is False:
        repo_branch = payload.get('commits', False)
        if repo_branch is False:
            return JsonResponse({'success': False, 'message': 'Not exist branch'})
        repo_branch = repo_branch[0].get('branch', False)
    else:
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
    return JsonResponse({'success': True})


def get_payload(request):
    # Git repo information from post-receive payload
    if request.META.get('CONTENT_TYPE') == "application/json":
        payload = json.loads(request.body.decode('utf8'))
    else:
        # Probably application/x-www-form-urlencoded
        payload = json.loads(request.POST.get("payload", "{}"))

    repo_data = payload.get('repository', {})

    user = repo_data.get('owner', {})
    repo = repo_data.get('name', None)

    if isinstance(user, dict):
        user = user.get('name', None)

    return payload, user, repo
