# Ensure the SSH configuration file exists
file { '/etc/ssh/ssh_config':
  ensure => file,
  owner  => 'root',
  group  => 'root',
  mode   => '0644',
}

# Declare the identity file
file_line { 'Declare identity file':
  path  => '/etc/ssh/ssh_config',
  line  => '    IdentityFile ~/.ssh/school',
  match => '    IdentityFile',
}

# Turn off password authentication
file_line { 'Turn off passwd auth':
  path  => '/etc/ssh/ssh_config',
  line  => '    PasswordAuthentication no',
  match => '    PasswordAuthentication',
}
