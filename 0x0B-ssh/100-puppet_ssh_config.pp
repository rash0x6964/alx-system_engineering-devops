# make changes on config file

$ssh_config_path = '/etc/ssh/ssh_config'

file_line { 'Turn off passwd auth':
  ensure => present,
  path   => $ssh_config_path,
  line   => '    PasswordAuthentication no',
  replace => true,
}

file_line { 'Delare identity file':
  ensure => present,
  path   => $ssh_config_path,
  line   => '     IdentityFile ~/.ssh/school',
  replace => true,
}
