from rest_framework.pagination import PageNumberPagination

class MyNumberPagination(PageNumberPagination):
    page_size = 5