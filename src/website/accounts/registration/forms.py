from django.forms.formsets import formset_factory
from django.forms.models import inlineformset_factory
from django.utils.translation import ugettext_lazy as _
from django_compositeform import CompositeModelForm, FormSetField
import floppyforms as forms

from website.accounts.models import User, Experience
from website.faq.models import Question
from website.local_map.models import Map
from website.local_minds.models import LocalMind, Ethnicity
from website.news.models import PositiveNews
from website.resources.models import Resource
from website.services.models import Service
from website.tasks.models import Task


class SignupLocalMindForm(forms.ModelForm):
    accept_tos = forms.BooleanField(label=_('Terms'), required=True,
        help_text=_(
            'We (above LM) agree to all terms and conditions of the openhub '
            'site.'))

    class Meta:
        model = LocalMind
        fields = (
            'name',
            'region',
            'address',
            'postcode',
            'income_restricted',
            'charity_no',
            'charity_type',
            'email',
            'telephone',
            'website',
            'income_unrestricted',
            'reserves',
            'deficit',
            'statement',
            'group_avatar',
        )


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ('experience',)


ExperienceFormSet = inlineformset_factory(
    parent_model=User,
    model=Experience,
    form=ExperienceForm,
    can_delete=False)


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('text',)


TaskFormSet = inlineformset_factory(
    parent_model=User,
    model=Task,
    form=TaskForm,
    fk_name='assigned_to',
    can_delete=False)


class SignupProfileForm(CompositeModelForm):
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }

    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Re-enter password'), widget=forms.PasswordInput)

    experiences = FormSetField(ExperienceFormSet)
    tasks = FormSetField(TaskFormSet)

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'job_title',
            'skills',
            'user_avatar',
            'biography',
            'telephone',
            'mobile',
            'twitter',
        )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'])
        return password2

    def save(self, commit=True):
        user = super(SignupProfileForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            self.save_m2m()
        return user


class SelectEthnicityForm(forms.Form):
    ethnicity = forms.ModelChoiceField(
        label=_('Ethnicity'),
        queryset=Ethnicity.objects.all())


EthnicityFormSet = formset_factory(
    form=SelectEthnicityForm,
    extra=1)


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = (
            'name',
            'type',
            'users_count',
        )


ServiceFormSet = inlineformset_factory(
    parent_model=LocalMind,
    model=Service,
    form=ServiceForm,
    extra=3,
    can_delete=False)


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = (
            'question',
            'notifications',
            'privacy',
        )


QuestionFormSet = inlineformset_factory(
    parent_model=LocalMind,
    model=Question,
    form=QuestionForm,
    extra=3,
    can_delete=False)


class SignupLocalMindMembersForm(CompositeModelForm):
    trustees_ethnicities = FormSetField(EthnicityFormSet)
    volunteers_ethnicities = FormSetField(EthnicityFormSet)
    staff_ethnicities = FormSetField(EthnicityFormSet)

    services = FormSetField(ServiceFormSet)
    faqs = FormSetField(QuestionFormSet)

    class Meta:
        model = LocalMind
        fields = (
            'chairman',
            'chairman_email',
            'ceo',
            'ceo_email',
            'ceo_telephone',
            'chair_ethnicity',
            'staff_count',
            'trustees_count',
            'volunteers_count',
            'trustees_active',
        )


class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = (
            'name',
            'privacy',
        )


ResourceFormSet = inlineformset_factory(
    parent_model=LocalMind,
    model=Resource,
    form=ResourceForm,
    extra=3,
    can_delete=False)


class MapForm(forms.ModelForm):
    class Meta:
        model = Map
        fields = (
            'name',
            'email',
            'address',
            'telephone',
            'relationship',
            'postcode',
            'category',
            'website',
            'privacy',
        )


MapFormSet = inlineformset_factory(
    parent_model=LocalMind,
    model=Map,
    form=MapForm,
    extra=1,
    can_delete=False)


class PositiveNewsForm(forms.ModelForm):
    class Meta:
        model = PositiveNews
        fields = (
            'title',
            'description',
            'date',
            'tags',
        )


PositiveNewsFormSet = inlineformset_factory(
    parent_model=LocalMind,
    model=PositiveNews,
    form=PositiveNewsForm,
    extra=1,
    can_delete=False)


class SignupPartnersForm(CompositeModelForm):
    resources = FormSetField(ResourceFormSet)
    key_partners = FormSetField(MapFormSet)
    positive_news = FormSetField(PositiveNewsFormSet)

    class Meta:
        model = LocalMind
        fields = ()


class InvitationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'privileges',
            'job_title',
        )


InvitationFormSet = inlineformset_factory(
    parent_model=LocalMind,
    model=User,
    form=InvitationForm,
    extra=3,
    can_delete=False)


class SignupInviteForm(CompositeModelForm):
    invites = FormSetField(InvitationFormSet)

    class Meta:
        model = LocalMind
        fields = ()
