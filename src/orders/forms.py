from django import forms
from . import models



class CreateOrderGoodsForm(forms.ModelForm):
    
    class Meta:
        model = models.OrderGoods
        fields = ['tel',
                  'address',
                  ]
                  
        
