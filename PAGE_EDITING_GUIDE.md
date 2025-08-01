# Page Editing Guide - Gateway Schools Website

## 📁 **File Structure Overview**

```
Gateway site/
├── core/
│   ├── templates/
│   │   └── core/
│   │       ├── base.html          # Main template (header, footer, navigation)
│   │       ├── home.html          # Home page
│   │       ├── about.html         # About page
│   │       ├── programs.html      # Programs page
│   │       ├── contact.html       # Contact page
│   │       ├── news.html          # News page
│   │       └── events.html        # Events page
│   ├── views.py                   # Page logic (what data to show)
│   └── urls.py                    # URL routing
├── users/
│   ├── templates/
│   │   └── users/
│   │       ├── login.html         # Login page
│   │       └── signup.html        # Signup page
│   └── views.py                   # User authentication logic
└── media_gallery/
    ├── templates/
    │   └── media_gallery/
    │       └── gallery.html       # Gallery page
    └── views.py                   # Gallery logic
```

## 🎨 **How to Edit Existing Pages**

### 1. **Edit Page Content (HTML)**
To edit the content of any page, find the corresponding template file:

- **Home page**: `core/templates/core/home.html`
- **About page**: `core/templates/core/about.html`
- **Programs page**: `core/templates/core/programs.html`
- **Contact page**: `core/templates/core/contact.html`
- **News page**: `core/templates/core/news.html`
- **Events page**: `core/templates/core/events.html`
- **Gallery page**: `media_gallery/templates/media_gallery/gallery.html`

### 2. **Edit Page Logic (Python)**
To change what data is displayed on pages, edit the view files:

- **Main pages**: `core/views.py`
- **User pages**: `users/views.py`
- **Gallery**: `media_gallery/views.py`

### 3. **Edit Navigation/Footer**
The navigation and footer are in `core/templates/core/base.html` - this affects ALL pages.

## 🆕 **How to Create New Pages**

### Step 1: Create the Template
Create a new HTML file in the appropriate template directory:

```bash
# Example: Create a new "Admissions" page
touch core/templates/core/admissions.html
```

### Step 2: Add the View
Add a new function in `core/views.py`:

```python
def admissions(request):
    context = {
        'page_title': 'Admissions',
        'admission_info': 'Your admission content here'
    }
    return render(request, 'core/admissions.html', context)
```

### Step 3: Add the URL
Add a new URL pattern in `core/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    # ... existing URLs ...
    path('admissions/', views.admissions, name='admissions'),
]
```

### Step 4: Add to Navigation
Edit `core/templates/core/base.html` to add the new page to the navigation menu.

## 📝 **Common Editing Tasks**

### **1. Change Text Content**
Find the HTML file and edit the text between the tags:

```html
<!-- Before -->
<h1>Welcome to Gateway Schools</h1>

<!-- After -->
<h1>Welcome to Our Amazing School</h1>
```

### **2. Change Images**
Replace image sources:

```html
<!-- Before -->
<img src="/static/images/old-image.jpg" alt="Old Image">

<!-- After -->
<img src="/static/images/new-image.jpg" alt="New Image">
```

### **3. Change Colors**
Edit the CSS in `core/templates/core/base.html`:

```css
/* Change primary color from teal to blue */
.text-teal {
    color: #0066cc !important;
}
.bg-teal {
    background-color: #0066cc !important;
}
```

### **4. Add New Sections**
Add new HTML sections to any template:

```html
<!-- Add a new section -->
<section class="py-5 bg-light">
    <div class="container">
        <h2 class="text-center text-teal mb-4">New Section</h2>
        <p>Your new content here...</p>
    </div>
</section>
```

### **5. Change Fees/Prices**
Edit the program data through Django admin or update the database directly.

## 🔧 **Advanced Editing**

### **1. Add Dynamic Content**
Edit the view to pass more data:

```python
# In core/views.py
def programs(request):
    programs_list = Program.objects.filter(is_active=True)
    services_list = Service.objects.filter(is_available=True)
    
    context = {
        'programs': programs_list,
        'services': services_list,
        'total_programs': programs_list.count(),  # New data
    }
    return render(request, 'core/programs.html', context)
```

### **2. Add Forms**
Create forms in `core/forms.py` and add them to views:

```python
# In core/forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
```

### **3. Add JavaScript**
Add JavaScript to any template:

```html
{% block extra_js %}
<script>
    // Your JavaScript code here
    console.log('Page loaded!');
</script>
{% endblock %}
```

## 🎯 **Quick Reference**

### **Common Template Tags**
```html
{% url 'page_name' %}          <!-- Generate URL -->
{{ variable_name }}            <!-- Display variable -->
{% if condition %}...{% endif %} <!-- Conditional -->
{% for item in items %}...{% endfor %} <!-- Loop -->
{% extends 'core/base.html' %} <!-- Extend base template -->
{% block content %}...{% endblock %} <!-- Content block -->
```

### **Bootstrap Classes**
```html
text-teal          <!-- Teal text color -->
bg-teal            <!-- Teal background -->
btn-teal           <!-- Teal button -->
shadow-sm          <!-- Small shadow -->
rounded            <!-- Rounded corners -->
py-5              <!-- Padding top/bottom -->
mb-3              <!-- Margin bottom -->
```

### **Font Awesome Icons**
```html
<i class="fas fa-school"></i>      <!-- School icon -->
<i class="fas fa-user"></i>        <!-- User icon -->
<i class="fas fa-envelope"></i>    <!-- Email icon -->
<i class="fas fa-phone"></i>       <!-- Phone icon -->
<i class="fas fa-map-marker-alt"></i> <!-- Location icon -->
```

## 🚀 **Testing Your Changes**

1. **Start the server**:
   ```bash
   python manage.py runserver 8001
   ```

2. **Visit the page**:
   - http://127.0.0.1:8001/ (home)
   - http://127.0.0.1:8001/programs/ (programs)
   - http://127.0.0.1:8001/about/ (about)

3. **Check for errors**:
   - Look at the terminal for error messages
   - Check browser console for JavaScript errors

## 📋 **Common Issues & Solutions**

### **Page not found (404)**
- Check if URL is added to `urls.py`
- Check if view function exists in `views.py`

### **Template not found**
- Check if template file exists in correct directory
- Check template name in `render()` function

### **Changes not showing**
- Refresh browser (Ctrl+F5 for hard refresh)
- Check if server is running
- Check for syntax errors in template

### **Styling not working**
- Check if Bootstrap CSS is loaded
- Check if custom CSS is in `base.html`
- Check for CSS syntax errors

## 🎨 **Design System**

### **Colors**
- Primary: #008080 (Teal)
- Secondary: #6c757d (Gray)
- Success: #28a745 (Green)
- Warning: #ffc107 (Yellow)
- Danger: #dc3545 (Red)

### **Typography**
- Font: Montserrat
- Headings: Bold weights
- Body: Regular weight

### **Spacing**
- Use Bootstrap spacing classes (p-*, m-*, py-*, px-*, etc.)
- Consistent padding: py-5 for sections
- Consistent margins: mb-3, mb-4, mb-5

---

**Need Help?** Check the Django documentation or ask for assistance with specific changes! 