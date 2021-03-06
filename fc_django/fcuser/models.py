from django.db import models

# Create your models here.


class Fcuser(models.Model):
    objects = models.Manager()  # no objects 오류 수정을 위한 추가 코드(없어도됨)
    email = models.EmailField(verbose_name='이메일')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    register_date = models.DateTimeField(
        auto_now_add=True, verbose_name='등록날짜')

    def __str__(self):
        return self.email

    class Meta:  # admin 페이지 관리의 유용성 향상
        db_table = 'fastcampus_fcuser'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'
