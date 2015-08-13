__author__ = 'pylover'
from django.conf.urls import patterns, url, include

from .views import Home, SubmitTrip, TripLists, TripDetail, newsletter, Signup, \
                   Signin, AfterSignup, ForgotPasswordView, ProfileView, logout, \
                   triplist_filter, submit_like, submit_interest, logout

urlpatterns = patterns('',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^tripsubmit/(?P<token>[\w-]+)/$', SubmitTrip.as_view(template_name='submit.html',), name='success'),
    url(r'^profile/$', ProfileView.as_view(template_name='profile.html',), name='profile'),
    url(r'^tripdetails/(?P<pk>[\d]+)/$', TripDetail.as_view(), name='tripdetail'),
    url(r'^submitinterest/(?P<trip_id>[\d]+)/$', submit_interest, name='submit-interest'),
    url(r'^triplists/$', TripLists.as_view(), name='listtrips'),
    url(r'^newsletter/$', newsletter, name='newsletter'),
    url(r'^signup/$', Signup.as_view(), name='signup'),
    url(r'^signin/$', Signin.as_view(), name='signin'),
    url(r'^aftersignup/$', AfterSignup.as_view(template_name="aftersignup.html"), name='aftersignup'),
    url(r'^forgotpassword/$', ForgotPasswordView.as_view(template_name="forgot_password.html"), name='forgot_password'),
#    url(r'^logout/$', logout, name='logout'),
    url(r'^logout/$', logout, name="customer-logout"),
    url(r'^triplistfilter/(?P<fieldname>[\w]+)/$', triplist_filter, name='trip-filter'),
    url(r'^submitlike/(?P<trip_id>[\d]+)/$', submit_like, name='submit-like'),
)

