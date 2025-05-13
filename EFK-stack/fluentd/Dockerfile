FROM fluent/fluentd:edge-debian

USER root

RUN gem install fluent-plugin-elasticsearch \
    && gem sources --clear-all \
    && rm -rf /home/fluent/.gem/ruby/*/cache/*.gem

USER fluent
