# CloudSphere
## Cloud Services Management Platform

Professional self-contained PHP/MySQL cloud infrastructure management project.

### Features
- Cloud services, virtual servers, storage and database management
- Authentication and protected dashboard
- CRUD operations
- Local CSS and Vanilla JavaScript only
- MySQL database and CSV dataset
- Google Colab analysis script

### Requirements
PHP 8+, MySQL, XAMPP or compatible server.

### Installation
1. Copy project to `htdocs/CloudSphere`.
2. Import `database/cloudsphere_db.sql` using phpMyAdmin.
3. Edit `config/database.php`.
4. Open `http://localhost/CloudSphere/`.

Demo login: `admin@cloudsphere.com` / `admin123`

### InfinityFree
Upload project files to `htdocs`, create a MySQL database, import the SQL file, then update DB_HOST, DB_NAME, DB_USER and DB_PASS.

### Git
```bash
git init
git add .
git commit -m "Initial CloudSphere project"
git branch -M main
git remote add origin REPOSITORY_URL
git push -u origin main
git clone REPOSITORY_URL
git pull origin main
git push origin main
```

### Google Colab
Upload `data/cloud_usage_data.csv` to Google Drive folder `MyDrive/CloudSphere/`, then run `Google_Colab_Cloud_Analysis.py` cells in Colab.
