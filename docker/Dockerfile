FROM python:3.8.13

RUN apt-get update && apt-get -y upgrade

RUN pip install --upgrade pip
RUN pip install streamlit \
                streamlit-elements==0.1.*

WORKDIR /workspace

# streamlitの起動
ENTRYPOINT ["streamlit"]
CMD ["hello"]
EXPOSE 8501
