from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('register/',views.register),
    path('login/',views.login),
    path('demoteUsers/', views.demoteUsers, name='demote_users'),

# USER
    path('userDash/',views.userDash),
    path('userRequest/',views.userRequest),
    path('request/',views.request),
    path('addPost/',views.addPost),
    path('viewPost/',views.viewPost),
    path('donate/',views.donate),
    path('viewDonations/',views.viewDonations),
    path('withdraw/',views.withdraw),
    path('usercomment/',views.usercomment),
    path('userreport/',views.userreport),
    path('confirm/',views.confirm),
    path('deletepost/',views.deletepost),
    

# BANNED
    path('bannedUser/',views.bannedUser),
    path('banviewPost/',views.banviewPost),
    path('banviewDonations/',views.banviewDonations),
    path('comment/',views.comment),


#ADMIN
    path('adminDash/',views.adminDash),
    path('viewUsers/',views.viewUsers),
    path('approveUser/',views.approveUser),
    path('rejecteUser/',views.rejecteUser),
    path('deleteUsers/',views.deleteUsers),
    
    path('createBadge/',views.createBadge),
    path('viewBadge/',views.viewBadge),
    
    path('updateBadge/',views.updateBadge),
    path('badgeDelete/',views.badgeDelete),

    path('admincomment/',views.admincomment),

    # path('a/',views.a),
    
#MODERATORS
    path('modDash/',views.modDash),
    path('modViewUsers/',views.modViewUsers),
    path('banUsers/',views.banUsers),
    path('deletebadge/',views.deletebadge),
    
    path('ban/',views.ban),
    path('unban/',views.unban),
    path('modcomment/',views.modcomment),
    
    
    
    # path('badge/',views.badge),
    path('assignBadge/',views.assignBadge),

#like
    path('like/',views.like),
    path('viewachievments/',views.viewachievments),
    path('viewachievmentsus/',views.viewachievmentsus),

]