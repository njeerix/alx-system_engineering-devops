#!/usr/bin/env ruby

#Get the argument from the command line
input = ARGV[0]

#Define the regular expression to match "School"
regex = /School/

#Use the regular expression matching method
matches = input.scan(regex)

#join the matches into a single string
result = matches.join

#Print the result or an empty string if no matches
puts result.empty? ? "" : result
