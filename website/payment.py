from django.contrib import messages
from django.shortcuts import redirect
from instamojo_wrapper import Instamojo
from skill_india.settings import PAYMENT_API_AUTH_TOKEN, PAYMENT_API_KEY
from website.models import Application, Job, PaymentMethod

api = Instamojo(api_key=PAYMENT_API_KEY, auth_token=PAYMENT_API_AUTH_TOKEN, endpoint='https://test.instamojo.com/api/1.1/')


def payment_method(request, job_id):
    user = request.user.email
    job = Job.objects.get(id=job_id)

    application = Application.objects.get(job=job, user=request.user)
    payment = PaymentMethod.objects.create(application=application, user=request.user)
# Create a new Payment Request
    response = api.payment_request_create(
    amount = job.amount,
    purpose = job.job_name,
    send_email = True,
    email = request.user.email,
    redirect_url = "http://localhost:8000/payment_status/" + str(payment.id) + "/" + str(application.id)
    )
    payment_id = response['payment_request']['id']
    payment.payment_id = payment_id
    payment.save()
    # print the long URL of the payment request.
    return redirect(response['payment_request']['longurl'])
    # print the unique ID(or payment request ID)
    

def payment_status(request, pid, aid):
    payment = PaymentMethod.objects.get(id=pid)
    application = Application.objects.get(id=aid)
    response = api.payment_request_status(payment.payment_id)
    status = response['payment_request']['status']
    print(status)
    if status == 'Completed':
        payment.payment_status = status
        application.payment_status1 = status
        payment.save()
        application.save()
        messages.success(request, 'your payment is successfully completed.')
    return redirect('candidate')
    