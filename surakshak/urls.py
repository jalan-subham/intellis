from django.urls import path, include
from .views import (
    homepage,
    stream_page,
    video_feed,
    notify_page,
    logs_page,
    settings,
    toggle_status,
    notify_api,
    timings_page,
    heartbeat,
    resolve
    respondents_page,
    add_respondent
)

urlpatterns = [
    path("", homepage, name="homepage"),
    path("streams/", stream_page, name="stream_page"),
    path("notify/", notify_page, name="notify_page"),
    path("logs/", logs_page, name="logs_page"),
    path("settings/", settings, name="settings"),
    path("video_feed/<str:camera_name>/", video_feed, name="video_feed"),
    path("toggle-status/", toggle_status, name="toggle_status"),
    path("__reload__/", include("django_browser_reload.urls")),
    path("notify_api/", notify_api, name="notify_api"),
<<<<<<< HEAD
    path("settings/timings", timings_page, name="timings"),
    path("heartbeat", heartbeat, name="heartbeat"),
    path("resolve/<str:incident_id>", resolve, name="resolve")
=======
    path("settings/respondents/", respondents_page, name="respondents_page"),
    path("settings/add_respondent/", add_respondent, name="add_respondent"),
>>>>>>> dd43d1c144239e6c3fe9b98e46c9d4c894b0a0e3
]
