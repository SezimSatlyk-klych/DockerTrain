FROM python:3.13.3-slim-bullseye



#create virtual environment
#isolate python app and installs from system-level python
RUN python -m venv /opt/venv
ENV PATH=/opt/venv/bin:$PATH


WORKDIR /app

#copy local_folder/file container_destination
COPY requirements.txt  /tmp/requirements.txt

#run within_container_while_building
RUN pip install -r  /tmp/requirements.txt

COPY ./src .

CMD ["python","-m","http.server","8000"]
