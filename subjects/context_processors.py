from subjects.models import SubjectResult


def subject_result_choices(request):
    return {
        "SubjectResultType": SubjectResult,
    }
