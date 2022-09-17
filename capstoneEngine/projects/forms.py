from django import forms


class ProjectForm(forms.Form):
	title = forms.CharField(max_length=500,label='title', widget=forms.Textarea)
	description = forms.CharField(label='description', widget=forms.Textarea)
	in_scope = forms.CharField(label='in_scope', widget=forms.Textarea)
	out_scope = forms.CharField(label='out_scope', widget=forms.Textarea)
	skill = forms.CharField(label='skill', widget=forms.Textarea)
	team_size = forms.IntegerField(min_value=1, max_value=10, label='team_size')
	duration = forms.IntegerField(min_value=1, max_value=30, label='duration')
