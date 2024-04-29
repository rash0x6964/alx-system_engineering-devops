# Setup New Ubuntu server with nginx
# and add a custom HTTP header

package { 'nginx':
	ensure => 'installed',
}

file_line { 'install':
  ensure => 'present',
  path   => '/etc/nginx/sites-enabled/default',
  after  => 'server_name _;',
  line   => 'rewrite ^/redirect_me https://twitter.com/rash0x6964 permanent;',
}

file {'/var/www/html/index.html':
	content => 'Hello World!'
}

file_line { 'header':
  ensure => 'present',
  path   => '/etc/nginx/sites-enabled/default',
  after  => 'server_name _;',
  line   => 'add_header X-Served-By $hostname;',
}

service {'nginx':
	ensure => running,
	require => Package['nginx']
}
