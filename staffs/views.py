from django.shortcuts import render, redirect
from.forms import SendDocumentForm
from .models import Document

def landing_page(request):
    return render(request, 'landing_page.html')

def send_or_receive_view(request):
    return render(request, 'send_or_receive.html')

def send_document(request):
    form = SendDocumentForm()
    context = {
        "form": form,
    }
    if request.method == 'GET':
        print("GETTTTTTTT")
        if request.user.is_authenticated:
            return render(request, "./staffs/send.html", context)
        else:
            return redirect(f"/login/?next={request.path}")
    else:
        print("POSTTTT")
        form = SendDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            print("VALID")
            form = form.save(commit=False)
            form.sender=request.user.userprofile
            form.is_sent = True
            form.is_received = False
            form.save()
            return redirect("/select_send_or_receive")
        else:
            print("INVALID")
            return render(request, "./staffs/send.html", {"form":SendDocumentForm(request.POST)})

def receive_document(request):
   

    if request.user.is_authenticated:
        documents = Document.objects.filter(recipient=request.user)
        context = {
            "documents":documents,
        }


        for document in documents:
            document.is_received = True
            document.save()
        return render(request, "./staffs/receive.html", context)
    else:
        return redirect(f"/login/?next={request.path}")
        
    
def dashboard(request):
    if request.user.is_authenticated:
        sender_documents = Document.objects.filter(sender=request.user.userprofile)
        print("SENDER:", sender_documents)
        recipient_documents = Document.objects.filter(recipient=request.user)
        context = {
            "sender_documents":sender_documents,
            "recipient_documents":recipient_documents,
        }
        return render(request, "./staffs/dashboard.html", context)
    else:
        return redirect(f"/login/?next={request.path}")



