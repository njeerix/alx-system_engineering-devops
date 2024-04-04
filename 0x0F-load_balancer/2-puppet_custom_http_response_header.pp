package { 'nginx':
  ensure => installed,
}

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "
    server {
      listen 80 default_server;
      listen [::]:80 default_server;
      add_header X-Serverd-By $::hostname;

      location / {
        root /var/www/html;
        index index.html index.htm;
      }
   }
 ",
 require => Package['nginx'],
 notify  => Service['nginx'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
