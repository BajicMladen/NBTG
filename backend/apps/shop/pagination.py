from rest_framework.pagination import CursorPagination, PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = "page_size"
    max_page_size = 40


class CursorSetPagination(CursorPagination):
    page_size = 1
    page_size_query_param = "page_size"
    ordering = "-created_at"
