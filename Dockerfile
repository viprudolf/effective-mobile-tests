FROM python:3.10

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y chromium-driver chromium

ENV PATH="/usr/lib/chromium-browser/:$PATH"

CMD ["pytest", "--alluredir=allure-results"]
