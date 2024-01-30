#!/usr/bin/env ruby

#Get the argument from the command line
input = ARGV[0]

#Define the regular expression to match astring starting with 'h', endingwith 'n', and having any single character in between
regex = /^h.n$/

#Use the regular expression matching method
match_result = input.match(regex)

#Print the match result or an empty string if no match
puts match_result ? match_result[0]: " "
