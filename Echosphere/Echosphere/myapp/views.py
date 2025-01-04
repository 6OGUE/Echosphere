from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate
from datetime import date, datetime
from django.db.models import Q
from datetime import date as d, datetime as dt
from django.db.models import Max
from .models import Post, Register, Donation
from django.http import HttpResponse





def index(request):
    post = Post.objects.all()
    
    return render(request,'index.html',{'post':post})

    


# def register(request):
#     return render(request,'register.html')

# def login(request):
#     return render(request,'login.html')


def login(request):
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.user_type == 'admin':
                print('admin#####')
                messages.info(request, 'Welcome to admin dashboard')
                return redirect('/adminDash')
            elif user.user_type == 'User':
                request.session['uid'] = user.id
                print('user#####')
                messages.info(request, 'Welcome to ECHOSPHERE')
                return redirect('/userDash')
            elif user.user_type == 'Moderator':
                request.session['uid'] = user.id
                print('moderator#####')
                messages.info(request, 'Welcome to ECHOSPHERE')
                return redirect('/modDash')
            elif user.user_type == 'Banned':
                request.session['uid'] = user.id
                print('banned#####')
                messages.info(request, 'Welcome to ECHOSPHERE')
                return redirect('/bannedUser')
            else:
                pass
        else:
            pass
    return render(request, "login.html")


def register(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        password = request.POST['password']

        # Check if email already exists
        if Login.objects.filter(username=email).exists():
            messages.error(request, "User already exists.")
            return render(request, "register.html")

        try:
            log = Login.objects.create_user(username=email, password=password, user_type="User", view_password=password, is_active="1")
            log.save()

            reguser = Register.objects.create(name=name, address=address, email=email, password=password, phone=phone, loginid=log)
            reguser.save()

            messages.success(request, "Registered Successfully")
        except Exception as e:
            # In case of any other error, log it or send a different message
            messages.error(request, "An error occurred during registration. Please try again.")
            
    return render(request, "register.html")


def userDash(request):
    uid = request.session["uid"]  
    Uid = Register.objects.get(loginid=uid)
    
    uid = Register.objects.filter(loginid=uid)
    post = Post.objects.all()
    badge = AssignBadge.objects.all()
    return render(request,'USER/userDash.html',{'post':post,'uid':uid,"Uid":Uid,"badge":badge})

def adminDash(request):
    post = Post.objects.all()
    return render(request,'ADMIN/adminDash.html',{'post':post})

def request(request):
    data = Register.objects.all()
    print(data, "###############")
    return render(request,'ADMIN/request.html',{'data':data})

def viewUsers(request):
    data = Register.objects.all()
    badge = AssignBadge.objects.all()
    
    return render(request,'ADMIN/viewUsers.html',{'data':data,'badge':badge})

def deleteUsers(request):
    id = request.GET["id"]
    Login.objects.filter(id=id).delete()
    return redirect('/viewUsers')


def createBadge(request):
    if request.POST:
        badge=request.POST['badge']
        reguser=Badge.objects.create(badge=badge)
        reguser.save()
        messages.success(request,"Badge Created Successfully")
        return redirect('/viewBadge')
    return render(request,'ADMIN/createBadge.html')


def updateBadge(request):
    id = request.GET["id"]
    data = Badge.objects.filter(id=id)
    if request.POST:
        badge = request.POST['badge']
        update = Badge.objects.filter(id=id).update(badge=badge)
        return redirect('/viewBadge')
    return render(request,'ADMIN/updateBadge.html',{'data':data})


def userRequest(request):
    id = request.session["uid"]
    if Register.objects.filter(loginid__id=id, type='requested').exists():
        return HttpResponse("<script>alert('Already applied');window.location.href='/userDash'</script>")
    else:        
        Register.objects.filter(loginid__id=id).update(type='requested')
        messages.success(request,"Requested Successfully")
    return redirect('/userDash')

def approveUser(request):
    # uid = request.session["uid"]
    id = request.GET["id"]
    print(id,"################################id")
    Login.objects.filter(id=id).update(user_type='Moderator')
    Register.objects.filter(loginid=id).update(type='Moderator')
    messages.success(request,"MOD Request Approved Successfully")
    return redirect('/request')

def demoteUsers(request):
    id = request.GET["id"]
    Login.objects.filter(id=id).update(user_type='User')
    Register.objects.filter(loginid=id).update(type='User')
    messages.success(request, "User demoted successfully")
    return redirect('/request')


def rejecteUser(request):
    # uid = request.session["uid"]
    id = request.GET["id"]
    print(id,"################################id")
    Login.objects.filter(id=id).update(user_type='User')
    Register.objects.filter(loginid=id).update(type='User')
    messages.success(request,"Request Rejected")
    return redirect('/request')


def addPost(request):
    uid = request.session["uid"]
    uid = Register.objects.get(loginid=uid)
    if request.POST:
        image = request.FILES["image"]
        title = request.POST['title']
        tag =request.POST['tag']
        post=Post.objects.create(image=image,title=title,tag=tag,registerId=uid)
        post.save()
        messages.success(request,"Post Uploaded Successfully")    
        return redirect('/viewPost')
    return render(request,'USER/addPost.html')



def viewPost(request):
    uid = request.session["uid"]    
    post = Post.objects.filter(registerId__loginid__id=uid)
    return render(request,'USER/viewPost.html',{'post':post})

def modDash(request):
    post = Post.objects.all()
    uid = request.session["uid"]    
    uid = Register.objects.filter(loginid=uid)
    return render(request,'MODER/modDash.html',{'post':post,'uid':uid})

def modViewUsers(request):
    uid = request.session["uid"]    
    uid = Register.objects.filter(loginid=uid)

    data = Register.objects.all()
    return render(request,'MODER/modViewUsers.html',{'data':data,'uid':uid })

def banUsers(request):
    uid = request.session["uid"]    
    uid = Register.objects.filter(loginid=uid)

    data = Register.objects.all()
    return render(request,'MODER/ban.html',{'data':data,'uid':uid })

def ban(request):  
    id = request.GET["id"]
    print(id,"################################id")
    Login.objects.filter(id=id).update(user_type='Banned')
    Register.objects.filter(loginid=id).update(type='Banned')
    messages.info(request, 'User Banned')
    
    return redirect('/modViewUsers')

def unban(request):  
    id = request.GET["id"]
    print(id,"################################id")
    Login.objects.filter(id=id).update(user_type='User')
    Register.objects.filter(loginid=id).update(type='User')
    messages.info(request, 'User Ban Removed')    
    return redirect('/modViewUsers')



def viewBadge(request):
    badges = Badge.objects.all()
    return render(request,'ADMIN/viewBadges.html',{'badges':badges})


def badgeDelete(request):
    id = request.GET["id"]
    badges = Badge.objects.filter(id=id).delete()
    messages.info(request, 'Badge Removed')    
    return redirect('/viewBadge')




def admincomment(request):
    uid = request.session["uid"]
    uid = Register.objects.get(loginid=uid)
    id = request.GET['id']
    post=Post.objects.filter(id=id)
    postid=Post.objects.get(id=id)
    comments=Comments_on_Posts.objects.filter(pid=id)
    print(post,"########################################################")
    if request.POST:
        comment=request.POST['comment']
        reguser=Comments_on_Posts.objects.create(comment=comment,pid=postid,uid=uid)
        reguser.save()
        
        update_post = Post.objects.get(id=id)
        update_post.comment += 1
        update_post.save()
        return redirect('/userDash')
    return render(request,'ADMIN/comment.html',{'post':post,'comments':comments})


def assignBadge(request):
    id = request.GET["id"]
    data = Register.objects.filter(loginid=id)
    user = Register.objects.get(loginid=id)
    badge = Badge.objects.all()
    
    if request.POST:
        assigned_badges = AssignBadge.objects.filter(userId=user)
        assigned_badge_names = [ab.badgeId.badge for ab in assigned_badges]
        assign_badge_name = request.POST['badge']
        
        if assign_badge_name not in assigned_badge_names:
            assign_badge = Badge.objects.get(badge=assign_badge_name)
            assign = AssignBadge.objects.create(badgeId=assign_badge, userId=user)
            assign.save()
            messages.info(request, 'Badge Assigned')
        else:
            messages.info(request, 'Badge Already Assigned')
        
        return redirect('/modViewUsers')
    
    return render(request, 'MODER/assignBadge.html', {'data': data, 'badge': badge})



def deletepost(request):
    id = request.GET["id"]
    Post.objects.filter(id=id).delete()
    messages.info(request, 'Post Deleted')    
    last_page = request.META.get('HTTP_REFERER', '/')
    return redirect(last_page)


# def updateBadge(request):
#     id = request.GET["id"]
#     data = Badge.objects.filter(id=id)
#     if request.POST:
#         badge = request.POST['badge']
#         update = Badge.objects.filter(id=id).update(badge=badge)
#         return redirect('/viewBadge')
#     return render(request,'ADMIN/updateBadge.html',{'data':data})


def donate(request):
    id = request.GET["id"]
    uid = request.session["uid"]    
    postid = Post.objects.get(id=id)
    userid = Register.objects.get(loginid=uid)
    if request.POST:
        amount = request.POST['amount']
        assign = Donation.objects.create(amount=amount,postId=postid,userId=userid)
        assign.save()   
        messages.info(request, 'Donated Successfully')
        return redirect('/userDash')
    return render(request,'USER/donate.html')


def viewDonations(request):
    uid = request.session["uid"]
    print(uid,'<--------------------------------')
    uid = Post.objects.get(registerId__loginid=uid)
    print(uid,"<<uid?????")
    donations = Donation.objects.filter(postId=uid)
    print(donations,"<--------------------------------")
    return render(request,'USER/viewDonations.html',{'donations':donations})


def withdraw(request):
    id = request.GET["id"]
    Donation.objects.filter(id=id).update(status='Withdrawn')
    messages.info(request, 'Withdrawn Successfully')
    return redirect('/viewDonations')

def confirm(request):
    return render(request,'USER/confirm.html')


# def a(request):
#     Post.objects.all().update(comment=0)
#     return HttpResponse('deleeee')



def like(request):
    uid = request.session["uid"]
    Uid = Register.objects.get(loginid=uid)
    pid = request.GET.get("pid")
    Pid = Post.objects.get(id=pid)

    if not Like.objects.filter(liker=Uid, pid=Pid).exists():
        add_like = Like.objects.create(liker=Uid, pid=Pid)
        add_like.save()
        update_like = Post.objects.get(id=pid)
        update_like.like_count += 1
        update_like.save()
    else:
        
        add_like = Like.objects.filter(liker=Uid, pid=Pid).delete()
        update_like = Post.objects.get(id=pid)
        update_like.like_count -= 1
        update_like.save()

    return redirect("/userDash")

def userreport(request):
    uid = request.session["uid"]
    Uid = Register.objects.get(loginid=uid)
    pid = request.GET.get("pid")
    Pid = Post.objects.get(id=pid)

    if not Report.objects.filter(liker=Uid, pid=Pid).exists():
        # If the user has not reported this post before, increment the report count
        add_report = Report.objects.create(liker=Uid, pid=Pid)
        add_report.save()
        Pid.report_count += 1
        Pid.save()
        messages.info(request, 'Reported Successfully')
    else:
        # If the user has already reported this post, remove the report and decrement the report count
        Report.objects.filter(liker=Uid, pid=Pid).delete()
        Pid.report_count -= 1
        Pid.save()
        messages.info(request, 'Reported Removed Sucessfully')

    return redirect("/userDash")


def usercomment(request):
    uid = request.session["uid"]
    uid = Register.objects.get(loginid=uid)
    id = request.GET['id']
    post=Post.objects.filter(id=id)
    postid=Post.objects.get(id=id)
    comments=Comments_on_Posts.objects.filter(pid=id)
    print(post,"########################################################")
    if request.POST:
        comment=request.POST['comment']
        reguser=Comments_on_Posts.objects.create(comment=comment,pid=postid,uid=uid)
        reguser.save()
        
        update_post = Post.objects.get(id=id)
        update_post.comment += 1
        update_post.save()
        return redirect('/userDash')
    return render(request,'USER/comment.html',{'post':post,'comments':comments})


def modcomment(request):
    uid = request.session["uid"]
    uid = Register.objects.get(loginid=uid)
    id = request.GET['id']
    post=Post.objects.filter(id=id)
    postid=Post.objects.get(id=id)
    comments=Comments_on_Posts.objects.filter(pid=id)
    print(post,"########################################################")
    if request.POST:
        comment=request.POST['comment']
        reguser=Comments_on_Posts.objects.create(comment=comment,pid=postid,uid=uid)
        reguser.save()
        
        update_post = Post.objects.get(id=id)
        update_post.comment += 1
        update_post.save()
        return redirect('/userDash')
    return render(request,'MODER/comment.html',{'post':post,'comments':comments})




# Banned users




from django.shortcuts import get_object_or_404

def bannedUser(request):
    uid = request.session.get("uid")  # Get the user's ID from the session
    if uid:  # Check if the user is logged in
        user = get_object_or_404(Register, loginid=uid)  # Get the user object
        if not request.session.get('banned_message_displayed', False):  # Check if the banned message has been displayed
            messages.info(request, 'YOU HAVE BEEN BANNED TEMPORARILY AND HAVE ONLY LIMITED FUNCTIONALITIES')
            request.session['banned_message_displayed'] = True  # Set the flag to indicate that the message has been displayed
    post = Post.objects.all()
    return render(request, 'BANNED/userDash.html', {'post': post, 'user': user})


def banviewPost(request):
    uid = request.session["uid"]    
    post = Post.objects.filter(registerId__loginid__id=uid)

    return render(request,'BANNED/viewPost.html',{'post':post})


def banviewDonations(request):
    uid = request.session["uid"]
    donations = Donation.objects.filter(userId=uid)
    return render(request,'BANNED/viewDonations.html',{'donations':donations})


def comment(request):
    uid = request.session["uid"]
    uid = Register.objects.get(loginid=uid)
    id = request.GET['id']
    post=Post.objects.filter(id=id)
    postid=Post.objects.get(id=id)
    comments=Comments_on_Posts.objects.filter(pid=id)
    print(post,"########################################################")
    if request.POST:
        comment=request.POST['comment']
        reguser=Comments_on_Posts.objects.create(comment=comment,pid=postid,uid=uid)
        reguser.save()
        
        update_post = Post.objects.get(id=id)
        update_post.comment += 1
        update_post.save()
        return redirect('/userDash')
    return render(request,'BANNED/comment.html',{'post':post,'comments':comments})



def deletebadge(request):
    id = request.GET["id"]
    print(id,"sjfdyug")
    AssignBadge.objects.filter(badgeId=id).delete()
    return redirect('/viewachievments')

    


def viewachievmentsus(request):
    badge = AssignBadge.objects.all()
    return render(request,'USER/viewachievments.html',{'badge':badge})

    

def viewachievments(request):
    badge = AssignBadge.objects.all()
    return render(request,'MODER/viewachievments.html',{'badge':badge})

   

   