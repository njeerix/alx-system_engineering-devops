#!/usr/bin/env ruby

#Get the argument from the command line
input = ARGV[0]

#Define The regular expression to match only capital letters
regex = /[A-Z]/

#Use the regular expression matching method to extract all capital letters
matches = input.scan(regex)

#Join the matches into a single string
result = matches.join

#Print the result or an empty string if no matches
puts result.empty? ? " " : result
