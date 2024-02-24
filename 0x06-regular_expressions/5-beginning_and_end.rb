#!/usr/bin/env ruby
input_argument = ARGV[0]
result = input_argument.scan(/^h.n$/).join
puts result

