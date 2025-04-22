def profile_add(request):
    if request.method == "POST":
        form = ProfileAddForm(request.POST)
        if form.is_valid():
            try:
                profile = form.save()
                return redirect(reverse("profile", kwargs={"pk": profile.pk}))
            except Exception as e:
                # Add error handling
                form.add_error(None, f"Error saving profile: {str(e)}")
        else:
            # Form is invalid - will display errors in template
            pass
    else:
        form = ProfileAddForm()
    
    # Add some debug output
    print("Form errors:", form.errors if request.method == "POST" else "No errors (GET request)")
    return render(request, 'studybuddy_app/profile_add.html', {'form': form})