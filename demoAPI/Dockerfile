FROM openjdk:11
RUN apt-get update -y && \
    apt-get install -y \
            python3 python3-pip
RUN java -version
RUN python3 --version

ENV USER=1001

# set the working directory in the container
WORKDIR /code

COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY src/ .
RUN chown $USER:$USER -R .
#EXPOSE 8080
USER $USER
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
