FROM amazon/aws-lambda-python:3.8

# install chrome using yum
RUN yum install -y wget unzip libX11 GConf2 fontconfig

# install chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
RUN yum install -y ./google-chrome-stable_current_*.rpm

# install chromedriver matching chrome version
RUN wget https://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip
RUN mv chromedriver /usr/bin/chromedriver
RUN chown root:root /usr/bin/chromedriver
RUN chmod +x /usr/bin/chromedriver



# Copy project files
COPY . /app

# Set working directory
WORKDIR /app

# Install requirements
RUN pip install -r requirements.txt

# open port 5000
EXPOSE 5000


# Run flask
# CMD ["python3", "app.py"]
CMD ["app.handler"]