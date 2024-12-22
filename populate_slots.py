from datetime import datetime, timedelta
from django.utils.timezone import make_aware
from surf_sessions.models import Slot

# Sample data
session_types = ['Beginner Lesson', 'Beginner Session', 'Waikiki Lesson', 'Waikiki Session', 'Intermediate Lesson', 'Intermediate Session', 'Advanced Lesson', 'Advanced Session', 'Advanced Plus Session', 'Expert Turns Session', 'Expert Barrels Session']
start_date = datetime(2024, 12, 23, 9, 0)
end_date = datetime(2024, 12, 25, 17, 0)
time_interval = timedelta(hours=2)  # Every 2 hours

for session_type in session_types:
    current_time = start_date
    while current_time <= end_date:
        Slot.objects.get_or_create(
            session_type=session_type,
            date=current_time.date(),
            time=current_time.time(),
            is_available=True
        )
        current_time += time_interval