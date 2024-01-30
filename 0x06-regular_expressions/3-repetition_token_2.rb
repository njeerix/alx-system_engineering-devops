#!/usr/bin/env ruby

#Get the arguments from the command line
input = ARGV[0]

#Define the regular expression to match "hbtn" followed by one or more 't' characters and then "n"
regex = /hbt+n/

#Use the regular expression matching method
match_result = input.match(regex)

#Print the match result or an empty string if no match
puts match_result ? match_result[0]: " "
