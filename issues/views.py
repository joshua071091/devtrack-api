import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Reporter, Issue, CriticalIssue, LowPriorityIssue

def read_json(file):
    with open(file, 'r') as f:
        return json.load(f)

def write_json(file, data):
    with open(file, 'w') as f:
        json.dump(data, f, indent=2)

@csrf_exempt
def reporters(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            reporter = Reporter(
                data['id'],
                data['name'],
                data['email'],
                data['team']
            )
            reporter.validate()

            reporters = read_json('reporters.json')
            reporters.append(reporter.to_dict())
            write_json('reporters.json', reporters)

            return JsonResponse(reporter.to_dict(), status=201)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    elif request.method == 'GET':
        reporters = read_json('reporters.json')
        reporter_id = request.GET.get('id')

        if reporter_id:
            reporter_id = int(reporter_id)
            for r in reporters:
                if r['id'] == reporter_id:
                    return JsonResponse(r, status=200)
            return JsonResponse({'error': 'Reporter not found'}, status=404)

        return JsonResponse(reporters, safe=False)

@csrf_exempt
def issues(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            # Subclass selection
            if data['priority'] == 'critical':
                issue = CriticalIssue(**data)
            elif data['priority'] == 'low':
                issue = LowPriorityIssue(**data)
            else:
                issue = Issue(**data)

            issue.validate()

            issues = read_json('issues.json')
            issues.append(issue.to_dict())
            write_json('issues.json', issues)

            response = issue.to_dict()
            response['message'] = issue.describe()

            return JsonResponse(response, status=201)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    elif request.method == 'GET':
        issues = read_json('issues.json')

        issue_id = request.GET.get('id')
        status = request.GET.get('status')

        if issue_id:
            issue_id = int(issue_id)
            for i in issues:
                if i['id'] == issue_id:
                    return JsonResponse(i, status=200)
            return JsonResponse({'error': 'Issue not found'}, status=404)

        if status:
            filtered = [i for i in issues if i['status'] == status]
            return JsonResponse(filtered, safe=False)

        return JsonResponse(issues, safe=False)