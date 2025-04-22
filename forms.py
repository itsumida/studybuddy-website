from django import forms
from .models import Profile, Course

class ProfileAddForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["fname", "lname", "email", "bio", "availability", "courses", "study_methods"]
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Tell us about yourself and your study preferences...'}),
            'availability': forms.TextInput(attrs={'placeholder': 'e.g., Weekdays 6-8 PM'}),
            'study_methods': forms.TextInput(attrs={'placeholder': 'e.g., Group study, Flashcards'}),
        }

    courses = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

class CourseAddForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["code", "name", "description"]

    