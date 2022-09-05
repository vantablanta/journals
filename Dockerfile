FROM alpine:3.16

WORKDIR /.

COPY pipfile.lock /./

RUN pipen sync

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver" ]

