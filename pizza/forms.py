from django import forms
from .models import Pizza, Size

# class PizzaForm(forms.Form):
#     topping1 = forms.CharField(label='topping1', max_length=100, widget=forms.Textarea)
#     topping2 = forms.CharField(label='topping2', max_length=100, widget=forms.PasswordInput)
#     size = forms.ChoiceField(label='size', choices=[('small','small'),('medium','medium'),('large','large')])

# class PizzaForm(forms.Form):
#     toppings = forms.MultipleChoiceField(choices=[('pep','Peperoni'),('cheese','Cheese')], widget=forms.CheckboxSelectMultiple())
#     size = forms.ChoiceField(label='size')

class PizzaForm(forms.ModelForm):

    size = forms.ModelChoiceField(queryset=Size.objects, empty_label=None, widget=forms.RadioSelect)

    class Meta:
        model = Pizza
        fields = ['topping1','topping2','size']
        labels = {'topping1':'Topping 1', 'topping2':'Topping 2', 'size': 'Size'}
        
