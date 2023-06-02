# Microservice App

## Services
### Frontend Service
سرویس frontend مسئولیت ساخت و اجرای اپلیکیشن frontend را بر عهده دارد. دارای پیکربندی زیر است:

* ساخت: Dockerfile را به عنوان frontend.Dockerfile مشخص می کند. این بدان معناست که سرویس frontend با استفاده از فایل های موجود در مسیر ./front ساخته می شود.
* پورت ها: پورت 3000 کانتینر را به پورت 3000 دستگاه میزبان مپ میکند. این امکان دسترسی به برنامه frontend را از http://localhost:3000 فراهم می کند.
* مبتنی است بر: وابستگی به سرویس Backend وجود دارد. این تضمین می‌کند که سرویس بکند قبل از سرویس frontend شروع شده است.

### Backend Service

سرویس Backend وظیفه ساخت و اجرای برنامه Backend را بر عهده دارد. دارای پیکربندی زیر است:

* ساخت: Dockerfile را به عنوان backend.Dockerfile مشخص می کند. این بدان معناست که سرویس بکند با استفاده از فایل‌های موجود در دایرکتوری ./api ساخته می‌شود.
* پورت ها: پورت 8000 کانتینر را به پورت 8000 دستگاه میزبان مپ میکند. این امکان دسترسی به برنامه بکند را از http://localhost:8000 فراهم می کند.
## Running the Application

```bash
docker compose up --build
```

این دستور ایمیج های Docker را برای سرویس‌های frontend و backend می‌سازد و کانتینرها را شروع می‌کند. می توانید در مرورگر وب خود در http://localhost:3000 به برنامه frontend و در http://localhost:8000 به برنامه backend دسترسی داشته باشید.

```bash
docker compose stop
```
## screenshots

### `docker images`
![docker images](https://github.com/sfmqrb/se-lab-microservice/assets/45316558/c8ba46ba-5a3b-4f17-a3c8-14349543e50d)

### `docker compose up --build`
![docker-build](https://github.com/sfmqrb/se-lab-microservice/assets/45316558/de5aab14-7d0e-4102-8e14-4f069edd0086)

### `docker ps`
![docker ps](https://github.com/sfmqrb/se-lab-microservice/assets/45316558/71ff09e3-f491-4ef1-99b1-43a99c907a35)

