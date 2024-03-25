# Ensure SSH client configuration file exists
include stdlib

# Disable password authentication in SSH client configuration
file_line { 'Turn off passwd auth':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  replace => true,
}

# Declare identify file in SSH client configuration
file_line { 'Declare identity file':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  replace => true,
}
