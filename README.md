
**Build and run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

**Alternative: Manual Docker commands**
   ```bash
   # Build the image
   docker build -t steinadler-demo .

   # Run the container
   docker run -p 7860:7860 steinadler-demo
   ```
   