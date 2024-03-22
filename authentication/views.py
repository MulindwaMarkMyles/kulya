from django.shortcuts import render
from shop.views import *
from shop.urls import *
from shop.templates import *

# Create your views here
def profile(request):
    context={
        'title':'Uer Profile',
        'name':'USER NAME',
        'email':'USER EMAIL',
        'phone_number':'PHONE NUMBER'
         }

    return render(request, "shop/profile.html",context)  

def login(request):

    return render(request, "shop/login.html")

def signup(request):
    
    return render(request, "shop/signup.html")    


def index (request):
    orders = Order.objects.filter(user=request.user).order_by('-date') 
    context = {
               'orders':orders,
              }
    return render (request,"shop/index.html",context) 

def UserCreationFrom(request):
    """
    A Form that creates a UserProfile along with a regular User.
    """
    class Meta(UserCreationForm.Meta):
        model = User
        

def manage_users(request):
    users = User.objects.all().order_by('last_name','first_name')
    ctx = {"users": users}
    return render(request, "admin/  manage_users.html",ctx)

# @staff_member_required

def add_user(request):
    if request.method == 'POST':
        form = UserAdditionForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Signal that a new user has been created. Passing the `raw` parameter set to True means
            # that we want to skip sending the signal until the very end of this function, when we know for sure
            # that we get the original dictionary passed to our forms ``clean`` methods rather than a
            # ``forms.models.ModelChoiceField`` instance.
            signals.user_created.send(sender=user.__class__, instance=user, raw=True, request=request)
            msg = _('Successfully added user %s.') % user
            messages.info(request, msg)
            return redirect('manage_users')
        else:
            msg = _('The following errors occurred')
            for k,v in form['password1'].errors.items():
                msg += ": %s" % v
            messages.error(request,msg)
    else:
        form = UserAdditionForm()
    ctx = {'form': form}
    template = 'dashboard/modal_content.html'
    return TemplateResponse(request,template,   ctx)




       

# Create your views here.
