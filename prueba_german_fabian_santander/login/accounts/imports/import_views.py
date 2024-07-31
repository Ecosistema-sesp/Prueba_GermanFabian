from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from ..forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.cache import never_cache
from ..utils import check_database_connection