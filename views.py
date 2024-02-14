from django.shortcuts import render
from .models import MinecraftTime

def home(request):
    return render(request, 'home.html')

def calculate_time(request):
    if request.method == 'POST':
        minecraft_time = request.POST.get('minecraft_time')
        
        if minecraft_time:
            if minecraft_time.isnumeric():
                minecraft_time = float(minecraft_time)
        
                # Perform the calculation here

                # Save the results to the database for logging
                MinecraftTime.objects.create(minecraft_time=minecraft_time, real_time=calculated_real_time)
        
                return render(request, 'result.html', {'calculated_real_time': calculated_real_time})
    
    return render(request, 'home.html', {'error': 'Invalid input. Please enter a valid number.'})