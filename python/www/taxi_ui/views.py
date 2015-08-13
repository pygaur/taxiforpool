import datetime
import time
import json

from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, ListView, DetailView, FormView

from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db.models import Q


from taxi_communicate.models import EmailTrigger, Newsletter
from taxi_trip.models import Trip, TripLikeLogs
from .forms import TripForm, CustomerSignupForm, CustomerSigninForm,\
    ForgotPasswordForm
from taxi_communicate.email_notification import SendEmail
from taxi_customer.models import Customer
from .utils import randomword, enc_password, get_hexdigest


def triplist_filter(request, fieldname):
    if request.is_ajax():
        message = ["ActionScript", "AppleScript", "Asp", "BASIC", "C", "C++",
                   "Clojure", "COBOL", "ColdFusion", "Erlang", "Fortran",
                   "Groovy", "Haskell", "Java", "JavaScript", "Lisp",
                   "Perl", "PHP", "Python", "Ruby", "Scala", "Scheme"]
        data = json.dumps(message)
        return HttpResponse(data, mimetype='application/json')


class AfterSignup(TemplateView):
    pass


class SubmitTrip(TemplateView):
    """"""
    pass


def logout(request):
    """"""
    try:
        del request.session['customer_id']
    except KeyError:
        return HttpResponseRedirect(reverse('home',))
    return HttpResponseRedirect(reverse('home',))


class ProfileView(TemplateView):
    """"""
    model = Customer   
    
    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('customer_id'):
            return reverse("home", kwargs={}) 
            
        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        return handler(request, *args, **kwargs)
       
 
class ForgotPasswordView(FormView):
    """
    """
    form_class = ForgotPasswordForm
    template_name = "forgot_password.html"

#    def get_success_url(self):
#        return reverse("account", kwargs={})

    def get_context_data(self, **kwargs):
        context = super(ForgotPasswordView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        try:
            obj = Customer.objects.\
                get(Q(email=self.request.POST.get('user_name'))
                    | Q(mobile=self.request.POST.get('user_name'))
                    | Q(user_name=self.request.POST.get('user_name')))
        except:
            form.non_field_errors = "Please provide valid account details."
            return self.render_to_response(self.get_context_data(form=form))
        return super(Signin, self).form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

class Signup(CreateView):
    """
    view to handle customer signup
    either mobile or Email id is needed
    Password and other Details will be emailed
    """
    form_class = CustomerSignupForm
    template_name = "signup.html"

    def get_success_url(self):
        return reverse("aftersignup", kwargs={})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        existed_object_with_email = self.object._default_manager.\
            filter(email=self.request.POST.get('email')).exclude(email="\
            ").count()
        if existed_object_with_email > 0:
            form.non_field_errors = "Email-ID is already registered."
            return self.render_to_response(self.get_context_data(form=form))
        existed_object_with_mobile = self.object._default_manager.\
            filter(mobile=self.request.POST.get('mobile')).exclude(mobile="").count()
        if existed_object_with_mobile > 0:
            form.non_field_errors = "Mobile Number is already registered."
            return self.render_to_response(self.get_context_data(form=form))
        self.object.account_creation_ip = \
             self.request.META.get('REMOTE_ADDR')
        self.object.level_id = 1         
        password = randomword(4)
        encpassword = enc_password(password)
        self.object.password = encpassword
        self.object.user_name = self.object.email
#        if self.request.POST.get('email'):
#            emailobj = SendEmail(model=EmailTrigger, trigger_name="Signup_Successful")
#            emailobj.signup_success(entry=self.object, password=password)
        if self.request.POST.get('mobile'):
            print "Welcome %s, Your password is %s" % (self.object.mobile, password)
        self.object.save()
        return super(Signup, self).form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class Signin(FormView):
    """
    """
    form_class = CustomerSigninForm
    template_name = "signin.html"

    def get_success_url(self):
        return reverse("profile", kwargs={})

    def get_context_data(self, **kwargs):
        context = super(Signin, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        try:
            obj = Customer.objects.\
                get(Q(email=self.request.POST.get('user_name'))\
                | Q(mobile=self.request.POST.get('user_name'))\
                | Q(user_name=self.request.POST.get('user_name')))
        except:
            form.non_field_errors = "Please provide valid account details."
            return self.render_to_response(self.get_context_data(form=form))
        password = self.request.POST.get('password')
        dbpassword = obj.password
        a = dbpassword.split('$')
        hashdb = str(a[2])
        salt = str(a[1])
        usrhash = get_hexdigest(a[0], a[1], password)
        if hashdb != usrhash:
            form.non_field_errors = "Password you entered is wrong."
            return self.render_to_response(self.get_context_data(form=form))
        self.request.session['customer_id'] = str(obj.id)
#        self.get('response').set_cookie('customer_session' , )
        return super(Signin, self).form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

class Home(CreateView):
    template_name = "home.html"
    form_class = TripForm 
 
    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse("success", kwargs={'token': self.object.tokens})

    def form_valid(self, form):
        """ execute if form is valid with valid form data """
        self.object = form.save(commit=False)
        self.object.tokens =  datetime.datetime.fromtimestamp(time.time()).strftime("%y%m%d%H%M%S")
        self.object.ip = self.request.META.get('REMOTE_ADDR')
        try:
            customer_id = self.request.session.get('customer_id')
        except KeyError:
            customer_id = None
        self.object.customer_id = customer_id
        self.object.save()
        emailobj = SendEmail(model=EmailTrigger, trigger_name="Trip_Submitted")
        emailobj.trip_submit(entry=self.object)
        return super(Home, self).form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

class TripLists(ListView):
    """

    list all available trips

    """
    template_name = 'triplist.html'
    queryset = Trip.objects.all()
    http_method_names= [u'get']


class TripDetail(DetailView):
    """"""
    model = Trip
    template_name = "tripdetails.html"

    def get_context_data(self, **kwargs):
        """"""
        context = super(TripDetail, self).get_context_data(**kwargs)
        context['interest_entries_count'] = self.object.interest.count()
        return context




def newsletter(request):
    """"""
    result = {}

    if request.is_ajax():
        email = request.POST.get('email')
        name = request.POST.get('name')
        Newsletter.objects.create(email=email, name=name)
        result['message'] = "Thanks we will get back to you."
        data = json.dumps(result)
        return HttpResponse(data, mimetype='application/json')


def submit_like(request, trip_id):
    """"""
    data = {}
    if request.is_ajax():
        customer_id = request.session.get('customer_id', None)
        TripLikeLogs.objects.create(trip_id=trip_id,
                                    customer_id=customer_id,
                                    like=True)
        data['message'] = "Thanks for liking trip."
        return HttpResponse(data, mimetype='application/json')


def submit_interest(request, trip_id):
    """
    """
    data = {}
    if request.is_ajax():
        customer_id = request.session.get('customer_id', None)
        if not customer_id:
            return HttpResponseRedirect(reverse('signin',))
        try:
            trip_object = Trip.objects.get(id=trip_id)
        except Exception as exc:
            # TODO need to catch here unauthorize action
            pass
        customer_object = Customer.objects.get(id=customer_id)
        emailobj = SendEmail(model=EmailTrigger, trigger_name="Trip_Interest_Submit_To")
        #emailobj.trip_interest(trip_object=trip_object, customer_object=customer_object, email=trip_object.email)
        emailobj = SendEmail(model=EmailTrigger, trigger_name="Trip_Interest_Submit_From")
        #emailobj.trip_interest(trip_object=trip_object, customer_object=customer_object, email=customer_object.email)
        trip_object, is_exist = trip_object.add_relationship(customer_object)
        if is_exist is False:
            data['message'] = "Already submitted."
        else:
            data['message'] = "We have sent a request to respective person .Please check ur email for reciept."
        data = json.dumps(data)
        return HttpResponse(data, mimetype='application/json')
