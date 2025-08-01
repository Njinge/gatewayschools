# 🆓 Free Hosting Guide for Gateway Schools Website

## 🚀 **Option 1: Render (Recommended)**

### **Step 1: Prepare Your Code**
Your project is already configured for Render deployment with:
- ✅ `render.yaml` configuration file
- ✅ `build.sh` build script
- ✅ Updated `requirements.txt`
- ✅ Production settings in `settings.py`

### **Step 2: Deploy on Render**

1. **Create Render Account**
   - Go to [render.com](https://render.com)
   - Sign up with GitHub/GitLab

2. **Connect Your Repository**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Render will auto-detect Django settings

3. **Configure Service**
   - **Name**: `gateway-schools`
   - **Environment**: `Python`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn school_portal.wsgi:application`
   - **Plan**: Free

4. **Environment Variables** (Auto-configured):
   - `DEBUG`: `False`
   - `SECRET_KEY`: Auto-generated
   - `ALLOWED_HOSTS`: `.onrender.com`
   - `DATABASE_URL`: Auto-configured

5. **Deploy**
   - Click "Create Web Service"
   - Wait for build to complete (5-10 minutes)
   - Your site will be live at: `https://gateway-schools.onrender.com`

### **Step 3: Set Up Database**
1. In your Render dashboard, go to "Databases"
2. Create a new PostgreSQL database
3. Connect it to your web service
4. Run migrations: `python manage.py migrate`

---

## 🚀 **Option 2: Railway**

### **Step 1: Deploy on Railway**
1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your repository
5. Railway will auto-detect Django

### **Step 2: Configure**
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn school_portal.wsgi:application`
- **Environment Variables**:
  - `DEBUG`: `False`
  - `SECRET_KEY`: Generate a new one
  - `DATABASE_URL`: Auto-provided by Railway

---

## 🚀 **Option 3: PythonAnywhere**

### **Step 1: Create Account**
1. Go to [pythonanywhere.com](https://pythonanywhere.com)
2. Sign up for free account

### **Step 2: Upload Code**
1. Go to "Files" tab
2. Upload your project files
3. Or clone from GitHub

### **Step 3: Configure Web App**
1. Go to "Web" tab
2. Click "Add a new web app"
3. Choose "Django"
4. Set Python version to 3.12

### **Step 4: Install Dependencies**
```bash
pip install -r requirements.txt
```

### **Step 5: Configure Settings**
Update `settings.py`:
```python
DEBUG = False
ALLOWED_HOSTS = ['yourusername.pythonanywhere.com']
```

---

## 🚀 **Option 4: Heroku (Legacy Free)**

### **Step 1: Create Heroku Account**
1. Go to [heroku.com](https://heroku.com)
2. Sign up (requires credit card for verification)

### **Step 2: Install Heroku CLI**
```bash
# macOS
brew install heroku/brew/heroku

# Windows
# Download from heroku.com
```

### **Step 3: Deploy**
```bash
# Login to Heroku
heroku login

# Create app
heroku create gateway-schools

# Add PostgreSQL
heroku addons:create heroku-postgresql:mini

# Deploy
git add .
git commit -m "Deploy to Heroku"
git push heroku main

# Run migrations
heroku run python manage.py migrate
```

---

## 📋 **Deployment Checklist**

### **Before Deployment**
- [x] All legal pages created (Privacy Policy, Terms, Sitemap)
- [x] Footer links working
- [x] Database migrations ready
- [x] Static files configured
- [x] Production settings updated
- [x] Requirements.txt updated

### **After Deployment**
- [ ] Test all pages load correctly
- [ ] Test user registration/login
- [ ] Test admin panel access
- [ ] Test contact form
- [ ] Test mobile responsiveness
- [ ] Set up custom domain (optional)

---

## 🎯 **Quick Start Commands**

### **For Render:**
```bash
# Your code is ready! Just push to GitHub and connect to Render
git add .
git commit -m "Ready for deployment"
git push origin main
```

### **For Railway:**
```bash
# Same as Render - just connect your GitHub repo
```

### **For PythonAnywhere:**
```bash
# Upload files via web interface or:
git clone https://github.com/yourusername/gateway-schools.git
```

---

## 🔗 **Your Deployed URLs**

After deployment, your site will be available at:

- **Render**: `https://gateway-schools.onrender.com`
- **Railway**: `https://gateway-schools.railway.app`
- **PythonAnywhere**: `https://yourusername.pythonanywhere.com`
- **Heroku**: `https://gateway-schools.herokuapp.com`

---

## 💡 **Tips for Free Hosting**

### **Render Tips:**
- ⚠️ Free tier sleeps after 15 minutes of inactivity
- 🔄 First visit after sleep takes 30-60 seconds
- 📊 750 hours/month free
- 🌐 Custom domains supported

### **Railway Tips:**
- 💰 $5 credit monthly
- ⚡ Faster than Render
- 🔄 No sleep issues
- 🌐 Custom domains supported

### **PythonAnywhere Tips:**
- 📱 Mobile-friendly interface
- 🐍 Python-focused
- 📚 Great for learning
- ⚠️ Limited bandwidth (1GB/month)

### **Heroku Tips:**
- ⚠️ Free tier being phased out
- 💳 Requires credit card
- 🔄 Sleep after 30 minutes
- 🌐 Custom domains supported

---

## 🆘 **Troubleshooting**

### **Common Issues:**

1. **Build Fails**
   - Check `requirements.txt` is complete
   - Verify Python version compatibility

2. **Database Errors**
   - Run migrations: `python manage.py migrate`
   - Check database URL configuration

3. **Static Files Not Loading**
   - Run: `python manage.py collectstatic`
   - Check `STATIC_ROOT` configuration

4. **500 Errors**
   - Check `DEBUG = False` in production
   - Review server logs
   - Verify `ALLOWED_HOSTS` settings

---

## 🎉 **Success!**

Once deployed, your Gateway Schools website will be:
- ✅ Live on the internet
- ✅ Accessible worldwide
- ✅ Mobile-responsive
- ✅ SEO-ready
- ✅ Legal-compliant
- ✅ Free to host

**Next Steps:**
1. Test all functionality
2. Set up custom domain (optional)
3. Configure analytics
4. Set up backups
5. Monitor performance

---

**Last Updated**: August 1, 2024  
**Status**: Ready for Free Deployment! 🚀 