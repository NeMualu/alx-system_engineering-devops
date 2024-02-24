#!/usr/bin/env ruby
input_argument = ARGV[0]
result = input_argument.scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")
puts result

