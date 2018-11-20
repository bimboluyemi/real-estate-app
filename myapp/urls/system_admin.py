from django.urls import path

from myapp.views import manage_features, manage_roles
from myapp.views.manage_users import UserList, UserCreate, UserUpdate, UserDelete, UserEnable, AssignRole
from myapp.views.manage_roles import RoleDelete

app_name = 'system-admin'
urlpatterns = [
    path('users/', UserList.as_view(extra_context={'title': 'Manage Users'}), name='users'),
    path('users/new/', UserCreate.as_view(extra_context={'title': 'Create User'}), name='create-user'),
    path('users/<int:pk>/', UserUpdate.as_view(extra_context={'title': 'Edit User'}), name='edit-user'),
    path('users/<int:pk>/assign-roles/', AssignRole.as_view(extra_context={'title': 'Assign Roles to User'}),
         name='assign-role'),
    path('users/<int:pk>/enable-user/', UserEnable.as_view(extra_context={'title': 'Enable User'}), name='enable-user'),
    path('users/<int:pk>/delete-user/', UserDelete.as_view(extra_context={'title': 'Delete User'}), name='delete-user'),
    path('roles/', manage_roles.all_roles, name='roles'),
    path('roles/new/', manage_roles.role, name='create-role'),
    path('roles/<int:pk>/permissions/',
         manage_roles.ManagePermission.as_view(extra_context={'title': 'Assign Features to Role'}),
         name='permissions'),
    path('roles/<int:pk>/delete-role/', RoleDelete.as_view(extra_context={'title': 'Delete Role'}),
         name='delete-role'),
    path('features/', manage_features.all_features, name='features'),
    path('features/new/', manage_features.feature, name='create-feature'),
    path('features/<int:pk>/delete/',
         manage_features.FeatureDelete.as_view(extra_context={'title': 'Delete Feature'}),
         name='delete-feature'),
]
