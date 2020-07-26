FROM python:3

MAINTAINER dand-or

# タイムゾーン
RUN cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

# 実行ユーザー作成
ARG UID=501
ARG USER=developer
RUN useradd -m -u ${UID} ${USER}
# ユーザ変更
USER ${UID}

# パッケージ
RUN pip install --upgrade pip && \
pip install requests && \
pip install bs4
