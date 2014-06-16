import re

import autofixture
from django.core.urlresolvers import reverse
from django.core import mail
from django_webtest import WebTest

from website.accounts.models import User, Experience, ReservedEmail
from website.faq.models import Question
from website.local_map.models import Map
from website.local_minds.models import LocalMind, Ethnicity, Person
from website.news.models import PositiveNews
from website.resources.models import Resource
from website.services.models import Service
from website.tasks.models import Task


class AuthViewTests(WebTest):
    def test_login_signup_url(self):
        response = self.app.get(reverse('signup'))
        response = response.follow()
        self.assertEqual(response.request.path, reverse('login'))


class SignupTests(WebTest):
    def test_email_signup_form(self):
        url = reverse('login')
        response = self.app.get(url)

        response.forms[1]['email'] = 'myemail@example.com'
        response = response.forms[1].submit('signup')
        self.assertEqual(response.status_code, 200)

        self.assertTrue(response.context['signup_form'].is_bound)
        self.assertTrue('email' in response.context['signup_form'].errors)

        local_mind = LocalMind.objects.all()[0]
        reserved_email = ReservedEmail.objects.create(
            email='myemail@example.com',
            local_mind=local_mind)

        response.forms[1]['email'] = 'myemail@example.com'
        response = response.forms[1].submit('signup')
        self.assertEqual(response.status_code, 302)

        self.assertEqual(len(mail.outbox), 1)
        email = mail.outbox[0]
        self.assertTrue(email.subject)

    def test_signup_steps(self):
        white = Ethnicity.objects.get(name='White')

        local_mind = LocalMind.objects.all()[0]
        local_mind.ceo_two = Person.objects.create(name='CEO Name')
        local_mind.save()

        original_local_mind = local_mind

        reserved_email = ReservedEmail.objects.create(
            email='myemail@example.com',
            local_mind=local_mind)

        url = reserved_email.get_signup_url()

        response = self.app.get(url)
        response = response.follow()
        self.assertEqual(response.status_code, 200)

        self.assertTrue(re.match('^/signup/[^/]+/local-mind/$', response.request.path))

        # First step. Local Mind.

        # Check prefilled local mind name
        self.assertEqual(response.form['local-mind-name'].value, local_mind.name)

        response.form['local-mind-name'] = 'My Local Mind'
        response.form['local-mind-hours'] = '11 am to 5pm'

        response = response.form.submit()
        self.assertTrue(response.context['form'].errors['accept_tos'])

        response.form['local-mind-accept_tos'] = True
        response = response.form.submit()

        self.assertEqual(response.status_code, 302)
        response = response.follow()

        # Second step. Profile.

        response = response.form.submit()
        self.assertTrue(response.context['form'].errors['password1'])
        self.assertTrue(response.context['form'].errors['password2'])

        response.form['profile-password1'] = 'TestPassword'
        response.form['profile-password2'] = 'NonEqual'

        response.form['profile-formset-experiences-0-experience'] = 'First experience'
        response.form['profile-formset-experiences-1-experience'] = 'Further details blabla'

        response.form['profile-formset-tasks-1-text'] = 'Fst'
        response.form['profile-formset-tasks-2-text'] = 'Snd'

        response = response.form.submit()

        # Error: Passwords are not equal.
        self.assertFalse('password1' in response.context['form'].errors)
        self.assertTrue('password2' in response.context['form'].errors)

        # First/Last name are required.
        self.assertTrue('first_name' in response.context['form'].errors)
        self.assertTrue('last_name' in response.context['form'].errors)

        response.form['profile-first_name'] = 'Maxwell'
        response.form['profile-last_name'] = 'McCog'

        response.form['profile-password1'] = 'TestPassword'
        response.form['profile-password2'] = 'TestPassword'


        response = response.form.submit()
        response = response.follow()

        # Third step. Members.

        response.form['members-form-ceo_one-name'] = 'A big man'
        self.assertEqual(response.form['members-form-ceo_two-name'].value, 'CEO Name')

        # Services are temporarily disabled.

#        response.form['members-formset-services-0-name'] = 'Service information'
#        response.form['members-formset-services-0-type'] = 'type'
#        response.form['members-formset-services-0-users_count'] = 10

        self.assertRaises(AssertionError, lambda: response.form['members-formset-services-0-name'])

        response.form['members-formset-faqs-0-question'] = 'Foo Question'
        response.form['members-formset-faqs-0-notifications'] = True

        response.form['members-formset-faqs-1-question'] = 'Bar Question'
        response.form['members-formset-faqs-1-privacy'] = 'private'
        response.form['members-formset-faqs-1-notifications'] = False

        response = response.form.submit()
        response = response.follow()

        # Fourth step.

        response.form['partners-formset-resources-2-name'] = 'My Resource'
        response.form['partners-formset-resources-2-privacy'] = 'local'

        response.form['partners-formset-key_partners-0-name'] = 'An excellent partner'

        response.form['partners-formset-positive_news-0-title'] = 'Good News: We had success'
        response.form['partners-formset-positive_news-0-tags'] = 'positive, news'

        response = response.form.submit()
        response = response.follow()

        # Fifth step.

        response.form['invites-formset-invites-0-first_name'] = 'John'
        response.form['invites-formset-invites-0-last_name'] = 'Doe'
        response.form['invites-formset-invites-0-email'] = 'john.doe@example.com'
        response.form['invites-formset-invites-0-privileges'] = 'admin'

        response = response.form.submit()
        response = response.follow()

        # We are done.Here we check if everything was saved
        # correctly and that we are redirected to the dashboard.

        self.assertEqual(response.status_code, 302)

        response = response.follow()
        self.assertEqual(response.request.path, reverse('dashboard'))

        local_mind = LocalMind.objects.get(name='My Local Mind')

        self.assertEqual(local_mind.pk, original_local_mind.pk)

        self.assertEqual(local_mind.hours, '11 am to 5pm')

        self.assertNotEqual(local_mind.ceo_one, None)
        self.assertEqual(local_mind.ceo_one.name, 'A big man')

        self.assertNotEqual(local_mind.ceo_two, None)
        self.assertEqual(local_mind.ceo_two.name, 'CEO Name')

        self.assertEqual(local_mind.chair, None)

        # TODO: Test more local mind fields.

        user = User.objects.get(email=reserved_email.email)
        self.assertEqual(user.privileges, 'superuser')
        self.assertEqual(user.local_mind, local_mind)
        self.assertEqual(user.first_name, 'Maxwell')
        self.assertEqual(user.last_name, 'McCog')
        self.assertTrue(user.check_password('TestPassword'))

        # TODO: Test more user fields.

        experiences = Experience.objects.all()
        self.assertEqual(len(experiences), 2)
        ex1, ex2 = experiences

        self.assertEqual(ex1.experience, 'First experience')
        self.assertEqual(ex1.user, user)
        self.assertEqual(ex2.experience, 'Further details blabla')
        self.assertEqual(ex2.user, user)

        tasks = Task.objects.order_by('created')
        self.assertEqual(len(tasks), 2)
        task1, task2 = tasks
        self.assertEqual(task1.text, 'Fst')
        self.assertEqual(task1.slug, 'fst')
        self.assertEqual(task1.local_mind, local_mind)
        self.assertEqual(task1.assigned_to, user)
        self.assertEqual(task1.created_by, user)
        self.assertEqual(task1.due_date, None)
        self.assertEqual(task1.done, False)
        self.assertEqual(task1.done_date, None)
        self.assertEqual(task1.is_priority, False)

        self.assertEqual(task2.text, 'Snd')
        self.assertEqual(task2.slug, 'snd')
        self.assertEqual(task2.local_mind, local_mind)
        self.assertEqual(task2.assigned_to, user)
        self.assertEqual(task2.created_by, user)
        self.assertEqual(task2.due_date, None)
        self.assertEqual(task2.done, False)
        self.assertEqual(task2.done_date, None)
        self.assertEqual(task2.is_priority, False)

        services = Service.objects.all()
#        self.assertEqual(len(services), 1)
        self.assertEqual(len(services), 0)

#        service = services[0]
#        self.assertEqual(service.local_mind, local_mind)
#        self.assertEqual(service.slug, 'service-information')
#        self.assertEqual(service.name, 'Service information')
#        self.assertEqual(service.type, 'type')
#        self.assertEqual(service.users_count, 10)

        questions = Question.objects.all()
        self.assertEqual(len(questions), 2)

        q1, q2 = questions
        self.assertEqual(q1.local_mind, local_mind)
        self.assertEqual(q1.question, 'Foo Question')
        # This was set by default.
        self.assertEqual(q1.privacy, 'national')
        self.assertEqual(q1.notifications, True)
        self.assertEqual(q2.local_mind, local_mind)
        self.assertEqual(q2.question, 'Bar Question')
        self.assertEqual(q2.privacy, 'private')
        self.assertEqual(q2.notifications, False)

        resources = Resource.objects.all()
        self.assertEqual(len(resources), 1)

        resource = resources[0]
        self.assertEqual(resource.local_mind, local_mind)
        self.assertEqual(resource.slug, 'my-resource')
        self.assertEqual(resource.name, 'My Resource')
        self.assertEqual(resource.privacy, 'local')

        maps = Map.objects.all()
        self.assertEqual(len(maps), 1)

        partner = maps[0]
        self.assertEqual(partner.local_mind, local_mind)
        self.assertEqual(partner.name, 'An excellent partner')

        news = PositiveNews.objects.all()
        self.assertEqual(len(news), 1)

        news = news[0]
        self.assertEqual(news.local_mind, local_mind)
        self.assertEqual(news.user, user)
        self.assertEqual(news.title, 'Good News: We had success')
        self.assertEqual(news.date, None)
        self.assertEqual(len(news.tags.all()), 2)
        self.assertEqual([tag.name for tag in news.tags.order_by('name')], ['news', 'positive'])
        self.assertEqual(news.privacy, 'national')
        self.assertEqual(news.description, '')
        self.assertEqual(news.source, '')

        invites = User.objects.exclude(pk=user.pk)
        self.assertEqual(len(invites), 1)

        john = invites[0]
        self.assertEqual(john.first_name, 'John')
        self.assertEqual(john.last_name, 'Doe')
        self.assertEqual(john.email, 'john.doe@example.com')
        self.assertEqual(john.privileges, 'admin')
        self.assertEqual(john.local_mind, local_mind)
        self.assertEqual(john.date_joined, None)

        # An invitation email was sent.
        self.assertEqual(len(mail.outbox), 1)
        email = mail.outbox[0]
        self.assertEqual(email.to, [john.email])
        self.assertTrue(email.subject)

    def test_profile_signup(self):
        local_mind = autofixture.create_one(LocalMind)
        user = User.objects.create(
            local_mind=local_mind,
            email='foo@example.com',
            date_joined=None)

        url = user.get_signup_url()

        response = self.app.get(url)

        self.assertEqual(response.status_code, 200)

        response.form['password1'] = 'TestPassword'
        response.form['password2'] = 'NonEqual'

        response = response.form.submit()

        self.assertFalse('password1' in response.context['form'].errors)
        self.assertTrue('password2' in response.context['form'].errors)
        self.assertTrue('first_name' in response.context['form'].errors)
        self.assertTrue('last_name' in response.context['form'].errors)

        response.form['first_name'] = 'Foo'
        response.form['last_name'] = 'Bar'

        response.form['password1'] = 'TestPassword'
        response.form['password2'] = 'TestPassword'

        response = response.form.submit()

        # We are done.

        response = response.follow()
        self.assertEqual(response.request.path, reverse('dashboard'))

        user = User.objects.get(pk=user.pk)

        self.assertEqual(user.first_name, 'Foo')
        self.assertEqual(user.last_name, 'Bar')
        self.assertTrue(user.check_password('TestPassword'))
        self.assertTrue(user.date_joined is not None)

    def test_local_mind_with_existing_user(self):
        local_mind = LocalMind.objects.all()[0]
        reserved_email = ReservedEmail.objects.create(
            email='myemail@example.com',
            local_mind=local_mind)

        user = User.objects.create(
            email='myemail@example.com',
            local_mind=local_mind)

        url = reserved_email.get_signup_url()

        response = self.app.get(url, status=400)

        # We won't get redirected. We get the message that we hit an invalid
        # link.
        self.assertEqual(response.status_code, 400)

        # We should not be redirected to the signup process.
        self.assertFalse(re.match('^/signup/[^/]+/.+/$', response.request.path))
