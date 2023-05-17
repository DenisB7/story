def header(request):
    path = request.path.split("/")[-1]
    if not path:
        path = "main"
    return {f"{path}_active": "active"}
