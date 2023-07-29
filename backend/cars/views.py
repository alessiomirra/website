from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, HttpResponseRedirect 
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.contrib.auth.mixins import LoginRequiredMixin

from cars.models import Car, CompanyInfo
from cars.forms import NewCarForm, InfoesUpdate

#### 

class Homepage(LoginRequiredMixin,ListView):
    template_name = 'cms/homepage.html'
    paginate_by = 6

    def get_queryset(self):
        return Car.objects.all().order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["car_number"] = Car.objects.all().count()
        return context 

class Showcase(LoginRequiredMixin, ListView):
    template_name = 'cms/showcase.html'

    def get_queryset(self):
        return Car.objects.filter(showcase = True)

class NewCar(LoginRequiredMixin, CreateView):
    template_name = 'cms/new_car.html'
    model = Car 
    form_class = NewCarForm
    success_url = reverse_lazy('homepage')
    
    def form_valid(self, form):
        if form.cleaned_data["showcase"]:
            showcase_items = Car.objects.filter(showcase = True).count()
            if showcase_items == 6:
                form.add_error('showcase', 'You have 6 cars in the showcase section. Delete a car and then add this car')
                return self.form_invalid(form)
        
        if not form.cleaned_data['make']:
            form.add_error('make', "Make field can't be empty")
            return self.form_invalid(form)
        if not form.cleaned_data['model']:
            form.add_error('model', "Model field can't be empty")
            return self.form_invalid(form)
        if not form.cleaned_data['slug']:
            form.add_error('slug', "Slug field can't be empty")
            return self.form_invalid(form)
        if not form.cleaned_data['price']:
            form.add_error('Price', "Price field can't be empty")
            return self.form_invalid(form)
        if not form.cleaned_data['year']:
            form.add_error('year', "Year field can't be empty")
            return self.form_invalid(form)
        if not form.cleaned_data['gear']:
            form.add_error('gear', "Gear field can't be empty")
            return self.form_invalid(form)
        if not form.cleaned_data['power']:
            form.add_error('power', "Power field can't be empty")
            return self.form_invalid(form)
        if not form.cleaned_data['fuel']:
            form.add_error('fuel', "Fuel field can't be empty")
            return self.form_invalid(form)
        if not form.cleaned_data['mileage']:
            form.add_error('mileage', "Mileage field can't be empty")
            return self.form_invalid(form)

        return super().form_valid(form)


class UpdateCarView(LoginRequiredMixin,UpdateView):
    template_name = 'cms/update_car.html'
    model = Car 
    form_class = NewCarForm
    success_url = reverse_lazy('homepage')

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        queryset = queryset or self.get_queryset()
        obj = get_object_or_404(queryset, slug=slug)
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object = self.get_object()
        if object.showcase: 
            context["inShowcase"] = True 
        else: 
            context["inShowcase"] = False 
        return context

    def form_valid(self, form):
        if form.cleaned_data["showcase"]:
            showcase_items = Car.objects.filter(showcase = True).count()
            if showcase_items == 6:
                form.add_error('showcase', 'You have 6 cars in the showcase section. Delete a car and then add this car')
                return self.form_invalid(form)

        if not form.cleaned_data['make']:
            form.add_error('make', "Make field can't be empty")
            return self.form_invalid(form)
        if not form.cleaned_data['model']:
            form.add_error('model', "Model field can't be empty")
            return self.form_invalid(form)
        if not form.cleaned_data['slug']:
            form.add_error('slug', "Slug field can't be empty")
            return self.form_invalid(form)
        if not form.cleaned_data['price']:
            form.add_error('Price', "Price field can't be empty")
            return self.form_invalid(form)
        if not form.cleaned_data['year']:
            form.add_error('year', "Year field can't be empty")
            return self.form_invalid(form)
        if not form.cleaned_data['gear']:
            form.add_error('gear', "Gear field can't be empty")
            return self.form_invalid(form)
        if not form.cleaned_data['power']:
            form.add_error('power', "Power field can't be empty")
            return self.form_invalid(form)
        if not form.cleaned_data['fuel']:
            form.add_error('fuel', "Fuel field can't be empty")
            return self.form_invalid(form)
        if not form.cleaned_data['mileage']:
            form.add_error('mileage', "Mileage field can't be empty")
            return self.form_invalid(form)

        return super().form_valid(form)
    

class Remove(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug')
        car = Car.objects.get(slug=slug)
        car.showcase = False 
        car.save()
        return HttpResponseRedirect(reverse_lazy('showcase-page'))

class DeleteCarView(LoginRequiredMixin, DeleteView):
    model = Car
    success_url = reverse_lazy('homepage')
    template_name = "cms/car_confirm_delete.html"

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        queryset = queryset or self.get_queryset()
        obj = get_object_or_404(queryset, slug=slug)
        return obj


class InfoesUpdateView(LoginRequiredMixin, UpdateView):
    model = CompanyInfo 
    template_name = "cms/info_update.html"
    form_class = InfoesUpdate
    success_url = reverse_lazy('company-infoes-page')

    def get_object(self, queryset=None):
        obj = get_object_or_404(CompanyInfo, pk=1)
        return obj