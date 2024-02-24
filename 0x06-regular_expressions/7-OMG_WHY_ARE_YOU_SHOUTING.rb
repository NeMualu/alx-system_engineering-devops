#!/usr/bin/env ruby
input_argument = ARGV[0]
result = input_argument.scan(/[A-Z]*/).join
puts result

