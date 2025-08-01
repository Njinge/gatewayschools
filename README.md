# Gateway Schools Website

A comprehensive Django-based school management and information website for Gateway Schools.

## Features

### 🏠 **Home Page**
- Modern, responsive hero section
- Feature highlights with animated cards
- Program previews
- Statistics showcase
- Testimonials from parents
- Call-to-action sections

### 📚 **Programs & Services**
- Comprehensive program listings
- Service offerings
- Enrollment tracking
- Fee information
- Capacity management

### 👥 **About Us**
- School history and mission
- Staff profiles and bios
- Core values presentation
- Parent testimonials

### 📰 **News & Events**
- Blog posts and announcements
- Event calendar
- Category filtering
- Featured content

### 📸 **Media Gallery**
- Photo and video gallery
- Category-based filtering
- Search functionality
- Album organization
- Pagination

### 📞 **Contact System**
- Contact form with validation
- School information
- Location details
- Multiple contact methods

### 👤 **User Management**
- User registration and login
- Role-based access (Admin, Teacher, Parent, Student)
- Profile management

### 🎨 **Design Features**
- Modern, responsive design
- Bootstrap 5 framework
- Custom teal color scheme
- Font Awesome icons
- Smooth animations and transitions

## Technology Stack

- **Backend**: Django 5.2.4
- **Database**: SQLite (development)
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Icons**: Font Awesome 6
- **Images**: Pillow (Python Imaging Library)

## Apps Structure

### Core Apps
- **core**: Main website pages and views
- **users**: User authentication and profiles
- **staff**: Staff management system
- **programs**: Educational programs and services
- **blog**: News and blog posts
- **media_gallery**: Photo and video gallery
- **admissions**: Student admission system
- **academics**: Academic management
- **notifications**: Notification system

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd gateway-schools
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Populate sample data**
   ```bash
   python manage.py populate_sample_data
   ```

7. **Run development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the website**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Key Models

### Staff Management
- **Staff**: Teacher and administrator profiles
- **StaffType**: Role classification (Teacher, Admin, Support, Headteacher)

### Programs & Services
- **Program**: Educational programs (Nursery, Pre-primary, Primary, After-school)
- **Service**: Additional services (Meals, Transport, Health, etc.)

### Content Management
- **Post**: Blog posts and news articles
- **Event**: School events and activities
- **MediaItem**: Gallery photos and videos
- **Album**: Photo album organization

### User Management
- **CustomUser**: Extended user model with roles
- **User Roles**: Admin, Teacher, Parent, Student

## Admin Features

The Django admin interface provides comprehensive management for:

- **Staff Management**: Add, edit, and manage staff profiles
- **Program Management**: Create and manage educational programs
- **Content Management**: Publish news, events, and gallery items
- **User Management**: Manage user accounts and permissions
- **System Configuration**: Configure school settings and preferences

## Customization

### Styling
- Primary color: Teal (#008080)
- Secondary color: Gray (#6c757d)
- Font: Montserrat
- Icons: Font Awesome

### Adding Content
1. **Staff**: Add through Django admin under Staff app
2. **Programs**: Create programs in Programs app
3. **News**: Publish posts through Blog app
4. **Gallery**: Upload media through Media Gallery app

## Development

### Adding New Features
1. Create new Django app: `python manage.py startapp app_name`
2. Add to INSTALLED_APPS in settings.py
3. Create models, views, and templates
4. Add URL patterns
5. Run migrations

### Database Management
- **Create migrations**: `python manage.py makemigrations`
- **Apply migrations**: `python manage.py migrate`
- **Reset database**: Delete db.sqlite3 and run migrations

## Deployment

### Production Setup
1. Set `DEBUG = False` in settings.py
2. Configure production database (PostgreSQL recommended)
3. Set up static file serving
4. Configure media file storage
5. Set up web server (Nginx + Gunicorn)

### Environment Variables
- `SECRET_KEY`: Django secret key
- `DEBUG`: Debug mode (False for production)
- `ALLOWED_HOSTS`: Allowed host domains
- `DATABASE_URL`: Database connection string

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For support and questions, please contact the development team or create an issue in the repository.

---

**Gateway Schools** - Nurturing Bright Minds for a Brighter Future # gatewaysite
# gatewaysite
