#!/usr/bin/env ruby

#Get the argument from the command line
input = ARGV[0]

#Define the regular expression to match "hbtn" followed by 0 or more 't' characters
regex = /hbt+n/

#Use the regular expression matching method
match_result = input.match(regex)

#Print the match result or an empty atring if no match
puts match_result ? match_result[0] : " "
