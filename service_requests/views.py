

from django.shortcuts import render, redirect

from .forms import ServiceRequestForm
from .models import ServiceRequest
from django.contrib.auth.decorators import login_required  # To ensure only logged-in users can submit

@login_required  # Requires user to be logged in to submit a request
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)  # Create object but don't save yet
            service_request.user = request.user       # Assign the current user
            service_request.save()                    # Save the object with the user
            return redirect('track_request')          # Redirect after saving
    else:
        form = ServiceRequestForm()

    return render(request, 'service_requests/submit_request.html', {'form': form})


# def submit_request(request):
#     if request.method == 'POST':
#         form = ServiceRequestForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             print("Form saved successfully.")  # Debugging output
#             return redirect('track_request')
#         else:
#             print("Form errors:", form.errors)  # Log form errors for debugging
#     else:
#         form = ServiceRequestForm()
#
#     return render(request, 'service_requests/submit_request.html', {'form': form})




from django.shortcuts import render
from .models import ServiceRequest  # Import the model


def track_request(request):
    # Fetch all service requests from the database
    requests = ServiceRequest.objects.all().order_by('-created_at')  # Orders by creation date (optional)

    return render(request, 'service_requests/track_request.html', {'requests': requests})

