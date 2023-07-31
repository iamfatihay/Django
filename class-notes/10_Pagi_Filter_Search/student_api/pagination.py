from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class MyNumberPagination(PageNumberPagination):
    page_size = 5  # * Maksimum gosterilecek obje sayisi her sayfa icin
    page_query_param = "sayfa"  # * URL de page yazisi yerine gosterilecek ifade
    page_size_query_param = "adet"  # * Dönen veriyi sinirlamak icin, mesela:  "/$adet=5"
    max_page_size = 3

class MyLimitPagination(LimitOffsetPagination):
    default_limit = 8
    limit_query_param = "kac_tane"
    offset_query_param = "kacinci"

class MyCursorPagination(CursorPagination):
    page_size = 10
    ordering = "first_name"    
