#!/usr/bin/env ruby

#Get the argument from the command line
input = ARGV[0]

#Define the regular expression to match "School"
regex = /School/

#Use the regular expression matching method
match_result = input.match(regex)

#Print the match resukt or an empty string if no match
puts match_result ? match_result[0] : " "
