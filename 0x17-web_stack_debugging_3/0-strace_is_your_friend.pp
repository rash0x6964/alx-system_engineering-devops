# Replace a line in a file

file { '/var/www/html/wp-settings.php':
  ensure  => present,
  replace => {
    '/phpp/' => 'php',
  },
}
