from django.urls import path

from myapp.views import manage_users, manage_features, manage_roles
from myapp.views.manage_users import UserList, UserCreate, UserUpdate, UserDelete

app_name = 'system-admin'
urlpatterns = [
    path('users/', UserList.as_view(extra_context={'title': 'Manage Users'}), name='users'),
    path('users/new/', UserCreate.as_view(extra_context={'title': 'Create User'}), name='create-user'),
    path('users/<int:pk>/', UserUpdate.as_view(extra_context={'title': 'Edit User'}), name='edit-user'),
    path('users/<int:user_id>/assign-roles/', manage_users.assign_role, name='assign-role'),
    path('users/<int:pk>/delete-user/', UserDelete.as_view(extra_context={'title': 'Delete User'}), name='delete-user'),
    path('roles/', manage_roles.all_roles, name='roles'),
    path('roles/new/', manage_roles.role, name='create-role'),
    path('roles/<int:role_id>/permissions/', manage_roles.role, name='permissions'),
    path('roles/<int:role_id>/delete-role/', manage_roles.delete_role, name='delete-role'),
    path('system-features/', manage_features.all_features, name='features'),
    path('system-features/new/', manage_features.feature, name='create-feature'),
    path('system-features/<int:feature_id>/delete/', manage_features.delete_feature, name='delete-feature'),
]
