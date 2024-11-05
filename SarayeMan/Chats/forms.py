from django import forms

class MessageForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        for item in MessageForm.visible_fields(self):
            item.field.widget.attrs["class"] = "form-control"

    message= forms.CharField(required=True,max_length=1000,widget=forms.Textarea,label="پیام")

