from django.contrib import messages
from django.forms import modelformset_factory, BaseModelFormSet
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from .models import Profile, CreativeField, PortfolioLink
from .forms import ProfileForm, PortfolioLinkFormSet

# Create your views here.
class SkippingBaseFormSet(BaseModelFormSet):
    def clean(self):
        super().clean()
        for form in self.forms:
            if self.can_delete:
                delete = form.cleaned_data.get('DELETE', False)
                obj_id = form.cleaned_data.get('id')
                if delete and not obj_id:
                    form._errors = {}


class ProfileListView(ListView):
    model = Profile
    template_name = 'profiles/profile_list.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileListView, self).get_context_data(**kwargs)
        context['role'] = self.request.session['role']
        return context


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'
    slug_field = 'name'
    slug_url_kwarg = 'name'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['portfolio_links'] = self.object.portfolio_links.all()
        context['role'] = self.request.session['role']
        return context


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profiles/profile_create.html'
    success_url = reverse_lazy('profiles:profile-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = PortfolioLinkFormSet(self.request.POST)
        else:
            context['formset'] = PortfolioLinkFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.success_url)
        else:
            return self.form_invalid(form)


class ProfileDeleteView(DeleteView):
    model = Profile
    slug_field = 'name'
    slug_url_kwarg = 'name'
    success_url = reverse_lazy('profiles:profile-list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Profile deleted successfully.")
        return super().delete(request, *args, **kwargs)


class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profiles/profile_edit.html'
    context_object_name = 'profile'
    slug_field = 'name'
    slug_url_kwarg = 'name'

    def get_success_url(self):
        return reverse_lazy('profiles:profile-detail', kwargs={'name': self.object.name})

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['formset'] = PortfolioLinkFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            data['formset'] = PortfolioLinkFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']

        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        context = self.get_context_data()
        return self.render_to_response(self.get_context_data(form=form, formset=context['formset']))