# kill a process named killmenow

exec { 'killmenow_process':
  command     => 'pkill -f killmenow',
  provider => 'shell',
}
