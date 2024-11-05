from django.urls import path
from rest_framework.routers import SimpleRouter

from lms.apps import LmsConfig
from lms.views import CourseViewSet, LessonCreateApiView, LessonListApiView, LessonRetrieveApiView, LessonUpdateApiView, LessonDestroyApiView, SubscriptionCreateAPIView

app_name = LmsConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [
    path("lesson/", LessonListApiView.as_view(), name="lesson_list"),
    path("lesson/detail/<int:pk>/", LessonRetrieveApiView.as_view(), name="lesson_detail"),
    path("lesson/create/", LessonCreateApiView.as_view(), name="lesson_create"),
    path("lesson/update/<int:pk>/", LessonUpdateApiView.as_view(), name="lesson_update"),
    path("lesson/delete/<int:pk>/", LessonDestroyApiView.as_view(), name="lesson_delete"),

    path("course_subscription/", SubscriptionCreateAPIView.as_view(), name="course_subscription"),
]

urlpatterns += router.urls
