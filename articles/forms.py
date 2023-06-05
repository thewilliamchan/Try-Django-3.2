from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
   class Meta:
      model = Article
      fields = ['title', 'content']

   def clean(self):
        cleaned_data = self.cleaned_data
        print("cleaned all", cleaned_data)
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")
        qs = Article.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error("title", f"{title} was already in use")
        return cleaned_data

class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    # def clean_title(self):
    #     cleaned_data = self.cleaned_data
    #     print("cleaned data", cleaned_data)
    #     title = cleaned_data.get('title')
    #     return title
    
    def clean(self):
        cleaned_data = self.cleaned_data
        print("cleaned all", cleaned_data)
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")
        qs = Article.objects.filter(title__icontains="On Call")
        if qs.exists():
            self.add_error("title", f"{title} was already in use")
      #   if title.lower().strip() == "the office":
      #     self.add_error("title", "This title is taken")
      #     # raise forms.ValidationError("This title is taken")
      #   if "office" in content:
      #      self.add_error("content", "Office cannot have content")
      #      raise forms.ValidationError("Office is not allowed")
        return cleaned_data