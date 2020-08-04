from django.db import models

# Create your models here.


class Order(models.Model):
    fcuser = models.ForeignKey(
        'fcuser.Fcuser', on_delete=models.CASCADE, verbose_name="사용자")
    # ForeignKey로 fcuser의 Fcuser클래스를 가져오고 사용자가 삭제됐을때 order를 어떻게 관리할건지 on_delete로 설정 models.CASCADE : 같이삭제
    product = models.ForeignKey(
        'product.Product', on_delete=models.CASCADE, verbose_name="상품")
    product = models.IntegerField(verbose_name="수량")
    register_date = models.DateTimeField(
        auto_now_add=True, verbose_name='등록날짜')

    class Meta:  # admin 페이지 관리의 유용성 향상
        db_table = 'fastcampus_order'
        verbose_name = '주문'
        verbose_name_plural = '주문'
