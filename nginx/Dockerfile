FROM nginx:alpine

# remove the old nginx.conf
RUN rm /etc/nginx/conf.d/default.conf

# Copy custom nginx config
COPY ./nginx.conf /etc/nginx/conf.d

# COPY conf.d/app.conf /etc/nginx/conf.d/app.conf

# COPY ./Client/dist /usr/share/nginx/html

EXPOSE 80 433

# CMD ["nginx", "-g", "daemon off;"]
