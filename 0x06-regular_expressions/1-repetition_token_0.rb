#!/usr/bin/env ruby
input_argument = ARGV[0]
result = input_argument.scan(/hbt{2,5}n/).join
puts result

