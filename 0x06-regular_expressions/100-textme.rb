#!/usr/bin/env ruby

#Get the log file path from the command line
log_file_path = ARGV[0]

#Read the log file content
log_content = File.read(log_file_path)

#Define a regular expression to extract relevant information
regex = /\[from:(.*?)\]\[to:(.*?)\]\[flags:(.*?)\]/

#Use the regular expression to find matches in the log content
matches = log_content.scan(regrex)
