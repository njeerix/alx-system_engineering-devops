#!/usr/bin/env ruby

#Get the log file path from the command line
input = ARGV[0]

#Define a regular expression to extract relevant information
regex = /^\S+ \d+ \d+:\d+:\d+ ip-[\d.]+ mdr: \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} Sent SMS .* from:([^\]]+) \[to:([^\]]+) \[flags:([^\]]+)/

#Use the regular expression to find matches in the log content
match_result = input.match(regrex)

#Print the match result or an empty string if no match
puts match_result ? "#{match_result[1]},#{match_result[2]},#{match_result[3]}" : ""
