#!/usr/bin/env ruby
input_argument = ARGV[0]
result = input_argument.scan(/^\d{10,10}$/).join
puts result

