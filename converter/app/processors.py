from datetime import datetime

def current_year_processor(request):
    return {'current_year': datetime.now().year}
