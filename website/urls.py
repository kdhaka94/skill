from os import name
from django.urls import path
from .views import home, register
from . import views
from .payment import payment_method, payment_status


urlpatterns = [
    path('', views.home, name='home'),
    path('edit_register/<str:pid>/', views.register, name='edit_register'),
    path('register/', views.register, name='register'),
    path('notice/', views.notice, name='notice'),
    path('AdmitCard/', views.admit_card, name='admit'),
    path('AnswerKey/', views.answer_key, name='answer'),
    path('Apply/', views.apply, name='apply'),
    path('Result/', views.results, name='result'),
    path('Feedback/', views.feedback, name='feedback'),
    path('login-user/', views.login_user, name='login_user'),
    path('addition-details/', views.additionDetails, name='addition_details'),
    path('edit_additional/<int:pid>/', views.additionDetails, name='edit_additional'),
    path('agreecondition/', views.AgreeCondition, name='agreecondition'),
    path('change-password/', views.Change_Password, name='change_password'),
    path('match_otp/', views.match_otp, name='match_otp'),
    path('logout/', views.Logout, name='logout'),
    path('ApplicationForm/<int:job_id>/', views.application_form, name='application_form'),
    path('ApplicationFormEdit/<int:job_id>/<int:pid>/', views.application_form, name='application_form_edit'),
    path('AdminPanel/', views.admin_portal),


    path('get-district/', views.get_district),
    path('AdminPanel/', views.admin_portal, name='dashboard'),
    path('UserPortal/', views.user_portal, name='user_portal'),
    path('Notifications/', views.notification_portal, name='notifications'),
    path('get-education/', views.get_board),
    path('candidate-profile/', views.candidate_profile, name='candidate'),
    path('candidate-marks/', views.candidate_marks, name='candidate-marks'),
    path('candidate-history/', views.candidate_history, name='candidate-history'),
    path('application-view/', views.application_view, name='application-view'),
    path('issue-admit-card/<int:aid>/', views.issue_admit_card, name='issue-admit-card'),
    path('view-admit-card/<int:pid>/', views.view_admit_card, name='view_admit_card'),
    path('forget-password/', views.forgetpassword, name='forget_password'),

    path('payment_method/<int:job_id>', payment_method, name='payment_method'),
    path('payment_request/<int:job_id>', views.payment_request, name='payment_request'),
    path('payment_status/<int:pid>/<int:aid>', payment_status, name='payment_status'),
    path('available_application/', views.available_application, name='available_application'),

    path('privacy/', views.web_privacy, name='privacy'),
    path('terms&policy/', views.web_terms, name='terms&policy'),
    path('about-us/', views.about_us, name='about-us'),
    path('contact-us/', views.contact_us, name='contact-us'),
    path('refund-policy/', views.refund_policy, name='refund-policy'),


]