# Setup New Ubuntu server with nginx
# and add a custom HTTP header

package { 'nginx':
	ensure => 'installed',
}

file_line { 'install':
  ensure => 'present',
  path   => '/etc/nginx/sites-enabled/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://twitter.com/rash0x6964 permanent;',
}

file {'/var/www/html/index.html':
	content => 'Hello World!'
}

exec {'HTTP header':
	command => 'sed -i "s/server_name _;/server_name _;\n\tadd_header X-Served-By \$hostname;/" /etc/nginx/sites-enabled/default',
	provider => 'shell'
}

service {'nginx':
	ensure => running,
	require => Package['nginx']
}
